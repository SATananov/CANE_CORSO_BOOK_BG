# BG-04 — TARGETED CORRECTION PASS REPORT

Date: 2026-08-19  
Phase: **BG-04 — IMAGE-TEXT INVENTORY**  
Mode: **TARGETED CORRECTION / INVENTORY ONLY**  
Result: **PASS WITH MANUAL REVIEW QUEUE**

## Authorized scope completed

The correction pass addressed the two CRITICAL, three IMPORTANT, and one MICRO findings in `BG-04_INDEPENDENT_ACCEPTANCE_AUDIT.md`; rechecked all 27 classified manual blocks; resolved all 25 class-B blocks; removed the class-D page-121 block from the translation/manual queue; and preserved the single class-A page-16 unit without guessing.

No PDF, graphic, Bulgarian page master, source file, or phase state was modified. BG-05 was not started.

## Pages and graphics affected

Inventory/authority data updated for 38 pages and 38 graphics:

`011, 018, 044, 048, 061, 066, 070, 076, 078, 079, 081, 083, 085, 087, 090, 091, 092, 093, 094, 095, 097, 098, 101, 103, 105, 106, 108, 110, 113, 116, 117, 121, 122, 125, 128, 131, 133, 134`

Page 16 / graphic 016-A was also rechecked against every named authority but remains unchanged as the isolated A-class exception.

## Finding closure

| Severity | Before | Resolved | After |
|---|---:|---:|---:|
| CRITICAL | 2 | 2 | **0** |
| IMPORTANT | 3 | 3 | **0** |
| MICRO | 1 | 1 | **0** |

### CRITICAL closure

1. Added stable element-ID rules and explicit target packs. Visible headings, paragraphs, bullets, cells, numbers, credits, warnings, and preservation-only strings are separately addressable in visual reading order.
2. Withdrew the unsupported 734-target figure. The corrected authority distinguishes 752 Bulgarian targets, 8 preserve-unchanged documentary strings, and 1 genuinely unresolved UI string. Directive-only wording is superseded by explicit construction packs; BG-05 may not translate or infer text.

### IMPORTANT closure

1. All 25 recoverable blocks were manually read from enlarged final-PDF pages, checked against editable/source context, translated under the terminology lock, and marked `RESOLVED / AUTHORITATIVE TARGET READY`.
2. Dense tables and medical graphics now include explicit rows, cells, units, ranges, cautions, and source-status instructions for pages 61, 97, 101, 103, 105, 106, 108, 110, 113, 116, and 117.
3. Atlas pages 79, 81, 83, 85, 87, and 90–95 now have explicit region/card/note/legend targets and mandatory hypothesis/non-genealogy wording.

### MICRO closure

Page 121 is now classified as `D — NO IN-IMAGE BULGARIAN TARGET REQUIRED`. Its authentic photographed signage remains untouched and is excluded from the manual translation queue. An optional accessibility legend, if later authorized, must be placed outside the photograph.

## Manual-review queue

| Class | Before | Result | After |
|---|---:|---|---:|
| A — genuinely unresolved | 1 | Rechecked; retained | **1** |
| B — recoverable | 25 | Resolved | **0** |
| D — duplicate/not required | 1 | Verified and removed from queue | **0** |

- B resolved: **25/25**
- B remaining: **0**
- D verified/removed from translation queue: **1/1**
- A after: **1**

The remaining unit is `P016-016-A-E09`, fine interface text inside the two embedded USG website screenshots. The final visual authority, editable manuscripts, source map, Flavio corpus, and correspondence do not safely establish every string. It remains explicitly marked:

`UNRESOLVED GRAPHIC TEXT — MANUAL REVIEW REQUIRED`

It does not contaminate resolved page-16 headings, archive paragraph, QR identity, or credit.

## Counts before and after

| Measure | Before | After |
|---|---:|---:|
| BG-04 pages | 47 | **47** |
| Graphics | 47 | **47** |
| Italian text units | 761 | **761** |
| Bulgarian targets | 734 reported | **752 verified** |
| Preserve-unchanged documentary units | not separated | **8** |
| Unresolved blocks/units | 27 | **1** |
| LOW graphics | 7 | **7** |
| MEDIUM graphics | 13 | **13** |
| HIGH graphics | 27 | **27** |

The Italian-unit count remains 761 because page-121 signage is genuine visible Italian text and remains inventoried; only its incorrect translation-queue status was removed.

## Atlas and control pages

- Atlas pages affected: `078, 079, 081, 083, 085, 087, 090, 091, 092, 093, 094, 095`
- Manual B atlas pages resolved: **11/11**
- Control pages affected: `061, 110, 116, 121`
- Control pages rechecked but unchanged/excluded: `055, 130, 140, 141`

No approved BG-03 native prose was reopened or reclassified.

## Post-correction QA

- Affected pages exactly 47: **YES**
- Graphics accounted for: **47/47**
- B blocks resolved: **25/25**
- D block correctly handled: **YES**
- A block isolated: **YES**
- Terminology violations: **0**
- OCR authority violations: **0**
- Duplicate inventory items: **0**
- Missing recoverable elements: **0**
- Recoverable items still marked manual review: **0**
- Native BG-03 captions misclassified: **0**
- MANUAL DECISION REQUIRED items: **0**

## Immutable-reference verification

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before correction | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After correction | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

- Reference unchanged: **YES**
- PDFs modified: **NO**
- Graphics modified: **NO**
- Page masters modified: **NO**
- BG-05 started: **NO**
- Phase state changed: **NO**
- Commit performed: **NO**

# FINAL RESULT: PASS WITH MANUAL REVIEW QUEUE

Only the single genuinely unresolved A-class page-16 screenshot-UI unit remains. BG-04 stays active and awaits independent re-audit and human approval.
