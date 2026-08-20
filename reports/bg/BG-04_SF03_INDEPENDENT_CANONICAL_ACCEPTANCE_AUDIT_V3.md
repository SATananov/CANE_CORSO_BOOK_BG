# BG-04 SF-03 INDEPENDENT CANONICAL ACCEPTANCE AUDIT V3

Final verdict: **FAIL**

Mode: final independent read-only SF-03 acceptance audit
Scope: P101-GA, P103-GA, P105-GA, P106-GA, P108-GA, P110-GA, P113-GA, P116-GA, P117-GA
Repairs performed: **NONE**
OCR authority: **NO**

## Executive result

V2 successfully closes the 8 over-merges, 12 over-split boundaries, 2 Italian source mismatches, and 9 named spatial-region contradictions. Canonical arithmetic, visible-text completeness, R/G handling, legacy preservation, and global metrics also pass. Acceptance still fails because the replacement Bulgarian target for the P105 source `Morsi affinato in sviluppo.` omits `in sviluppo`, and the all-record regression sweep finds 83 ELEMENT_ROLE conflicts. The active ledger is therefore not reconstruction-quality.

## V2 finding closure

| Category | V2 count | Verified fixed | Remaining | Verdict |
|---|---:|---:|---:|:---:|
| Over-merged | 8 | 8 | 0 | PASS |
| Over-split | 12 | 12 | 0 | PASS |
| Italian source fidelity | 2 | 2 | 0 | PASS |
| Unsupported BG target | 1 | 0 | 1 | FAIL |
| Contradictory spatial anchors named by V2 | 9 | 9 | 0 | PASS |

The structural fixes were checked against the affected native blocks. No visible text was lost or duplicated by the V2 merges and splits.

## Regression sweep

| Check | New/remaining defects |
|---|---:|
| New over-merges | 0 |
| New over-splits | 0 |
| Missing visible text | 0 |
| Duplicated visible text | 0 |
| Source regressions | 0 |
| BG target regressions / incomplete correction | 1 |
| Classification regressions | 0 in T/R/G class |
| Duplicate IDs | 0 |
| Missing ordinals | 0 |
| Wrong reading order | 0 blocking |
| Spatial/role metadata regressions or residual conflicts | 84 |

## Native identity

**9/9 SCALED_NATIVE — PASS**

| Graphic | Native PNG |
|---|---|
| P101-GA | image-gen-1(20260810-073754).png |
| P103-GA | image-gen-2(20260810-073758).png |
| P105-GA | image-gen-3(20260810-073802).png |
| P106-GA | image-gen-4(20260810-073804).png |
| P108-GA | image-gen-5(9).png |
| P110-GA | image-gen-6(7).png |
| P113-GA | image-gen-7(4).png |
| P116-GA | image-gen-8(4).png |
| P117-GA | image-gen-9(4).png |

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

- Arithmetic: **538 + 46 + 0 + 15 + 0 = 599 — PASS**
- Unique IDs: **599**
- Duplicate IDs: **0**
- Missing ordinals: **0**
- C001 starts: **9/9**
- Wrong prefixes: **0**
- Superseded V1 rows mixed into active table: **0**

## Final granularity and visual completeness

- Over-merged units: **0 confirmed**
- Over-split boundaries: **0 confirmed**
- Missing visible text: **0 confirmed**
- Duplicate visible text: **0 confirmed**
- Wrong visible-block boundaries: **0 confirmed**

The P105 age labels now form single boxed units; the P108 muscle card is split into heading/body; the P110 introductory paragraph and first bullet are correctly separated; and the six P117 secondary headings are separate from their panel prose.

## Source fidelity

- Verified: **599/599**
- Mismatches: **0**
- `P105-GA-C072` visibly reads `Morsi affinato in sviluppo.`; the active source field now matches it.
- `P106-GA-C037` includes the visible final period.
- Numeric ranges, temperature values, time values, abbreviations, and fixed marks checked: no remaining mismatch recorded.
- OCR used: **NO**

The earlier `Morso` claim is not supported by direct inspection of the native PNG; the pixels visibly show `Morsi`. V2 correctly restores that visible wording.

## Bulgarian targets

- T targets present: **538/538**
- Fully supported: **537/538**
- Unsupported or materially incomplete: **1**
- Terminology violations: **0 confirmed**
- Broken Cyrillic/mojibake: **0**
- Unintended residual Italian: **0 confirmed**

Exact blocker:

- `P105-GA-C072`
  - Source: `Morsi affinato in sviluppo.`
  - Target: `Захапванията се усъвършенстват.`
  - Finding: `in sviluppo` (“in development / in the course of development”) is omitted. The target does not cover the complete source unit and therefore does not close the V2 equivalence finding.

## R, G, crest, and medallion handling

- R verified: **46/46**
- Invalid retention rationales: **0**
- Normal prose hidden as R: **0**
- G verified: **15/15**
- Invented English in G source fields: **0**
- Readable crest/medallion text hidden in G: **0**
- Original 15 text-bearing crest/medallion regions properly separated: **15/15**
- Duplicate visible seal text occurrences: **0**

## Spatial anchors and ELEMENT_ROLE consistency

