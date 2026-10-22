# Design Rules

## 1. Anti-generic checklist (apply to Design Direction)
AI-produced design clusters around defaults. These are fine when the brief demands them, but should be a choice, not a reflex. If the direction matches several of these for a subject where they don't belong, revise it and say what changed.
- Warm cream background + high-contrast serif + terracotta accent.
- Near-black background + one acid-green/vermilion accent.
- Newspaper style: hairline rules, zero radius, dense columns.
- The "SaaS card kit": identical rounded cards, one radius everywhere, the same soft shadow, gradient washes.
- Template chrome: tracked-out ALL-CAPS eyebrow above every heading, middle-dot meta strings, "→" on every link, monospace for every small label.
- Numbered markers (01 / 02 / 03) on content that is not actually a sequence.
- Accenting a single word in a headline.

Ground the direction in the subject: a children's learning app, a clinic scheduler, and a logistics dashboard should look clearly different. If the user states a direction, follow it exactly.

## 2. Token rules
- Define 4-6 base colors, then semantic roles. Components use roles, never raw hex.
- One or two typefaces, with distinct roles. State a type scale (e.g., 12/14/16/20/24/32) and body line length < 80 characters.
- Radius and elevation follow hierarchy (e.g., inputs, cards, modals differ) rather than one value for all.
- Spacing from a fixed scale. No one-off values.

## 3. State coverage
Every screen with data or actions covers: default, loading (skeleton or spinner, with the longest acceptable wait), empty (explains what belongs here and offers the next action), error (what happened and how to fix it), success. Add offline, permission-denied, and partial-data states when the PRD edge cases mention them. Forms: field-level validation, disabled/submitting button state, unsaved-changes handling.

## 4. Accessibility floor
- Contrast: 4.5:1 body text, 3:1 large text and UI boundaries/icons.
- Touch targets ≥ 44×44 px; spacing between adjacent targets ≥ 8 px.
- Visible keyboard focus on every interactive element; logical focus order.
- Color is never the only signal (pair with icon or text).
- Inputs have visible labels; icon-only buttons have accessible names.
- Respect reduced motion: provide a non-animated equivalent.

## 5. Microcopy
- Write from the user's perspective in plain language; avoid system terms.
- Active voice, sentence case. Buttons say what happens ("Save changes", not "Submit").
- The same action keeps the same name across the flow (Publish → "Published").
- Errors state what happened and how to fix it; they don't apologize or blame the user.
- Empty states invite the next action.

## 6. Motion
- Motion answers user actions (open, expand, confirm) and shows what changed.
- Non-user-triggered motion: at most one orchestrated moment.
- Specify duration (typically 150-300 ms for UI feedback), easing, and a reduced-motion fallback.

## 7. Wireframe conventions (ASCII)
Use `+---+` frames, `[ Button ]` for actions, `( )` radio, `[x]` checkbox, `____` input, `{ }` image placeholder. One mobile wireframe per screen minimum; add desktop where the layout changes materially. Wireframes show hierarchy and placement, not final styling.