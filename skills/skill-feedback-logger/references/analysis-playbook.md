# Analysis Playbook: from logs to skill improvements

## 1. When is a pattern worth acting on?
- **Act on a single event** if severity is `blocker`/`high` and it has a clear `skill_gap`.
- **Otherwise act on a pattern:** the same category + skill + step (or the same `skill_gap` text) appears **3 or more times**, or across **2 or more models/projects**.
- Ignore one-off `low` events; keep them for trend counts.

## 2. Read the logs in this order
1. Counts by category and by skill (where is the pain?).
2. Counts by detection source (how much came from validators vs. users? Many `user` entries means missing validators or rules).
3. Counts by model (is the failure model-specific or universal?).
4. Group by `skill_gap` text; merge near-duplicates.
5. Check chain-boundary events (`id_drift`, `contract_violation`, `spec_gap`): they usually mean the interface between two skills is underspecified.

## 3. Choose the type of fix (cheapest effective first)
| Fix type | Use when | Example |
|---|---|---|
| **Add a deterministic check** | The error can be detected by a script | Validator for IDs that do not exist in the PRD |
| **Add/strengthen a checklist item** | The agent forgets a step | "Every P0 feature maps to a screen" |
| **Clarify the rule with its reason** | The instruction was ambiguous | State what to do when a screen has no matching feature |
| **Add a worked example (good and bad)** | The format is violated or misread | Example of a correct state table |
| **Make a template fill-in** | Structure drifts | Replace prose guidance with a table to complete |
| **Split or shorten a step** | Long steps get partially executed | Break Step 4 into two |
| **Add a gate (stop and confirm)** | A risky action happened silently | Ask before regenerating the whole document |
| **Add to a reference file** | Domain knowledge was missing | Stack-specific notes |

Prefer fixes at the top of the table: scripts and checklists beat longer prose.

## 4. Writing a proposal
For each proposal in `LESSONS.md`:
```markdown
### P-01: [short title]
- **Skill / file:** frontend-builder / SKILL.md, Step 2
- **Evidence:** E-0004, E-0011, E-0019 (3 events, 2 models)
- **Problem:** [what keeps going wrong, in one sentence]
- **Proposed change:**
  - Before: "..."
  - After: "..."
- **Fix type:** checklist item + validator
- **Expected effect:** [measurable, e.g., "no invented F-xx IDs in 3 consecutive runs"]
- **Retest:** [scenario to rerun, which models]
- **Risk:** [could this over-constrain other cases?]
```

## 5. Apply and retest
1. User approves proposals (all, some, or none).
2. Apply to the skill; note the change and date in a `CHANGELOG` section or file for that skill.
3. Rerun the **same scenario** that produced the logs, and one **different** scenario (to check for overfitting).
4. Compare event counts before/after for the targeted category. A fix that works only on the original scenario is too specific; generalize the rule.
5. If a change makes outputs worse elsewhere, revert it and record why.

## 6. Keep skills from bloating
- Prefer deleting or merging rules over appending forever. Review the skill after every 3-4 improvement rounds.
- Move detail to `references/` and keep `SKILL.md` as the workflow.
- Rules that never prevent a logged event are candidates for removal.

## 7. Suggested cadence
- After each project or test run: Mode C retrospective.
- After a skill change: targeted retest.
- Monthly or after ~20 events: review trends by model and skill.