# Making Skills Work on Weaker or Cheaper Models

Be realistic: a skill can raise a weaker model's floor, but it cannot make every model equal. The practical aim is that **checks and structure live in the skill and in scripts, not in the model's judgment**, so quality depends less on the model.

## Techniques (most effective first)
1. **Deterministic validators.** Anything a script can check (ID existence, section presence, balanced Mermaid fences, hex colors outside tokens, build/lint/tests) should be checked by a script. Weak models fail silently; scripts do not.
2. **Fill-in templates over prose guidance.** A table or skeleton to complete drifts less than "write a section about X".
3. **Small steps with exit conditions.** One stage per pass with a "done when" check. Weak models lose track of long procedures.
4. **Explicit DO / DO NOT lists** for the failures seen in logs, phrased with the reason.
5. **Worked examples**, including one bad example with the correction, for formats that get violated.
6. **Closed choices instead of open ones.** "Pick one of: A / B / C" beats "decide the best approach".
7. **Evidence-quoting self-checks.** Instead of "confirm all P0 are covered", require a table: feature → screen ID. Gaps become visible.
8. **Stop-and-ask gates** where a wrong guess is costly (stack unknown, destructive change, overwriting an existing document).
9. **Shorter SKILL.md, details in references.** Smaller context per step helps weaker models; load references only when the step needs them.
10. **Stable IDs and fixed names.** Reduces confusion across documents.

## What does NOT transfer to weaker models
- Subtle judgment calls (visual taste, nuanced tradeoffs): expect lower quality; compensate with stricter direction questions and human review.
- Security reasoning: never rely on a model alone for authentication, authorization, secrets, or data protection. Use checklists, linters, dependency audits, and human review.
- Long-context consistency: keep documents modular and validate with scripts.

## Comparing models fairly
- Same scenario, same inputs, same skill version; vary only the model.
- Log with `--model` and use `summarize_logs.py` to compare event counts by category.
- Track: events per run, severity mix, user corrections needed, validator failures, whether the build passes.
- A model tier is "good enough" for a stage when it completes the scenario with no high/blocker events across 3 runs.

## Production readiness gate (human, not model)
Before shipping, regardless of model: build/lint/tests pass, validator clean, security review done, secrets handled, data migrations reviewed, accessibility spot-check done, and a person has used the product in each role.