# BG-04 — TARGETED CORRECTION PASS V2 REPORT

Date: 2026-08-19  
Phase: **BG-04 — IMAGE-TEXT INVENTORY**  
Task: **ELEMENT-BY-ELEMENT AUTHORITY REBUILD**  
Result: **MANUAL DECISION REQUIRED**

## Outcome

The requested authoritative unit ledger was not completed. Independent validation confirmed that the current inventory contains page-level estimates, one individual unit ID, 38 ID ranges, and grouped target packs—not one record per semantic graphic-text unit.

The repository contains no editable graphic-generation text source or native text layer for the rasterized artwork. Exact reconstruction therefore requires manual visual transcription and verification of every graphic. Converting summaries or range descriptions into purported exact Italian strings would violate the source-authority and no-guessing rules.

The unsupported PASS and aggregate authority claims were withdrawn. BG-04 remains active and BG-05 is not authorized.

## V2 audit findings

| Severity | Before | Resolved | After |
|---|---:|---:|---:|
| CRITICAL | 2 | 0 | **2** |
| IMPORTANT | 4 | 0 | **4** |
| MICRO | 1 | 0 | **1** |

No finding was closed merely by changing report numbers.

## Structure

- Affected pages: **47**
- Graphics: **47**
- Missing affected-page records: **0**
- Duplicate affected-page records: **0**
- Page 121 documentary handling preserved: **YES**

## Unit accounting

- Previous claimed Italian units: **761 — WITHDRAWN / NON-AUTHORITATIVE**
- Authoritative rebuilt active units: **NOT ESTABLISHED**
- Excluded X units: **NOT ESTABLISHED**
- T count: **NOT ESTABLISHED**
- R count: **NOT ESTABLISHED**
- N count: **NOT ESTABLISHED**
- G count: **NOT ESTABLISHED**
- U count: **NOT ESTABLISHED**
- Arithmetic validation: **FAIL**

The earlier page-16 UI issue is still genuinely unresolved, but it cannot yet be asserted as exactly one U unit because the two screenshots contain multiple independently positioned UI strings. Its visual boundaries must be instantiated during the manual ledger rebuild.

## Bulgarian accounting

- Previous claimed targets: **752 — WITHDRAWN / NON-AUTHORITATIVE**
- Authoritative distinct Bulgarian targets: **NOT ESTABLISHED**
- T targets: **NOT ESTABLISHED**
- G/shared targets: **NOT ESTABLISHED**
- Recoverable units lacking an individually instantiated target: **PRESENT; exact count not established**
- Unsupported target-count claims remaining as authority: **0 — explicitly withdrawn**

## Authority assessment

- Units with individually instantiated authoritative source records: **1 ID exists, but the full ledger is absent**
- Units genuinely unresolved: **at least the page-16 screenshot UI region; exact U-unit count pending segmentation**
- OCR authority violations: **0**
- Terminology violations confirmed in existing explicit targets: **0**
- Exact Italian-unit authority: **FAIL**
- Exact Bulgarian-target authority: **FAIL**

## Required manual rebuild

A compliant continuation must:

1. render each of the 47 affected graphics at sufficient resolution without modifying the reference;
2. transcribe every independently meaningful visible unit;
3. assign a unique `Pxxx-Gx-Uxxx` ID to every unit;
4. record exact Italian wording or exact numeric/symbolic value;
5. assign exactly one T/R/N/G/U/X action;
6. supply exact Bulgarian targets for all T units and valid references for G units;
7. record preservation/exclusion/unresolved reasons where applicable;
8. validate uniqueness, required fields, action totals, and target totals programmatically;
9. perform a second visual verification against the final PDF.

No aggregate estimate may be promoted during that work.

## Atlas and controls

- Affected atlas pages remain: `078, 079, 081, 083, 085, 087, 090, 091, 092, 093, 094, 095`
- Page 121 preserved: **YES**
- Control-page classifications changed: **NO**
- Native BG-03 captions reclassified: **NO**

## MANUAL DECISION REQUIRED

Human direction is required on resourcing the full manual transcription and verification pass. The available repository sources do not permit an exact automatic rebuild without converting raster reading or summaries into unsupported authority.

## Immutable-reference verification

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before V2 correction attempt | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After V2 correction attempt | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

- Reference unchanged: **YES**
- PDFs modified: **NO**
- Graphics modified: **NO**
- Page masters modified: **NO**
- BG-05 started: **NO**
- `BG_PHASE_STATE.json` changed: **NO**
- Commit performed: **NO**

# FINAL RESULT: MANUAL DECISION REQUIRED

BG-04 remains active. The unsupported aggregate authorities are withdrawn, but the required exact unit ledger remains to be created manually.
