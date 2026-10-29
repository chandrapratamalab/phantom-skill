---
name: "prd-writer"
description: Generate a comprehensive, developer-ready PRD (Product & Technical Requirements Document) as PRD.md with Mermaid diagrams (user flow, architecture, ERD) through a clarify-then-generate workflow. Use whenever the user wants to create a PRD, spec, requirements document, technical design, or system architecture for a software, web, mobile, AI/agent, game, 3D/interactive web, CLI, or enterprise project. Also trigger on phrases like "buatkan PRD", "rancang aplikasi", "spesifikasi proyek", "dokumen kebutuhan", "saya punya ide aplikasi", "plan this app", or when the user describes a product idea and wants it planned before coding, even if they never say "PRD". Also use to revise an existing PRD.md. Do NOT use for writing code, fixing bugs, business plans, pitch decks, marketing copy, or detailed visual UI/UX design (colors, typography, pixel layouts).
---

# Universal PRD Writer

Turn any project idea into a complete, consistent, developer-ready `PRD.md`. The PRD must be good enough that a developer (or a coding agent) can break it into tasks without asking follow-up questions.

## Core Principles

1. **Language:** Write the PRD in the language the user writes in. Technical terms (API, endpoint, schema, etc.) may stay in English. Section headings stay in English for consistency across projects.
2. **Never block on questions:** Ask at most ONE round of clarification. Unanswered points get sensible defaults, which are recorded as Assumptions (never silently invented).
3. **Be concrete:** Numbers over adjectives. "p95 API latency < 300 ms", not "fast". "≥ 60 FPS on mid-range mobile", not "smooth".
4. **Stay consistent:** Every feature appears in the flow, the architecture, and (if applicable) the data model. See the Quality Checklist.
5. **Stable IDs:** FR, NFR, F, and S (screen) IDs are permanent. On revision, never renumber or reuse an ID; mark removed items as `(removed)` instead. Downstream work (design, code, tests) references these IDs.
6. **Right-size the depth:** Small MVP or prototype → concise (roughly 3-6 pages). Multi-role, multi-service, or enterprise system → full detail. Do not pad.

## Workflow

### Step 0: Check for an existing PRD

If `PRD.md` already exists in the conversation or workspace and the user asks for a change, **edit only the affected sections** (and any sections that must stay consistent with them). Do not regenerate the whole document. Briefly list what changed.

### Step 1: Analyze Context and Ask Clarifying Questions (only if needed)

**Skip this step and go straight to Step 2 when ANY of these is true:**
- The brief already states core flows, key features, and platform/architecture.
- The user says things like "build directly", "skip questions", "buat langsung", "langsung aja".
- The user answers a previous clarification round (even partially).

**Otherwise, do not generate the PRD yet.** Instead:

1. **Detect the project archetype:** SaaS/Web App, Mobile App, 3D/Interactive Web, AI Agent/Bot, Game, CLI/Plugin/Library, Enterprise/Internal System, Marketplace, or other.
2. **Ask 3 to 5 questions**, chosen from `references/question-bank.md` for that archetype. Rules:
   - Never ask what can already be inferred from the user's prompt.
   - Prioritize questions that most change architecture or scope: core goal and target user, domain-specific mechanics, MVP boundary, platform and tech constraints.
   - Put quick options in parentheses after each question so the user can answer in a few words.
   - Match the user's language.
3. **Close with this callout** (translate to the user's language):
   > *"Answer only the points you've already decided, or reply **'build directly'** (or **'buat langsung'**) and I'll use the best standard defaults."*

### Step 2: Generate the PRD

1. Read `references/template.md` and follow the 7-section structure plus the Appendix.
2. Read `references/mermaid-rules.md` before writing any diagram.
3. Apply the ID and format conventions below.
4. Run the Quality Checklist silently before delivering. Fix problems instead of reporting them.

**ID and format conventions (for traceability):**
- Functional requirements: `FR-01`, `FR-02`, ...
- Non-functional requirements: `NFR-01`, ...
- Features: `F-01`, ... each linking to the FR IDs it satisfies.
- Acceptance criteria: **Given / When / Then**, one testable behavior per criterion.
- Priorities: P0 (Must), P1 (Should), P2 (Nice-to-have). P0 should be the minimum viable launch, not everything.

**Assumptions are mandatory.** Whenever the user skipped a question or opted for "build directly", every default you picked (auth method, deployment target, platform, stack, scale) must be listed in the Assumptions section.

### Step 3: Deliver

1. Create the file `PRD.md` (in `/mnt/user-data/outputs/` when file tools are available) and present it to the user.
2. In chat, give only a short summary: 2-3 sentences on what the PRD covers, followed by the top assumptions to confirm (max 5 bullets). Do not paste the whole document into chat.
3. Offer next steps in one line: revise a section or export to another format.

## Quality Checklist (run before delivering)

- [ ] Every P0 feature has Given/When/Then acceptance criteria that can be tested.
- [ ] Every feature in Section 3 appears in the user flow (Section 4) and is covered by a module or endpoint (Section 5).
- [ ] Entities in the ERD / data schema (Section 6) match the features and endpoints.
- [ ] Success metrics in Section 1 have a number, a target, and a way to measure.
- [ ] NFRs contain concrete numbers.
- [ ] Out of Scope is explicit and does not contradict P0/P1 features.
- [ ] All Mermaid diagrams follow `references/mermaid-rules.md` and are syntactically valid.
- [ ] Assumptions and Open Questions are filled in (never empty when defaults were used).
- [ ] Section 4 has a Screen Inventory (`S-xx`) when the product has a UI; every P0 feature maps to at least one screen.
- [ ] PRD header shows Version and Date (downstream work can record which version it used).
- [ ] Language matches the user's language.

## Behavior vs. Visual Design (do not break)

`PRD.md` is the **single source of truth for behavior**: what features exist, what they do, and in what order. Visual design decisions belong outside the PRD.

- Do not put colors, fonts, spacing, or pixel layouts in the PRD. Describe behavior and states only (the Screen Inventory is the one place that names screens).

## Feedback Logging (optional, never blocks)

If `skill-feedback-logger` is installed:
- Log notable events (user corrections, validator or build failures, assumptions made, spec gaps) using its protocol.
- Before delivering, run its `scripts/check_traceability.py` when scripts can run, fix real errors, and report warnings.
- If logging or the validator is unavailable or fails, continue the workflow and mention it in one line. Never put secrets or personal data in logs, and never edit project documents because of a log entry.

## Reference Files

- `references/template.md`: Full 7-section template with the Appendix. Read in Step 2.
- `references/question-bank.md`: Clarifying questions per archetype. Read in Step 1.
- `references/mermaid-rules.md`: Syntax rules that prevent broken diagrams. Read before drawing any diagram.
