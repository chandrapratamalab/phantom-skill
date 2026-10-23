#!/usr/bin/env python3
"""Summarize .skill-logs/events.jsonl into a draft markdown report (stdlib only)."""
import argparse, json, os, sys
from collections import Counter, defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".skill-logs")
    ap.add_argument("--out", default="")
    ap.add_argument("--threshold", type=int, default=3)
    a = ap.parse_args()

    path = os.path.join(a.dir, "events.jsonl")
    if not os.path.exists(path):
        print("No events logged yet."); return 0
    events = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try: events.append(json.loads(line))
                except json.JSONDecodeError: pass

    def table(title, key):
        c = Counter(e.get(key) or "(none)" for e in events)
        out = [f"### {title}", "| Value | Count |", "|---|---|"]
        out += [f"| {k} | {v} |" for k, v in c.most_common()]
        return "\n".join(out)

    lines = ["# Draft Log Summary", f"Events: {len(events)}\n"]
    for t, k in (("By category","category"),("By skill","skill"),("By severity","severity"),
                 ("By detection source","detected_by"),("By model","model")):
        lines += [table(t, k), ""]

    cm = defaultdict(Counter)
    for e in events: cm[e.get("category")][e.get("model") or "(none)"] += 1
    lines += ["### Category by model", "| Category | Breakdown |", "|---|---|"]
    for cat, c in sorted(cm.items(), key=lambda x: -sum(x[1].values())):
        lines.append(f"| {cat} | " + ", ".join(f"{m}: {n}" for m, n in c.most_common()) + " |")
    lines.append("")

    gaps = defaultdict(list)
    for e in events:
        g = (e.get("skill_gap") or "").strip().lower()
        if g: gaps[g].append(e)
    lines += [f"### Recurring skill gaps (threshold >= {a.threshold}, or any high/blocker)",
              "| Skill gap | Count | Skills | Event IDs |", "|---|---|---|---|"]
    shown = False
    for g, evs in sorted(gaps.items(), key=lambda x: -len(x[1])):
        severe = any(e.get("severity") in ("high","blocker") for e in evs)
        if len(evs) >= a.threshold or severe:
            shown = True
            lines.append(f"| {g} | {len(evs)} | {', '.join(sorted({e['skill'] for e in evs}))} | {', '.join(e['id'] for e in evs)} |")
    if not shown: lines.append("| (none yet) | | | |")
    lines.append("")

    sev = [e for e in events if e.get("severity") in ("high","blocker") and e.get("status") != "resolved"]
    lines += ["### Open high/blocker events", "| ID | Skill | Category | Description |", "|---|---|---|---|"]
    lines += [f"| {e['id']} | {e['skill']} | {e['category']} | {e['description']} |" for e in sev] or ["| (none) | | | |"]
    lines += ["", "> Next: read references/analysis-playbook.md and write proposals into LESSONS.md."]

    text = "\n".join(lines)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f: f.write(text)
        print(f"written {a.out}")
    else:
        print(text)
    return 0

if __name__ == "__main__":
    sys.exit(main())