# BG-04 — INDEPENDENT ACCEPTANCE AUDIT V2

Date: 2026-08-19  
Phase audited: **BG-04 — IMAGE-TEXT INVENTORY**  
Audit mode: **REPORT ONLY**  
BG-05 readiness: **NO**

## Scope

V2 independently audited the corrected `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`, the updated BG-04 inventory report, the correction-pass report, the V1 acceptance findings, the final Italian reference, source map, page inventory, terminology lock, and applicable guardian instructions.

No inventory, PDF, graphic, page master, source, or phase-state file was edited.

## Executive result

The targeted correction materially improves the inventory: the 47-page set remains correct, page 121 is now correctly treated as documentary preservation, the manual-status metadata is reduced to one record, and substantial Bulgarian target prose was added.

However, the two V1 CRITICAL findings are not actually closed. The correction introduces 38 element-ID **ranges**, not 761 individually addressable element records, and only 122 visible Italian-to-Bulgarian arrow mappings are present. The reported 752 exact Bulgarian targets therefore remain neither countable nor independently reproducible. Multiple packs still replace exact text with summaries, ellipses, generalized progressions, or instructions.

## Structural verification

| Check | Result |
|---|---:|
| Affected page records | **47** |
| Graphic records | **47** |
| Missing affected pages | **0** |
| Duplicate page records | **0** |
| Declared per-record counts summed | **761** |
| LOW / MEDIUM / HIGH | **7 / 13 / 27** |
| `Manual review required: YES` records | **1** |
| `RESOLVED / AUTHORITATIVE TARGET READY` markers | **25** |
| Remaining unresolved record markers | **1** |

The page, graphic, manual-status, and difficulty arithmetic is internally consistent.

## Element-addressability audit

| Evidence | Count |
|---|---:|
| Claimed Italian text units | **761** |
| Individually written element IDs | **1** (`P016-016-A-E09`) |
| Element-ID ranges | **38** |
| Explicit `Italian → Bulgarian` mappings | **122** |
| Original `Bulgarian target text` lines still containing “translate” instructions | **33** |

The statement that units “receive stable IDs in top-to-bottom, left-to-right reading order” does not instantiate those IDs. A range such as `P105-105-A-E01–E24` identifies a page-level group, but it does not state which visible string is E01, E02, E03, and so on. Consequently:

- omission and duplication checks cannot be performed at element level;
- the declared 761 units cannot be reconciled to 761 records;
- the declared 752 Bulgarian targets cannot be counted;
- BG-05 would still have to infer how grouped target prose maps to individual visual boxes, cells, values, and labels.

V1 CRITICAL finding 1: **NOT RESOLVED**.  
V1 CRITICAL finding 2: **NOT RESOLVED**.

## Exact-target audit

The following are representative construction blockers, not an exhaustive list:

1. **Page 11:** four publication titles, four author lines, and four publisher/year lines are described collectively as `PRESERVE ORIGINAL`; the exact twelve strings are not recorded.
2. **Page 16:** the archive paragraph is still introduced in the base record with “translate ... faithfully,” and the correction annex does not supply its exact Bulgarian target. The single unresolved `E09` also aggregates numerous distinct UI strings visible in two screenshots.
3. **Page 76:** the Italian source is written as `Le incisioni di Bartolomeo Pinelli...`; four distinct vignette captions are replaced with generalized topic labels rather than exact source-to-target pairs.
4. **Page 85:** context and evidentiary prose were added, but the five legend entries are not individually mapped to exact Bulgarian targets.
5. **Pages 93–95:** map/ocean/geographical labels are described in the base inventory but are not individually assigned target or preserve-original actions in the correction packs.
6. **Page 103:** the four phase headings and durations are supplied, but the phase body paragraphs and their individual bullet lists are not fully translated element by element.
7. **Page 105:** fifty-four week-by-category cells are reduced to a generalized progression using arrows. This is not the exact wording for every visible cell.
8. **Page 106:** eight movement cards and their explanatory prose are reduced to short category phrases; the visible card text is not fully mapped.
9. **Page 108:** weight ranges are present, but the proportions, movement, and body-condition table cells across the month columns are not individually reproduced.
10. **Page 110:** module headings, meal counts, and risk labels are present, but several visible explanatory paragraphs and callouts are summarized rather than exactly translated.
11. **Page 116:** the pack explicitly says to “retain the final-PDF bullet order” and provides condensed imperatives. This remains a construction instruction, not exact target text for each bullet.

The annex’s declaration that it supersedes directive-only wording does not eliminate ambiguity while the original 33 directive lines remain and the annex itself contains grouped or incomplete target descriptions.

## Manual-review classification V2

### A-class block

Page 16’s fine screenshot UI remains genuinely unresolved: **CONFIRMED**.

Its isolation is incomplete, however, because multiple visible screenshot strings are represented by a single `E09` unit. Before acceptance, the unresolved block must be explicitly bounded—for example, by screenshot panel and UI region—without guessing the wording.

