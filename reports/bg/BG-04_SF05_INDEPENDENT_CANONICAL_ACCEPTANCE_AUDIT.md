# BG-04 SF-05 INDEPENDENT CANONICAL ACCEPTANCE AUDIT

Final verdict: **PASS**

Mode: read-only independent canonical acceptance audit after the human-authorized SF-05 rebuild
Scope: `P133-GA`, `P134-GA` only
Repairs performed during acceptance audit: **NONE**
OCR authority: **NO**
BG-04 state: **ACTIVE**
BG-05 state: **PENDING**

## Executive result

SF-05 passes the canonical acceptance gate after the pre-acceptance source/granularity normalization documented in the rebuild report.

Final gate:

- CRITICAL: **0**
- IMPORTANT: **0**
- MICRO: **0**
- construction-ready: **2/2**

Final SF-05 canonical structure:

- canonical units: **109**
- T/R/N/G/U: **93 / 12 / 0 / 4 / 0**
- unresolved SF-05 U: **0**
- duplicate canonical IDs: **0**
- missing ordinals: **0**
- Bulgarian targets present for T units: **93/93**

## Authority / target lock

Human-locked visual targets:

1. `references/source_text/sf05_visual_targets/P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png`
   - SHA-256: `D6448CCC0BCC0D4B7C0368DE56E28342598C3D50B7611D1EDD9C38E4B3D50E03`

2. `references/source_text/sf05_visual_targets/P134_TEMPERAMENTO_TARGET.png`
   - SHA-256: `A7E2578E64D78093168CDDA5B880B653F689F9DD80B2A88FBD8C713E3DC09418`

Both hashes were recomputed in the audit workspace and match exactly.

A higher-resolution Phase7I page rendering was used only as a readability aid after projective registration against the locked screenshots. It was not promoted to authority and no OCR output was used as source text.

## Pre-acceptance normalization history

Before this final acceptance gate, direct visual review caught two draft-level issues and they were corrected in the rebuild input:

1. Source transcription:
   - draft: `CORPO — rilassato ma pronto`
   - visually verified: `CORPO — rilassato ma presente`
   - final Bulgarian value: `отпуснато, но събрано`

2. Canonical granularity:
   - the first draft merged 24 visually separate bold-label/value pairs on P133;
   - these were split before acceptance to match the accepted SF-03 granularity convention;
   - P133 changed from 52 to **76** canonical units;
   - SF-05 changed from 85 to **109** canonical units;
   - no visible wording was added or removed by the split.

The final audit was run only after this normalization.

## Direct visual source-fidelity audit

A fresh direct-visual checklist was transcribed from the locked targets, with the registered higher-resolution rendering used only to make the same pixels easier to read.

### P133-GA

- final canonical units: **76**
- text-bearing units: **74**
- artwork-only G units: **2**
- direct-visual text checklist items: **74**
- exact checklist-to-ledger matches: **74/74**
- missing visible text blocks: **0**
- duplicate visible text blocks: **0**
- over-merged semantic blocks: **0**
- over-split semantic blocks: **0**

The audit explicitly checked:

- crest marks;
- title, subtitle and introduction;
- all four body-language panels;
- each `ORECCHIE / SGUARDO / MUSO / CORPO / CODA` label separately from its value;
- both warning callouts;
- all four context-strip labels and their bodies;
- leadership motto;
- synthesis title and all three synthesis messages;
- signature/role line;
- bottom USG medallion text.

### P134-GA

- final canonical units: **33**
- text-bearing units: **31**
- artwork-only G units: **2**
- direct-visual text checklist items: **31**
- exact checklist-to-ledger matches: **31/31**
- missing visible text blocks: **0**
- duplicate visible text blocks: **0**
- over-merged semantic blocks: **0**
- over-split semantic blocks: **0**

The audit explicitly checked:

- crest marks;
- main title/subtitle/introduction;
- panels 1–6;
- each panel heading;
- each explanatory paragraph;
- each owner-guidance line;
- `NOTA BENE`, explanation and disclaimer;
- signature/role line;
- bottom USG medallion text.

### Aggregate source fidelity

- text-bearing units: **105**
- exact direct-visual matches: **105/105**
- artwork-preservation G units: **4/4**
- source mismatches: **0**

## Canonical ID / arithmetic audit

| Graphic | Total | T | R | N | G | U | Contiguous |
|---|---:|---:|---:|---:|---:|---:|:---:|
| P133-GA | 76 | 68 | 6 | 0 | 2 | 0 | YES |
| P134-GA | 33 | 25 | 6 | 0 | 2 | 0 | YES |
| **TOTAL** | **109** | **93** | **12** | **0** | **4** | **0** | **YES** |

