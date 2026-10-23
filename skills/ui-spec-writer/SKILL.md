---
name: ui-spec-writer
description: Generate a developer- and designer-ready UI design specification (UI-SPEC.md) from an existing PRD.md produced by prd-writer, covering visual direction, information architecture, screen-by-screen specs with all states, design tokens, component library, microcopy, accessibility, and motion. Use whenever the user wants a UI spec, UI/UX design document, wireframes, design system, screen designs, style guide, or says things like "buatkan UI spec", "desain tampilan", "rancang UI/UX", "wireframe aplikasi", "design system", or asks to design the interface after a PRD exists, even if they don't say "spec". Also use to revise an existing UI-SPEC.md. Do NOT use for writing the PRD itself (use prd-writer), writing front-end code (use frontend-builder), or generating images/mockup files.
---

# UI Spec Writer

Turn a `PRD.md` into a complete `UI-SPEC.md`: the visual and interaction blueprint for every screen. The output is a **specification document**, not code. A developer (or the `frontend-design` skill) should be able to build the interface from it without guessing.

## The Contract with prd-writer (read first)

`PRD.md` is the **source of truth for behavior**. `UI-SPEC.md` is the source of truth for **appearance and interaction**. To keep both consistent and never break the project:

1. **Read-only on the PRD.** Never edit, rewrite, or "fix" `PRD.md`. Never add, remove, or rename features.
2. **Reuse IDs, never invent parallel ones.** Reference PRD IDs exactly: `F-xx` (features), `FR-xx` / `NFR-xx` (requirements), `S-xx` (screens). The UI spec may only create its own IDs for things the PRD does not define: `C-xx` (components), `T-` prefixed tokens, `M-xx` (motion).
3. **Gaps go to Change Requests, not silent fixes.** If the PRD is missing a screen, state, or flow the design needs, add it to the "PRD Change Requests" section of the UI-SPEC with a proposed wording. Do not design around it silently and do not edit the PRD.
4. **Record the source version.** The UI-SPEC header states which PRD version/date it was built from.
5. **Behavior conflicts → the PRD wins.** If a design idea contradicts a PRD requirement, follow the PRD and log the conflict as a Change Request.

## Workflow

### Step 0: Locate inputs

- Look for `PRD.md` in the conversation, workspace, or uploads.
- **If `UI-SPEC.md` already exists** and the user wants a change: edit only the affected screens/tokens/components, then update the Change Log. Do not regenerate everything. If the PRD version differs from the one recorded in the UI-SPEC, list which `S-xx` screens may be affected and update only those.
- **If no PRD exists:** do not invent a product. Ask the user for a short description (or offer to run prd-writer first). If the user insists on proceeding, ask 3 questions: what the product does, who uses it, and the main screens. Mark the spec header `Source: no PRD (user brief)` and treat all derived screens as assumptions.

### Step 1: Read the PRD and extract

Pull out, silently: personas (Section 1), features with priorities and edge cases (Section 3), user flows (Section 4), the Screen Inventory (Section 4), roles (Sections 2-3), platform and stack (Sections 5, 7), NFRs that affect UI (performance, accessibility, devices).

If the PRD has no Screen Inventory, derive screens from the flows and features, number them `S-xx`, and log in Assumptions that the inventory was derived (and suggest adding it to the PRD via a Change Request).

### Step 2: Ask visual-direction questions (only if needed)

PRDs rarely say how the product should *feel*. **Skip this step** if the user already gave a clear visual direction, references, or said "build directly" / "buat langsung" / "langsung aja".

Otherwise ask **3 to 5 questions** from `references/question-bank.md` and never ask what the PRD already answers (platform, audience, features). Include quick options in parentheses. Close with:
> *"Answer only what you've decided, or reply **'build directly'** / **'buat langsung'** and I'll choose a fitting direction and list it as an assumption."*

One round only. Unanswered points get defaults recorded in Assumptions.

### Step 3: Define visual direction BEFORE detail

Before writing screens, settle (in the spec's Section 1) the direction: 3-4 mood words, the product's subject-specific visual vernacular, what to avoid, and one memorable design move. Check it against `references/design-rules.md` (anti-generic checklist). If the direction reads like what you would produce for any similar product, revise it and say what changed.

### Step 4: Generate UI-SPEC.md

1. Read `references/template.md` and follow its structure.
2. Read `references/design-rules.md` for tokens, states, accessibility, and copy rules.
3. Read `references/mermaid-rules.md` before drawing the sitemap or any flow diagram.
4. Define tokens and components **once**; screens only reference them (e.g., `Button/Primary`, `color.surface`). Never redefine inside a screen.
5. Run the Quality Checklist silently and fix issues before delivering.

### Step 5: Deliver

1. Create `UI-SPEC.md` (in `/mnt/user-data/outputs/` when file tools are available) and present it.
2. In chat: 2-3 sentence summary, the visual direction in one line, and up to 5 assumptions to confirm. Do not paste the whole document.
3. State plainly that wireframes and tokens are a proposal that should be validated visually (prototype or design tool), since text cannot confirm how it looks.
4. Offer next steps in one line: revise a screen, add dark mode, or build the frontend with the frontend-builder skill using this spec.

## Quality Checklist (run before delivering)

- [ ] Header records the PRD version/date used.
- [ ] Every P0 feature (F-xx) is served by at least one screen; every screen lists the F-xx it serves.
- [ ] Screen IDs match the PRD's Screen Inventory (or are marked as derived).
- [ ] Every screen specifies all relevant states: default, loading, empty, error, success, plus offline/permission-denied when the PRD edge cases mention them.
- [ ] Every edge case from PRD Section 3 appears as a state or message somewhere.
- [ ] Every component used in a screen is defined in the Component Library; every token used is defined in Design Tokens.
- [ ] Text/background pairs meet WCAG AA (4.5:1 body, 3:1 large text and UI parts); contrast values are stated for the main pairs.
- [ ] Touch targets ≥ 44×44 px (mobile) and visible keyboard focus are specified.
- [ ] Responsive behavior is defined for each breakpoint the PRD platform requires.
- [ ] Visual direction passes the anti-generic checklist.
- [ ] No PRD content was changed; all gaps/conflicts are in PRD Change Requests.
- [ ] Language matches the user's language (section headings stay in English).

## Reference Files

- `references/template.md`: Full UI-SPEC structure with per-screen template. Read in Step 4.
- `references/question-bank.md`: Visual-direction questions per product type. Read in Step 2.
- `references/design-rules.md`: Anti-generic checklist, token rules, states, accessibility, microcopy. Read in Steps 3-4.
- `references/mermaid-rules.md`: Mermaid syntax rules for the sitemap and flows. Read before drawing diagrams.