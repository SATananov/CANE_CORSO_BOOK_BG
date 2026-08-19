# BG-03 — INDEPENDENT ACCEPTANCE AUDIT

Date: 2026-08-19  
Mode: **REPORT ONLY**  
Audited phase: **BG-03 — BULGARIAN TEXT MASTER**

## Final result

# FAIL

The structural shell is complete, but the submitted page masters do not satisfy the BG-03 native-text, linguistic, terminology, caption, page-alignment, and bibliography gates. No corrections were made during this audit.

## Structural result

| Check | Result |
|---|---|
| Page-master files present | **143** |
| Unique page numbers | **143** |
| Missing pages | **0** |
| Duplicate pages | **0** |
| Index rows | **143** |
| Source-confidence totals | **2 EXACT / 137 HIGH / 4 MEDIUM / 0 UNRESOLVED** |
| BG-04 marker pages | **47/47** |
| Structural result | **PASS** |

The phase remains BG-03 ACTIVE. `BG_PHASE_STATE.json` was not changed.

## Linguistic result

**FAIL**

The page set contains material mixed-language and grammatical defects incompatible with a final native Bulgarian text master.

Confirmed examples include:

- page 55: „Защото тогава **захват** вече не е...“ — incorrect article/agreement; natural Bulgarian requires an inflected subject;
- page 110: „кучето и **стопанство**“, `Mastini`, `Cani da захват`, `massaro`, `mastini`, `pane canino`, `Cane da захват`;
- page 110: untranslated Italian category names are mechanically combined with Bulgarian words;
- page 111: `Volpini` and `Mastini Abruzzesi` remain inside Bulgarian prose;
- page 121: generic `mastini` and `volpini` remain untranslated;
- page 141: `review disponibile tramite PMC` remains Italian prose inside a bibliographic annotation;
- page 108: `rustico` remains untranslated in a Bulgarian heading and running prose without consistent locked handling.

Confirmed accidental untranslated/mixed Italian items: **at least 15**. This count excludes intentionally retained publication titles, institutional names, historical names, and original quotations accompanied by Bulgarian.

## Caption/native-text coverage result

**FAIL — CRITICAL**

`BG_PAGE_INVENTORY.md` identifies **61 pages with captions**. The page masters do not supply authoritative translated caption text for those pages.

- **46** page files contain the placeholder: `[Нативният надпис е включен в съответния преведен текстов блок; съпоставянето с изображението се проверява при набора.]`
- The placeholder is not a translated caption and does not identify the corresponding Bulgarian wording.
- The remaining caption-bearing inventory pages do not contain a dedicated authoritative caption translation.
- Actual independently identifiable translated caption records: **0/61**.

This contradicts the BG-03 report's claim that native captions are represented and prevents acceptance of full native-text coverage.

## Terminology result

**FAIL**

Several headline checks pass:

- `Кане корсо` / `кане корсо`: **0**;
- forbidden „Функцията създава типа“: **0**;
- `Пугнакс` / `Белатор`: **0**;
- `куче тип Кане Корсо`: **0**;
- `абруцки мастиф` replacing `Mastino Abruzzese`: **0**.

However, full lock compliance fails because:

- generic Italian `mastini` remains in Bulgarian prose;
- `Mastini Abruzzesi` is used instead of the locked visible canonical historical/regional name `Mastino Abruzzese` with an appropriate Bulgarian grammatical construction;
- mixed forms `Cani da захват` and `Cane da захват` violate the locked Bulgarian handling of `cane da presa`;
- untranslated `rustico` is used inconsistently outside a clearly preserved original title/quotation;
- the locked distinction between a retained original term and its Bulgarian prose form is not applied consistently.

## Attribution result

**PARTIAL / IMPORTANT FINDING**

Flavio Bruno and Stefano De Tanini are generally named distinctly, and the visual-atlas material is attributed to Stefano. Hypothesis warnings are present.

Acceptance nevertheless fails because some page text is condensed or reassigned without a traceable quotation/caption record. Where the final wording is not reproduced, attribution cannot be fully audited against the authoritative page text.

## Historical/evidentiary result

**PARTIAL**

The atlas repeatedly states that similarity is not genealogy and that hypotheses are not proof. Page 130 correctly distinguishes testimony from universal fact.

No systematic conversion of hypothesis into established fact was found. However, the source/page mismatch and condensed atlas records mean evidentiary fidelity is not fully verifiable for every final-page passage.

## Visual-atlas assessment — pages 78–96

**FAIL FOR NATIVE-TEXT COMPLETENESS; PASS FOR PHASE BOUNDARY**

- Pages 78–96 are correctly identified as a visual atlas.
- Part VI is not forced onto those pages.
- Embedded graphics are marked for BG-04.
- No reconstructed graphic assets were created.

But the page masters frequently provide condensed summaries instead of the complete native explanatory text visible in the final PDF. Page 78, for example, contains only a shortened paragraph while the final page contains multiple native explanatory/status passages. Pages 93–95 contain generalized source summaries under `## Body`, even though their exact page-level wording remains MEDIUM and predominantly graphic.

