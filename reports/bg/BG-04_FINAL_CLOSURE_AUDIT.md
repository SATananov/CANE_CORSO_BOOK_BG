# BG-04 — FINAL INDEPENDENT CLOSURE AUDIT

Date: 2026-08-19  
Phase audited: **BG-04 — ACTIVE**  
Mode: **REPORT ONLY**  
BG-05 readiness: **NOT READY**

## Executive result

The affected-page and affected-graphic structure is correct at **47/47**. PAGE 16 independently passes with **106** individually instantiated units and no unresolved U record.

The current inventory does not, however, contain an active unit-level ledger for the other 46 graphics. Its own controlling notice states that range-form IDs and grouped target packs are withdrawn as acceptance authority, that no aggregate or range record is an active construction unit, and that the inventory is not construction-ready. The only conforming active records are the 106 PAGE 16 records.

Consequently, the complete 47-graphic totals, target coverage, terminology coverage and construction readiness required by this gate cannot be established. The later PASS claim in `BG-04_IMAGE_TEXT_INVENTORY_REPORT.md` conflicts with the controlling content of the current inventory and is not supported by active records.

## Audit 1 — structure

| Check | Result |
|---|---:|
| Affected BG-04 pages | **47/47 — PASS** |
| Affected graphics | **47/47 — PASS** |
| Missing affected pages | **0** |
| False-positive affected pages | **0** |
| Duplicate page/graphic records | **0** |
| Graphics with a page-level inventory record | **47/47** |
| Graphics with a conforming active unit ledger | **1/47** |

Affected pages verified against `BG_TEXT_MASTER_INDEX.md`:

`001, 006, 011, 014, 016, 018, 041, 044, 048, 050, 051, 054, 061, 066, 068, 070, 076, 078, 079, 081, 083, 085, 087, 090, 091, 092, 093, 094, 095, 097, 098, 101, 103, 105, 106, 108, 110, 113, 116, 117, 121, 122, 125, 128, 131, 133, 134`.

## Audit 2 — authoritative active-unit ledger

The withdrawn figures **761** and **752** were not used. Counts below are derived only from current, individually instantiated `P016-GA-Uxxx` table records. Range headings such as `P061-061-A-E01–E22` are excluded because the inventory expressly says that no range record is an active construction unit.

| Measure | Count |
|---|---:|
| Final authoritative active units | **106** |
| T — translate | **89** |
| R — retain unchanged | **16** |
| N — numeric/symbolic | **1** |
| G — grouped | **0** |
| U — unresolved | **0** |
| Unique Unit IDs | **106** |
| Duplicate Unit IDs | **0** |

Arithmetic reconciliation:

`106 = 89 + 16 + 1 + 0 + 0` — **PASS**.

All 106 active records contain a unique ID, page and graphic identity, visual position/type, Italian text or symbolic value, verification basis, action class, Bulgarian target or retention/reproduction instruction, and reconstruction/terminology note.

This arithmetic describes PAGE 16 only. It is not a complete-book BG-04 unit total.

## Audit 3 — Bulgarian target authority

| Check | Result |
|---|---:|
| Distinct Bulgarian translated targets among active T units | **85** |
| Active T units lacking targets | **0** |
| Unsupported active Bulgarian targets | **0** |
| Active R units without intentional retention basis | **0** |
| Active N units without reproduction instruction | **0** |
| Invalid active G relationships | **0** |
| Active U units | **0** |
| Recoverable units lacking conforming active records/targets | **PRESENT — exact count cannot be derived; 46 graphics lack an active unit ledger** |

Four Bulgarian target strings intentionally occur twice on PAGE 16 because they occupy separate visible interface positions: `История`, `Помощ`, `Кандидатствай като партньор`, and the repeated Knowledge Center explanatory paragraph. They are distinct units but not distinct target strings.

## Audit 4 — PAGE 16

| Check | Result |
|---|---:|
| Current PAGE 16 units | **106** |
| Unique PAGE 16 IDs | **106** |
| Duplicate PAGE 16 IDs | **0** |
| Previous U regions resolved | **6/6** |
| Remaining PAGE 16 U units | **0** |
| Original screenshots correspond to embedded LEFT/RIGHT UI | **YES** |
| Omitted screenshot UI region found | **0** |
| Unsupported UI translation found | **0** |
| PAGE 16 construction-ready | **YES** |

The human-reviewed source package, rather than OCR, is recorded as authority. PAGE 16 was not reverted to its superseded 18-block representation.

## Audit 5 — historical BG-04 findings

| Historical category | Closure result |
|---|---|
| V1 CRITICAL: affected-page/graphic identity | **CLOSED** |
| V1/V2 CRITICAL: individually addressable ledger for every graphic | **OPEN for 46/47 graphics** |
| V1/V2 CRITICAL: countable exact target authority | **OPEN for 46/47 graphics** |
| Twenty-five recoverable B blocks | **Target-pack prose exists, but closure is not accepted because the packs are range/group summaries explicitly declared non-active** |
| Previous D item, PAGE 121 | **Documentary decision handled correctly; active R-unit ledger still absent** |
| Previous PAGE 16 A/U uncertainty | **CLOSED** |
| Previous MICRO documentary classification | **CLOSED semantically** |

Historical BG-04 failures closed: **NO**.

## Audit 6 — visual atlas pages 78–96

