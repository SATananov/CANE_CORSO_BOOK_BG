# BG-04 SF-03 INDEPENDENT CANONICAL LEDGER ACCEPTANCE AUDIT

Final verdict: **FAIL**

Mode: independent read-only acceptance audit
Scope: P101-GA, P103-GA, P105-GA, P106-GA, P108-GA, P110-GA, P113-GA, P116-GA, P117-GA
Repairs performed: **NONE**
OCR authority: **NO**

## Executive result

The native-source and legacy-preservation claims pass. Canonical ID arithmetic also passes. Acceptance fails because the canonical ledger is not reconstruction-complete at the required unit granularity: 106 canonical units merge independently placed headings, labels, table cells, warnings, or paragraphs; 15 text-bearing crest/medallion regions are not faithfully inventoried; nine G records contain wording absent from the native source and overlap text-bearing brand artwork; and at least one Italian transcription is visibly wrong. These defects invalidate the 9/9 construction-ready claim.

## 1. Native source identity

**9/9 PASS**

| Graphic | Native file | Independent result | Evidence |
|---|---|:---:|---|
| P101-GA | image-gen-1(20260810-073754).png | SCALED_NATIVE | Title/subtitle, six-stage structure, pregnancy illustrations, right panels, crest and footer correspond. |
| P103-GA | image-gen-2(20260810-073758).png | SCALED_NATIVE | Title/subtitle, four birth phases, warning column, timing/advice strips and footer correspond. |
| P105-GA | image-gen-3(20260810-073802).png | SCALED_NATIVE | Title/subtitle, nine development rows, six repeated columns, illustrations and footer correspond. |
| P106-GA | image-gen-4(20260810-073804).png | SCALED_NATIVE | Growth-plate diagram, recommended/avoid card order, lower panels, title and footer correspond. |
| P108-GA | image-gen-5(9).png | SCALED_NATIVE | Growth table, age order, observation cards, warning strip and footer correspond. |
| P110-GA | image-gen-6(7).png | SCALED_NATIVE | Six numbered sections, central puppy/feeding composition, callouts and footer correspond. |
| P113-GA | image-gen-7(4).png | SCALED_NATIVE | Internal/external parasite panels, three lower panels, icons, motto and footer correspond. |
| P116-GA | image-gen-8(4).png | SCALED_NATIVE | Anatomy, five care panels, alteration/veterinarian panels, motto and footer correspond. |
| P117-GA | image-gen-9(4).png | SCALED_NATIVE | Exact title/subtitle, six cause panels, six-sign strip, reminder and footer correspond. |

The full compositions are present with page-level scaling/resampling; no content-changing crop or derived panel order was found.

## 2. Legacy preservation

**216/216 PASS**

- 24 original U IDs remain present for each of nine graphics.
- Unique historical SF-03 legacy IDs found: 216.
- Original IDs remain unchanged.
- The inventory explicitly preserves each set as `SUPERSEDED_BY_CANONICAL_LEDGER`.
- The required reason is recorded: the legacy ordinals have no surviving positional anchors and cannot be mapped without inventing correspondence.
- No legacy ID is assigned to specific canonical wording.
- No legacy record was silently deleted.
- The active metric excludes the 216 records; the historical metric retains them.

## 3. Canonical ID integrity

**PASS**

| Graphic | Canonical units | First | Last | Contiguous | Duplicates |
|---|---:|---|---|:---:|---:|
| P101-GA | 32 | C001 | C032 | YES | 0 |
| P103-GA | 29 | C001 | C029 | YES | 0 |
| P105-GA | 16 | C001 | C016 | YES | 0 |
| P106-GA | 23 | C001 | C023 | YES | 0 |
| P108-GA | 20 | C001 | C020 | YES | 0 |
| P110-GA | 21 | C001 | C021 | YES | 0 |
| P113-GA | 27 | C001 | C027 | YES | 0 |
| P116-GA | 24 | C001 | C024 | YES | 0 |
| P117-GA | 19 | C001 | C019 | YES | 0 |

- Total: 211
- Unique: 211
- Duplicate canonical IDs: 0
- Missing ordinals: 0
- Wrong-graphic IDs: 0

## 4. Visual completeness and granularity

**FAIL**

