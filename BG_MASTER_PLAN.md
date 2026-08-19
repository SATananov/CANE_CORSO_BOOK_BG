# CANE CORSO BOOK BG — MASTER PLAN

Project: `CANE_CORSO_BOOK_BG`  
Edition: Bulgarian  
Visual authority: locked Italian Phase 7I FINAL  
Target page count: **143**  
Mode: phased, gated, audit-first workflow

## Non-negotiable project rule

The Italian reference PDF is immutable. The Bulgarian edition must preserve the same book architecture and visual language. Translation is allowed to change language-dependent content only. No phase may silently redesign the book.

---

## BG-00 — PROJECT LOCK

**Status:** COMPLETE

### Input
- Clean BG repository.
- Immutable Italian reference:
  `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

### Required reference SHA-256
`A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`

### Pass conditions
- BG repository exists independently from IT repository.
- Working tree is clean.
- IT reference exists and hash matches.
- BG working folders exist.

---

## BG-01 — 143-PAGE INVENTORY

**Status:** ACTIVE  
**Mode:** REPORT ONLY — DO NOT MODIFY PDF

### Goal
Classify every page 1–143 before translation begins.

### Required classification fields
- page number
- page class
- body text present
- heading/subheading present
- caption present
- table present
- infographic/diagram present
- Italian text embedded in image
- bibliography/reference content
- decorative Cane Corso head present
- special visual notes
- translation difficulty
- reconstruction required
- review notes

### Output
`BG_PAGE_INVENTORY.md` completed for all 143 pages.

### Pass conditions
- 143/143 pages recorded.
- No page omitted.
- Embedded Italian text candidates identified.
- Special pages identified.
- No source PDF modification.

---

## BG-02 — TERMINOLOGY LOCK

**Status:** PENDING

### Goal
Create a single Bulgarian terminology authority before bulk translation.

### Output
`bg_text/BG_TERMINOLOGY_LOCK.md`

### Must include
- Cane Corso / Кане Корсо usage rules
- historical terms
- Latin expressions
- breed/type names
- Flavio Bruno terminology
- hunting/herding/guarding terminology
- table/diagram labels
- names that remain untranslated

### Pass conditions
- Terms are consistent.
- No unresolved high-frequency terminology remains.

---

## BG-03 — BULGARIAN TEXT MASTER

**Status:** PENDING

### Goal
Translate the complete textual content outside the PDF.

### Rules
- Natural Bulgarian, not literal machine translation.
- Preserve meaning and evidentiary status.
- Preserve separation between Dott. Flavio Bruno and Stefano De Tanini.
- No silent shortening of historical claims.
- No translation directly into page artwork before text approval.

### Output
`bg_text/pages/page_001.md` through `page_143.md` as applicable.

### Pass conditions
- All translatable text covered.
- Terminology lock respected.
- No Italian remains in approved BG text master except intentionally preserved names/titles.

---

## BG-04 — IMAGE-TEXT INVENTORY

**Status:** PENDING  
**Mode:** REPORT ONLY

### Goal
Identify every image/table/diagram containing Italian text.

### Output
`reports/bg/BG_IMAGE_TEXT_INVENTORY.md`

### Pass conditions
- Every embedded-text image is listed.
- Reconstruction method assigned.
- Original image identity protected.

---

## BG-05 — BULGARIAN IMAGE RECONSTRUCTION

**Status:** PENDING

### Goal
Create Bulgarian-language versions of language-dependent graphics.

### Rules
- Preserve image identity, framing, geometry, illustration, photograph and graphic hierarchy.
- Replace only language-dependent text.
- Do not paint Bulgarian text over visible Italian text.
- Rebuild cleanly from source/background wherever necessary.
- Keep a side-by-side IT/BG proof for every reconstructed graphic.

### Output
`assets_bg/...`

### Pass conditions
- No accidental Italian text remains.
- BG labels match terminology lock.
- Visual identity remains faithful to IT master.

---

## BG-06 — PAGE ASSEMBLY

**Status:** PENDING

### Goal
Build the Bulgarian 143-page candidate using IT layout as visual reference.

### Target
`output/PREDI_I_SLED_CANE_CORSO_BG_CANDIDATE.pdf`

### Rules
- 143 pages.
- Same page order.
- Same image identity and placement logic.
- Same ornamental system.
- Same footer/page-number geometry.
- Same decorative head identity.
- No automatic global reflow.

---

## BG-07 — CYRILLIC TYPOGRAPHY PASS

**Status:** PENDING

### Goal
Normalize Bulgarian Cyrillic typography.

### Check
- font supports high-quality Cyrillic
- body-size consistency
- line spacing
- paragraph spacing
- heading hierarchy
- captions
- table cells
- overflow
- widows/orphans where visually disruptive
- no text collisions

### Pass conditions
No page is solved by illegibly shrinking text.

---

## BG-08 — MASTER STYLE PASS

**Status:** PENDING

### Authority
Italian Phase 7I FINAL.

### Check
- header
- frame
- footer
- numbering
- margins
- image framing
- decorative Cane Corso head
- vertical rhythm
- divider pages
- medallion/branding where applicable

### Special control pages
55, 61, 78, 110, 116, 121, 130, 140, 141.

---

## BG-09 — LINGUISTIC PROOF

**Status:** PENDING  
**Mode:** REPORT FIRST

### Check
- spelling
- grammar
- punctuation
- natural Bulgarian
- terminology
- internal consistency
- names
- quotations
- historical claim wording
- Flavio/Stefano attribution

---

## BG-10 — FINAL VISUAL PROOF 1–143

**Status:** PENDING  
**Mode:** REPORT ONLY BEFORE CORRECTION

### Required result
For every page: `PASS`, `IMPORTANT`, or `CRITICAL`.

### Mandatory checks
- no Italian residue
- no ghost/overlay
- no clipping
- no duplicated text
- no duplicated images
- no dog-head mismatch
- no header drift
- no footer/page-number drift
- no blurred embedded text
- no unexpected blank regions

---

## BG-11 — PRE-PRESS

**Status:** PENDING

### Check
- 143 pages
- correct page geometry
- intended print resolution
- font/image structure
- printer-specific bleed requirements
- OutputIntent/PDF-X only if required by printer
- no accidental review/proof layers
- final metadata

---

## BG-12 — FINAL PRINT MASTER

**Status:** PENDING

### Target
`output/PREDI_I_SLED_CANE_CORSO_BG_FINAL_PRINT_MASTER.pdf`

### Release gates
- linguistic approval
- visual approval
- 1–143 audit PASS
- pre-press PASS
- SHA-256 recorded
- clean checkpoint ZIP produced
- Git checkpoint committed

---

# Phase transition rule

A phase may advance only when:
1. its required outputs exist;
2. its pass conditions are satisfied;
3. the phase report explicitly says `PASS`;
4. any `MANUAL DECISION REQUIRED` items are resolved by the human owner.

The orchestrator must stop on FAIL.
