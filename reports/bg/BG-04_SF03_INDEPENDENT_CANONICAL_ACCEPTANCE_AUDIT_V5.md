# BG-04 SF-03 INDEPENDENT CANONICAL ACCEPTANCE AUDIT V5

Final verdict: **PASS**

Mode: final independent differential acceptance audit after the V4 manual correction
Scope: P101-GA, P103-GA, P105-GA, P106-GA, P108-GA, P110-GA, P113-GA, P116-GA, P117-GA
Repairs performed during audit: **NONE**
OCR authority: **NO**

## Executive result

The V4 correction closes all six remaining metadata defects identified by the independent V4 audit.

The V4-to-V5 differential is exact and narrow:

- changed active records: **6**
- changed `ELEMENT_ROLE` fields: **6**
- changed `RELATIVE_POSITION` fields: **1**
- canonical IDs changed: **0**
- reading order changed: **0**
- REGION changed: **0**
- PANEL changed: **0**
- ASSOCIATED_VISUAL changed: **0**
- Italian source changed: **0**
- Bulgarian target changed: **0**
- T/R/N/G/U class changed: **0**
- source-image field changed: **0**
- unit boundaries changed: **0**

The active inventory section mirrors the canonical ledger exactly, row-for-row: **599/599**.

All V3 and V4 blocking findings are now closed. SF-03 is accepted as construction-ready.

## V4 finding closure

| V4 finding | Required correction | V5 verification | Verdict |
|---|---|---|:---:|
| `P101-GA-C012` explanatory prose mislabeled | `BODY_TEXT` | exact | PASS |
| `P103-GA-C007` explanatory prose mislabeled | `BODY_TEXT` | exact | PASS |
| `P103-GA-C014` explanatory prose mislabeled | `BODY_TEXT` | exact | PASS |
| `P103-GA-C022` explanatory prose mislabeled | `BODY_TEXT` | exact | PASS |
| `P103-GA-C030` explanatory prose mislabeled | `BODY_TEXT` | exact | PASS |
| `P110-GA-C033` bullet/list-role conflict | `BODY_TEXT`, `/2of2/1of4` | exact | PASS |

Native visual inspection confirms:

- P101 C012 is the explanatory paragraph under `3 SVILUPPO PRECOCE`.
- P103 C007/C014/C022/C030 are the explanatory prose blocks for phases 1–4.
- P110 C033 is the first bullet item under `5 OSSERVAZIONE DEL CANE`, and its `/2of2/1of4` position now matches sibling bullets C034–C036.

## V3 finding closure

The V3 blockers remain closed:

- incomplete Bulgarian target `P105-GA-C072`: **PASS**
- V3-listed role conflicts: **84/84 closed**

`P105-GA-C072`:

- Italian source: `Morsi affinato in sviluppo.`
- Bulgarian target: `Захапванията се усъвършенстват в хода на развитието.`
- exact Unicode comparison: **PASS**
- semantic coverage of `in sviluppo`: **PASS**

## Differential regression proof

Compared with the V4-audited package, the current V5 package changes only the seven metadata fields required to close the six V4 findings.

Therefore the already accepted V3/V4 results remain non-regressed for:

- canonical unit boundaries
- visible-text completeness
- Italian source fidelity
- Bulgarian targets other than the already-accepted P105 correction
- T/R/N/G/U classification
- native source correspondence
- canonical IDs
- reading order
- R/G handling
- crest/medallion text handling
- legacy preservation
- active metric arithmetic

## Canonical structure

| Graphic | Total | T | R | N | G | U | Contiguous |
|---|---:|---:|---:|---:|---:|---:|:---:|
| P101-GA | 43 | 35 | 6 | 0 | 2 | 0 | YES |
| P103-GA | 60 | 56 | 3 | 0 | 1 | 0 | YES |
| P105-GA | 134 | 126 | 6 | 0 | 2 | 0 | YES |
| P106-GA | 47 | 43 | 3 | 0 | 1 | 0 | YES |
| P108-GA | 77 | 69 | 6 | 0 | 2 | 0 | YES |
| P110-GA | 57 | 48 | 7 | 0 | 2 | 0 | YES |
| P113-GA | 57 | 49 | 6 | 0 | 2 | 0 | YES |
| P116-GA | 59 | 55 | 3 | 0 | 1 | 0 | YES |
| P117-GA | 65 | 57 | 6 | 0 | 2 | 0 | YES |
| **TOTAL** | **599** | **538** | **46** | **0** | **15** | **0** | **9/9** |

Checks:

- arithmetic: **599 = 538 + 46 + 0 + 15 + 0 — PASS**
- unique canonical IDs: **599**
- duplicate canonical IDs: **0**
- missing ordinals: **0**
- C001 starts: **9/9**
- active inventory vs canonical ledger: **599/599 exact**
- U: **0**

## Role / anchor consistency

Final semantic role sweep:

- known V3 role defects remaining: **0**
- known V4 role defects remaining: **0**
- `BODY_TEXT` rows whose relative-position metadata says heading/label/title: **0**
- `HEADING_OR_LABEL` rows whose relative-position metadata says paragraph/explanation/body/bullet: **0**
- remaining contradictory role metadata: **0**

Anchor gate:

- sufficient / internally consistent: **599/599**
- ambiguous: **0**
- contradictory: **0**

## Source fidelity and visual completeness

No source or unit-boundary field changed after the V3 full-source audit.

Final differential regression result:

- source regressions: **0**
- missing visible text regressions: **0**
- duplicate visible text regressions: **0**
- over-merge regressions: **0**
- over-split regressions: **0**

The V3 source-fidelity result of 599/599 and visual-completeness result of 0 missing / 0 duplicate remain intact because V4/V5 changed metadata only.

## Bulgarian targets

- T units: **538**
- targets present: **538/538**
- unsupported known targets remaining: **0**
- terminology regressions introduced by V4 correction: **0**
- broken Cyrillic introduced: **0**
- unintended Italian introduced: **0**

## Legacy preservation

The inventory prefix before the active SF-03 V2 section is byte-identical between V4 and V5.

Therefore:

- legacy SF-03 U records preserved: **216/216**
- false legacy-to-canonical mapping introduced: **0**
- active double-counting introduced: **0**

## Construction readiness

| Graphic | Ready |
|---|:---:|
| P101-GA | YES |
| P103-GA | YES |
| P105-GA | YES |
| P106-GA | YES |
| P108-GA | YES |
| P110-GA | YES |
| P113-GA | YES |
| P116-GA | YES |
| P117-GA | YES |

**Construction-ready: 9/9**

## Active global metric

The V5 changes do not alter canonical count or class.

- historical metric: **867 = 171 T + 50 R + 1 N + 0 G + 645 U**
- active formula: **867 − 216 + 599 = 1250**
- active total: **1250**
- active T/R/N/G/U: **709 / 96 / 1 / 15 / 429**
- non-SF03 unresolved U: **429**
- arithmetic: **PASS**

## Package and evidence hashes

- V5 package ZIP: `C8F2DA50E35C38E36E70B92AFB651D788B58628DA1E95AA07B365F99281884B3`
- V5 canonical ledger: `7DEC4CE55879B4793F97C474C41B737AF4EE96FB10DDCC1ED7A07C9CEDFD966D`
- V5 inventory: `3689E8E800197CBBCDE1229565A526778DDCEEA3FE32BB278E3BD9D48680CA81`

Native evidence used read-only:

- `image-gen-1(20260810-073754).png` — `371D8D4C553C5D164964DE7CF67D6564765BC4D34574341DDE007DE4045CA57D`
- `image-gen-2(20260810-073758).png` — `15C7433DF6CB1EC36A30499506DCBAD56C5F55C962DC93396DEEEE068FD3872C`
- `image-gen-3(20260810-073802).png` — `25F84178587BBAD32D0A8FBF7890A290A8A69E18DB9D94842A82A9D155C6A8D5`
- `image-gen-4(20260810-073804).png` — `FC9DEA4FAD6E020514DA0446EE816C20A04C1E274EBF919F86C4965C334543F7`
- `image-gen-5(9).png` — `262C3F22708A74FFC23E966179ACBD36E8F25E234FE15B06271624582C0CB953`
- `image-gen-6(7).png` — `7E8B524EE75A0870361F931CBFD9EA89BCBFECABDB6314A155DF2339B4C1CC14`
- `image-gen-7(4).png` — `8D1326FCF61B3440EF7BFE538B692686C3E6F06AC1D641F0C6A8C398AF6BD581`
- `image-gen-8(4).png` — `859821F58440D7BDBE6F28EEC5668731786F4460B3D64BC7C8DB5568AFF8BB5A`
- `image-gen-9(4).png` — `BDBD97BBA9DEDEB36F6A106559305227A245B3524A60D59AF9B72E57201DFC4E`

The immutable Italian reference PDF is not contained in the V5 audit package, so its SHA-256 was not recomputed during this differential audit. The last independent audit evidence records the locked reference hash as `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`; the V5 work touched only the two Markdown audit inputs and had no operation on the reference PDF.

## Findings

### CRITICAL — 0

None.

### IMPORTANT — 0

None.

### MICRO — 0

None.

## Final verdict

**PASS**

Acceptance gate:

- CRITICAL: **0**
- IMPORTANT: **0**
- MICRO: **0**
- construction-ready: **9/9**
- canonical structure: **PASS**
- source/visual regression: **PASS**
- Bulgarian target support: **PASS**
- role/anchor consistency: **PASS**
- active metric: **PASS**

**SF-03 is accepted for BG-04 and may be checkpointed.**

BG-04 remains ACTIVE. BG-05 remains PENDING.