- Missing visible text regions: **15** text-bearing crest/medallion regions. The ledger records `USG`, but does not separately and spatially account for the visible ribbon/perimeter wording such as `UNICO SUO GENERE` and, where present, `CANE CORSO`. The ordinary bottom brand line is a different visible occurrence and cannot stand in for seal text.
- Duplicated text units: **0 proven verbatim duplicate placements**.
- Granularity defects: **106 confirmed OVER-MERGED units**.
- Over-split units: 0 confirmed.
- Wrong spatial anchors caused by the over-merges: included in the spatial audit below.

Confirmed over-merging by graphic:

| Graphic | Defective units | Nature |
|---|---:|---|
| P101-GA | 3 | Panel headings merged with panel prose/lists. |
| P103-GA | 6 | Phase heading, time range and prose merged; advice cells merged. |
| P105-GA | 10 | Each development row merges age plus six independently positioned column cells; rules block merged. |
| P106-GA | 12 | Panel/card headings merged with prose; anatomy labels grouped; lower lists merged. |
| P108-GA | 12 | Eight age headers grouped; table cells merged across columns; card headings merged with prose; warning items merged. |
| P110-GA | 14 | Numbered headings, prose, icon labels, table cells and callouts merged. |
| P113-GA | 21 | Section/panel headings merged with subtitles; parasite names merged with prose; lower items and warning list merged. |
| P116-GA | 15 | Anatomy/care/sign headings merged with prose; veterinarian items merged. |
| P117-GA | 13 | Cause headings, secondary headings, lists and sign headings merged with prose. |

This violates the authorized requirement for one unit per independently translatable visible element and prevents direct placement without re-segmenting the source during BG-05.

## 5. Italian source fidelity

**FAIL**

- Faithful or visually supportable canonical source records: **201/211**.
- Mismatches/absent source wording: **10**.

Specific findings:

1. `P105-GA-C008` records `Morsi affinato in sviluppo.`; the native PNG visibly reads `Morso affinato in sviluppo.` This is a source-wording mismatch.
2. The nine G units `P101-GA-C030`, `P103-GA-C027`, `P105-GA-C014`, `P106-GA-C021`, `P108-GA-C018`, `P110-GA-C019`, `P113-GA-C025`, `P116-GA-C022`, and `P117-GA-C017` place the English editorial phrase `Non-language illustration and icon system` in the “Exact Italian source” column. That wording is not visible in any native source.

The nine G records therefore fail source fidelity even before their classification problem is considered.

## 6. Classification

Recorded aggregate arithmetic is confirmed:

- T: 184
- R: 18
- N: 0
- G: 9
- U: 0

Classification acceptance: **FAIL**

Misclassifications: **9** — the G units listed above describe an entire illustration/icon/seal system as a single graphic-only unit. The scope includes text-bearing seals, so those entries both over-group the artwork and hide readable brand text. The crest/logo graphic may be G, but each readable fixed mark must be separately represented and classified R. As written, the logo is also effectively counted through both the broad G unit and the R `USG` unit without clean spatial separation.

U=0 is not itself disproved by unreadability; the native PNGs are readable. The failure is incomplete/incorrect segmentation and classification.

## 7. Bulgarian targets

- T targets structurally present: **184/184**
- Broken/malformed Cyrillic: 0
- Unintended residual Italian: 0 confirmed
- Terminology-lock violations: 0 confirmed
- Unsupported or materially unreliable targets: **3**

Findings:

1. `P105-GA-C008`: its target is attached to an incorrectly transcribed Italian source.
2. `P106-GA-C001`: `ESERCIZIO` is rendered as `ФИЗИЧЕСКО НАТОВАРВАНЕ`, which strengthens “exercise” into “physical load” rather than preserving the neutral source term.
3. `P117-GA-C006`: `INDIZI COMUNI` is rendered as `ЧЕСТИ НАСОКИ`; in this diagnostic context it means common signs/indications, not guidance.

Because the audit is read-only, no replacement wording is proposed or applied.

## 8. Spatial reconstruction readiness

**FAIL**

- Sufficient anchors: **90/211**
- Ambiguous/insufficient anchors: **121/211**

The 121 consist of:

- 106 over-merged units whose single anchor covers multiple independently positioned elements;
- six R units anchored jointly to “crest and medallion,” although those are distinct locations in the graphics where both occur;
- nine G units anchored to the whole illustration/icon/ornamental system rather than a discrete reconstructable element.

Broad anchors such as “upper left,” “lower strip,” or a complete table row are insufficient when the unit contains text intended for several distinct cells or headings.

## 9. Construction-ready determination

**0/9 construction-ready**

