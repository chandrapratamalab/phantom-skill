# PRD Template

Use these 7 sections in this exact order, then the Appendix. Adapt the depth, not the structure. If a sub-item truly does not apply (e.g., no database in a CLI tool), replace it with the adaptive alternative described below instead of deleting the section.

```markdown
# PRD-Project: [Project Name]
> Version: 1.0 | Date: [date] | Status: Draft

## 1. Overview
- **Product Summary:** Concept, core problem solved, unique value proposition (3-5 sentences).
- **Target Audience & Personas:** For each persona: role, goals, pain points.
- **Goals & Success Metrics:**
  | Metric | Baseline | Target | How Measured |
  |---|---|---|---|
  (e.g., signup→activation rate, FPS / load time, task accuracy, 30-day retention)

## 2. Requirements
- **Functional Requirements:** `FR-01`... grouped by role, module, or screen.
- **Non-Functional Requirements:** `NFR-01`... performance, security, compatibility, accessibility, resource limits, all with numbers.
- **Out of Scope (Phase 1):** Features intentionally excluded, with a one-line reason each.

## 3. Core Features
For each feature `F-xx: [Name]`:
- **Priority:** P0 / P1 / P2
- **Satisfies:** FR-xx, FR-yy
- **User Story:** As a [role], I want to [action], so that [benefit].
- **Acceptance Criteria:**
  - Given [context], When [action], Then [observable result].
- **Edge Cases & Fallbacks:** Errors, empty states, offline / weak devices / unsupported browsers, failed requests, permission denied.

## 4. User Flow
- **Step-by-Step Journey:** Numbered path from entry to goal completion, including at least one failure path.
- **Visual Flowchart:** One `mermaid` diagram (`flowchart TD` or `sequenceDiagram`). Split into several diagrams if more than ~15 nodes.
- **Screen Inventory** (include whenever the product has a UI; skip for CLI/library/backend-only):
  | Screen ID | Name | Purpose | Features (F-xx) | Entry Points | Role / Access |
  |---|---|---|---|---|---|
  Screen IDs (`S-01`...) are stable and never renumbered. This table names screens only; it does not describe their visual design.

## 5. Architecture
- **System Overview:** How UI, logic, APIs, render loops, and external services interact.
- **Architecture Diagram:** `mermaid` diagram.
- **Folder Structure:** Recommended directory layout (code block).
- **Core Modules / Endpoints:**
  | Module / Route | Method / Trigger | Purpose | Related Feature |
  |---|---|---|---|

## 6. Database Schema (Adaptive)
- **Backend / persistent app:** Mermaid `erDiagram` plus table definitions:
  | Field | Type | Constraints | Notes |
  |---|---|---|---|
  Include PK/FK, indexes for frequent queries, and relationships.
- **Frontend-only / static / 3D / game / CLI / tool:** Define instead the Local State Schema, Config JSON structure, Asset Manifest, or Event/Form Payload schema.

## 7. Tech Stack
| Layer | Choice | Why (tied to the user's constraints) |
|---|---|---|
| Frontend / UI | | |
| Logic / Backend | | |
| Data / Assets | | |
| Deployment / CI | | |

## Appendix (Optional, include when relevant)
### A. Assumptions & Open Questions
- **Assumptions:** Defaults chosen because the user did not specify them (e.g., "Auth: email + password", "Deploy: Vercel", "Mobile-first responsive").
- **Open Questions:** Items to confirm before development starts.

### B. Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|

### C. Milestones
| Phase | Scope | Exit Criteria |
|---|---|---|
```

## Depth Guide

| Project size | Depth |
|---|---|
| Landing page, prototype, small tool | Short bullets, 1 diagram per section max, Appendix A only |
| Standard MVP (SaaS, mobile app, bot) | Full 7 sections, Appendix A + C |
| Multi-role, multi-service, enterprise | Full detail, all appendices, separate diagrams per major flow |

## Archetype Notes

- **SaaS / Web App:** Roles and permissions, billing/subscription logic, multi-tenancy, onboarding flow.
- **Mobile App:** Offline behavior, push notifications, platform permissions, store requirements.
- **3D / Interactive Web:** Asset pipeline and budgets (poly count, texture size), scroll/interaction triggers, fallback for low-end GPUs and reduced-motion users.
- **AI Agent / Bot:** Tools and their schemas, context/memory strategy, guardrails, failure and hallucination handling, evaluation criteria, cost per task.
- **Game:** Core loop, progression, state/save schema, input methods, performance targets.
- **CLI / Plugin / Library:** Command surface, config format, exit codes, versioning, distribution.