The affected visual-atlas graphics are correctly identified on pages 78, 79, 81, 83, 85, 87 and 90–95. Pages 80, 82, 84, 86, 88, 89 and 96 contain native BG-03 prose/captions rather than embedded graphic language.

| Page | Result | Finding |
|---:|:---:|---|
| 78 | **CRITICAL** | Graphic identified and target pack present, but no active individual unit records. |
| 79 | **CRITICAL** | Range/group pack is explicitly non-active; construction completeness is not independently countable. |
| 80 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |
| 81 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 82 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |
| 83 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 84 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |
| 85 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 86 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |
| 87 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 88 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |
| 89 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |
| 90 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 91 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 92 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 93 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 94 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 95 | **CRITICAL** | Range/group pack is explicitly non-active. |
| 96 | **PASS** | No BG-04 embedded-text graphic; native BG-03 caption remains excluded. |

Visual atlas result: **7 PASS / 0 IMPORTANT / 12 CRITICAL**. Expected 19/19 PASS is not met.

No native BG-03 caption duplication or unsupported inferred text was found in the seven correctly excluded pages. The 12 affected graphics cannot be certified complete from non-active range/group packs.

## Audit 7 — terminology

- Confirmed terminology violations in the 106 active records: **0**.
- `Кане Корсо` and retained names/brands in PAGE 16 follow the human-reviewed authority and terminology lock.
- Full 47-graphic terminology compliance: **NOT AUDITABLE**, because 46 graphics lack active unit records.
- The historical target packs visibly use locked forms including `Pugnax`, `Mastino Abruzzese`, `молос/молосоид`, `функционална приемственост`, `генеалогична приемственост` and `ФУНКЦИЯТА ФОРМИРА ТИПА`, but those packs cannot be promoted as active unit authority under the inventory's own notice.

Terminology violations established: **0**. Completeness gate: **FAIL**.

## Audit 8 — OCR and invention

| Check | Result |
|---|---:|
| OCR authority violations | **0** |
| Unsupported Italian transcriptions among active units | **0** |
| Unsupported Bulgarian targets among active units | **0** |
| Invented graphic text among active units | **0** |
| Human visual/source verification of PAGE 16 correctly identified | **YES** |

These zeroes apply to the active PAGE 16 ledger; they do not cure absent active records for the remaining graphics.

## Audit 9 — BG-05 construction readiness

| Measure | Result |
|---|---:|
| Construction-ready graphics | **1/47** |
| Not construction-ready | **46/47** |
| BG-05 readiness | **NOT READY** |

PAGE 16 is ready. The remaining 46 graphics have page-level descriptions and/or historical range target packs, but not active per-unit records satisfying the required fields. PAGE 121 remains a correct documentary-preservation decision, yet its eight sign units are represented only by a withdrawn range-form record and therefore do not satisfy this audit's unit-ledger gate.

## Issue register

### CRITICAL — 2

1. **Incomplete active unit ledger.** Forty-six of 47 graphics have no conforming active unit records; the final authoritative whole-inventory unit and action totals cannot be calculated.
2. **Unsupported construction-ready claim.** The inventory report claims PASS, while the current inventory explicitly says `NOT CONSTRUCTION READY`, declares its range/group records non-active, and requires a conforming rebuild. The historical element-addressability and exact-target failures therefore remain open.

### IMPORTANT — 2

1. **Visual atlas closure fails:** 12 affected atlas graphics lack active per-unit records; the atlas result is 7/19 PASS rather than 19/19.
2. **PAGE 121 is semantically correct but ledger-incomplete:** preservation is justified, yet eight independently addressable active R records are absent.

### MICRO — 0

None.

### MANUAL DECISION REQUIRED — 0

No source-meaning decision is required for this audit result. The blocker is a clearly defined missing conforming ledger, not an ambiguous editorial choice.

## Required report fields

- Affected pages: **47/47**
- Graphics: **47/47 identified; 1/47 with active unit ledger**
- Final authoritative active-unit count: **106**
- T / R / N / G / U: **89 / 16 / 1 / 0 / 0**
- Arithmetic reconciliation: **PASS — 106 = 89 + 16 + 1 + 0 + 0**
- Duplicate Unit IDs: **0**
- Distinct Bulgarian translated targets: **85**
- Unsupported targets: **0 among active units**
- Recoverable units lacking targets: **PRESENT; exact count not derivable because 46 graphics lack active units**
- Unresolved U units: **0 active units**
- PAGE 16 result: **PASS**
- PAGE 16 units: **106**
- Historical BG-04 failures closed: **NO**
- PAGE 121 result: **PASS documentary handling / IMPORTANT ledger conformance**
- Visual atlas 78–96: **7 PASS / 12 CRITICAL**
- Terminology violations: **0 confirmed; full coverage not auditable**
- OCR authority violations: **0**
- Unsupported Italian transcriptions: **0 among active units**
- Construction-ready graphics: **1/47**
- CRITICAL issues: **2**
- IMPORTANT issues: **2**
- MICRO issues: **0**
- MANUAL DECISION REQUIRED items: **0**
- BG-05 readiness: **NOT READY**

## Immutable reference

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

Reference unchanged: **YES**

## Safety

- PDFs modified: **NO**
- Production graphics modified: **NO**
- Page masters modified: **NO**
- BG-05 started: **NO**
- Phase state changed: **NO**
- Commit performed: **NO**

# FINAL RESULT: FAIL

BG-04 remains active. Stop before BG-05.