Checks:

- `109 = 93 + 12 + 0 + 4 + 0` — **PASS**
- P133 IDs `C001`–`C076` contiguous — **PASS**
- P134 IDs `C001`–`C033` contiguous — **PASS**
- reading-order ordinals contiguous — **PASS**
- duplicate IDs — **0**

## Role / anchor audit

Final role checks:

- artwork G rows use `ARTWORK`: **4/4**
- retained R text rows use `FIXED_MARK`: **12/12**
- visually separate label rows use `HEADING_OR_LABEL`: **PASS**
- corresponding value/body rows use `BODY_TEXT`: **PASS**
- title, callout, body and fixed-mark roles are compatible with their spatial anchors: **PASS**
- contradictory anchor metadata: **0**
- ambiguous construction anchors: **0**

Anchor sufficiency:

- sufficient / internally consistent: **109/109**
- ambiguous: **0**
- contradictory: **0**

## Bulgarian target audit

- T units: **93**
- Bulgarian targets present: **93/93**
- empty T targets: **0**
- terminology conflict with locked `temperamento → темперамент`: **0**
- terminology conflict with locked `carattere → характер`: **0**
- `Cane Corso → Кане Корсо` handling: **PASS**
- unsupported strengthening of source claims: **0**
- invented factual content: **0**
- unintended untranslated Italian in T targets: **0** except intentionally retained brand `UNICO SUO GENERE`

The two awkward Italian source phrases are kept exactly in the Italian-source column and translated naturally rather than silently rewriting the source:

- `CORPO — più rigido, incurvamento muscolare`
- `MUSO — chiuso, profilo distante`

## Legacy preservation audit

Historical SF-05 records present before activation:

- P133 legacy U: **20**
- P134 legacy U: **20**
- total legacy SF-05 U: **40/40**

Policy compliance:

- legacy records preserved as historical evidence: **PASS**
- set-level status `SUPERSEDED_BY_CANONICAL_LEDGER`: **PASS**
- fabricated legacy-ID → canonical-ID mappings: **0**
- legacy records counted simultaneously as active units: **NO**

The earlier source-lead table may remain in the inventory as historical evidence showing the pre-rebuild state; the later SF-05 active canonical section explicitly supersedes it for construction.

## Construction readiness

| Graphic | Ready |
|---|:---:|
| P133-GA | YES |
| P134-GA | YES |

**Construction-ready: 2/2**

## Active global metric transition

Accepted pre-SF05 active metric:

- **1250 = 709 T + 96 R + 1 N + 15 G + 429 U**
- construction-ready: **17/47**

SF-05 activation removes 40 historical U records from the active count and adds 109 accepted canonical units.

Post-activation metric:

- active units: **1319**
- active T/R/N/G/U: **802 / 108 / 1 / 19 / 389**
- arithmetic: **1319 = 802 + 108 + 1 + 19 + 389 — PASS**
- formula: **867 − 216 − 40 + 599 + 109 = 1319 — PASS**
- unresolved active U after SF-05: **389**
- construction-ready after activation: **19/47**

This transition is authorized only after this PASS and is implemented by the supplied surgical apply script.

## Change-scope audit

- Italian immutable reference modified: **NO**
- Bulgarian PDF modified: **NO**
- production graphics modified: **NO**
- target PNGs modified: **NO**
- BG phase-state file modified: **NO**
- BG-05 started: **NO**
- Git commit created by rebuild/audit: **NO**

## Evidence hashes

- final SF-05 canonical ledger SHA-256: `C3C09E2B23DFE008362568FCC55A676CFE87F27BF1EF12A7C8AF0C52B35FCF3E`
- final SF-05 rebuild report SHA-256: `C6FF3C447C9074B7C963B59C1273C10EDD42DA37DD540901D22E2C5804053F88`
- P133 target SHA-256: `D6448CCC0BCC0D4B7C0368DE56E28342598C3D50B7611D1EDD9C38E4B3D50E03`
- P134 target SHA-256: `A7E2578E64D78093168CDDA5B880B653F689F9DD80B2A88FBD8C713E3DC09418`

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
- construction-ready: **2/2**
- source fidelity: **PASS**
- canonical granularity: **PASS**
- Bulgarian targets: **PASS**
- role/anchor consistency: **PASS**
- legacy preservation: **PASS**
- active-metric arithmetic: **PASS**

**SF-05 is accepted inside BG-04 and may be integrated into the active inventory.**

BG-04 remains **ACTIVE**. BG-05 remains **PENDING**.
