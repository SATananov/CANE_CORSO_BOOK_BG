# BG-04 — INDEPENDENT ACCEPTANCE AUDIT

Date: 2026-08-19  
Phase audited: **BG-04 — IMAGE-TEXT INVENTORY**  
Audit mode: **REPORT ONLY**  
BG-05 readiness: **NO**

## Scope and independence

This audit independently checked the final 143-page Italian reference, `BG_PAGE_INVENTORY.md`, the approved BG-03 page masters and source map, the terminology lock, `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`, and the BG-04 inventory report.

No inventory entry, page master, source, PDF, graphic, or phase-state file was corrected or modified.

## Audit results

| Audit | Result | Finding |
|---|---|---|
| 1. Affected-page set | **PASS** | The 47 recorded pages match the 47 BG-04 markers and the established embedded-Italian-text set. No additional affected page or false positive was identified. |
| 2. One record per affected graphic | **PASS** | 47 page records and 47 graphic records are present; page IDs are unique and complete for the affected set. |
| 3. Claimed 761 Italian elements | **FAIL** | The declared per-record counts sum arithmetically to 761, but many records aggregate multiple labels, table cells, paragraphs, values, bullets, source lines, or map names into a single prose description. The inventory does not expose a uniquely addressable 761-item list, so completeness, omissions, and duplicates cannot be independently verified. |
| 4. Claimed 734 Bulgarian targets | **FAIL** | The figure is derived as 761 minus 27, but the inventory does not contain 734 exact element-to-target translations. In 33 of 47 `Bulgarian target text` fields, wording such as “translate the descriptions/rows/cards/blocks” replaces the required Bulgarian target text. One record intentionally has no in-image target. The reported 734 prepared translations are therefore not substantiated. |
| 5. Locked terminology | **PARTIAL PASS** | The Bulgarian wording that is explicitly supplied generally follows the lock, including `Кане Корсо`, Pugnax, molos/molոսoid distinctions, functional continuity, and `Функцията формира типа`. Compliance cannot be audited for omitted target prose or table cells because those translations do not yet exist in the inventory. |
| 6. Names, titles, Latin forms, numbers, dates, credits | **FAIL** | Relevant categories are mentioned, but dense tables, atlas cards, medical graphics, and screenshot/signage records do not enumerate every exact string and exact preservation/translation action. Several numerical ranges are explicitly deferred “after manual check.” |
| 7. Caption versus artwork classification | **PASS** | Native BG-03 captions are kept outside the graphic inventory. Integral artwork captions/status lines and authentic documentary signage are distinguished. Page 121 correctly proposes no alteration inside the photograph. |
| 8. Visual atlas pages 78–96 | **FAIL** | The affected subset is correctly identified as 78, 79, 81, 83, 85, 87, 90–95. However, eleven atlas graphics retain grouped or unresolved card/note prose rather than exact Italian strings paired with exact Bulgarian targets; the atlas inventory is not construction-ready. |
| 9. Difficulty classification | **PASS** | The reported distribution—7 LOW, 13 MEDIUM, 27 HIGH—is internally consistent and proportionate to the visible complexity. |

## Verified affected-page set

`001, 006, 011, 014, 016, 018, 041, 044, 048, 050, 051, 054, 061, 066, 068, 070, 076, 078, 079, 081, 083, 085, 087, 090, 091, 092, 093, 094, 095, 097, 098, 101, 103, 105, 106, 108, 110, 113, 116, 117, 121, 122, 125, 128, 131, 133, 134`

- Expected affected pages: **47**
- Inventory page records: **47**
- Inventory graphic records: **47**
- Missing affected-page records: **0**
- Duplicate page records: **0**
- Additional affected pages found: **0**
- False-positive affected pages: **0**

## Manual-review block audit

Classification key:

- **A — genuinely unresolved:** no safe authoritative wording is presently recoverable.
- **B — recoverable from authority:** final-PDF visual reading and/or editable upstream material is sufficient; the block should be transcribed and mapped before BG-05.
- **C — classification error:** not language-dependent artwork.
- **D — duplicate/not required:** no Bulgarian in-image reconstruction target is required.

