---
name: prd-writer
description: Generate a comprehensive Product and Technical Requirements Document (PRD-Project) with visual Mermaid diagrams through an interactive two-step workflow. Use when the user asks to create a PRD, plan any software/web/mobile/AI/game project, write specifications, or design system architecture.
---

# Universal PRD Writer

Transform any project idea into a complete, developer-ready Product and Technical Requirements Document (`PRD.md`).

## Workflow

### Step 1: Analyze Prompt & Ask Dynamic Clarifying Questions

**DO NOT generate the full PRD on the first turn** unless the user explicitly says "buat langsung" / "skip questions" or already provided complete details.

1. **Detect Project Nature:** Identify what the user is building from their prompt (e.g., 3D/Motion Website, SaaS/Web App, Mobile App, AI Agent/Bot, Game, CLI/Plugin, or Enterprise System).
2. **Ask 4 to 5 Hyper-Relevant Questions:** Formulate questions strictly tailored to that specific project's domain:
   - Ask about the **core goal/target user** and expected final action.
   - Ask about **domain-specific mechanics** (e.g., 3D/scroll interactions for a motion page; user roles & payment flow for SaaS; trigger/API flow for a bot; game loop for a game).
   - Ask about **MVP scope boundaries** and **technical/library preferences** or device constraints.
3. **Provide Quick Examples:** Include short options in parentheses after each question so the user can reply quickly, and remind them: *"Jawab poin yang sudah ada di bayangan Anda, atau ketik **'buat langsung'** agar saya pilihkan opsi terbaik secara otomatis."*

---

### Step 2: Generate the 7-Section PRD-Project

Once the user answers (or asks to proceed immediately), save the output to `PRD.md` (if in a code workspace) and present the document following this exact 7-section structure, dynamically adapting the technical content to the project type:

```markdown
# PRD-Project: [Project Name]
## Requirements Document

### 1. Overview
- **Product Summary:** Concept, core problem solved, and unique value proposition.
- **Target Audience & Personas:** User roles, goals, and pain points.
- **Goals & Success Metrics:** Measurable KPIs suited to the project (e.g., conversion rate, FPS/load speed, retention, or task accuracy).

### 2. Requirements
- **Functional Requirements:** Core capabilities grouped logically by role, module, or screen section.
- **Non-Functional Requirements:** Performance benchmarks, responsiveness, security, compatibility, and resource limits.
- **Out of Scope (Phase 1):** Features intentionally excluded from the initial version.

### 3. Core Features
For each feature/module, specify:
- **Priority:** P0 (Must-Have), P1 (Should-Have), P2 (Nice-to-Have).
- **User Story:** As a [role], I want to [action], so that [benefit].
- **Acceptance Criteria:** Concrete, testable pass/fail conditions.
- **Edge Cases & Fallbacks:** Handling errors, empty states, weak devices/unsupported browsers, or failed requests.

### 4. User Flow
- **Step-by-Step Journey:** Chronological user or system interaction path from start to finish.
- **Visual Flowchart:** Render a clean `mermaid` diagram (`flowchart TD` or `sequenceDiagram`).

### 5. Architecture
- **System & Folder Structure:** High-level component interaction and recommended directory layout.
- **Architecture Diagram:** Render a `mermaid` diagram showing how UI, logic, APIs, render loops, or external services connect.
- **Core Modules / Endpoints:** Table of key routes, controllers, or event handlers.

### 6. Database Schema (Adaptive to Project Type)
- **If Backend / Persistent App:** Provide a Mermaid `erDiagram` and table schemas (Fields, Types, PK/FK constraints, Relationships).
- **If Frontend-Only / Static / 3D / CLI / Tool:** Define the Local State Schema, Configuration JSON structure, Asset Manifest, or Form/Event Payload schema instead of SQL tables.

### 7. Tech Stack
Recommend the optimal tools with brief justifications tailored to the user's constraints (Frontend/UI, Logic/Backend, Data/Assets, Deployment).
```

## Diagram & Quality Rules

- **Valid Mermaid Only:** Always wrap node labels containing spaces, parentheses, or symbols in double quotes (e.g., `A["Hero Section (3D View)"] --> B["Scroll Trigger"]`) so diagrams render cleanly without syntax errors.
- **Zero Fluff:** Keep specifications concrete, actionable, and ready for direct implementation by developers or AI coding agents.