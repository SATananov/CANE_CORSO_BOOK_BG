# BG-03 — BULGARIAN TEXT MASTER REPORT

Date: 2026-08-19  
Phase: **BG-03 — BULGARIAN TEXT MASTER**  
Final status: **MANUAL DECISION REQUIRED**  
BG-03 phase transition: **NOT PERMITTED**

## Outcome

BG-03 cannot safely produce or approve the authoritative Bulgarian text master from the current immutable PDF alone.

The Italian reference is predominantly flattened artwork. Native PDF extraction yielded meaningful text on only **6 of 143 pages**. A full 143-page Italian OCR transcription pass was therefore performed on temporary page renders, followed by a temporary machine-assisted Bulgarian draft. Review of ordinary pages and control/reconstruction pages found recurrent source-transcription corruption and unacceptable Bulgarian distortion.

The temporary OCR and translation drafts were **not** committed to the repository and were **not** presented as approved Bulgarian page text.

## Mandatory stop condition

The following repository rule applies:

> Stop when source meaning is uncertain enough that translation would be speculative.

Observed problems include:

- corrupted occurrences of `Cane Corso` and other proper names;
- damaged quotations and speaker wording;
- merged or split lines that change sentence structure;
- lost punctuation and attribution boundaries;
- incorrect readings in historical and veterinary terminology;
- severe noise in tables, diagrams, maps, screenshots, and dense infographics;
- unreliable bibliography transcription, including names, dates, titles, DOI strings, and publication data;
- machine-assisted Bulgarian that is literal, grammatically unstable, and inconsistent with the required professional editorial standard.

These defects cannot be silently guessed or normalized under `BG_TRANSLATION_RULES.md`.

## Progress and coverage

- Reference pages inspected for transcription feasibility: **143/143**
- Native-text pages detected: **6/143**
- Pages OCR-transcribed to temporary working files: **143/143**
- Temporary machine-assisted Bulgarian drafts generated: **143/143**
- Bulgarian page-master files approved/created in `bg_text/pages/`: **0/143**
- Pages linguistically reviewed to final standard: **0/143**
- Index created: **NO**
- Repository text master completed: **NO**

Temporary drafts do not count as translated or reviewed pages because they fail the language and source-fidelity gates.

## Reconstruction-page coverage

- Expected embedded-image/reconstruction pages from BG-01: **47**
- Temporarily OCR-processed: **47/47**
- Reliably transcribed and approved: **0/47**
- Bulgarian reconstruction wording approved: **0/47**

Dense embedded-image text is the least reliable OCR category and requires source-quality text or controlled human transcription against high-resolution page evidence.

## Quality-control findings

| Check | Result |
|---|---|
| 143/143 source pages assessed | PASS |
| Authoritative Bulgarian files created | FAIL |
| Natural professional Bulgarian | FAIL in temporary draft |
| No speculative source reconstruction | PASS — unreliable draft withheld |
| Terminology-lock compliance | NOT GATEABLE until reliable transcription exists |
| Cane Corso capitalization | Violations present in temporary OCR/draft |
| Pugnax/Bellator historical status | Cannot be fully verified from damaged OCR |
| Mastino Abruzzese handling | Cannot be fully verified from damaged OCR |
| molosso vs molossoide | Cannot be fully verified from damaged OCR |
| Bruno/De Tanini attribution | FAIL in temporary draft where OCR merged boundaries |
| Historical fact/hypothesis distinction | NOT RELIABLY PRESERVED |
| Bibliography integrity | FAIL in temporary draft |
| Control pages 55, 61, 78, 110, 116, 121, 130, 140, 141 | Assessed; OCR noise is material on several control pages |
| Forbidden terminology variants | Present in temporary draft; no repository page text was created |

## Unresolved terminology

- New terminology-lock entries required: **0**
- Terminology uncertainty: **0**
- Source-transcription and editorial uncertainty: **material across the book**

The blocker is not a missing Bulgarian term. It is unreliable recovery of the Italian source wording from flattened artwork.

## MANUAL DECISION REQUIRED

The human owner must select or provide one of the following before BG-03 can continue:

1. **Preferred:** provide the authoritative editable Italian text source used to create the PDF, page-aligned if available.
2. Provide a verified Italian transcription for pages 1–143, including all embedded-image labels and bibliography data.
3. Explicitly authorize a slower manual transcription workflow using high-resolution page evidence, with page batches reviewed and approved before Bulgarian translation proceeds.

Until one of these paths is selected, no Bulgarian page master should be treated as authoritative.

## Immutable-reference verification

Reference:

`references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before BG-03 feasibility/transcription work | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After BG-03 stop decision | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

Reference unchanged: **YES**

## Phase-boundary verification

- PDFs modified: **NO**
- Italian reference modified: **NO**
- Graphics modified: **NO**
- Bulgarian artwork assembled: **NO**
- BG-04 started: **NO**
- BG-05 started: **NO**
- `BG_PHASE_STATE.json` advanced: **NO**
- Automatic commit created: **NO**

## Files created or changed

- Created: `reports/bg/BG-03_BULGARIAN_TEXT_MASTER_REPORT.md`

No `PAGE_XXX_BG.md` files were created because the available drafts do not satisfy the authoritative-text requirement.

# FINAL RESULT: MANUAL DECISION REQUIRED

BG-03 remains active and incomplete. Stop and wait for the human owner’s decision.

