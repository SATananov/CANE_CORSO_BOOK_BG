# BG-04 SF-02 INVENTORY ACTIVATION REPORT

Result: **PASS — SANDBOX ACTIVATION APPLIED; INDEPENDENT POST-ACTIVATION AUDIT REQUIRED**

Phase: **BG-04**
Family: **SF-02**
Baseline Git checkpoint: `a6640f8 Checkpoint BG-04 SF-01 canonical acceptance`
OCR authority: **NO**

## Acceptance authority

- SF-02 accepted canonical ledger: **331 units**
- T/R/N/G/U: **298 / 31 / 0 / 2 / 0**
- independent canonical acceptance V2: **PASS**
- findings: **CRITICAL 0 / IMPORTANT 0 / MICRO 0**
- construction-ready SF-02 at canonical gate: **11/11**
- canonical ledger SHA-256: `F727E2C991EDAF330789D1B6948062D2BD877F8EAE13F1E56C688DC9AEDEC1E7`
- canonical acceptance audit SHA-256: `C388F4D63C7A8B825A028C82F1351D4F058AA0A19E7C6BD7B1BEBA8BFB0AA668`

## Legacy preservation

- legacy SF-02 U located in baseline inventory: **253/253**
- per-page legacy counts: `{79: 20, 81: 22, 83: 25, 85: 25, 87: 25, 90: 24, 91: 24, 92: 24, 93: 24, 94: 20, 95: 20}`
- legacy rows deleted: **0**
- legacy row text changed: **0**
- set-level supersession rows added: **253**
- fabricated legacy-to-canonical mappings: **0**

The historical U rows remain in their original inventory locations. The activation appends a separate set-level supersession register using `SUPERSEDED_BY_CANONICAL_LEDGER`.

## Active metric transition

Before:

`1480 = 1039 T + 168 R + 1 N + 19 G + 253 U`

Transition:

`1480 − 253 + 331 = 1558`

After:

`1558 = 1337 T + 199 R + 1 N + 21 G + 0 U`

Construction-ready:

`36/47 → 47/47`

Full family formula:

`867 − 216 − 40 − 10 − 47 − 79 − 253 + 599 + 109 + 59 + 67 + 171 + 331 = 1558`

## Inventory integrity

- pre-activation SHA-256: `C0E62279C2DE80814C4B54E253E1018E1E2EDFACA0FCF2855AB23AC60902F132`
- sandbox post-activation SHA-256: `1A513521946833219D1641BF35F2B9D9CAD523236C65A22822BF55B8F7C150B0`
- canonical rows appended: **331/331**
- canonical row content copied exactly from accepted V2 ledger: **331/331**
- duplicate SF-02 canonical IDs introduced: **0**
- SF-02 legacy supersession entries: **253/253**
- stale `CURRENT LEDGER TOTALS` block normalized to the final active metric: **PASS**

## Change scope

Modified in sandbox:

- `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`

Created for SF-02 evidence:

- `reports/bg/BG-04_SF02_SOURCE_RECOVERY_CENSUS_REPORT.md`
- `reports/bg/BG-04_SF02_CANONICAL_UNIT_LEDGER.md`
- `reports/bg/BG-04_SF02_CANONICAL_CORRECTION_PASS_V1_REPORT.md`
- `reports/bg/BG-04_SF02_INDEPENDENT_CANONICAL_ACCEPTANCE_AUDIT_V2.md`
- `reports/bg/BG-04_SF02_CANONICAL_LEDGER_REBUILD_REPORT_V2.md`
- `reports/bg/BG-04_SF02_INVENTORY_ACTIVATION_REPORT.md`

Explicitly unchanged by activation:

- immutable Italian reference/master
- Bulgarian PDF
- production graphics
- BG phase state
- BG-05 state
- accepted prior-family ledgers

BG-04 remains **ACTIVE** pending the final BG-04 closure audit.
BG-05 remains **PENDING**.

## Next gate

Run the independent post-activation audit before Git staging or commit.
