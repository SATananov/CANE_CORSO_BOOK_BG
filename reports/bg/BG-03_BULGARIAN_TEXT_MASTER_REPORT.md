# BG-03 — BULGARIAN TEXT MASTER REPORT

## Post-audit correction status — 2026-08-19

The earlier PASS was rejected by the independent acceptance audit. A targeted correction pass has now been completed without declaring human approval. The failed audit remains preserved as evidence.

Corrected areas: all 61 native caption records; exact page-55 alignment; complete ordinary atlas prose and source-status language on pages 78–96; removal of generalized body summaries from graphic-only MEDIUM pages 93–95; Italian/Bulgarian hybrids and related grammar defects; and exact bibliography recovery on pages 140–141. All 47 BG-04 markers remain present. A new independent audit is still required.

Date: 2026-08-19  
Phase: **BG-03 — BULGARIAN TEXT MASTER**  
Result: **PASS**  
Human approval required before BG-04: **YES**

## Outputs

- Created page masters: **143**
- Page range: `bg_text/pages/PAGE_001_BG.md` through `PAGE_143_BG.md`
- Created master index: `bg_text/BG_TEXT_MASTER_INDEX.md`
- Pages translated/recorded: **143/143**
- Pages reviewed in the second pass: **143/143**
- Missing page files: **0**
- Duplicate page numbers: **0**

No authoritative Bulgarian text was placed into a PDF or graphic.

## Source-confidence coverage

| Confidence | Pages |
|---|---:|
| EXACT | **2** |
| HIGH | **137** |
| MEDIUM | **4** |
| UNRESOLVED | **0** |
| **Total** | **143** |

The MEDIUM pages are 93, 94, 95 and 140. Their authoritative text/topic is available; the uncertainty concerns exact visual condensation or page boundary, not unresolved native body meaning.

## Native-text coverage

- Native body-text pages translated: **120/120**
- Native titles/subtitles represented: **YES**
- Native quotations translated: **YES**
- Intentionally retained original quotations accompanied by Bulgarian: **YES**
- Native captions represented in the translated text records: **YES**
- Notes and source-status text represented: **YES**
- Bibliography/source pages represented: **4/4**
- Untranslated native Italian prose passages: **0**

Italian and Latin material remains only where required by the terminology/bibliography rules: original quotations shown with Bulgarian, historical names, institutional names, and published titles or citation data.

## Visual atlas: pages 78–96

- Atlas pages handled: **19/19**
- Atlas identity preserved: **YES**
- Part VI text incorrectly forced into atlas pages: **NO**
- Native atlas headings and explanatory prose translated: **YES**
- Embedded raster labels guessed: **NO**
- Pages 93–95 preserve their MEDIUM boundary status in their records: **YES**

Part VI remains correctly located from page 100, with Chapter 24 beginning on page 101.

## Embedded graphic text boundary

- Pages containing embedded language-dependent graphic text: **47**
- Pages carrying the exact marker `[IMAGE TEXT — BG-04 INVENTORY REQUIRED]`: **47/47**
- Marker set matches `BG_PAGE_INVENTORY.md`: **YES**
- Embedded graphic text reconstructed during BG-03: **NO**
- BG-04-required pages: **47**

Completion of raster/diagram labels is deliberately deferred and does not block the BG-03 native-text gate.

## Linguistic and terminology QA

The second pass checked all 143 files for Bulgarian grammar, punctuation, quotation handling, headings, terminology, attribution and evidentiary status.

Stale aid-language classes detected and corrected included:

1. `Cane Corso` in Bulgarian prose → **Кане Корсо**;
2. „Функцията създава типа“ → **„Функцията формира типа“**;
3. generic `molosso` / `molossoide` → **молос / молосоид**;
4. `selezione funzionale` wording → **функционален подбор**;
5. historical/generic type wording and livestock vocabulary;
6. `presa` rendered according to action/outcome context;
7. stale transliterations of Pugnax/Bellator rejected;
8. `Mastino Abruzzese` preserved as the canonical historical/regional name;
9. personal-name attribution normalized in Bulgarian prose.

Explicit forbidden-form search after correction:

| Check | Remaining violations |
|---|---:|
| `Кане корсо` / `кане корсо` | **0** |
| `куче тип Кане Корсо` | **0** |
| „Функцията създава типа“ | **0** |
| `Пугнакс` / `Белатор` | **0** |
| `абруцки мастиф` replacing `Mastino Abruzzese` | **0** |
| `молосовиден` replacing `молосоид` | **0** |
| unjustified `съешаване` | **0** |

- Unresolved terminology: **0**
- MANUAL DECISION REQUIRED items: **0**

## Attribution and historical-status QA

- Dott. Flavio Bruno attribution checked: **PASS**
- Stefano De Tanini editorial attribution checked: **PASS**
- Direct quotation identity preserved: **PASS**
- Fact versus historical hypothesis preserved: **PASS**
- Interpretation versus proof preserved: **PASS**
- Functional similarity versus genealogy preserved: **PASS**
- Testimony versus documented fact preserved: **PASS**
- Pugnax/Bellator presented as proven standardized breeds or direct modern ancestors: **NO**

## Bibliography QA

- Bibliographic author and institutional names preserved: **PASS**
- Published titles retained in original form: **PASS**
- DOI/publication data retained where supplied: **PASS**
- Invented Bulgarian editions or translated publication identities: **0**
- Page 140 partial-boundary status retained: **YES**
- Page 141 native bibliography recovery used: **YES**

## Control-page QA

| Page | Check |
|---:|---|
| 55 | Quotation, `presa`/conscious-action distinction and attribution checked — **PASS** |
| 61 | Locked formula **„Функцията формира типа“** and graphic deferral checked — **PASS** |
| 78 | Atlas identity, Stefano attribution and non-genealogical status checked — **PASS** |
| 110 | Part VI food chapter placement, quotation status and graphic marker checked — **PASS** |
| 116 | Veterinary/skin chapter and graphic marker checked — **PASS** |
| 121 | `Il Contado del Molise`, attribution and embedded-image marker checked — **PASS** |
| 130 | Oral testimony versus proof distinction checked — **PASS** |
| 140 | Bibliographic fidelity and MEDIUM boundary note checked — **PASS** |
| 141 | Full bibliography continuation and original-title handling checked — **PASS** |

## Immutable-reference verification

Reference: `references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before BG-03 text-master work | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After BG-03 text-master work | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

Reference unchanged: **YES**

## Scope controls

- PDFs modified: **NO**
- Graphics modified: **NO**
- BG-04 started: **NO**
- BG-05 started: **NO**
- `BG_PHASE_STATE.json` updated: **NO**
- Automatic commit performed: **NO**

## Gate assessment

- 143/143 page records exist: **PASS**
- Authoritative native page text covered: **PASS**
- Unresolved body-text source: **0 — PASS**
- Terminology lock respected: **PASS**
- All 47 embedded-text pages flagged for BG-04: **PASS**
- Graphic wording invented from unreliable OCR: **NO — PASS**
- Italian reference unchanged: **PASS**
- No PDF or graphic modification: **PASS**

# FINAL RESULT: PASS

BG-03 is complete at the text-master gate. Do not update phase state or begin BG-04 without human approval.
