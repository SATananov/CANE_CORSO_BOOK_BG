# BG ORCHESTRATOR

Role: phase controller for the Bulgarian Cane Corso edition.

## Startup sequence

1. Read `AGENTS.md`.
2. Read `BG_MASTER_PLAN.md`.
3. Read `BG_STYLE_LOCK.md`.
4. Read `BG_TRANSLATION_RULES.md`.
5. Read `BG_PHASE_STATE.json`.
6. Verify the Italian reference exists and its SHA-256 matches the locked value.
7. Determine the active phase.
8. Perform only work permitted by that phase.

## Current initial assignment

BG-01 is REPORT ONLY.

For BG-01:
- inspect all 143 pages;
- populate `BG_PAGE_INVENTORY.md`;
- do not translate;
- do not edit PDFs;
- do not create replacement graphics;
- do not advance to BG-02 automatically.

## Phase completion

At the end of a phase:
- create a phase report under `reports/bg/`;
- list PASS / FAIL / MANUAL DECISION REQUIRED;
- state files created/changed;
- state whether IT reference hash remained unchanged;
- wait for human approval before changing `BG_PHASE_STATE.json`.

## Forbidden

- skipping phases
- changing immutable style rules
- modifying IT reference
- silently solving ambiguity by invention
- declaring FINAL from partial page coverage
