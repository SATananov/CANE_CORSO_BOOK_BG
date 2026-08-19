# BG-03 — ITALIAN SOURCE RECOVERY REPORT

Date: 2026-08-19  
Phase: **BG-03 — BULGARIAN TEXT MASTER**  
Sub-pass: **READ-ONLY ITALIAN SOURCE RECOVERY**  
Final result: **MANUAL DECISION REQUIRED**

## Scope

The Italian project was searched recursively and read-only:

`C:\Users\stana\Desktop\CANE_CORSO_BOOK_IT`

The search covered:

- the complete non-environment working tree, including ignored and hidden files;
- Markdown, TXT, JSON, Python, PowerShell, and other structured/textual files;
- all project PDFs;
- content searches for representative manuscript wording, titles, terminology, captions, bibliography, and page identifiers;
- script input/output paths and hard-coded replacement strings;
- the complete Git tree and all Git revisions, including deleted-file history.

No file was written, renamed, formatted, deleted, staged, or committed in the Italian project.

## Source files discovered

### Primary visual/final sources

- `book_master.pdf` — 143-page flattened master; meaningful native text survives only on isolated pages.
- `output/PRIMA_E_DOPO_IL_CANE_CORSO_IT_FINAL_PRINT_MASTER.pdf` — 143-page final derivative; meaningful native text survives only on six pages.
- `approved_front_cover.png` — approved raster cover.
- `final_cover_assets/cover_phase7f_final.png`
- `final_prepress_assets/final_cover_approved_stefano.png`
- `final_prepress_assets/page_061_final_cleanup_patch.png`
- `final_prepress_assets/headers/page_078_header_clean.png` through `page_096_header_clean.png`
- `final_prepress_assets/dog_heads/page_116_tone_patch.png`, `page_119_tone_patch.png`, and `page_121_tone_patch.png`

These are visual/raster sources, not an editable manuscript.

### Relevant scripts and structured evidence

- `tools/apply_final_cover_phase7f.py` — contains the exact corrected cover author line.
- `tools/apply_final_prepress.py`
- `tools/apply_phase7b_corrections.py`
- `tools/apply_phase7c_corrections.py`
- `tools/apply_phase7d_preview_v2.py`
- `tools/build_current_book_preview.py`
- `tools/build_final_review_preview_v3.py`
- `reports/pdf_inventory.json`
- `reports/page_classification.json`
- `reports/final_correction_plan.json`
- `reports/phase7a_proof_report.json`
- `reports/phase7c_proof_report.json`
- `reports/final_prepress_apply_report.json`
- related Markdown audit/proof reports.

These files document page classes, coordinates, image-object structure, corrections, and visual provenance. They do **not** contain the original page-by-page manuscript.

## Repository-history finding

The current working tree and all Git revisions contain no:

- manuscript Markdown/TXT corpus;
- page-aligned JSON/YAML/CSV text data;
- HTML/template page definitions;
- caption dictionary;
- bibliography source dataset;
- infographic-label dataset;
- deleted or renamed earlier manuscript file.

The Git history contains the same final-prepress/audit family of files and no recoverable upstream text source.

## Page recovery results

The detailed 1–143 mapping is recorded in:

`bg_text/BG_ITALIAN_SOURCE_MAP.md`

| Confidence | Pages | Count |
|---|---|---:|
| EXACT | 141 | 1 |
| HIGH | — | 0 |
| MEDIUM | 1, 54, 55, 61, 70, 104, 140 | 7 |
| UNRESOLVED | all remaining pages | 135 |
| **Total** | 1–143 | **143** |

### Exact recovery

- **Page 141:** complete native bibliography/project-note text block is extractable, including names, titles, dates, DOI data, FCI/NKU/ENCI references, veterinary sources, ESCCAP/WSAVA references, and USG attribution.

### Partial native fragments

- **Page 1:** exact corrected author line exists in `tools/apply_final_cover_phase7f.py`; other cover text is raster-only.
- **Page 54:** exact illustrative-reconstruction caption survives in `book_master.pdf`, duplicated in the PDF object stream.
- **Page 55:** exact 847-character body fragment survives in the final PDF, including explicit Flavio attribution.
- **Page 61:** exact comparative-table caption survives; the table labels do not.
- **Page 70:** exact FCI note survives and identifies Bruno’s statement as a personal position.
- **Page 104:** exact veterinary caution note survives.
- **Page 140:** two bibliography subsections/entries survive, but the rest of the page is flattened.

These pages are classified MEDIUM because their full page text is not recoverable. The exact fragments may be reused only as fragments; they do not authorize reconstruction of missing wording.

## Category recovery

| Category | Result |
|---|---|
| Full native body text | **NO** |
| Titles/subtitles | **NO** — generally flattened |
| Captions | **PARTIAL** — isolated exact captions on pages 54 and 61 |
| Quotations | **NO** |
| Flavio Bruno passages | **PARTIAL** — isolated native fragment/note only |
| Stefano De Tanini passages | **NO** |
| Bibliography | **PARTIAL** — page 141 complete; page 140 incomplete |
| Table text | **NO** |
| Infographic/diagram labels | **NO** |
| Text embedded in raster artwork | **NO editable source found** |
| Page alignment | **EXACT for PDF page objects; not sufficient for editable text recovery** |

## Forty-seven reconstruction pages

Expected graphic-text/reconstruction pages from BG-01: **47**

- Pages with a complete authoritative editable label set found: **0/47**
- Pages with isolated related native text but incomplete graphic labels: **4** — 1, 54, 61, 70
- Pages without editable graphic-label sources: **47/47**

The isolated fragments do not constitute full graphic-label recovery.

## OCR status

OCR is still required somewhere if no upstream source is supplied: **YES**

However, under the human instruction, OCR may be used only as a secondary visual cross-check for isolated labels. It cannot be the authority for names, quotations, bibliography, historical claims, or attribution. Therefore OCR alone cannot unblock BG-03.

## Success-gate assessment

PASS requires enough authoritative source text to resume BG-03 without relying on corrupted OCR.

- Authoritative editable manuscript found: **NO**
- Full body text recoverable: **NO**
- Complete bibliography recoverable: **NO**
- All 47 graphic-text label sets recoverable: **NO**
- Enough authoritative text to resume full BG-03: **NO**

The success gate is not met.

## Required human resolution

Provide or identify an upstream authoritative source outside the searched Italian repository, such as:

1. the original manuscript/editorial document;
2. the page-generation project that predates `book_master.pdf`;
3. a page-aligned export of the Italian text and graphic labels;
4. verified bibliography and infographic source data.

Without such a source, the remaining alternative is a separately authorized manual transcription process with human verification. OCR cannot serve as authority.

## Integrity verification

Immutable BG reference:

`C:\Users\stana\Desktop\CANE_CORSO_BOOK_BG\references\PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before source recovery | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After source recovery | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

- Reference unchanged: **YES**
- Italian project modified: **NO**
- BG project PDFs modified: **NO**
- Bulgarian page masters created: **NO**
- BG-04 started: **NO**
- `BG_PHASE_STATE.json` changed: **NO**
- Commit created: **NO**

## Files created in the BG project

- `bg_text/BG_ITALIAN_SOURCE_MAP.md`
- `reports/bg/BG-03_SOURCE_RECOVERY_REPORT.md`

# FINAL RESULT: MANUAL DECISION REQUIRED

The source recovery sub-pass is complete, but it did not recover enough authoritative editable Italian text to resume translation. BG-03 remains active and incomplete.

