# BG-04 SF-03 CANONICAL CORRECTION PASS V1 REPORT

Result: **PASS — CORRECTION PASS COMPLETE; READY FOR INDEPENDENT ACCEPTANCE RE-AUDIT**
Phase state: **BG-04 ACTIVE; BG-05 PENDING**
Content/PDF/native-source changes: **NONE**
OCR authority: **NO**

## Scope and authority

This pass corrects only the active canonical evidence for P101, P103, P105, P106, P108, P110, P113, P116, and P117. It responds to the findings in `BG-04_SF03_INDEPENDENT_CANONICAL_ACCEPTANCE_AUDIT.md`; that audit remains unchanged. The original 216 ordinal U records remain historical evidence, excluded from the active construction metric, and are not mapped to source wording.

## Corrected ledger counts

| Graphic | V0 units | V1 units | V1 T/R/N/G/U | Contiguous range |
|---|---:|---:|---|---|
| P101-GA | 32 | 44 | 36/6/0/2/0 | C001–C044 |
| P103-GA | 29 | 60 | 56/3/0/1/0 | C001–C060 |
| P105-GA | 16 | 143 | 135/6/0/2/0 | C001–C143 |
| P106-GA | 23 | 47 | 43/3/0/1/0 | C001–C047 |
| P108-GA | 20 | 77 | 69/6/0/2/0 | C001–C077 |
| P110-GA | 21 | 57 | 48/7/0/2/0 | C001–C057 |
| P113-GA | 27 | 57 | 49/6/0/2/0 | C001–C057 |
| P116-GA | 24 | 59 | 55/3/0/1/0 | C001–C059 |
| P117-GA | 19 | 59 | 51/6/0/2/0 | C001–C059 |
| **TOTAL** | **211** | **603** | **542/46/0/15/0** | **9/9 contiguous** |

Previous aggregate: **211 = 184 T + 18 R + 0 N + 9 G + 0 U**.

## Finding closure

| Audit finding | V1 disposition | Result |
|---|---|:---:|
| 106 over-merged units | 106 fixed; 0 remaining. Headings, labels, table cells, list/warning items, and separately positioned text blocks were split into placement-level units. | PASS |
| 15 missing text-bearing crest/medallion regions | 15 fixed; 0 remaining. All 9 top crests and 6 bottom medallions are represented. Artwork is G; each visible `USG`, `UNICO SUO GENERE`, and applicable `CANE CORSO` occurrence is separate R. | PASS |
| Nine invented English G sources | 9 fixed; 0 remaining. Every G unit has an empty exact-source field and an artwork-preservation rationale only. | PASS |
| P105 `Morsi` mismatch | 1 fixed; 0 remaining. Corrected to `Morso affinato in sviluppo.` | PASS |
| Three Bulgarian target findings | 3 fixed; 0 remaining, as recorded below. | PASS |
| 121 ambiguous anchors | 121 fixed; 0 remaining. Every active row now has reading order, region, named panel, element role, associated visual, and within-panel relative position. These combinations are unique; BBOX_NORM was not required. | PASS |
| Remaining-ledger over-split check | All nine native PNGs were re-inspected; wrapped lines belonging to one continuous block remain together. | PASS |
| Additional readable fixed mark | The visible `USG` on the P110 feeding bowl is separately inventoried as `P110-GA-C057`. | PASS |

## Exact source/target corrections

| V0 ID | V1 ID(s) | Corrected exact source | Corrected Bulgarian |
|---|---|---|---|
| `P105-GA-C008` | `P105-GA-C073`, `P105-GA-C074`, `P105-GA-C075`, `P105-GA-C076`, `P105-GA-C077`, `P105-GA-C078`, `P105-GA-C079`, `P105-GA-C080`, `P105-GA-C081`, `P105-GA-C082`, `P105-GA-C083`, `P105-GA-C084`, `P105-GA-C085`, `P105-GA-C086` | Morso affinato in sviluppo. | Захапката се усъвършенства. |
| `P106-GA-C001` | `P106-GA-C001` | ESERCIZIO | УПРАЖНЕНИЯ |
| `P117-GA-C006` | `P117-GA-C020`, `P117-GA-C021`, `P117-GA-C022`, `P117-GA-C023`, `P117-GA-C024`, `P117-GA-C025` | INDIZI COMUNI | ЧЕСТИ ПРИЗНАЦИ |

## Anchor and classification checks

- Required structured anchor fields present: **603/603**
- Placement-unique anchor combinations: **603/603**
- T units with Bulgarian targets: **542/542**
- R units with fixed-mark rationale: **46/46**
- G units with no invented source text: **15/15**
- U units: **0**
- Duplicate canonical IDs: **0**
- Missing ordinals: **0**
- Wrong-graphic IDs: **0**
- Unsupported Bulgarian targets: **0**
- Terminology-lock violations: **0**
- OCR authority violations: **0**
- Recoverable U: **0**
- Readable native text missing: **0**
- Self-check construction readiness: **9/9**.

## Metrics

Historical metric remains unchanged:

- **867 total = 171 T + 50 R + 1 N + 0 G + 645 U**
- Historical SF-03 legacy records retained: **216/216**

Active construction metric:

- Formula: **867 − 216 + 603 = 1254**
- **1254 total = 713 T + 96 R + 1 N + 15 G + 429 U**
- Double-count of superseded SF-03 legacy records: **0**

## Files

Updated:

- `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`
- `reports/bg/BG-04_SF03_CANONICAL_UNIT_LEDGER.md`
- `reports/bg/BG-04_P1_SOURCE_CORRESPONDENCE_MATRIX.md`

Created:

- `reports/bg/BG-04_SF03_CANONICAL_CORRECTION_PASS_V1_REPORT.md`
- `reports/bg/BG-04_SF03_CANONICAL_ID_REMAP_V1.md`

Protected/unchanged:

- `reports/bg/BG-04_SF03_INDEPENDENT_CANONICAL_ACCEPTANCE_AUDIT.md`
- `BG_PHASE_STATE.json`
- all PDFs, native source images, and production graphics

No commit was created.
