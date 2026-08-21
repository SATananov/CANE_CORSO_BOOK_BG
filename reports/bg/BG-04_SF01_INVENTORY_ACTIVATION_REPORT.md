# BG-04 SF-01 INVENTORY ACTIVATION REPORT

Result: **PASS — ACTIVATION APPLIED; INDEPENDENT POST-ACTIVATION AUDIT PENDING**

Phase: **BG-04**
Family: **SF-01**
Git HEAD before activation: `dce67c5`

## Acceptance authority

- SF-01 canonical ledger: **171 units**
- T/R/N/G/U: **129 / 42 / 0 / 0 / 0**
- independent acceptance V3: **PASS**
- findings: **CRITICAL 0 / IMPORTANT 0 / MICRO 0**
- construction-ready SF-01: **10/10**

## Legacy preservation

- legacy SF-01 U located before activation: **79/79**
- per-page legacy counts: `{11: 12, 44: 9, 48: 2, 66: 5, 70: 11, 76: 6, 78: 3, 98: 1, 61: 22, 121: 8}`
- legacy rows deleted: **0**
- set-level supersession rows added: **79**
- fabricated legacy-to-canonical mappings: **0**

## Active metric transition

Before:
`1388 = 910 T + 126 R + 1 N + 19 G + 332 U`

Transition:
`1388 − 79 + 171 = 1480`

After:
`1480 = 1039 T + 168 R + 1 N + 19 G + 253 U`

Construction-ready:
`26/47 → 36/47`

## Inventory integrity

- pre-activation SHA-256: `4E506CBD9E628371087B3BB1452597D1EACC379337D6017350EBD8863039B98A`
- post-activation SHA-256: `C0E62279C2DE80814C4B54E253E1018E1E2EDFACA0FCF2855AB23AC60902F132`
- canonical IDs appended: **171/171**
- duplicate SF-01 canonical IDs introduced: **0**
- active marker count: **1**
- aggregate marker count: **1**
- current-summary lines surgically updated where exact old markers were present: **4**

## Change scope

Modified:
- `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`

Created:
- `reports/bg/BG-04_SF01_INVENTORY_ACTIVATION_REPORT.md`

Unchanged:
- Italian reference/master
- BG PDF
- production graphics
- accepted SF-01 canonical ledger
- accepted SF-01 V3 audit
- phase-state transition to BG-05

BG-04 remains **ACTIVE**.
BG-05 remains **PENDING**.

## Next gate

Run an independent post-activation audit before Git staging/commit.
