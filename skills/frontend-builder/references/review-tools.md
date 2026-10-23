# Review Tools

## Default: invisible
The app opens as the clean product UI. Review tools exist but are **off unless review mode is on**.
- **Turn on:** an environment flag (`REVIEW_MODE=true`) for team builds, or a URL parameter (`?review=1`) / keyboard shortcut for quick checks. Pick one and document it in README.
- **When off:** no role switcher, no gallery routes registered, no dev buttons, no extra navigation items. A reviewer who has not been told about it never sees it.
- **When on:** a small collapsed handle appears at a screen edge; galleries are reached by direct route or from that handle, never from the product's own navigation.
- Never place review controls inside product screens, headers, or menus.

The purpose of this prototype is to let people of every role judge clarity and look-and-feel. These tools make that possible without developer help. All are **dev-only**, behind one flag (e.g., `REVIEW_MODE`), and removable in one step.

## 1. Role switcher
- A small floating panel (corner of the screen) listing the PRD roles. Selecting a role swaps the fake session and routes to that role's home.
- Show the current role clearly, plus a "reset data" action.
- Keep it visually distinct from the product UI so it is never mistaken for product design.

## 2. State gallery (`/__states` or equivalent)
- A page listing every screen `S-xx`; opening one shows it in each state: default, loading, empty, error, success, plus offline/permission-denied where the spec defines them.
- States are rendered from the real screen component with forced data conditions, not static screenshots.
- Group by screen, with the spec's state table next to the render so reviewers can compare.

## 3. Component gallery (`/__components` or equivalent)
- Every `C-xx` with all variants and states side by side, on the real tokens.
- Include a token page: color roles with contrast values, type scale, spacing, radius.

## 4. Viewport helper
- Quick buttons for the spec's breakpoints (e.g., 360 / 768 / 1280) or a note on how to resize, so reviewers check responsive layouts.

## 5. REVIEW.md (generate this file)
Structure:
```markdown
# Review Guide
**How to open:** [run instructions] | **Roles:** [list] | **Galleries:** [paths]

## Per-role tasks
### Role: [Admin]
| # | Task (from PRD flow) | Expected effort | Pass? | Notes |
|---|---|---|---|---|
| 1 | [Complete flow X] | ≤ 3 clicks, no instructions needed | | |

## UX questions (answer per role)
- Can you tell what this screen is for within 5 seconds?
- Is the main action obvious?
- When something goes wrong, do you know what to do next?
- Is any wording confusing?
- Is text readable and comfortable (size, contrast, spacing)?
- Does it feel pleasant? What looks off?

## Responsive check
- Open at each breakpoint: anything cut off, cramped, or hard to tap?

## Feedback log
| # | Screen (S-xx) | Role | Issue | Severity | Spec change needed? |
|---|---|---|---|---|---|
```
Build the task table from the PRD user flows and features, one row per key task per role.

## 6. Feedback loop rule
Reviewer feedback about look, flow, or wording changes **UI-SPEC.md first** (via ui-spec-writer, logged in its Change Log), then the code. Feedback that changes behavior goes to the PRD via prd-writer. State this in README so reviewers' suggestions do not silently diverge the code from the documents.

## 7. Removal
Document in README how to disable review mode (flag) and what files to delete to strip all dev tools for production.