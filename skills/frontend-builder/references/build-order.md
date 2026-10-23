# Build Order

Do the stages in order. Each stage has a "done when" so you know it is finished before moving on. Keep each pass small enough to review.

## Stage 1: Scaffold
- Create the project with the chosen stack, folder structure per PRD Section 5 (adapt if the PRD gives none).
- Set up lint/format, and a README stub.
- **Done when:** the empty app builds and runs.

## Stage 2: Design tokens
- Translate UI-SPEC Section 4 into the stack's theming mechanism: color roles, type scale, spacing, radius/elevation, breakpoints. Include dark mode only if the spec defines it.
- Load fonts as specified, with fallbacks.
- **Done when:** a single file/area defines every token and nothing else defines raw values.

## Stage 3: Component library
- Implement each `C-xx` from UI-SPEC Section 5 with all variants and states (default, hover, focus, active, disabled, loading, error).
- Keyboard support and accessible names as specified.
- Name components after the spec (`Button` for `C-01 Button`) and note the ID in a comment.
- **Done when:** every component in the spec exists and renders all its variants.

## Stage 4: Contract and data layer (mock)
- First write `API-CONTRACT.md` (see `mock-data-layer.md`), then implement mock services against it.
- Start `BACKEND-RULES.md`; add an entry whenever a service simulates a business rule.
- Follow `mock-data-layer.md`. Define types/schemas from the PRD ERD, service functions from the PRD endpoints, and seeded data per role.
- Include simulated latency and error switches so loading and error states can be seen.
- **Done when:** the contract covers every endpoint a P0 feature needs, and a mock service implements each one.

## Stage 5: App shell and routing
- Navigation model from UI-SPEC Section 2 (tab bar, sidebar, top nav), route list from the Screen Inventory, and role-based access from the PRD (redirect or hide per role).
- Layout frame, responsive behavior, and global error/not-found handling.
- **Done when:** every `S-xx` route exists (even as a stub) and role access rules work.

## Stage 6: Screens (by priority)
For each screen in the UI-SPEC, in P0 → P1 → P2 order:
1. Build the layout from the wireframe using library components only.
2. Wire to the data layer.
3. Implement all states from the screen's state table, with spec copy.
4. Implement interactions and navigation targets.
5. Check responsive layouts at the spec breakpoints.
- If a needed component is missing from the library, add it to the library and log it as a spec gap in `CHANGE-REQUESTS.md`; do not make a one-off inline style.
- **Done when:** the screen matches its spec section and every state is reachable (via the state gallery).

## Stage 7: Review tools
- Build the role switcher, state gallery, component gallery, and `REVIEW.md` per `review-tools.md`, all OFF by default and shown only in review mode.
- **Done when:** the default app shows no dev controls, and in review mode a non-developer can open the app, pick a role, and reach any state of any screen without using dev tools or editing code.

## Stage 8: Verify and document
- Run build, lint, type-check, tests. Capture screenshots if the environment allows.
- Finish `README.md` and `CHANGE-REQUESTS.md`.

## Definition of Done (per pass)
All items in scope exist, all states implemented, review tools working, checklist in SKILL.md passed, and verification status stated honestly.