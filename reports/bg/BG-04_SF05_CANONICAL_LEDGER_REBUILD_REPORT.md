# BG-04 SF-05 CANONICAL LEDGER REBUILD REPORT

Status: **REBUILD COMPLETE — READY FOR INDEPENDENT ACCEPTANCE AUDIT**
Scope: `P133-GA`, `P134-GA`
BG-04: **ACTIVE**
BG-05: **PENDING**
PDF modified: **NO**
Production graphics modified: **NO**
OCR authority: **NO**

## Human authorization

The human explicitly authorized:

> SF-05 canonical rebuild under the same methodology as SF-03.

This authorization applies to SF-05 only.

## Inputs

### Locked visual targets

1. `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png`
   - repo evidence path: `references/source_text/sf05_visual_targets/P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png`
   - SHA-256: `D6448CCC0BCC0D4B7C0368DE56E28342598C3D50B7611D1EDD9C38E4B3D50E03`

2. `P134_TEMPERAMENTO_TARGET.png`
   - repo evidence path: `references/source_text/sf05_visual_targets/P134_TEMPERAMENTO_TARGET.png`
   - SHA-256: `A7E2578E64D78093168CDDA5B880B653F689F9DD80B2A88FBD8C713E3DC09418`

The entire `references/source_text/` tree is intentionally ignored by Git. The target hashes are therefore recorded in tracked reports.

### Supporting governance

- `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md`
- `BG_TERMINOLOGY_LOCK.md`
- `BG_TRANSLATION_RULES.md`
- accepted SF-03 legacy-preservation methodology

## Visual identity / readability aid

A 143-page Phase7I visual review candidate available in the audit workspace was used only to enlarge the same page imagery for direct visual reading.

Projective image registration against the locked screenshots gave:

- P133: 225 good ORB matches, 172 RANSAC inliers, aligned SSIM ≈ 0.854
- P134: 244 good ORB matches, 199 RANSAC inliers, aligned SSIM ≈ 0.825

This is sufficient to use the higher-resolution rendering as a **readability aid**, not as an authority replacement. The locked screenshot hashes remain the authority.

## Legacy preservation

The historical inventory contains:

- P133-GA: 20 legacy ordinal U records
- P134-GA: 20 legacy ordinal U records
- total: 40 legacy U records

Rebuild policy:

- preserve all **40/40** historical U records;
- mark the two legacy sets `SUPERSEDED_BY_CANONICAL_LEDGER`;
- exclude those 40 records from the active construction metric;
- create fresh canonical IDs from the locked visual targets;
- claim **zero** fabricated legacy-to-canonical positional mappings.

## Pre-acceptance direct-visual correction

During the read-only pre-acceptance visual cross-check, one transcription defect was found and corrected before the independent acceptance gate:

- `P133-GA-C011`
  - incorrect draft source: `CORPO — rilassato ma pronto`
  - visually verified source: `CORPO — rilassato ma presente`
  - Bulgarian target normalized to: `ТЯЛО — отпуснато, но събрано`

This source correction itself changes no class or legacy policy.

The same pre-acceptance review also found that the first draft had merged visually separate bold labels with their values in P133. Before acceptance, 24 such label/value blocks were split into separate canonical units, matching the accepted SF-03 granularity rule:

- panels 1–4: five label/value pairs per panel → 20 additional units
- context strip: four heading/body pairs → 4 additional units
- net P133 change: 52 → 76 canonical units
- net SF-05 change: 85 → 109 canonical units
- no visible wording was added or removed by the split
- no legacy-to-canonical remap was created

All P133 canonical IDs were then renumbered contiguously before the independent acceptance audit.

## Canonical rebuild result

### P133-GA

- canonical IDs: `P133-GA-C001`–`P133-GA-C076`
- total: **76**
- T/R/N/G/U: **68 / 6 / 0 / 2 / 0**
- Bulgarian targets: **68/68 T units**
- construction-ready after rebuild: **YES**

### P134-GA

- canonical IDs: `P134-GA-C001`–`P134-GA-C033`
- total: **33**
- T/R/N/G/U: **25 / 6 / 0 / 2 / 0**
- Bulgarian targets: **25/25 T units**
- construction-ready after rebuild: **YES**

### SF-05 aggregate

- canonical units: **109**
- T/R/N/G/U: **93 / 12 / 0 / 4 / 0**
- U: **0**
- duplicate canonical IDs: **0**
- missing ordinals: **0**
- construction-ready: **2/2**

## Translation handling

Translations follow the locked BG rules:

- `Cane Corso` → `Кане Корсо`
- `temperamento` remains distinct from `carattere`
- headings/captions are translated consistently
- fixed USG marks remain in canonical form
- no content was shortened solely for layout
- no historical or behavioral claim was strengthened

Two visibly awkward Italian phrases were retained exactly in the Italian-source column and rendered naturally in Bulgarian:

- `CORPO — più rigido, incurvamento muscolare`
- `MUSO — chiuso, profilo distante`

## Active global metric after SF-05 activation

Accepted pre-SF05 active metric:

- **1250 = 709 T + 96 R + 1 N + 15 G + 429 U**

SF-05 transition:

- remove 40 historical SF-05 U from active construction count
- add 109 canonical SF-05 units

New active metric:

- **1319**
- active T/R/N/G/U: **802 / 108 / 1 / 19 / 389**
- arithmetic: **1319 = 802 + 108 + 1 + 19 + 389 — PASS**
- formula: **867 − 216 − 40 + 599 + 109 = 1319 — PASS**
- remaining non-SF03/non-SF05 U: **389**

Construction-ready graphics after SF-05 activation:

- prior accepted ready graphics: **17/47**
- SF-05 newly ready: **2**
- new total: **19/47**

## Files to integrate

Tracked:

- `reports/bg/BG-04_SF05_CANONICAL_UNIT_LEDGER.md`
- `reports/bg/BG-04_SF05_CANONICAL_LEDGER_REBUILD_REPORT.md`
- `reports/bg/BG-04_SF05_INDEPENDENT_CANONICAL_ACCEPTANCE_AUDIT.md`
- `graphics_bg/BG_IMAGE_TEXT_INVENTORY.md` (via the supplied surgical apply script)

Ignored local evidence:

- the two target PNGs under `references/source_text/sf05_visual_targets/`

## Gate

The rebuild itself is complete. Acceptance remains subject to the independent SF-05 canonical audit.
