# Mock Data Layer

Goal: the screens must not know whether data is fake. When the real backend arrives, only this layer changes.

## Contract first (prevents double work later)
Before writing services, create `API-CONTRACT.md` from PRD Sections 5-6 and treat it as the agreement between frontend and the future backend:
- For each endpoint: method + path, auth/role required, request fields (type, required, validation limits), success response shape, **error shape** (validation, not found, forbidden, conflict, server error), pagination/filter/sort format.
- Status values and allowed transitions (state machine) where the PRD defines them.
- Anything the PRD leaves open is marked `TBD` and logged as a Change Request, not guessed.
Mock services implement exactly this file. The backend later implements the same file, so swapping is a change in one layer only.

## Structure (any stack)
```
data/
  types      # entities from PRD Section 6 (ERD / schemas)
  seed       # seeded records, grouped by role scenario
  services   # one function per PRD endpoint / operation (Section 5)
  client     # the only place that decides "mock" vs "real"
```
- **types:** mirror the ERD fields and relations exactly. If the PRD uses different names in endpoints and tables, follow the endpoints for service I/O.
- **services:** same inputs and outputs as the PRD endpoints (including pagination, filters, and error shapes if defined). Components import services only, never `seed`.
- **client:** a single switch (config/env) between mock and real implementations. Real implementations can be empty stubs that throw "not implemented" until the backend exists.

## Behavior to simulate
- **Latency:** 300-800 ms random delay, configurable, so loading states are visible.
- **Errors:** a dev switch to force errors (network failure, validation error, permission denied, not found) per service or globally.
- **Persistence:** in-memory state during a session so create/update/delete flows feel real; optionally restore a clean seed with one reset action. Use browser storage only if the platform supports it and it is not blocked by the environment; otherwise keep memory only.
- **Auth:** a fake session from the role switcher. Permission checks follow PRD roles; never trust the client in the real backend later (note this in README).

## Seed data quality
Seed data decides whether reviewers believe the UI. Include:
- Realistic names, dates, amounts in the product's locale and language.
- **Extremes:** very long names/titles, empty collections, a single item, hundreds of items, zero and very large numbers, missing optional fields.
- **Every status** the PRD defines (e.g., draft, pending, approved, rejected), so all badges and flows appear.
- Per-role scenarios: each role has records they can act on and records they cannot.

## Do not
- Invent entities, fields, or rules not in the PRD. If a screen needs data the PRD lacks, log a Change Request and use a clearly marked placeholder.
- Embed mock values inside components or hardcode strings that should come from the spec's microcopy.
- Implement business logic in the client that belongs to the backend (pricing, availability/conflict checks, permission enforcement, status transitions, calculations). The client may do **presentational validation only** (required, format, length). Simulate rules inside the mock **service**, mark each with `// BACKEND RULE: <short description>`, and list them in `BACKEND-RULES.md` (rule, where simulated, PRD reference, expected real behavior). That file is the handoff to the backend.

## Backend swap checklist (for later)
1. Implement real services with the same signatures.
2. Flip the client switch.
3. Remove or isolate seed and dev tools.
4. Re-run the state gallery to confirm every state still works with real responses.