# Event Taxonomy

## Categories
| Category | Meaning | Example |
|---|---|---|
| `hallucination` | Invented something not in the source: feature, ID, entity, endpoint, library, API, fact | UI-SPEC serves `F-09`, which the PRD lacks; a package that does not exist |
| `contract_violation` | Broke a rule of the chain: edited a read-only document, invented a parallel ID scheme | Agent "fixed" PRD.md while building the UI |
| `id_drift` | IDs renumbered, reused, or mismatched between documents | `S-03` means a different screen in PRD and UI-SPEC |
| `scope_creep` | Added features or business rules not in the PRD | Added a loyalty-points system nobody asked for |
| `spec_gap` | The upstream document lacked information the next step needed | PRD has no edge cases for payment failure |
| `missing_state` | A screen lacks a required state (loading, empty, error, success, offline) | Error state missing on S-05 |
| `assumption` | A default chosen without user input (valid when logged, a problem when silent) | Assumed email+password auth |
| `ambiguity` | Instruction or document could be read two ways | "Fast" with no number |
| `instruction_skipped` | A required step was skipped | Generated the PRD without asking and without "build directly" |
| `format_violation` | Output structure deviates from the template | Missing Assumptions section |
| `syntax_error` | Invalid Mermaid, JSON, markup | Unquoted label with parentheses |
| `build_error` | Compile, lint, type-check, or runtime failure | Build fails on missing import |
| `tool_error` | Tool or environment failure | Network blocked, file write failed |
| `inconsistency` | Two parts of the output contradict | Feature P0 in section 3, listed Out of Scope in section 2 |
| `verification_gap` | A claim was made without verification | "Looks right" without seeing the render |
| `security_issue` | Insecure pattern | Role check only on the client, secret in code |
| `language_mismatch` | Output language differs from the user's | Indonesian user, English document |
| `user_correction` | The user had to correct the agent (use for corrections whose root category is unknown) | "That's not what I asked" |
| `other` | None of the above (describe it; reconsider adding a category if frequent) | |

## Severity
- `blocker`: the stage cannot continue or the output is unusable.
- `high`: wrong in a way that would reach users or break downstream stages.
- `medium`: needs correction but the work continues.
- `low`: cosmetic or minor.

## Detection source (`detected_by`)
`validator` (script) · `test` (build/test/lint) · `user` (human) · `self` (the model noticed). Prefer higher-trust sources and note when a `self` entry could not be confirmed.

## Fields
| Field | Required | Notes |
|---|---|---|
| `id` | auto | `E-0001` style |
| `timestamp` | auto | UTC |
| `project` | recommended | Project name, to separate runs |
| `skill` | yes | prd-writer, ui-spec-writer, frontend-builder, backend-builder, etc. |
| `step` | recommended | Step or stage in that skill |
| `model` | recommended | Model name/tier; enables cross-model comparison |
| `category` | yes | From the table above |
| `severity` | yes | blocker / high / medium / low |
| `detected_by` | yes | validator / test / user / self |
| `description` | yes | One sentence: what went wrong |
| `evidence` | yes | Short quote, file and line, or error message (≤ 300 chars, no secrets) |
| `expected` | optional | What should have happened |
| `actual` | optional | What happened |
| `root_cause` | optional | Best hypothesis |
| `resolution` | optional | How it was fixed |
| `skill_gap` | recommended | The missing, unclear, or weak rule in the skill that allowed this |
| `status` | auto | `open` by default; set `resolved` when fixed |

`skill_gap` is the most valuable field: it is what the retrospective turns into a skill change. Phrase it as a rule that is absent or unclear, e.g., "No rule says what to do when a screen has no matching feature".

## Manual fallback (when scripts cannot run)
Append rows to `.skill-logs/events.md`:
```markdown
| ID | Date | Project | Skill | Step | Model | Category | Severity | Detected by | Description | Evidence | Skill gap |
|---|---|---|---|---|---|---|---|---|---|---|---|
```
Use the same IDs sequentially (`E-0001`...).