#!/usr/bin/env python3
"""Deterministic checks across PRD.md, UI-SPEC.md and (optionally) code. Stdlib only.
Exit code 1 if any ERROR is found. Warnings do not fail the run."""
import argparse, os, re, subprocess, sys

ID_RE = {"F": re.compile(r"\bF-\d+\b"), "FR": re.compile(r"\bFR-\d+\b"),
         "NFR": re.compile(r"\bNFR-\d+\b"), "S": re.compile(r"\bS-\d+\b")}
CODE_EXT = {".css", ".scss", ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte", ".dart", ".html"}
HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")

findings = []  # (level, category, skill, message, evidence)

def add(level, cat, skill, msg, ev=""):
    findings.append((level, cat, skill, msg, ev))

def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()

def ids(text, kind):
    return set(ID_RE[kind].findall(text))

def p0_features(prd):
    """Feature IDs whose block (heading/row start to next feature) mentions P0."""
    res = set()
    lines = prd.splitlines()
    starts = [i for i, l in enumerate(lines)
              if re.search(r"(#+|\*\*)\s*F-\d+", l) or re.match(r"\s*\|?\s*F-\d+", l)]
    for k, i in enumerate(starts):
        end = starts[k + 1] if k + 1 < len(starts) else len(lines)
        block = "\n".join(lines[i:min(end, i + 25)])
        m = re.search(r"\bF-\d+\b", lines[i])
        if m and re.search(r"\bP0\b", block):
            res.add(m.group(0))
    return res

def check_mermaid(text, fname, skill):
    if len(re.findall(r"^```", text, flags=re.M)) % 2:
        add("ERROR", "format_violation", skill, f"{fname}: unbalanced ``` fences")
    for m in re.finditer(r"```mermaid\n(.*?)```", text, flags=re.S):
        body = m.group(1)
        first = body.strip().splitlines()[0] if body.strip() else ""
        if not re.match(r"(flowchart|graph|sequenceDiagram|erDiagram|stateDiagram|classDiagram|gantt|journey)", first):
            add("ERROR", "syntax_error", skill, f"{fname}: mermaid block does not start with a valid diagram type", first[:80])
        if first.startswith(("flowchart", "graph")):
            for line in body.splitlines():
                for lab in re.findall(r"\w+\[([^\]\"]*[()/:,][^\]\"]*)\]", line):
                    add("ERROR", "syntax_error", skill, f"{fname}: unquoted label with special characters in flowchart", lab[:80])
        nodes = len(set(re.findall(r"^\s*(\w+)[\[\(\{]", body, flags=re.M)))
        if nodes > 20:
            add("WARN", "format_violation", skill, f"{fname}: mermaid diagram has ~{nodes} nodes (limit ~15)")

def has_section(text, pattern):
    m = re.search(pattern, text, flags=re.I)
    return bool(m) and len(text[m.end(): m.end() + 600].strip()) > 40

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prd", required=True)
    ap.add_argument("--uispec")
    ap.add_argument("--code")
    ap.add_argument("--token-paths", default="token,theme,design-system",
                    help="path fragments allowed to hold raw colors")
    ap.add_argument("--log", action="store_true", help="append findings to .skill-logs/events.jsonl")
    ap.add_argument("--project", default="")
    ap.add_argument("--model", default="")
    a = ap.parse_args()

    prd = read(a.prd)
    prd_ids = {k: ids(prd, k) for k in ID_RE}

    # PRD checks
    if not has_section(prd, r"assumptions"):
        add("ERROR", "format_violation", "prd-writer", "PRD has no filled Assumptions section")
    if not prd_ids["F"]:
        add("ERROR", "format_violation", "prd-writer", "PRD has no F-xx feature IDs")
    if not prd_ids["FR"]:
        add("WARN", "format_violation", "prd-writer", "PRD has no FR-xx requirement IDs")
    if not re.search(r"p\d\d|\d+\s?ms|\d+\s?%|\d+\s?fps", prd, flags=re.I):
        add("WARN", "format_violation", "prd-writer", "PRD shows no concrete numbers (NFRs/metrics look vague)")
    if not re.search(r"Given.+When.+Then", prd, flags=re.S):
        add("WARN", "format_violation", "prd-writer", "No Given/When/Then acceptance criteria found")
    if re.search(r"\bUI\b|screen|layar|halaman", prd, flags=re.I) and not prd_ids["S"]:
        add("WARN", "spec_gap", "prd-writer", "Product seems to have a UI but PRD has no Screen Inventory (S-xx)")
    check_mermaid(prd, os.path.basename(a.prd), "prd-writer")
    if re.search(r"#[0-9a-fA-F]{6}\b", prd):
        add("WARN", "contract_violation", "prd-writer", "PRD contains hex colors (visual design belongs in UI-SPEC)")

    p0 = p0_features(prd)

    # UI-SPEC checks
    if a.uispec:
        ui = read(a.uispec)
        for kind, label in (("F", "feature"), ("FR", "requirement"), ("NFR", "requirement"), ("S", "screen")):
            if kind == "S" and not prd_ids["S"]:
                continue  # derived screens are allowed when the PRD has no inventory
            for bad in sorted(ids(ui, kind) - prd_ids[kind]):
                add("ERROR", "hallucination", "ui-spec-writer",
                    f"UI-SPEC references {label} ID {bad} that is not in the PRD", bad)
        for f in sorted(p0):
            if f not in ids(ui, "F"):
                add("ERROR", "spec_gap", "ui-spec-writer", f"P0 feature {f} is not served by any screen in UI-SPEC", f)
        if not re.search(r"Built from:.*PRD", ui, flags=re.I):
            add("WARN", "format_violation", "ui-spec-writer", "UI-SPEC header does not record the PRD version used")
        if not has_section(ui, r"assumptions"):
            add("ERROR", "format_violation", "ui-spec-writer", "UI-SPEC has no filled Assumptions section")
        if not re.search(r"change requests", ui, flags=re.I):
            add("WARN", "format_violation", "ui-spec-writer", "UI-SPEC has no PRD Change Requests section")
        for st in ("loading", "empty", "error"):
            if not re.search(st, ui, flags=re.I):
                add("WARN", "missing_state", "ui-spec-writer", f"No '{st}' state mentioned anywhere in UI-SPEC")
        check_mermaid(ui, os.path.basename(a.uispec), "ui-spec-writer")

    # Code checks
    if a.code and os.path.isdir(a.code):
        allowed = [t.strip() for t in a.token_paths.split(",") if t.strip()]
        ref_ids = {"F": set(), "S": set()}
        for root, dirs, files in os.walk(a.code):
            dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", "dist", "build", ".next")]
            for fn in files:
                if os.path.splitext(fn)[1] not in CODE_EXT:
                    continue
                path = os.path.join(root, fn)
                text = read(path)
                for k in ("F", "S"):
                    ref_ids[k] |= ids(text, k)
                if not any(t in path.lower() for t in allowed):
                    n = len(HEX_RE.findall(text))
                    if n:
                        add("WARN", "contract_violation", "frontend-builder",
                            f"{n} raw color value(s) outside token files", path)
        for k in ("F", "S"):
            if k == "S" and not prd_ids["S"]:
                continue
            for bad in sorted(ref_ids[k] - prd_ids[k]):
                add("ERROR", "hallucination", "frontend-builder", f"Code references {bad} that is not in the PRD", bad)
        if not any(os.path.exists(os.path.join(a.code, p)) for p in ("review", "__states", "dev")):
            add("WARN", "spec_gap", "frontend-builder", "No review/dev tools folder found (role switcher / galleries)")

    errors = [f for f in findings if f[0] == "ERROR"]
    warns = [f for f in findings if f[0] == "WARN"]
    for lvl, cat, skill, msg, ev in findings:
        print(f"[{lvl}] ({skill}/{cat}) {msg}" + (f"  -> {ev}" if ev else ""))
    print(f"\nSummary: {len(errors)} error(s), {len(warns)} warning(s)")

    if a.log and findings:
        logger = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_event.py")
        for lvl, cat, skill, msg, ev in findings:
            subprocess.run([sys.executable, logger, "--skill", skill, "--step", "validator",
                            "--category", cat, "--severity", "high" if lvl == "ERROR" else "low",
                            "--detected-by", "validator", "--description", msg,
                            "--evidence", ev or msg, "--project", a.project, "--model", a.model],
                           check=False, capture_output=True)
        print("Findings appended to .skill-logs/events.jsonl")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())