- Fully sufficient and internally consistent: **515/599**
- Ambiguous: **0**
- Contradictory role metadata: **84**

The nine V2 top-crest ribbon REGION corrections are closed. The remaining failures are ELEMENT_ROLE conflicts: the source and relative-position fields identify visible headings, labels, captions, bullets, or a paragraph, while ELEMENT_ROLE says `BODY_TEXT` or `HEADING_OR_LABEL` incompatibly.

### Exact affected records

- P101: C027, C029
- P103: C041
- P106: C003, C012, C015, C017, C019, C021, C024, C026, C028, C030, C032, C037, C038
- P108: C049, C051, C053, C057, C059
- P110: C003, C005–C009, C019, C023, C031–C033, C039, C041–C045
- P113: C005, C007, C009, C011, C015, C017, C019, C021, C023, C025, C027, C029, C031, C033, C035, C037, C039, C041
- P116: C004, C006, C008, C010, C012, C017, C022, C026, C030, C035, C037, C039, C041, C043, C045, C047
- P117: C003, C009, C016, C023, C030, C037, C044, C046, C048, C050, C052, C054

Representative contradictions:

1. `P110-GA-C032` is explicitly anchored as an “introductory paragraph,” but ELEMENT_ROLE is `HEADING_OR_LABEL`. This conflict was carried into the V2-created unit.
2. `P117-GA-C009` contains the panel heading `INFIAMMAZIONE`, but ELEMENT_ROLE is `BODY_TEXT`.
3. `P113-GA-C025` is the independently styled item heading `VERMIFUGO REGOLARE`, but ELEMENT_ROLE is `BODY_TEXT`.
4. `P110-GA-C033` is explicitly “bullet 1,” but ELEMENT_ROLE is `BODY_TEXT`.

Because the required schema includes ELEMENT_ROLE and demands field consistency, these records do not meet the 599/599 anchor gate even though their panel locations are otherwise identifiable. No BBOX_NORM resolves a semantic role contradiction.

## Legacy preservation

- Preserved: **216/216**
- Required status: `SUPERSEDED_BY_CANONICAL_LEDGER` — present
- Original IDs retained: **YES**
- False legacy-to-canonical mappings: **0**
- Active double-counting: **0**

## Construction readiness

**0/9 construction-ready**

| Graphic | Ready | Blocking reason |
|---|:---:|---|
| P101-GA | NO | ELEMENT_ROLE conflicts. |
| P103-GA | NO | ELEMENT_ROLE conflict. |
| P105-GA | NO | Unsupported/incomplete Bulgarian target C072. |
| P106-GA | NO | ELEMENT_ROLE conflicts. |
| P108-GA | NO | ELEMENT_ROLE conflicts. |
| P110-GA | NO | ELEMENT_ROLE conflicts, including V2-created C032/C033. |
| P113-GA | NO | ELEMENT_ROLE conflicts. |
| P116-GA | NO | ELEMENT_ROLE conflicts. |
| P117-GA | NO | ELEMENT_ROLE conflicts. |

## Active global metric

Historical metric:

- **867 = 171 T + 50 R + 1 N + 0 G + 645 U**

Active construction metric:

- Formula: **867 − 216 + 599 = 1250**
- Active total: **1250**
- Active T/R/N/G/U: **709/96/1/15/429**
- Legacy 216 U records active-counted: **NO**
- Non-SF03 unresolved U pool: **429**, unchanged
- Arithmetic: **PASS**

## Immutability

Before hashes:

| Item | SHA-256 |
|---|---|
| Italian reference PDF | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| BG phase state | `6DE06DBC9C95D76BB105B24D5A9831D320681632140E42A58587A3E8778D10D3` |
| Image-text inventory | `9A1F77F6009BB193DB32D7E8B5A4C154E987E50EF5AC852E2683929A95CC27FA` |
| Canonical ledger | `1B6DB53EB80B20D1576C9C5650247E44036E37B2F6DD035EE83CB81E130A5D4F` |
| V2 correction report | `54A7D7E91D109D41E9F6835ADE96BC84F7581AB356667EFAAA6B272D63897760` |
| V2 remap | `AA7B37FA892000ABD395FE2D468DBD1F6E65859B84E3F58FA7649F27190B99B6` |

Only this V3 report was created. No repair, phase transition, BG-05 work, or commit was performed.

Closing verification:

- Italian reference SHA-256 after: `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`
- Protected evidence hashes after: identical to the before table
- Native PNG hashes after: **9/9 unchanged**
- BG phase state after: BG-04 **ACTIVE**; BG-05 **PENDING**

## Findings

### CRITICAL — 0

None.

### IMPORTANT — 2

1. **I-01 — Bulgarian target incomplete:** `P105-GA-C072` omits the source concept `in sviluppo`.
2. **I-02 — Anchor-schema regression/residual defect:** 84 records have an ELEMENT_ROLE that conflicts with the visible unit and/or the row’s own relative-position metadata.

### MICRO — 0

None.

## Final verdict

**FAIL**

Counts:

- CRITICAL: **0**
- IMPORTANT: **2**
- MICRO: **0**

All 599 units are not yet anchor-consistent, all T targets are not fully supported, and construction readiness is **0/9**. BG-04 must remain ACTIVE; BG-05 must remain PENDING.
