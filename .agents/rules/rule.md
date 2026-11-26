---
trigger: always_on
---

# Yugaantar Agent Rules

## 1. Anti-"Vibe-Coded" UI & Design Rules (Do NOT Do These)
When designing or building websites, landing pages, or web apps, **NEVER** fall back to generic AI clichés:

- **No purple gradients** as default hero/card accents.
- **No Lucide icons** or **sparkle icons** (`✨`) as lazy visual filler.
- **No 3-cards-in-a-row** generic feature grids.
- **No bento grids** unless genuinely justified by the content hierarchy.
- **No glass cards** (`backdrop-blur` translucent cards everywhere).
- **No emojis in headings** (H1/H2/H3).
- **No em-dashes everywhere** (`—`) in UI copy.
- **No generic 3 pricing tiers** template layout.
- **No fake testimonials** or invented user quotes/avatars.
- **No dot-grid backgrounds** or **glowing orbs** behind sections.
- **No color-stripe-on-cards** (generic colored top/left border stripes).
- **No excessive/generic hover animations** on every element.
- **No `"Vite + React"` tab title** — always set a real, intentional `<title>`.
- **No default favicon** — always provide a real/custom favicon.
- **No `Lorem ipsum`** or placeholder copy — write real, domain-accurate copy.
- **No default `Inter` / `Geist` font** — choose intentional typography with character.
- **No generic SaaS template layouts** (cookie-cutter centered hero + 2 buttons + 3-column feature grid + pricing + fake FAQ); design layout around the actual product's content and user workflow.
- **Intentional spacing, contrast, and typography:** Maintain clear visual hierarchy, strong foreground/background contrast, and consistent spacing scales rather than uniform `p-6` cards everywhere.
- **Purposeful motion only:** Keep UI transitions fast (under 300ms) with natural easing (`ease-out` for entering elements); never animate every element on hover or scroll.
- **Reference design craft skills:** When building UI, follow installed skills (`emil-design-eng`, `impeccable`, `design-taste-frontend`, `web-design-guidelines`).

## 2. Zero-Hallucination & Precision Rules (Mandatory)
- **Never fabricate facts:** Never invent file paths, symbol names, API endpoints, CLI flags, package versions, counts, or command/test outputs.
- **Verify before stating:** Only state behavior, code, or tool results you directly observed in files you read or command output from the current session.
- **Verify after editing:** Run the relevant tests, linters, or builds after your final edit and report the exact observed scope and result—never claim "done" or "passing" from memory or partial/mocked runs.
- **No silent guessing:** If requirements, credentials, or APIs are missing or ambiguous, state what is missing and ask or report the blocker instead of guessing or faking a workaround.
- **Surgical precision:** Make the smallest, cleanest change required. Do not rewrite unrelated code, delete comments/docstrings, or add speculative abstractions.

## 3. Memory & Persistent Context
- **Persist decisions and progress:** Use installed memory skills (`agent-memory`, `memory-systems`, `conversation-memory`, `planning-with-files`, `session-handoff`) for multi-step or cross-session work so context is never lost or re-guessed.

## 4. Planning & Engineering Discipline
- **Before coding a new feature or project**, outline or prepare:
  1. Product Requirements Document (PRD)
  2. Technical Requirements Document (TRD)
  3. UI/UX Design Document
  4. Backend Schema
  5. Research
- **Think before coding:** State assumptions and trade-offs explicitly; do not silently guess.
- **Simplicity & surgical changes:** Write the minimal clean code needed; do not rewrite unrelated code or add speculative abstractions.
- **Verify before claiming done:** Run tests, builds, or checks after edits and only report observed results.
