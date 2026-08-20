# BG-04 SF-03 INDEPENDENT CANONICAL ACCEPTANCE AUDIT V4

Final verdict: **FAIL**

Mode: independent read-only differential acceptance audit after the manual V3 fix
Scope: P101-GA, P103-GA, P105-GA, P106-GA, P108-GA, P110-GA, P113-GA, P116-GA, P117-GA
Repairs performed: **NONE**
OCR authority: **NO**

## Executive result

The manual V3 correction is structurally clean and narrowly scoped. Compared with the V3-audited ledger, exactly **85 active records changed**: **84 ELEMENT_ROLE fields** and **1 Bulgarian target**. No canonical ID, reading order, region, panel, associated visual, relative position, Italian source, class, or source-image field changed. The active inventory mirrors the corrected ledger exactly.

The Bulgarian target blocker at `P105-GA-C072` is closed. The 84 V3-listed role findings are almost completely closed, but one listed record (`P110-GA-C033`) remains semantically inconsistent after being changed from `BODY_TEXT` to `HEADING_OR_LABEL`: the row explicitly identifies the unit as `bullet 1`, and the native graphic shows it as the first bullet item in a four-item list.

The all-record regression sweep also finds five pre-existing role inconsistencies that V3 did not list: `P101-GA-C012` and `P103-GA-C007/C014/C022/C030`. In each case the source is continuous explanatory prose and the relative-position metadata identifies an explanation/body block, but ELEMENT_ROLE is `HEADING_OR_LABEL`.

Therefore the ledger is not yet 599/599 role-consistent.

## V3 finding closure

| Category | V3 count | Verified fixed | Remaining | Verdict |
|---|---:|---:|---:|:---:|
| Incomplete BG target | 1 | 1 | 0 | PASS |
| V3-listed ELEMENT_ROLE conflicts | 84 | 83 | 1 | FAIL |

### P105-GA-C072

- Source: `Morsi affinato in sviluppo.`
- Current target: `Захапванията се усъвършенстват в хода на развитието.`
- `in sviluppo` is now represented.
- Exact Unicode target comparison: **PASS**.

## Differential regression proof

V3 ledger -> current V4 package:

- active records before: **599**
- active records after: **599**
- records changed: **85**
- ELEMENT_ROLE-only changes: **84**
- Bulgarian-target-only changes: **1**
- ID changes: **0**
- reading-order changes: **0**
- REGION changes: **0**
- PANEL changes: **0**
- ASSOCIATED_VISUAL changes: **0**
- RELATIVE_POSITION changes: **0**
- Italian source changes: **0**
- T/R/N/G/U class changes: **0**
- source-image changes: **0**

Because no unit boundary, source wording, class, ID, or spatial-placement field changed, the V3 passes for granularity, visible-text completeness, source fidelity, ID integrity, R/G handling, and active arithmetic remain structurally non-regressed.

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

- Arithmetic: **599 = 538 + 46 + 0 + 15 + 0 — PASS**
- Duplicate IDs: **0**
- Missing ordinals: **0**
- Empty mandatory anchor fields: **0**
- Inventory active section vs canonical ledger: **599/599 exact row match**

## V3-listed role corrections

Observed role transitions in the 84 V3-listed records:

- `BODY_TEXT -> HEADING_OR_LABEL`: **82**
- `BODY_TEXT -> FIXED_MARK`: **1** (`P106-GA-C037`)
- `HEADING_OR_LABEL -> BODY_TEXT`: **1** (`P110-GA-C032`)

The following representative corrections are valid:

- `P117-GA-C009` `INFIAMMAZIONE` -> `HEADING_OR_LABEL`
- `P113-GA-C025` `VERMIFUGO REGOLARE` -> `HEADING_OR_LABEL`
- `P110-GA-C032` introductory paragraph -> `BODY_TEXT`
- `P106-GA-C037` medallion slogan -> `FIXED_MARK`, consistent with the ledger's existing treatment of translated fixed mottos/marks

### Remaining V3-listed conflict

`P110-GA-C033`

- source: `Peso e forma corporea adeguati`
- current role: `HEADING_OR_LABEL`
- current relative position: `bullet 1`
- native graphic: first bullet item under `5 OSSERVAZIONE DEL CANE`
- sibling items C034-C036 are body/list items

Verdict: **role metadata still inconsistent**.

Recommended minimal correction: return C033 to `BODY_TEXT` and normalize its RELATIVE_POSITION to `/2of2/1of4`, matching C034-C036. This preserves the existing role vocabulary and removes the explicit role/position contradiction without creating a new enum value.

## Additional all-record regression findings

V4 independently swept all active rows for semantic contradictions between ELEMENT_ROLE, RELATIVE_POSITION, source form, and neighboring records.

