# BG-03 — UPSTREAM SOURCE ALIGNMENT REPORT

Date: 2026-08-19  
Phase: **BG-03 — ACTIVE / INCOMPLETE**  
Scope: **SOURCE ALIGNMENT ONLY — NO BULGARIAN PAGE MASTERS CREATED**

## Authority applied

1. `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf` — visual design, final page order and final-page wording where native text exists.
2. `references/source_text/IL_CANE_CORSO_TUTTI_I_CAPITOLI_COMPLETI.txt` — primary editable Italian textual authority.
3. `references/source_text/IL_CANE_CORSO_Flavio_Bruno_WhatsApp.docx` — secondary Italian cross-check for wording, quotations, attribution and earlier structure.
4. `references/source_text/CANE_CORSO_FINAL_MANUSCRIPT_BG.txt` — secondary Bulgarian translation aid only; it was not used as source or terminology authority.

`bg_text/BG_TERMINOLOGY_LOCK.md` remains the sole Bulgarian terminology authority. No Bulgarian translation was produced in this pass.

## Alignment result

The updated source map covers **143/143 pages**, each exactly once.

| Confidence | Pages | Count |
|---|---|---:|
| EXACT | 55, 141 | **2** |
| HIGH | 1–54, 56–77, 97–139, 142–143 | **121** |
| MEDIUM | 140 | **1** |
| UNRESOLVED | 78–96 | **19** |
| **Total** | 1–143 | **143** |

The primary TXT follows the final PDF's narrative sequence through page 77, then resumes at page 97. PDF pages **78–96** are an inserted visual/editorial atlas that is absent from the primary TXT, the Italian DOCX and the older Bulgarian manuscript.

The Italian DOCX contains an earlier **22-chapter** structure. It supports wording and attribution cross-checks but does not override the final **27-chapter** structure in the primary TXT.

## Recovery coverage

| Area | Coverage | Assessment |
|---|---|---|
| Body text | **112/120 body-text pages recoverable** from authoritative editable Italian; 8 body pages unresolved: 78, 80, 82, 84, 86, 88, 89, 96 | **93.3% / PARTIAL** |
| Titles and section order | Final narrative titles, chapter order and dividers recoverable outside pages 78–96 | **HIGH** |
| Quotations | Quotations in the primary manuscript sequence are recoverable with their attribution; quotation-like material in pages 78–96 is not supplied by an editable source | **PARTIAL** |
| Flavio Bruno / Stefano De Tanini attribution | Recoverable throughout the aligned primary manuscript; atlas-page attribution and explanatory copy remain unresolved | **PARTIAL** |
| Bibliography/reference content | Pages 138–139 recoverable from the primary TXT; page 141 is fully recoverable from authoritative native PDF text; page 140 has only partial native extraction and no complete editable upstream source | **PARTIAL** |
| Embedded-image text | **0/47 pages have a complete editable label set** outside the raster artwork | **UNRESOLVED FOR GRAPHIC LABELS** |

## Pages requiring visual/manual transcription

### Final-PDF-only editorial atlas

Pages **78–96** require authoritative manual transcription and editorial review because their prose and/or labels are absent from every recovered editable source.

### Text embedded in images

The 47 pages identified by `BG_PAGE_INVENTORY.md` remain subject to visual/manual label transcription:

**1, 6, 11, 14, 16, 18, 41, 44, 48, 50, 51, 54, 61, 66, 68, 70, 76, 78, 79, 81, 83, 85, 87, 90, 91, 92, 93, 94, 95, 97, 98, 101, 103, 105, 106, 108, 110, 113, 116, 117, 121, 122, 125, 128, 131, 133, 134.**

Pages **80, 82, 84, 86, 88, 89 and 96** add final-PDF-only ordinary editorial text not counted among those 47 embedded-image pages.

## OCR disposition

- Previous OCR route required as authoritative source: **NO**.
- OCR required for the recovered primary manuscript body: **NO**.
- OCR may be used later only as a secondary checking aid for isolated visual labels absent from editable sources: **YES, optional and non-authoritative**.
- Names, quotations, bibliography, historical claims and attribution may not be accepted from OCR without authoritative visual/manual verification.

## Immutable-reference verification

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before alignment | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After alignment | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

Reference unchanged: **YES**

## Scope controls

- PDFs modified: **NO**
- Graphics modified: **NO**
- Authoritative Bulgarian page masters created: **NO**
- `BG_PHASE_STATE.json` changed: **NO**
- BG-04 started: **NO**
- Automatic commit performed: **NO**

## Gate assessment

The recovered primary TXT is sufficient to replace corrupted OCR as the authority for the main narrative manuscript and permits reliable chapter-level alignment for 123 pages at EXACT/HIGH confidence. It does **not** provide the final-PDF-only atlas on pages 78–96, a complete page-140 bibliography, or complete embedded-image label sets.

Source alignment is therefore materially successful but not complete enough to authorize all 143 Bulgarian page masters without a human decision on the unresolved final-PDF-only material.

# FINAL RESULT: PARTIAL

BG-03 remains active and incomplete. Stop after source alignment and await human approval.
