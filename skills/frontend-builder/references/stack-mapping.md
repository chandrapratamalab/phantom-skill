# Stack Mapping (neutral)

## Choosing the stack
1. **PRD Section 7 names a stack:** use it. Do not substitute.
2. **PRD gives constraints but no stack** (e.g., "SEO matters", "offline use", "team knows X"): pick a stack that satisfies them; state why.
3. **Nothing specified:** choose a mainstream default for the platform and record it in Assumptions:
   - Web app / SaaS / dashboard: a component-based framework with TypeScript, a utility- or token-friendly styling approach, and a client-side router (or the framework's file routing).
   - Content/marketing site with SEO: a framework with static or server rendering.
   - Mobile: cross-platform framework unless the PRD requires native.
   - Desktop: web stack wrapped, unless the PRD requires native.
   Prefer widely documented, actively maintained tools. Pin dependency versions in the lockfile.

If the platform itself (web / mobile / desktop) is ambiguous, ask one question. Otherwise decide and proceed.

## Spec concept → implementation (any stack)
| Spec concept | Implementation idea |
|---|---|
| Design tokens (UI-SPEC §4) | CSS variables / theme object / design-token file; semantic roles, not raw values |
| Typography scale | Named text styles or classes; fonts with fallbacks |
| Breakpoints & grid | Shared constants used by layout primitives and media queries |
| Components `C-xx` (§5) | One component per spec entry with typed props for variants and states |
| Screens `S-xx` (§6) | One route/screen module per entry; composed only from library components |
| Navigation model (§2) | App shell with route table generated from the Screen Inventory |
| Role access (PRD) | Route guards + role-aware navigation, reading the fake session |
| States table | Explicit state handling (loading/empty/error/success) per screen, not ad hoc |
| Microcopy (§7) | Centralized strings file (also prepares for i18n) |
| Motion `M-xx` (§9) | Shared transition utilities; respect reduced-motion setting |
| Endpoints (PRD §5) | Service functions in the data layer |
| ERD (PRD §6) | Types/schemas in the data layer |

## Project structure (adapt to stack conventions)
```
src/
  tokens/        # theme, fonts, breakpoints
  components/    # C-xx library
  screens/       # S-xx modules
  data/          # types, seed, services, client (see mock-data-layer.md)
  routes/        # route table, guards
  content/       # microcopy strings
  review/        # dev-only: role switcher, galleries (REVIEW_MODE)
```
Follow the framework's own conventions where they differ (file-based routing, app directories, etc.).

## Quality floor regardless of stack
- Strict type checking where the language supports it.
- Linting and formatting configured.
- Accessible markup: semantic elements, labels, focus management, ARIA only where needed.
- No dependency added without a reason tied to the spec; no abandoned packages.
- No secrets or real credentials in the prototype.