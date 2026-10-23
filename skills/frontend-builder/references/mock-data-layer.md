# Mock Data Layer

Goal: the screens must not know whether data is fake. When the real backend arrives, only this layer changes.

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
- Implement business logic in the client that belongs to the backend (pricing, permission enforcement, calculations). Simulate the result only, and note it as "backend responsibility" in comments.

## Backend swap checklist (for later)
1. Implement real services with the same signatures.
2. Flip the client switch.
3. Remove or isolate seed and dev tools.
4. Re-run the state gallery to confirm every state still works with real responses.