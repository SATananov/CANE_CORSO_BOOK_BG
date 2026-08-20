# BG-04 SF-03 INDEPENDENT CANONICAL ACCEPTANCE AUDIT V2

Final verdict: **FAIL**

Mode: independent read-only acceptance audit
Scope: P101-GA, P103-GA, P105-GA, P106-GA, P108-GA, P110-GA, P113-GA, P116-GA, P117-GA
Repairs performed: **NONE**
OCR authority: **NO**

## Executive result

The corrected ledger passes native-source identity, ID integrity, crest/medallion separation, G-source cleanup, R/G classification, legacy preservation, and metric arithmetic. It fails acceptance because independently verified unit-boundary defects remain, one former source correction contradicts the visible native PNG, another source record omits visible punctuation, and nine top-crest ribbon anchors contain a contradictory region. Consequently the ledger is not construction-ready.

## Previous finding closure

| Finding category | V1 count | V2 verified fixed | V2 remaining | Verdict |
|---|---:|---:|---:|:---:|
| Over-merged units | 106 | 98 | 8 | FAIL |
| Text-bearing crests/medallions | 15 | 15 | 0 | PASS |
| Fabricated English in G | 9 | 9 | 0 | PASS |
| Source-fidelity defects | 1 word-level V1 finding | 0 | 1 former defect remains, plus 1 new punctuation mismatch | FAIL |
| BG target equivalence defects | 3 | 2 | 1 | FAIL |
| Ambiguous spatial anchors | 121 | 112 | 9 | FAIL |

The counts above were checked against the underlying V1 records and all nine native PNGs, not accepted from the correction report.

## Native source identity

**9/9 PASS — SCALED_NATIVE reconfirmed**

| Graphic | Native source | Result |
|---|---|:---:|
| P101-GA | image-gen-1(20260810-073754).png | SCALED_NATIVE |
| P103-GA | image-gen-2(20260810-073758).png | SCALED_NATIVE |
| P105-GA | image-gen-3(20260810-073802).png | SCALED_NATIVE |
| P106-GA | image-gen-4(20260810-073804).png | SCALED_NATIVE |
| P108-GA | image-gen-5(9).png | SCALED_NATIVE |
| P110-GA | image-gen-6(7).png | SCALED_NATIVE |
| P113-GA | image-gen-7(4).png | SCALED_NATIVE |
| P116-GA | image-gen-8(4).png | SCALED_NATIVE |
| P117-GA | image-gen-9(4).png | SCALED_NATIVE |

No contradiction to the established source-recovery conclusion was found.

## Canonical structure

| Graphic | Units | First | Last | Contiguous | Duplicate IDs |
|---|---:|---|---|:---:|---:|
| P101-GA | 44 | C001 | C044 | YES | 0 |
| P103-GA | 60 | C001 | C060 | YES | 0 |
| P105-GA | 143 | C001 | C143 | YES | 0 |
| P106-GA | 47 | C001 | C047 | YES | 0 |
| P108-GA | 77 | C001 | C077 | YES | 0 |
| P110-GA | 57 | C001 | C057 | YES | 0 |
| P113-GA | 57 | C001 | C057 | YES | 0 |
| P116-GA | 59 | C001 | C059 | YES | 0 |
| P117-GA | 59 | C001 | C059 | YES | 0 |
| **TOTAL** | **603** |  |  | **9/9** | **0** |

- T/R/N/G/U: **542/46/0/15/0**
- Arithmetic: **542 + 46 + 0 + 15 + 0 = 603 — PASS**
- Missing ordinals: **0**
- Wrong-graphic prefixes: **0**
- Inactive V0 IDs mixed into the active row set: **0**

## Granularity and visual completeness

### Confirmed remaining over-merges — 8