| Graphic | Independent status | Blocking reason |
|---|:---:|---|
| P101-GA | NO | Over-merged panels; seal text/classification and brand anchors incomplete. |
| P103-GA | NO | Over-merged phase/advice elements; crest text/classification incomplete. |
| P105-GA | NO | Nine rows merge multiple cells; one Italian mismatch; seal text incomplete. |
| P106-GA | NO | Over-merged cards/panels and labels; translation issue; crest text incomplete. |
| P108-GA | NO | Table headers/cells and cards over-merged; seal text incomplete. |
| P110-GA | NO | Numbered panels, table/icon labels and callouts over-merged; seal text incomplete. |
| P113-GA | NO | Parasite and lower-panel elements over-merged; seal text incomplete. |
| P116-GA | NO | Care/sign/veterinarian elements over-merged; crest text incomplete. |
| P117-GA | NO | Cause/sign elements over-merged; translation issue; seal text incomplete. |

The native identities are proven and no legacy ordinal mapping is needed, but the canonical ledger cannot yet drive reconstruction without re-segmentation and placement guesses.

## 10. Metric arithmetic

### Historical metric

Traceable and arithmetically valid:

- Total: 867
- T/R/N/G/U: 171/50/1/0/645
- Arithmetic: 171 + 50 + 1 + 0 + 645 = 867
- The historical count retains all 216 superseded SF-03 U records.

### Claimed active construction metric

Arithmetically valid and does not double-count the superseded set:

- Historical base excluding SF-03 legacy: 867 − 216 = 651
- Canonical SF-03 added: 211
- Active total: 862
- T/R/N/G/U: 355/68/1/9/429
- Arithmetic: 355 + 68 + 1 + 9 + 429 = 862
- Double-count errors in the stated formula: 0

Metric acceptance remains qualified: the arithmetic is correct, but the 211 canonical records are not acceptance-quality construction units.

## 11. Immutability and scope

- Reference SHA-256 before: `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`
- Reference SHA-256 after: `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`
- Reference byte-identical: **YES**
- Protected-file baseline hashes:
  - Inventory: `3C992478CF1F7F525699709DA489D8E68FB8E5C4C1A380F03BC404093CED3A6A`
  - Canonical ledger: `D9ECCA8B9A536FBFEFE3D505CFE151D0B1FC4815BA33048658908D857574B668`
  - Phase state: `6DE06DBC9C95D76BB105B24D5A9831D320681632140E42A58587A3E8778D10D3`
- BG-04 state before report: ACTIVE
- BG-05 state before report: PENDING
- Scope violations: 0
- OCR authority violations: 0
- Commit performed: NO
- Inventory closing hash: `3C992478CF1F7F525699709DA489D8E68FB8E5C4C1A380F03BC404093CED3A6A` — unchanged
- Canonical-ledger closing hash: `D9ECCA8B9A536FBFEFE3D505CFE151D0B1FC4815BA33048658908D857574B668` — unchanged
- Phase-state closing hash: `6DE06DBC9C95D76BB105B24D5A9831D320681632140E42A58587A3E8778D10D3` — unchanged
- Closing state: BG-04 ACTIVE; BG-05 PENDING

## Findings summary

### CRITICAL — 3 findings

1. **C-01 — Missing text-bearing seal inventory (15 regions):** readable fixed text inside crests/medallions is not separately and spatially represented.
2. **C-02 — Fabricated “exact source” content (9 G units):** English editorial wording absent from the native PNGs appears in the Exact Italian source field.
3. **C-03 — Wrong Italian source wording (1 unit):** `P105-GA-C008` records `Morsi` where the source reads `Morso`.

### IMPORTANT — 3 findings

1. **I-01 — Canonical granularity failure (106 units):** independently translatable headings, labels, cells, lists and paragraphs are over-merged.
2. **I-02 — Classification/brand overlap (9 units plus associated R units):** text-bearing logo systems are treated as non-language G while `USG` is also represented as R without discrete occurrence anchors.
3. **I-03 — Bulgarian semantic defects (3 targets):** the targets attached to `P105-GA-C008`, `P106-GA-C001`, and `P117-GA-C006` are unsupported or materially non-equivalent.

### MICRO — 0 findings

## Final verdict

**FAIL**

Counts:

- CRITICAL: 3
- IMPORTANT: 3
- MICRO: 0

The audit made no repairs. BG-05 must not start from this canonical ledger. BG-04 remains ACTIVE.
