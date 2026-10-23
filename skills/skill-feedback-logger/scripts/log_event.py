#!/usr/bin/env python3
"""Append one event to .skill-logs/events.jsonl (stdlib only)."""
import argparse, json, os, sys
from datetime import datetime, timezone

CATEGORIES = ["hallucination","contract_violation","id_drift","scope_creep","spec_gap","missing_state",
 "assumption","ambiguity","instruction_skipped","format_violation","syntax_error","build_error","tool_error",
 "inconsistency","verification_gap","security_issue","language_mismatch","user_correction","other"]
SEVERITIES = ["blocker","high","medium","low"]
SOURCES = ["validator","test","user","self"]

def next_id(path):
    n = 0
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    n += 1
    return f"E-{n+1:04d}"

def main():
    p = argparse.ArgumentParser(description="Log a skill-chain event")
    p.add_argument("--dir", default=".skill-logs")
    p.add_argument("--project", default="")
    p.add_argument("--skill", required=True)
    p.add_argument("--step", default="")
    p.add_argument("--model", default="")
    p.add_argument("--category", required=True, choices=CATEGORIES)
    p.add_argument("--severity", required=True, choices=SEVERITIES)
    p.add_argument("--detected-by", required=True, choices=SOURCES)
    p.add_argument("--description", required=True)
    p.add_argument("--evidence", required=True)
    p.add_argument("--expected", default="")
    p.add_argument("--actual", default="")
    p.add_argument("--root-cause", default="")
    p.add_argument("--resolution", default="")
    p.add_argument("--skill-gap", default="")
    p.add_argument("--status", default="open", choices=["open","resolved"])
    a = p.parse_args()

    os.makedirs(a.dir, exist_ok=True)
    path = os.path.join(a.dir, "events.jsonl")
    ev = {
        "id": next_id(path),
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "project": a.project, "skill": a.skill, "step": a.step, "model": a.model,
        "category": a.category, "severity": a.severity, "detected_by": a.detected_by,
        "description": a.description, "evidence": a.evidence[:300],
        "expected": a.expected, "actual": a.actual, "root_cause": a.root_cause,
        "resolution": a.resolution, "skill_gap": a.skill_gap, "status": a.status,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    print(f"logged {ev['id']} ({a.category}/{a.severity})")

if __name__ == "__main__":
    sys.exit(main())