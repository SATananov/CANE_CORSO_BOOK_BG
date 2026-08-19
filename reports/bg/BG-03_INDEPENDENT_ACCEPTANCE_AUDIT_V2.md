# BG-03 — SECOND INDEPENDENT ACCEPTANCE AUDIT

Date: 2026-08-19  
Phase audited: **BG-03 — ACTIVE / NOT HUMAN-APPROVED**  
Audit mode: **REPORT ONLY**  
Final result: **FAIL**

## Executive finding

The corrected BG-03 deliverables do not pass the independent acceptance gate. The page-master structure and confidence ledger are internally complete, but two release-blocking findings remain:

1. page 140 omits a material part of the final Italian reference bibliography;
2. although all 61 required caption sections exist, 23 captions omit, alter, add, or conflate source material, so caption fidelity is not 61/61.

No automatic correction was made. BG-04 was not started.

## A. Structural result

| Check | Result |
|---|---:|
| Page masters present | **143** |
| Unique page numbers | **143** |
| Missing pages | **0** |
| Duplicate pages | **0** |
| Index rows | **143** |
| Index/page-file mismatch | **0** |
| Page-class mismatch against `BG_PAGE_INVENTORY.md` | **0** |
| Required caption sections present | **61/61** |
| BG-04 embedded-graphic markers present | **47/47 pages** |
| Generic caption placeholders | **0** |

Structural file coverage: **PASS**. Structural completeness does not establish textual fidelity.

## B. Source-confidence result

The source map and index retain the required whole-book distribution:

| Confidence | Pages |
|---|---:|
| EXACT | **2** |
| HIGH | **137** |
| MEDIUM | **4** |
| UNRESOLVED | **0** |

The four MEDIUM pages are **93, 94, 95, and 140**. Page 93 is acceptably represented. Pages 94 and 95 still conflate page-native captions with text belonging to embedded graphics. Page 140 has unresolved authoritative bibliography omissions and therefore fails the substantive MEDIUM-page gate.

The correction report's listed corrected-page set contains **88 unique page numbers**, but the actual historical edit count cannot be independently reconstructed from the current untracked working-tree state. This does not alter the substantive findings below.

## C. Linguistic result

Result: **FAIL**.

Confirmed remaining Bulgarian-language defects:

| Page | Finding | Severity |
|---:|---|---|
| 11 | A sentence begins with lowercase `мастиф`; nearby phrasing around `захват` requires grammatical normalization. | IMPORTANT |
| 50 | `правилната захват` has incorrect gender; `позволява на месар` lacks the required article; Italian `musello` remains in Bulgarian native prose. | IMPORTANT |
| 61 | Doubled opening quotation marks in `„„Функцията формира типа“.“` | MICRO |
| 63 | Agreement error in `„Непретенциозен и издръжлив“ може да прозвучи като „грубо“, „селско“...` | IMPORTANT |
| 64 | The bare adjectival construction `Непретенциозен и издръжлив не означава...` is syntactically incomplete/ambiguous in context. | IMPORTANT |
| 110 | Defective constructions including `част от икономиката на семейството и стопанство` and `Освен това мастиф живее свободно`. | IMPORTANT |
| 111 | Multiple corrupted words and grammar defects, including `брапнени`, `брапна`, `нипестетата`, `кучепкия`, `Напият` and `в традиционна стопанство`. | IMPORTANT |
| 121 | Multiple corrupted words, including `саао`, `зеая`, `пааетта`, `аогат`, `необходиао`, `спряао`; malformed heading `Eabedded graphic text status`; additional awkward syntax. | IMPORTANT |

Accidental untranslated native Italian prose count: **1 confirmed occurrence**, `musello` on page 50. Permitted original titles, quotations, proper names, historical/Latin forms, and bibliography entries are excluded from this count.

## D. Terminology result

Result: **PASS WITH RESERVATION**.