Five additional pre-existing inconsistencies were found:

1. `P101-GA-C012`
   - role: `HEADING_OR_LABEL`
   - relative position: `stage explanation`
   - source: `Gli organi principali iniziano a formarsi: cuore, sistema nervoso, arti e organi interni. Il feto cresce rapidamente.`
   - native graphic: explanatory paragraph under `3 SVILUPPO PRECOCE`
   - expected role: `BODY_TEXT`

2. `P103-GA-C007`
   - role: `HEADING_OR_LABEL`
   - source is the explanatory prose for Phase 1
   - expected role: `BODY_TEXT`

3. `P103-GA-C014`
   - role: `HEADING_OR_LABEL`
   - source is the explanatory prose for Phase 2
   - expected role: `BODY_TEXT`

4. `P103-GA-C022`
   - role: `HEADING_OR_LABEL`
   - source is the explanatory prose for Phase 3
   - expected role: `BODY_TEXT`

5. `P103-GA-C030`
   - role: `HEADING_OR_LABEL`
   - source is the explanatory prose for Phase 4
   - expected role: `BODY_TEXT`

The native P101 and P103 graphics visually confirm that these five units are paragraph/explanation blocks, not headings or labels.

## Source fidelity and visual completeness

No source field changed after V3. The V3 audit had already verified 599/599 source transcriptions and 0 missing/duplicate visible text; the V4 differential comparison confirms no source or unit-boundary mutation occurred after that audit.

- source-field regressions introduced by manual fix: **0**
- unit-boundary changes: **0**
- missing/duplicate IDs introduced: **0**
- class changes: **0**

## Bulgarian targets

- T units: **538**
- unchanged targets already accepted by V3: **537**
- changed target independently rechecked: **1/1 PASS**
- supported targets after manual fix: **538/538**
- new target regressions: **0**

## Spatial / role consistency

- total active units: **599**
- remaining contradictory role metadata: **6**
- otherwise anchor fields present: **599/599**

Exact remaining records:

- `P101-GA-C012`
- `P103-GA-C007`
- `P103-GA-C014`
- `P103-GA-C022`
- `P103-GA-C030`
- `P110-GA-C033`

## Construction readiness

| Graphic | Ready | Blocking reason |
|---|:---:|---|
| P101-GA | NO | C012 role mismatch |
| P103-GA | NO | C007/C014/C022/C030 role mismatches |
| P105-GA | YES | V3 target blocker closed |
| P106-GA | YES | V3 role findings closed |
| P108-GA | YES | V3 role findings closed |
| P110-GA | NO | C033 bullet-role inconsistency |
| P113-GA | YES | V3 role findings closed |
| P116-GA | YES | V3 role findings closed |
| P117-GA | YES | V3 role findings closed |

Construction-ready: **6/9**

## Active metric

No canonical count or class changed, so the active metric remains:

- active total: **1250**
- active T/R/N/G/U: **709 / 96 / 1 / 15 / 429**
- non-SF03 unresolved U: **429**
- legacy 216 SF-03 U records remain excluded from active counting

## Current package hashes

- V4 package ZIP: `A4BEADD53C4F2E9DCE1FFAFE02B4EBB2B5398F36307FF509CFA1AD6D7587BDE4`
- corrected canonical ledger: `7EAC8183598F0F4375BE29E8606C26B395F5E26D612016519A634FAA0925919E`
- corrected inventory: `3F2788936A9A608D664CC2215CE3A6AC68E5A916B8924B45AD76AAC64A30263A`

Native assets were read-only during V4. No PDF, phase-state file, production graphic, or source PNG was modified by this audit.

## Findings

### CRITICAL — 0

None.

### IMPORTANT — 2

1. **I-01 — Residual/missed explanatory-paragraph role defects:** `P101-GA-C012`, `P103-GA-C007`, `P103-GA-C014`, `P103-GA-C022`, `P103-GA-C030` are explanatory prose but remain `HEADING_OR_LABEL`.
2. **I-02 — P110 bullet correction remains semantically inconsistent:** `P110-GA-C033` is a bullet/list item but is now `HEADING_OR_LABEL` while its sibling list items are body records.

### MICRO — 0

None.

## Final verdict

**FAIL**

Counts:

- CRITICAL: **0**
- IMPORTANT: **2**
- MICRO: **0**
- Construction-ready: **6/9**

The manual V3 fix successfully closes the Bulgarian-target defect and 83 of the 84 explicitly listed V3 role defects, but SF-03 is not yet ready to lock because six role-metadata inconsistencies remain. BG-04 must remain ACTIVE and BG-05 must remain PENDING.