1. `P108-GA-C056` merges the separately styled card heading `MUSCOLATURA IN SVILUPPO` with its body.
2. `P110-GA-C033` merges the continuation `il suo corpo racconta molto.` with the separately positioned first bullet `Peso e forma corporea adeguati`.
3. `P117-GA-C004` merges panel prose with `FATTORI DI RISCHIO`.
4. `P117-GA-C009` merges panel prose with `SEGNI TIPICI`.
5. `P117-GA-C015` merges panel prose with `DA CONTROLLARE`.
6. `P117-GA-C021` merges panel prose with `INDIZI COMUNI`.
7. `P117-GA-C027` merges panel prose with `FATTORI DI RISCHIO`.
8. `P117-GA-C033` merges panel prose with `REAGIRE IN TEMPO`.

### Confirmed over-split boundaries — 12

- `P101-GA-C012` + `P101-GA-C013`: a colon-led continuation inside one coherent paragraph was split.
- Nine P105 age blocks split a single boxed age label into two units:
  - C003+C004
  - C017+C018
  - C031+C032
  - C045+C046
  - C059+C060
  - C073+C074
  - C087+C088
  - C101+C102
  - C115+C116
- `P108-GA-C040` + `P108-GA-C041`: `Ideale: 4–5/9` is one line/block in the row-label cell.
- `P110-GA-C032` + the opening clause of `P110-GA-C033`: one continuous introductory sentence was split at the colon.

### Full-sweep totals

- Missing visible units: **0 confirmed**
- Duplicated visible units: **0 confirmed**
- Over-merged units: **8**
- Over-split boundaries: **12**
- Wrong-unit-boundary findings: **20**
- Granularity acceptance: **FAIL**

## Crest, medallion, R and G handling

- Text-bearing crest/medallion regions represented: **15/15**
- G units: **15/15 genuinely artwork-only**
- G exact-source fields containing invented English: **0**
- Readable crest/medallion text hidden inside G: **0**
- R units: **46/46 have a retention rationale**
- Readable prose improperly classified R: **0**
- Duplicate seal wording at the same visible occurrence: **0**
- P110 bowl `USG` occurrence is separately recorded.
- Classification result: **PASS**

## Italian source fidelity

Mismatches: **2**

1. `P105-GA-C078` records `Morso affinato in sviluppo.` The native PNG visibly reads `Morsi affinato in sviluppo.` The V1 correction therefore does not match the actual native pixels. The earlier audit finding was not successfully closed.
2. `P106-GA-C037` records `RADICI FORTI, FUTURO SOLIDO`; the native medallion visibly includes the terminal period: `RADICI FORTI, FUTURO SOLIDO.`

The former `Morsi`/ `Morso` record was located through the V1 remap. No OCR was used.

## Bulgarian targets

- T targets structurally present: **542/542**
- Semantically supported by the actual visible source: **541/542**
- Unsupported/materially mismatched: **1**
- Terminology-lock violations: **0 confirmed**
- Unintended residual Italian: **0 confirmed**
- Broken Cyrillic/mojibake: **0**
- Naturalness micro findings: **0 recorded**

The remaining unsupported record is `P105-GA-C078`: `Захапката се усъвършенства.` follows the corrected singular `Morso`, but the native record visibly uses plural `Morsi`. The other two specially requested corrections are supported:

- `P106-GA-C001`: `УПРАЖНЕНИЯ` is supported by `ESERCIZIO`.
- `P117-GA-C021`: `ЧЕСТИ ПРИЗНАЦИ` correctly renders `INDIZI COMUNI`, although that heading remains improperly merged with neighboring prose.

## Spatial anchors

- Sufficient: **594/603**
- Ambiguous or internally contradictory: **9**

The following top-crest ribbon records say `REGION: LOWER_CENTER` while their panel and associated visual place them inside the top-center crest:

- `P101-GA-C039`
- `P103-GA-C059`
- `P105-GA-C138`
- `P106-GA-C046`
- `P108-GA-C072`
- `P110-GA-C051`
- `P113-GA-C052`
- `P116-GA-C058`
- `P117-GA-C054`

This internal contradiction requires a reconstruction agent to choose which structured field to trust. No BBOX_NORM is supplied to resolve it. Anchor acceptance: **FAIL**.

## Legacy preservation