The audited page set does not show the previously forbidden variants `Функцията създава типа`, `куче тип Кане Корсо`, Bulgarianized Pugnax/Bellator forms, substitution of `Mastino Abruzzese` with `абруцки мастиф`, or collapse of `молос` and `молосоид`. The required forms for Кане Корсо, Pugnax, Bellator, Mastino Abruzzese, функционален подбор, функционална приемственост, генеалогична приемственост, and `Функцията формира типа` are generally retained.

The reservation is linguistic rather than a new terminology-policy conflict: page 50 contains the unexplained Italian word `musello`, and page 61 corrupts the typography of the locked formula.

## E. Attribution result

Result: **PASS WITH RESERVATION**.

No systematic conflation of Flavio Bruno's voice with Stefano De Tanini's editorial voice was found. Named attribution and quotation framing are generally preserved, including on the restored atlas prose and control page 130.

The reservation concerns captions: omissions and source-boundary conflation reduce the precision with which documentary, editorial, and illustrative statements are attributed. Pages **70 and 76** specifically omit explicit source-status qualifications from their captions.

## F. Historical and evidentiary result

Result: **FAIL**.

The body text generally preserves the distinctions among fact, hypothesis, interpretation, testimony, and personal/editorial position. Page 130 correctly maintains the testimony-versus-proof distinction. However:

- page 70 omits the source statement that the depicted material is not an official breed judgment;
- page 76 omits the source statement that the illustration is not an original Pinelli engraving;
- pages 94 and 95 move embedded-graphic propositions into the caption field, weakening source-layer separation;
- multiple other captions alter or omit functionally or historically meaningful wording.

These are not merely typographic deviations because they affect evidentiary status and source identity.

## G. Caption audit

Caption-section existence: **61/61**.  
Caption fidelity: **FAIL**.  
Pages with identified caption-fidelity defects: **23**.

| Page | Independent finding |
|---:|---|
| 6 | Omits the source qualifier `condivisa` (shared necessity). |
| 12 | Omits that Renzo Galassi was world president of homeopathic doctors, is honorary president, and repeatedly spoke at Contado del Molise meetings. |
| 13 | Replaces the source's living memory of dogs and territory with a statement about Italian working dogs. |
| 21 | Recasts `ambiente di sopravvivenza` as an environment that does not forgive errors. |
| 23 | Omits `first useful dog in Flavio's narrative` and adds `contemporary`. |
| 26 | Renders belonging (`appartenenza`) as protection. |
| 28 | Replaces the source sequence path, climate, and flock with territory, losing the flock element. |
| 43 | Omits selection, training, and functions. |
| 51 | Replaces reconstruction of the function described in the text with controlled detention. |
| 53 | Omits `punto` and the relationship with the human, substituting `decision`. |
| 63 | Changes `not measured only in exhibition` to `not only by appearance`. |
| 66 | Adds `functional type` where the source says the detail is read within the whole. |
| 68 | Replaces `within a living system` with `in relation to function`. |
| 70 | Omits `Non è un giudizio ufficiale di razza.` |
| 73 | Changes guard, work, and life beside humans to guard, hunting, and work. |
| 76 | Omits `Non è un'incisione originale di Pinelli.` |
| 78 | Uses an editorial synthesis not established as the exact page-native caption. |
| 94 | Adds a genealogy/origin proposition belonging to embedded graphic text. |
| 95 | Combines the bottom caption with the embedded final-note text. |
| 98 | Changes `not a genealogical map` to `not proof of origin`. |
| 113 | Omits individual and geographic risk. |
| 122 | Omits that the illustrative table is dedicated to Contado del Molise. |
| 133 | Changes `read the dog before judging it` to behavior reading rather than automatic diagnosis. |

Accordingly, no more than **38/61** captions are free of an identified material mismatch in this audit. This fails the required 61/61 caption-fidelity gate.

## H. Visual-atlas assessment, pages 78–96

Result: **IMPORTANT ISSUES REMAIN**.

The ordinary prose on pages **78, 80, 82, 84, 86, 88, 89, and 96** has been substantially restored, and the graphic-only pages retain BG-04 deferral markers. Page 93 is acceptably aligned. Pages **94 and 95**, however, do not preserve the boundary between the visible bottom caption and embedded infographic text. Page 78's caption is also an editorial synthesis rather than a demonstrably exact page-native caption.