These summaries cannot be accepted as complete final-page native text without a direct source-to-page record.

## BG-04 deferral result

| Check | Result |
|---|---|
| Inventory pages with embedded graphic text | **47** |
| Page masters with exact BG-04 marker | **47** |
| Marker set matches inventory | **YES** |
| Graphics reconstructed | **NO** |
| BG-04 started | **NO** |

The marker count passes. The audit cannot substantiate the BG-03 report's categorical claim that no OCR-derived wording was guessed, because some atlas prose is condensed without a page-verifiable textual citation. No raster labels should be promoted from these summaries.

## MEDIUM-page assessment

| Page | Assessment |
|---:|---|
| 93 | Topic and uncertainty are preserved, but the short `## Body` is a generalized summary rather than a demonstrated translation of exact native page wording — **IMPORTANT** |
| 94 | Same issue; regional scope is established, exact page text is not — **IMPORTANT** |
| 95 | Same issue; generalized summary must not be treated as exact native text — **IMPORTANT** |
| 140 | Bibliographic page is incomplete relative to the final PDF/source material and therefore does contain unresolved fidelity work — **CRITICAL** |

The assertion that all four MEDIUM pages contain no unresolved authoritative text is **not accepted**.

## Control-page results

| Page | Result | Finding |
|---:|---|---|
| 55 | **CRITICAL** | Marked EXACT, but its Bulgarian body does not correspond to the final PDF page-55 native passage. The final page begins with the wild-boar/presa discussion; the master instead contains the later `coscienza` discussion. |
| 61 | **IMPORTANT** | Locked formula is correct and BG-04 marker exists, but the caption is only a placeholder and the native page allocation is not independently demonstrated. |
| 78 | **CRITICAL** | Correct atlas identity and Stefano attribution, but native explanatory/status text is materially abbreviated. |
| 110 | **CRITICAL** | Multiple Italian/Bulgarian hybrid forms and grammatical errors; not publication-quality Bulgarian. |
| 116 | **IMPORTANT** | Substantive Bulgarian prose exists, but the caption is a placeholder rather than an authoritative translated caption. |
| 121 | **IMPORTANT** | Correct `Mastino Abruzzese` occurrence, but generic `mastini`/`volpini` remain untranslated and the caption is a placeholder. |
| 130 | **PASS WITH MICRO NOTE** | Testimony/proof distinction is preserved; capitalization after the source-note label should be editorially normalized. |
| 140 | **CRITICAL** | Bibliographic fidelity/coverage is incomplete; MEDIUM status is not resolved by the current record. |
| 141 | **CRITICAL** | Claimed EXACT, but the master differs from final-PDF native bibliography evidence and contains untranslated Italian annotation (`review disponibile tramite PMC`). The earlier native extraction also identifies an NKU BSI record not faithfully represented here. |

## Quotation assessment

**FAIL / IMPORTANT**

Several original quotations are accompanied by Bulgarian translations and speaker framing. However:

- not every retained Italian passage is translated;
- page-boundary reassignment prevents reliable quotation-to-final-page verification;
- generic Italian terms remain inside purported Bulgarian quotation translations;
- caption placeholders prevent caption attribution verification.

## Issue totals

### CRITICAL issues: **6 categories**

1. EXACT page-55 source/page mismatch.
2. Native caption translations absent or unidentifiable on 61 caption-bearing pages.
3. Materially incomplete native atlas prose, including page 78.
4. Mixed Italian/Bulgarian and ungrammatical text on page 110 and related pages.
5. Page-140 bibliography incomplete.
6. Page-141 EXACT bibliography claim contradicted by final-PDF evidence and untranslated annotation.

### IMPORTANT issues: **5 categories**

1. MEDIUM pages 93–95 contain generalized summaries rather than demonstrated page-native translations.
2. Generic Italian terminology remains across multiple Bulgarian pages.
3. Full quotation fidelity cannot be verified under the current page allocation.
4. Attribution is generally distinct but cannot be accepted wherever final native wording is missing/condensed.
5. The BG-03 PASS report overstates caption, bibliography, and native-text completion.

### MICRO issues: **multiple**

- grammatical inflection and article errors;
- inconsistent capitalization after labels;
- punctuation around quotations;
- mixed register in headings;
- editorial metadata phrasing requiring normalization.

## MANUAL DECISION REQUIRED

**NO.**

The defects are not unresolved source-policy questions; they are correctable translation, alignment, terminology, caption, and bibliography failures. BG-03 should remain active and be corrected, then independently re-audited.

## Immutable-reference and scope verification

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

Reference unchanged: **YES**

- PDFs modified: **NO**
- Graphics modified: **NO**
- BG-04 started: **NO**
- `BG_PHASE_STATE.json` changed: **NO**
- Commit performed: **NO**

# FINAL RESULT: FAIL

Stop. BG-03 is not accepted and must not advance to BG-04 until the critical and important findings are corrected and a new independent acceptance audit passes.