- Original SF-03 legacy U IDs preserved: **216/216**
- Status retained as `SUPERSEDED_BY_CANONICAL_LEDGER`: **YES**
- Individual false legacy-to-canonical mappings: **0**
- Legacy records included in active construction metric: **0**
- Active double-counting: **0**

## Construction readiness

**0/9 construction-ready**

| Graphic | Status | Blocking reason |
|---|:---:|---|
| P101-GA | NO | Over-split paragraph; contradictory top-crest ribbon region. |
| P103-GA | NO | Contradictory top-crest ribbon region. |
| P105-GA | NO | Nine over-split age blocks; native-source and BG-target mismatch; contradictory crest anchor. |
| P106-GA | NO | Source punctuation mismatch; contradictory crest anchor. |
| P108-GA | NO | Remaining over-merge and over-split cell; contradictory crest anchor. |
| P110-GA | NO | Remaining over-merge/over-split boundary; contradictory crest anchor. |
| P113-GA | NO | Contradictory top-crest ribbon region. |
| P116-GA | NO | Contradictory top-crest ribbon region. |
| P117-GA | NO | Six remaining over-merges; contradictory crest anchor. |

## Metrics

### Historical metric

- Total: **867**
- T/R/N/G/U: **171/50/1/0/645**
- Arithmetic: **867 = 171 + 50 + 1 + 0 + 645**
- Superseded SF-03 legacy records retained: **216**

### Active construction metric

- Formula: **867 − 216 + 603 = 1254**
- Active total: **1254**
- Active T/R/N/G/U: **713/96/1/15/429**
- Arithmetic: **1254 = 713 + 96 + 1 + 15 + 429**
- Global active U: **429**
- Metric arithmetic: **PASS**

The arithmetic is correct; it does not make the defective SF-03 units acceptance-quality.

## Scope and immutability

Baseline hashes:

| Protected file | SHA-256 before |
|---|---|
| Italian reference PDF | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| BG phase state | `6DE06DBC9C95D76BB105B24D5A9831D320681632140E42A58587A3E8778D10D3` |
| Image-text inventory | `AF946F401A38F4518ADB1ADE837D164B9AC9F0F7ADF82CEF713527684E72D52E` |
| Canonical ledger | `D9B33748F43126F605B84D0D2F529287C1CCBC2CBBAC3A4252B542269533D86F` |
| Correction report | `D8A779A7879CB5DA0F2A3F5385F8876D3C79AE0BAB79E67A04EB42766052F239` |
| Canonical remap | `4C8140E1579F01E5F66947A98F24A06AADF95378188A92EBF0982D128199E7F4` |

Closing hashes were recomputed after report creation and match every baseline above. In particular:

- Italian reference SHA-256 after: `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`
- BG phase-state SHA-256 after: `6DE06DBC9C95D76BB105B24D5A9831D320681632140E42A58587A3E8778D10D3`
- Protected evidence files byte-identical: **YES**

Only this V2 report was created. No ledger, inventory, correction report, remap, PNG, PDF, production graphic, page master, or phase-state file was modified. BG-04 remains ACTIVE and BG-05 remains PENDING. No commit was created.

## Findings

### CRITICAL — 0

None.

### IMPORTANT — 4 finding groups

1. **I-01 — Granularity remains invalid:** 8 over-merged records and 12 over-split boundaries remain.
2. **I-02 — Native source fidelity:** `P105-GA-C078` contradicts the visible native wording (`Morso` recorded; `Morsi` visible).
3. **I-03 — Bulgarian equivalence:** the target attached to `P105-GA-C078` follows the unsupported singular correction rather than the visible plural source.
4. **I-04 — Reconstruction anchors:** nine top-crest ribbon records contain contradictory REGION and PANEL/ASSOCIATED_VISUAL data.

### MICRO — 1

1. **M-01 — Source punctuation:** `P106-GA-C037` omits the visible terminal period.

## Final verdict

**FAIL**

Counts:

- CRITICAL: **0**
- IMPORTANT: **4**
- MICRO: **1**

The corrected active canonical ledger remains unsuitable for BG-05. BG-04 must remain ACTIVE. No repairs were made.
