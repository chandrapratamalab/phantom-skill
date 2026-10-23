---
name: skill-feedback-logger
description: Record, validate, and learn from mistakes made while running the PRD → UI-SPEC → frontend (→ backend) skill chain, so the skills can be sharpened with evidence. Logs errors, hallucinations, assumptions, spec gaps, contract violations, ID drift, tool/build failures, and user corrections into an append-only log, runs deterministic traceability checks between PRD.md, UI-SPEC.md and code, and turns accumulated logs into LESSONS.md with proposed skill patches. Use whenever the user says things like "catat kesalahan", "log error", "evaluasi skill", "analisis hasil uji", "kenapa agent salah", "pelajari dari kesalahan", "perbaiki skill berdasarkan log", "cek konsistensi PRD dan UI-SPEC", "bandingkan model", or asks to review how well the skills performed. Also use for a retrospective after finishing a project or a test run. Do NOT use to write the PRD, UI spec, or code themselves, and never to edit those documents.
---

# Skill Feedback Logger

Collect evidence about where the skill chain fails, then convert it into concrete skill improvements. The goal is skills that stay reliable even with weaker or cheaper models, by moving checks out of the model's judgment and into explicit rules, templates, and deterministic scripts.

## Principles (read first)

1. **Evidence over feelings.** Every log entry has a category, a detection source, and short evidence. "It felt wrong" is not an entry.
2. **Trust hierarchy of detection.** Most reliable first: `validator` (script) > `test` (build/test failure) > `user` (human correction) > `self` (the model noticing its own mistake). Models often cannot see their own hallucinations, so never rely on self-reports alone. Run the validators.
3. **Append-only, separate from project files.** Logs live in `.skill-logs/`. This skill never edits `PRD.md`, `UI-SPEC.md`, code, or any other skill file. Skill changes are only *proposed*, and the user decides.
4. **Never block the work.** Logging or validation failures are reported in one line; the main workflow continues.
5. **No secrets or personal data** in logs. Keep evidence short (≤ 300 characters, quote only what is needed).
6. **Honest limits.** The logs improve skills over time; they do not guarantee production readiness on any model. Production still needs human review (especially security, data, and legal aspects).

## Modes

### Mode A: Log an event (during any skill's work)

Log when one of these happens: a validator fails, a build/lint/test fails, the user corrects the agent, the agent finds it made an unsupported assumption, a spec gap is found, an instruction was skipped, or a claim could not be verified.

1. Pick a category from `references/taxonomy.md`.
2. Record with `scripts/log_event.py` (see usage below). If scripts cannot run, append the same fields by hand to `.skill-logs/events.md` using the table format in `references/taxonomy.md`.
3. Continue the task. Do not stop to discuss the log unless the event is a blocker.

```
python scripts/log_event.py --skill frontend-builder --step "Stage 6" \
  --category hallucination --severity high --detected-by validator \
  --description "UI-SPEC references F-09 which does not exist in PRD" \
  --evidence "UI-SPEC.md line 142: Serves F-09" \
  --expected "Only PRD feature IDs" --skill-gap "No rule forbids inventing IDs when a screen has no feature" \
  --model "model-name" --project clinic-booking
```
Fields are explained in `references/taxonomy.md`. Always include `--model` when known, so results can be compared across models.

### Mode B: Validate the chain (run before delivering each stage)

Run deterministic checks instead of trusting the model:

```
python scripts/check_traceability.py --prd PRD.md --uispec UI-SPEC.md [--code src/] [--log]
```
It checks: IDs referenced in UI-SPEC/code exist in the PRD, P0 features are covered by screens, assumptions are present, Mermaid fences are balanced and labels with special characters are quoted, and raw colors do not appear outside token files. With `--log`, every failure is appended as an event with `detected_by=validator`. Fix real errors before delivering; report warnings.

### Mode C: Retrospective (after a project or a test run)

1. Run `python scripts/summarize_logs.py` to produce a draft summary (counts by category, skill, severity, model, detection source, and recurring skill gaps).
2. Read `references/analysis-playbook.md` and turn recurring patterns into **proposed skill changes**: which skill, which file, what to add or change, and which event IDs justify it.
3. Write `.skill-logs/LESSONS.md` with: patterns found, evidence IDs, proposed patches (as before/after text), expected effect, and how to retest.
4. Present the proposals to the user. Apply nothing to the skills without approval. After approval, record the change in the skill's own changelog and note the version so later logs can be compared.

### Mode D: Make a skill robust for weaker models

When logs show that cheaper models fail more often, read `references/model-hardening.md` and propose hardening changes (shorter steps, fill-in templates, explicit do/don't lists, validators). Compare the same scenario across models using the `--model` field.

## Quality Checklist

- [ ] Every logged event has category, severity, detected_by, description, and evidence.
- [ ] No secrets, tokens, or personal data in logs.
- [ ] Validator results (not model opinion) were used wherever a script can check the claim.
- [ ] Proposed skill changes cite event IDs and a threshold (see playbook), not single anecdotes, unless severity is high or blocker.
- [ ] No project document or skill file was modified by this skill.
- [ ] LESSONS.md says how each proposed change will be retested.

## Reference Files

- `references/taxonomy.md`: Event categories, severity scale, detection sources, field definitions, manual log format.
- `references/analysis-playbook.md`: How to turn logs into skill patches, thresholds, change types, retest procedure.
- `references/model-hardening.md`: Techniques that make skills work on weaker or cheaper models.
- `scripts/log_event.py`: Append one event to `.skill-logs/events.jsonl`.
- `scripts/check_traceability.py`: Deterministic checks across PRD, UI-SPEC, and code.
- `scripts/summarize_logs.py`: Aggregate the log into a draft summary.