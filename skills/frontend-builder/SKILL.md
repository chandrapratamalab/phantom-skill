---
name: frontend-builder
description: Build a working, reviewable frontend prototype from UI-SPEC.md (and PRD.md) produced by ui-spec-writer and prd-writer, using a mock data layer, in any stack. Use whenever the user wants to build, code, implement, or "wujudkan" the UI from a UI spec, build the frontend first before the backend, get a clickable prototype to review UX with different roles, or says things like "bangun frontend", "buat tampilan berdasarkan UI-SPEC", "coding UI-nya", "prototype aplikasi", "implementasi desain". Also use to revise an existing frontend built from a UI-SPEC. Do NOT use for writing the PRD (prd-writer), writing the UI spec (ui-spec-writer), building the backend/API/database, or designing without a spec.
---

# Frontend Builder

Build the frontend from `UI-SPEC.md` so that stakeholders of every role can **see and click** the product and judge whether the UI/UX is easy to understand and pleasant to use, before any backend exists. The result is a foundation, not a throwaway demo: when the backend arrives, only the data layer changes.

This skill is **stack-neutral**. Follow the stack named in the PRD; if none is named, choose a mainstream default and record it as an assumption (see `references/stack-mapping.md`).

## The Contract with the Other Skills (read first)

- `PRD.md` = source of truth for **behavior** (features, roles, flows, endpoints, data shapes).
- `UI-SPEC.md` = source of truth for **appearance and interaction** (tokens, components, screens, states, copy).
- This skill = **implements** them. It never invents either.

Rules that keep the project from breaking:
1. **Read-only on PRD.md and UI-SPEC.md** while building. Do not edit them to match the code.
2. **No new features or business rules.** Only what the PRD defines. Gaps and conflicts go to a Change Request list (see Deliver), not into silent code.
3. **Design feedback changes the spec first.** If the user asks for a visual or flow change after review, tell them to update UI-SPEC.md via ui-spec-writer (or ask for permission to log the change there), then update the code. Never let code and spec drift apart.
4. **Traceability in code:** components, screens, and tokens carry the spec IDs in names or comments (`S-03`, `C-07`, `F-02`) so a spec revision maps to files.
5. **Mock data lives in ONE layer** shaped like the PRD's endpoints and ERD (see `references/mock-data-layer.md`). Screens never read mock data directly.

## Workflow

### Step 0: Locate inputs and check readiness

- Find `UI-SPEC.md` and `PRD.md`. If `UI-SPEC.md` is missing, do not improvise a design: offer to run ui-spec-writer first (or, if the user insists, build from the PRD alone and log "no UI-SPEC" as an assumption with minimal neutral styling).
- If a frontend already exists for this project, work incrementally: change only the screens, components, or tokens affected. Do not regenerate the app.
- Compare the PRD version recorded in the UI-SPEC header with the PRD you have. If they differ, warn the user and list the screens (`S-xx`) likely affected before building.

### Step 1: Plan (short, before coding)

Write a compact build plan in the chat or a `BUILD-PLAN.md`:
- **Stack decision:** from PRD Section 7, or the default you chose and why.
- **Scope of this pass:** which screens (`S-xx`) and features, by priority. Default: **all P0 first**, review, then P1.
- **Roles to demonstrate** and the seeded users for each.
- **Gaps found** in the spec (missing states, undefined components) and how you will handle each (Change Request vs. reasonable default listed in Assumptions).

If the stack is truly unknowable from the PRD and the platform is ambiguous (web vs. mobile vs. desktop), ask ONE question; otherwise choose and proceed.

### Step 2: Build in the order in `references/build-order.md`

Foundations first (project scaffold → design tokens → component library → data layer → app shell and routing → screens P0 → state gallery and role switcher), then screens by priority. Read the reference before starting.

Key requirements while building:
- Tokens become the stack's native theming mechanism (CSS variables, theme object, etc.). Components use semantic roles, never raw hex values.
- Every screen implements **all states** from the UI-SPEC (default, loading, empty, error, success, plus offline/permission-denied where specified).
- Responsive behavior follows the UI-SPEC breakpoints.
- Accessibility floor from the spec: contrast, focus visibility, touch targets, labels, reduced motion.
- Copy comes from the UI-SPEC microcopy, not invented.

### Step 3: Make it reviewable (mandatory)

The prototype must let non-developers evaluate UX. Read `references/review-tools.md` and add:
- **Role switcher** (dev-only panel) so one link serves every role.
- **State gallery** page showing each screen in every state.
- **Component gallery** showing each `C-xx` with its variants.
- **Realistic mock data** including extreme cases (long names, empty lists, large numbers).
- A **Review Checklist per role** in `REVIEW.md`.

These tools are clearly marked dev-only and removable by a single flag.

### Step 4: Verify

Run the checks you can actually run: build/compile, lint, type-check, and any tests derived from the UI-SPEC's Given/When/Then. If the environment supports a browser or screenshot tool, capture each screen at the spec's breakpoints and compare to the wireframes. If it does not, **say clearly that visual fidelity is unverified** and that the user must review it in a browser. Never claim a screen "looks right" without seeing it.

### Step 5: Deliver

1. Provide the code as a project (files in `/mnt/user-data/outputs/` when file tools are available) with a `README.md`: how to install, run, switch roles, open the galleries, and turn off dev tools.
2. Chat summary, max ~6 lines: what was built (screens by ID), how to run it, what was verified vs. not, top assumptions.
3. List **Change Requests** (gaps/conflicts found in PRD or UI-SPEC) in `CHANGE-REQUESTS.md` and mention them in one line.
4. Offer the next step in one line: review round with each role, P1 screens, or (after UI approval) building the backend against the same endpoint shapes.

## Quality Checklist (run before delivering)

- [ ] Every P0 screen in scope exists and its route works for the roles allowed in the PRD.
- [ ] Every screen implements all states specified in the UI-SPEC.
- [ ] Every component used is defined once in the shared component library; no screen redefines tokens or styles inline.
- [ ] No raw color/spacing values outside the token definitions.
- [ ] No component reads mock data directly; all data goes through the data layer, with PRD-shaped responses and error cases.
- [ ] Spec IDs (`S-xx`, `C-xx`, `F-xx`) appear in code names or comments.
- [ ] Role switcher, state gallery, and component gallery work and are dev-only.
- [ ] No feature or business rule exists that is not in the PRD.
- [ ] Project builds and runs from README instructions; lint/type-check pass where available.
- [ ] Visual verification status is stated honestly.
- [ ] Language of UI copy matches the UI-SPEC.

## Reference Files

- `references/build-order.md`: Step-by-step build sequence and definition of done per stage. Read in Step 2.
- `references/mock-data-layer.md`: How to structure the mock layer so the backend swap is trivial. Read in Step 2.
- `references/review-tools.md`: Role switcher, galleries, review checklist, REVIEW.md format. Read in Step 3.
- `references/stack-mapping.md`: Stack-neutral mapping from spec concepts to common stacks, and default choices. Read in Step 1.