| Page | Inventory block | Class | Acceptance finding |
|---:|---|:---:|---|
| 16 | Small USG screenshot UI | **A** | Fine interface text is not safely established by the cited editable sources; exact in-image wording remains genuinely unresolved. |
| 61 | Comparative-table fine row text | **B** | The final PDF and related manuscript/terminology material permit deliberate full-resolution transcription and source checking. |
| 70 | Head/anatomy fine explanatory text | **B** | The labelled plate is visually locatable and recoverable through full-resolution reading plus the established anatomy terminology. |
| 79 | Mediterranean/East note microcopy | **B** | The final artwork visibly supplies the wording and sequence; manual transcription is possible without OCR authority. |
| 81 | Rome/provinces node and note text | **B** | Map text and explanatory blocks can be transcribed from the final visual authority and checked against the upstream narrative. |
| 83 | Italy-development source/key paragraphs | **B** | The graphic and upstream sources jointly establish the text and evidentiary status. |
| 85 | Balkans/Thrace/Bulgaria context blocks | **B** | Final-PDF visual reading is sufficient, with hypothesis markers controlled by the lock. |
| 87 | Comparative-atlas central prose | **B** | The prose is visible and its methodological status is recoverable; it is not an authority gap. |
| 90 | World-atlas card bodies | **B** | Card bodies are recoverable by full-resolution visual transcription. |
| 91 | Mediterranean/Western Europe cards | **B** | Region-card prose is recoverable from the final page and supporting source context. |
| 92 | Balkans/Caucasus/Anatolia/Central Asia cards | **B** | Region-card prose is recoverable from the final page and supporting source context. |
| 93 | Tibet/China/Japan/Far East cards | **B** | Despite MEDIUM page-source confidence, the final PDF is the authoritative visible wording and can be manually transcribed. |
| 94 | Africa region cards | **B** | The final PDF provides sufficient visible wording; editable context protects status and terminology. |
| 95 | Americas region cards | **B** | The final PDF provides sufficient visible wording; editable context protects status and terminology. |
| 97 | Comparative-table fine cells | **B** | Full-resolution table transcription is feasible and must be enumerated cell by cell. |
| 101 | Pregnancy stages, values, and medical microcopy | **B** | The final graphic plus Part VI editable material permits controlled transcription; every value still requires explicit verification. |
| 103 | Birth-process clinical microcopy | **B** | Recoverable from the final graphic and the authoritative medical/veterinary source context. |
| 105 | Puppy-development table cells | **B** | Recoverable visually and must be recorded as distinct row/column cells. |
| 106 | Growth-plate anatomy/activity microcopy | **B** | Recoverable from full-resolution visual reading with locked anatomy vocabulary. |
| 108 | Growth-monitoring weights and cells | **B** | Recoverable, but exact ranges must be individually transcribed and checked before construction. |
| 110 | Feeding portion table and dense prose | **B** | Recoverable from the final graphic and editable health material; the current directive is not a target translation. |
| 113 | Parasite-control medical microcopy | **B** | Recoverable from the final graphic and editable veterinary material. |
| 116 | Skin/coat medical microcopy | **B** | Recoverable from the final graphic and editable veterinary material. |
| 117 | Skin/coat risk and sign lists | **B** | Recoverable from the final graphic and editable veterinary material. |
| 121 | Authentic photographed signage | **D** | The photograph must remain authentic and unaltered. An optional external accessibility legend is not an in-image reconstruction target. |
| 133 | Body-language fine phrases | **B** | Recoverable from the final graphic; exact phrases must be enumerated rather than summarized. |
| 134 | Temperament module prose | **B** | Recoverable from the final graphic; exact module text must be enumerated rather than summarized. |

Manual-review classification totals:

- **A — genuinely unresolved:** 1
- **B — recoverable from authoritative source:** 25
- **C — classification error:** 0
- **D — duplicate/not required:** 1
- **Total reviewed:** 27/27

The 25 class-B blocks are not valid unresolved-authority exceptions. They are outstanding inventory/transcription work that must be completed inside BG-04. The class-D page-121 block should not be counted as a missing Bulgarian in-image target. Only page 16 remains a genuine manual-review queue item on the evidence currently recorded.

## Issue register

### CRITICAL issues — 2

1. **The inventory is not element-addressable.** The reported 761 total is a sum of declared estimates such as “24 inventoried blocks,” while individual labels, body blocks, cells, values, and credits are often compressed into collective descriptions. BG-05 cannot use this as a deterministic build specification, and an independent reviewer cannot prove that all visible text was captured.
2. **The claimed 734 Bulgarian targets are not present.** Thirty-three graphic records contain instructions to translate unspecified remaining material rather than the exact Bulgarian target for each Italian element. Building from those instructions would require BG-05 to perform unapproved translation and source recovery, violating the phase boundary and creating a high risk of guessed, omitted, or inconsistent text.

### IMPORTANT issues — 3

1. **Twenty-five manual-review blocks are recoverable and should be completed now.** Deferring them would transfer inventory work into BG-05.
2. **Dense tables and medical graphics lack exact value-level mapping.** Pages 61, 97, 101, 103, 105, 106, 108, 110, 113, 116, and 117 require explicit cells, units, ranges, cautions, and credits before reconstruction.
3. **Atlas card prose is not construction-ready.** Pages 79, 81, 83, 85, 87, and 90–95 need exact Italian strings, exact Bulgarian targets, attribution/status controls, and unique element identifiers.

### MICRO issues — 1

1. Page 121 is included appropriately as an affected documentary image, but its fine signage block should be tagged **preserve unchanged / no in-image Bulgarian target**, not counted as an unresolved translation block.

## Control-page findings

| Page | Result |
|---:|---|
| 55 | Correctly excluded; no language-dependent embedded graphic requiring BG-04 reconstruction. |
| 61 | Correctly included, but the comparative table is not fully enumerated or translated. |
| 78 | Correctly included; methodology artwork is separated from native page prose. |
| 110 | Correctly included, but portion values and dense text remain unspecified. |
| 116 | Correctly included, but medical microcopy remains unspecified. |
| 121 | Correctly identified as authentic documentary signage; preserve the photograph unchanged. |
| 130 | Correctly excluded. |
| 140 | Correctly excluded; decorative Cane Corso head only. |
| 141 | Correctly excluded; decorative Cane Corso head only. |

## Gate assessment

- Complete affected-page set established: **PASS — 47/47**
- Unique per-graphic records: **PASS — 47/47**
- Exact per-element Italian inventory: **FAIL**
- Exact Bulgarian target for every recoverable element: **FAIL**
- Manual-review exceptions correctly limited: **FAIL**
- Caption/artwork boundary: **PASS**
- Atlas affected-page identification: **PASS**
- Atlas text specification completeness: **FAIL**
- Difficulty classification: **PASS**
- Ready to advance to BG-05: **NO**

Required BG-04 remediation before another acceptance audit:

1. assign a unique element ID to every visible Italian text unit;
2. record the exact Italian string or an explicit preserve-unchanged instruction;
3. supply the exact locked Bulgarian target for every recoverable unit;
4. resolve the 25 class-B blocks within BG-04;
5. remove page 121 from the unresolved translation count while retaining its documentary-preservation note;
6. retain only the genuinely unresolved page-16 UI block in the manual-review queue unless new authority resolves it.

## Integrity and phase controls

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

- PDFs modified: **NO**
- Graphics modified: **NO**
- BG-05 started: **NO**
- `BG_PHASE_STATE.json` modified: **NO**
- Commit performed: **NO**

# FINAL RESULT: FAIL

BG-04 remains active. The page set is correct, but the inventory is not yet a complete, exact, construction-ready authority for BG-05.