### B-class blocks

- Status markers changed to resolved: **25/25**
- Independently demonstrable as complete, element-addressable, exact target sets: **0/25**
- Still containing at least one grouped, unmapped, summarized, or instruction-only component: **25/25**

This does not mean every added translation is incorrect. It means no B record satisfies the acceptance requirement that every claimed unit be independently traceable from exact Italian wording to one exact Bulgarian construction target.

### D-class block

Page 121 documentary signage: **CORRECTLY HANDLED**.

The eight photographed sign strings remain genuine inventory content but have no Bulgarian in-image replacement target. Removing them from the manual translation queue while preserving the photograph is correct.

## Terminology and evidentiary controls

| Area | Result |
|---|---|
| Кане Корсо / Pugnax / Mastino Abruzzese handling | **PASS in sampled explicit targets** |
| молос / молосоид distinction | **PASS in sampled explicit targets** |
| Functional versus genealogical continuity | **PASS** |
| `Функцията формира типа` | **PASS** |
| Flavio versus Stefano attribution | **PASS in explicit atlas targets** |
| Hypothesis/interpretation not converted into fact | **PASS in explicit atlas targets** |
| Full-lock compliance across 752 claimed targets | **NOT AUDITABLE** because 752 targets are not individually present |

No confirmed terminology violation was found in the explicit Bulgarian prose sampled. This does not cure the missing-target problem.

## Visual-atlas audit

The affected atlas page set remains correct: `78, 79, 81, 83, 85, 87, 90, 91, 92, 93, 94, 95`.

The new prose generally preserves hypothesis status, Stefano attribution, and non-genealogy warnings. Nevertheless, atlas acceptance remains **FAIL** because individual map labels, legend entries, card paragraphs, source/status lines, and preserve-original actions are not exhaustively enumerated and mapped on every page.

## Control pages

| Page | V2 result |
|---:|---|
| 55 | Correctly excluded. |
| 61 | Table target prose substantially improved, but no individual E01–E22 mapping exists. |
| 78 | Methodological status is protected; individual element mapping remains range-based. |
| 110 | Still incomplete at paragraph/callout level. |
| 116 | Still contains condensed instructions instead of exact bullet targets. |
| 121 | **PASS** — authentic photograph preserved; no in-image Bulgarian target required. |
| 130 | Correctly excluded. |
| 140 | Correctly excluded; decorative head only. |
| 141 | Correctly excluded; decorative head only. |

## Finding register

### CRITICAL — 2

1. **No 761-item authority exists.** The 761 figure is still only the sum of declared page estimates; one explicit ID plus 38 ranges cannot prove element-level completeness.
2. **No 752-target authority exists.** The count is arithmetic (`761 − 8 − 1`), not a count of 752 explicit Bulgarian targets. BG-05 would still need to translate, expand, or infer missing text.

### IMPORTANT — 4

1. All 25 B records are marked resolved without satisfying element-level traceability.
2. Dense veterinary/table graphics remain incomplete, particularly pages 103, 105, 106, 108, 110, and 116.
3. Atlas maps retain unmapped geographic/legend text, particularly pages 85 and 93–95.
4. Thirty-three earlier target fields retain active-looking translation directives, creating conflicting authority inside the same file.

### MICRO — 1

1. The page-16 A block should be bounded into its actual screenshot/UI regions instead of being labelled as one undifferentiated element.

## Gate assessment

- 47 affected pages and graphics: **PASS**
- Difficulty counts: **PASS**
- Page-121 D handling: **PASS**
- Single A-class authority gap recognized: **PARTIAL PASS**
- 2/2 V1 CRITICAL findings resolved: **FAIL — 0/2**
- 3/3 V1 IMPORTANT findings resolved: **FAIL**
- 1/1 V1 MICRO finding resolved: **PARTIAL — page 121 fixed, page-16 bounding issue remains**
- 25/25 B blocks exact and construction-ready: **FAIL**
- Recoverable text remaining outside exact targets: **YES**
- Ready for BG-05: **NO**

Required remediation remains:

1. instantiate every `Pxxx-Gx-Exx` record individually;
2. record exact Italian wording or an explicit preserve-unchanged action for each record;
3. record one exact Bulgarian target for every translatable record;
4. eliminate all group summaries, ellipses, progressions, and “translate/retain” instructions where exact text is required;
5. recalculate totals from the actual records rather than declared page counts;
6. bound the page-16 unresolved screenshot regions precisely.

## Integrity and phase controls

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before V2 audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After V2 audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

- PDFs modified: **NO**
- Graphics modified: **NO**
- Inventory modified: **NO**
- Page masters modified: **NO**
- BG-05 started: **NO**
- Phase state changed: **NO**
- Commit performed: **NO**

# FINAL RESULT: FAIL

BG-04 remains active. The corrected inventory is materially improved but is not yet an exact, independently countable, construction-ready authority.
