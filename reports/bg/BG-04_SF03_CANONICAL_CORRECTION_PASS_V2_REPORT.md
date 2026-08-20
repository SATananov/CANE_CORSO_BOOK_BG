# BG-04 SF-03 CANONICAL CORRECTION PASS V2 REPORT

Result: **PASS**
Scope: surgical closure of `BG-04_SF03_INDEPENDENT_CANONICAL_ACCEPTANCE_AUDIT_V2.md`
Phase state: **BG-04 ACTIVE; BG-05 PENDING**
OCR authority: **NO**
Commit: **NONE**

## Correction closure

| Category | V2 audit | Fixed | Remaining | Result |
|---|---:|---:|---:|:---:|
| Over-merged records | 8 | 8 | 0 | PASS |
| Over-split boundaries | 12 | 12 | 0 | PASS |
| Italian source-fidelity mismatches | 2 | 2 | 0 | PASS |
| Unsupported Bulgarian targets | 1 | 1 | 0 | PASS |
| Contradictory spatial anchors | 9 | 9 | 0 | PASS |

## Surgical structural corrections

### Over-merged records

- `P108-GA-C056` → separate heading and body.
- `P110-GA-C033` → introductory continuation separated from bullet; combined with C032 as one continuous paragraph.
- `P117-GA-C004`, C009, C015, C021, C027, C033 → each panel body separated from its independently positioned secondary heading.

### Over-split boundaries

- P101 C012+C013 → one colon-led continuous paragraph.
- P105 age blocks C003+C004, C017+C018, C031+C032, C045+C046, C059+C060, C073+C074, C087+C088, C101+C102, C115+C116 → nine single boxed age blocks.
- P108 C040+C041 → one `Ideale: 4–5/9` row-label block.
- P110 C032 plus the opening continuation in C033 → one continuous introductory paragraph; the bullet remains separate.

Complete V1→V2 affected-ID lineage is recorded in `BG-04_SF03_CANONICAL_ID_REMAP_V2.md`.

## Source fidelity and Bulgarian target

| V1 record | Wrong source | Verified native source | Bulgarian impact |
|---|---|---|---|
| P105-GA-C078 | `Morso affinato in sviluppo.` | `Morsi affinato in sviluppo.` | Updated to `Захапванията се усъвършенстват.` so number and meaning follow the visible source. |
| P106-GA-C037 | `RADICI FORTI, FUTURO SOLIDO` | `RADICI FORTI, FUTURO SOLIDO.` | No semantic change; target remains `СИЛНИ КОРЕНИ, СТАБИЛНО БЪДЕЩЕ`. |

Changed T targets were checked against the terminology lock. Unsupported targets remaining: **0**.

## Spatial anchors

The following V1 records had `REGION: LOWER_CENTER` while identifying the top-crest lower ribbon:

- P101 C039
- P103 C059
- P105 C138
- P106 C046
- P108 C072
- P110 C051
- P113 C052
- P116 C058
- P117 C054

All nine now use `REGION: HEADER`, `PANEL: inside top-center crest, lower ribbon`, `ASSOCIATED_VISUAL: top crest`, and `RELATIVE_POSITION: inside crest lower ribbon`. The combined fields uniquely identify the placement; BBOX_NORM is not required. Contradictory anchors remaining: **0**.

## Canonical structure

| Graphic | V1 units | V2 units | V2 range |
|---|---:|---:|---|
| P101-GA | 44 | 43 | C001–C043 |
| P103-GA | 60 | 60 | C001–C060 |
| P105-GA | 143 | 134 | C001–C134 |
| P106-GA | 47 | 47 | C001–C047 |
| P108-GA | 77 | 77 | C001–C077 |
| P110-GA | 57 | 57 | C001–C057 |
| P113-GA | 57 | 57 | C001–C057 |
| P116-GA | 59 | 59 | C001–C059 |
| P117-GA | 59 | 65 | C001–C065 |
| **TOTAL** | **603** | **599** | **9/9 contiguous** |

Previous classification: **542 T / 46 R / 0 N / 15 G / 0 U**
New classification: **538 T / 46 R / 0 N / 15 G / 0 U**

Validation:

- Duplicate IDs: **0**
- Missing ordinals: **0**
- Wrong-graphic prefixes: **0**
- Every T has one supported Bulgarian target: **538/538**
- Every R has a retention rationale: **46/46**
- Every G has a graphic-only rationale: **15/15**
- Recoverable U: **0**
- OCR authority violations: **0**

## Affected-graphic visual revalidation

All nine graphics were checked because every graphic contained either a structural/source finding or one of the nine anchor findings.

- Remaining over-merges: **0**
- Remaining over-splits: **0**
- Missing visible text caused by V2 merges: **0**
- Duplicate visible text caused by V2 splits: **0**
- Remaining source mismatches in corrected records: **0**
- Remaining unsupported changed targets: **0**
- Remaining contradictory changed anchors: **0**

Self-check construction readiness after the surgical correction: **9/9**, subject to a separately authorized independent acceptance audit.

## Legacy preservation

- Original SF-03 legacy U records preserved: **216/216**
- Status: `SUPERSEDED_BY_CANONICAL_LEDGER`
- Legacy IDs deleted: **0**
- False legacy-to-canonical mappings: **0**
- Active double-counting: **0**

## Metrics

Historical metric remains unchanged:

- **867 = 171 T + 50 R + 1 N + 0 G + 645 U**

Active construction metric:

- Formula: **867 − 216 + 599 = 1250**
- **1250 = 709 T + 96 R + 1 N + 15 G + 429 U**
- Non-SF03 active unresolved U pool: **429**, unchanged

## Files

Updated:

- `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`
- `reports/bg/BG-04_SF03_CANONICAL_UNIT_LEDGER.md`
- `reports/bg/BG-04_P1_SOURCE_CORRESPONDENCE_MATRIX.md`

Created:

- `reports/bg/BG-04_SF03_CANONICAL_CORRECTION_PASS_V2_REPORT.md`
- `reports/bg/BG-04_SF03_CANONICAL_ID_REMAP_V2.md`

Unchanged:

- both independent acceptance audit reports
- `BG_PHASE_STATE.json`
- native PNGs
- Italian reference PDF
- all production graphics and PDFs

## Immutability

Italian reference SHA-256 before correction:

`A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`

Closing hash verification is recorded after final validation.

Italian reference SHA-256 after correction:

`A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`

Result: **byte-identical — PASS**

- BG phase-state closing hash: `6DE06DBC9C95D76BB105B24D5A9831D320681632140E42A58587A3E8778D10D3` — unchanged
- First independent audit closing hash: `9044A0689AF873A868411A0070F50E6FE107EE3B945562A6BF08F5A3D4116CF1` — unchanged
- V2 independent audit closing hash: `C43FDE0D3EA0A679D38D2D6F6B1908441C70F7E38D30D568751E2A04DFD49D83` — unchanged
- Native PNG closing hashes match their pre-correction values: **9/9**
- BG-04: **ACTIVE**
- BG-05: **PENDING**