OCR authority is not required for recovered editable body text. Isolated image text remains properly deferred to BG-04, but it must be visually transcribed/reconstructed under that phase's controls rather than promoted into BG-03 captions.

## I. BG-04 deferral result

| Check | Result |
|---|---:|
| Inventory pages with embedded graphic text | **47** |
| Page masters carrying the required marker | **47** |
| Missing marker pages | **0** |
| Extra marker pages | **0** |
| Marker text | `[IMAGE TEXT — BG-04 INVENTORY REQUIRED]` |

Marker coverage: **PASS**. No evidence was found that BG-04 had started, and no authoritative OCR-derived image wording was accepted as such. The page 94/95 caption conflation is nevertheless a source-boundary problem that must be corrected before approval.

## J. Control-page results

| Page | Result | Finding |
|---:|---|---|
| 55 | PASS | Native text is aligned and complete; no spillover identified. |
| 61 | MICRO | Caption and marker are present; locked formula has doubled opening quotation marks. |
| 78 | IMPORTANT | Restored prose and marker are present; caption is not established as an exact native caption. |
| 110 | IMPORTANT | Remaining Bulgarian grammar defects; caption and marker are present. |
| 116 | PASS | Content, caption/source status, and BG-04 marker are represented. |
| 121 | IMPORTANT | Publication-blocking character corruption and malformed English metadata heading. |
| 130 | PASS | Testimony is not converted into proof; attribution remains distinct. |
| 140 | CRITICAL | Materially incomplete bibliography. |
| 141 | PASS | Bibliography content is substantially complete and faithfully represented. |

## K. Page 140 and 141 bibliography verification

Page 140: **CRITICAL FAIL**. Compared with the final Italian reference page, the Bulgarian page master omits the introductory bibliography paragraph and the entries for **Columella**, **Tecce**, **Rees**, **Autengruber-Thüry**, **Marsh et al.**, and **Bergström et al.** It retains only Varro and Merola. The correction report's claim that page 140 bibliography content was fully represented is therefore not supported.

Page 141: **PASS**. The FCI/ENCI material and the Packer, Mila, Chastant/Mila, WSAVA, ESCCAP, Groat, Morgan, and USGS references are represented with their essential bibliographic identity intact.

## L. Issue register and gate decision

Issue counts below count audit issue categories; every affected page is listed.

### CRITICAL issues — 2

1. **Caption fidelity is not 61/61** — pages **6, 12, 13, 21, 23, 26, 28, 43, 51, 53, 63, 66, 68, 70, 73, 76, 78, 94, 95, 98, 113, 122, 133**.
2. **Materially incomplete bibliography** — page **140**.

### IMPORTANT issues — 4

1. **Bulgarian corruption, grammar, or syntax requiring editorial correction** — pages **11, 50, 63, 64, 110, 111, 121**.
2. **Accidental untranslated native Italian prose** — page **50** (`musello`).
3. **MEDIUM-page native-caption/embedded-graphic boundary remains inaccurate** — pages **94, 95**.
4. **Explicit evidentiary/source-status qualification omitted** — pages **70, 76**.

### MICRO issues — 1

1. **Doubled quotation marks around the locked formula** — page **61**.

### MANUAL DECISION REQUIRED

**None.** The identified problems are correctable from authoritative sources and do not require inventing terminology or adjudicating an irreducibly uncertain source meaning.

## Integrity and scope verification

Reference:

`references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

| Check | SHA-256 |
|---|---|
| Before audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |
| After audit | `A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170` |

- Reference unchanged: **YES**
- PDFs modified: **NO**
- Graphics modified: **NO**
- Bulgarian page masters modified: **NO**
- `BG_PHASE_STATE.json` modified: **NO**
- BG-04 started: **NO**
- Commit created: **NO**
- Files created by this audit: **`reports/bg/BG-03_INDEPENDENT_ACCEPTANCE_AUDIT_V2.md` only**

# FINAL RESULT: FAIL

BG-03 must remain active and not human-approved. Stop here pending human direction.
