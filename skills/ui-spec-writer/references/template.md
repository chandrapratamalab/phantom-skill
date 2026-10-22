# UI-SPEC Template

Follow this order. Adapt depth to project size (small MVP: 3-5 screens, compact; large product: full detail per screen). Keep the structure; if a part does not apply, replace it with a one-line note instead of deleting it.

```markdown
# UI-SPEC: [Project Name]
> Version: 1.0 | Date: [date] | Built from: PRD.md v[x.y] ([PRD date]) | Status: Draft

## 1. Design Direction
- **Subject & Audience:** One sentence from the PRD personas.
- **Mood:** 3-4 words (e.g., calm, precise, warm).
- **Visual vernacular:** What in this subject's world informs the look (materials, tools, industry conventions).
- **Memorable move:** The ONE distinctive element; everything else stays quiet.
- **Avoid:** 3-5 things this design should not look like.
- **Platform & responsive targets:** From PRD (e.g., mobile-first web, 360 / 768 / 1280 px).

## 2. Information Architecture
- **Sitemap / Navigation:** `mermaid` flowchart of screens (use S-xx IDs).
- **Navigation model:** Tab bar / sidebar / top nav, and why.
- **Role access:** Which roles see which screens (from PRD).

## 3. Screen Inventory & Traceability
| Screen | Name | Serves Features | PRD Flow Step | Priority |
|---|---|---|---|---|
| S-01 | | F-01, F-02 | Flow step 2 | P0 |

## 4. Design Tokens
Define once. Screens reference these names.
- **Color:** 4-6 base named hex values + semantic roles (`color.surface`, `color.text`, `color.text-muted`, `color.primary`, `color.danger`, `color.success`, `color.border`). Add dark-mode values only if the PRD or user asks for them.
  | Token | Value | Use | Contrast |
  |---|---|---|---|
- **Typography:** Typeface(s) and roles, type scale (size / line-height / weight), line length limit (<80 chars).
- **Spacing scale:** e.g., 4 / 8 / 12 / 16 / 24 / 32 / 48.
- **Radius & elevation:** Tied to hierarchy, not one value for everything.
- **Breakpoints & grid:** Columns, gutters, margins.

## 5. Component Library
For each `C-xx: [Name]`:
- **Purpose:** One line.
- **Variants:** (e.g., Primary / Secondary / Destructive)
- **States:** default, hover, focus, active, disabled, loading, error.
- **Anatomy & sizing:** Slots, min size, padding (token names).
- **Behavior:** Interactions, keyboard support.

## 6. Screen Specifications
For each screen `S-xx: [Name]`:
- **Serves:** F-xx, F-yy | **Role:** ... | **Entry / Exit:** ...
- **Layout (mobile):** ASCII wireframe.
  ```
  +------------------+
  | Header      [ ≡ ]|
  +------------------+
  | Content          |
  +------------------+
  ```
- **Layout (desktop):** Describe changes or add a second wireframe.
- **Components used:** C-xx list, with the key content/data shown.
- **Interactions:** Tap/click/keyboard behavior, navigation targets (S-xx).
- **States:**
  | State | What the user sees | Copy |
  |---|---|---|
  | Default | | |
  | Loading | | |
  | Empty | | |
  | Error | | |
  | Success | | |
  (Add offline, permission-denied, partial data when relevant.)
- **Acceptance (visual/interaction):** Given/When/Then, only for UI-specific behavior.

## 7. Microcopy & Content
- **Voice:** Plain verbs, sentence case, active voice.
- **Key strings:** Buttons, toasts, empty and error messages. The same action keeps the same name across the flow.

## 8. Accessibility
Contrast results, focus order and visible focus style, touch target sizes, labels for inputs and icons, reduced-motion behavior, screen-reader notes for non-obvious components.

## 9. Motion
`M-xx` list: trigger, what changes, duration/easing, reduced-motion fallback. Motion responds to user actions; at most one orchestrated non-user-triggered moment.

## 10. Assumptions, Open Questions & PRD Change Requests
- **Assumptions:** Defaults chosen because the user did not specify (mood, typeface, dark mode, etc.).
- **Open Questions:** To confirm before build.
- **PRD Change Requests:**
  | # | Type (gap / conflict) | Proposed change | Affects (F-xx / S-xx) |
  |---|---|---|---|
  The PRD is NOT edited by this skill. The user confirms, then prd-writer applies it.

## 11. Change Log
| Date | Change | Screens affected | PRD version |
|---|---|---|---|
```

## Depth Guide

| Project size | Depth |
|---|---|
| Landing page / small tool | Sections 1, 4, 6 (compact), 8, 10; components inline |
| Standard MVP | Full structure, 5-12 screens, compact component list |
| Multi-role / enterprise | Full detail, role-specific variants, data-dense states (tables, filters, bulk actions) |