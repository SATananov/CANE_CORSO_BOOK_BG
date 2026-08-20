# BG-04 SF-05 CANONICAL UNIT LEDGER — V1

Status: **ACTIVE SF-05 CONSTRUCTION AUTHORITY — V1**
Human authorization: **SF-05 canonical rebuild authorized under the same legacy-preservation method used for SF-03**
Scope: `P133-GA`, `P134-GA` only
OCR authority: **NO**
BG-04 state: **ACTIVE**
BG-05 state: **PENDING**

## Authority and evidence

The authoritative visual targets are the two human-supplied page screenshots stored locally under the ignored `references/source_text/` evidence tree:

- `references/source_text/sf05_visual_targets/P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png`
  - SHA-256: `D6448CCC0BCC0D4B7C0368DE56E28342598C3D50B7611D1EDD9C38E4B3D50E03`
- `references/source_text/sf05_visual_targets/P134_TEMPERAMENTO_TARGET.png`
  - SHA-256: `A7E2578E64D78093168CDDA5B880B653F689F9DD80B2A88FBD8C713E3DC09418`

Direct visual reading from these targets is the authority. A 143-page Phase7I review candidate was used only as a magnified readability aid after projective visual registration against the locked target screenshots; it is **not** promoted to source authority.

Legacy policy:

- 40 original SF-05 ordinal U records are preserved as historical audit evidence: 20 for P133 and 20 for P134.
- They are `SUPERSEDED_BY_CANONICAL_LEDGER` as sets.
- No legacy ordinal ID is mapped one-to-one to a canonical ID.
- No legacy wording is invented.

## Anchor schema

Each canonical row records `READING_ORDER`, `REGION`, `PANEL`, `ELEMENT_ROLE`, `ASSOCIATED_VISUAL`, and `RELATIVE_POSITION`. These anchors are intended to identify each visible semantic block without fabricated bounding boxes.

## PAGE 133 — P133-GA

- Visual target: `references/source_text/sf05_visual_targets/P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png`
- Target SHA-256: `D6448CCC0BCC0D4B7C0368DE56E28342598C3D50B7611D1EDD9C38E4B3D50E03`
- Reading-order rule: crest/brand → title/subtitle/introduction → panels 1–4 left-to-right/top-to-bottom → context strip → synthesis panel → signature and medallion.
- V1 range: `P133-GA-C001`–`P133-GA-C076` (76 contiguous IDs)
- Arithmetic: **76 = 68 T + 6 R + 0 N + 2 G + 0 U**

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P133-GA-C001` | 1 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C002` | 2 | HEADER | inside top-center crest | FIXED_MARK | top crest | central monogram | USG | R | Retain canonical USG mark. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C003` | 3 | HEADER | inside top-center crest | FIXED_MARK | top crest | lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C004` | 4 | HEADER | top | TITLE | named poster frame | main title | SEGNALI CORPOREI E DI STRESS | T | ТЕЛЕСНИ СИГНАЛИ И ПРИЗНАЦИ НА СТРЕС | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C005` | 5 | HEADER | below title | TITLE | named poster frame | subtitle | leggere il cane prima di giudicarlo | T | Разчети сигналите му, преди да го съдиш | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C006` | 6 | HEADER | below subtitle | BODY_TEXT | named poster frame | introduction | Il Cane Corso comunica costantemente attraverso il corpo. Saper leggere i suoi segnali ci permette di rispettarlo, evitare conflitti e costruire un rapporto basato su fiducia e consapevolezza. | T | Кане Корсо общува непрекъснато чрез тялото си. Умението да разчитаме сигналите му ни позволява да го уважаваме, да избягваме конфликти и да изграждаме връзка, основана на доверие и осъзнатост. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C007` | 7 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | dog body-language panel | panel heading | 1 CALMA E ATTENZIONE | T | 1 СПОКОЙСТВИЕ И ВНИМАНИЕ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C008` | 8 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | dog body-language panel | ears label | ORECCHIE | T | УШИ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C009` | 9 | UPPER_LEFT | panel 1 | BODY_TEXT | dog body-language panel | ears value | naturali, leggermente in avanti | T | естествени, леко насочени напред | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C010` | 10 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | dog body-language panel | gaze label | SGUARDO | T | ПОГЛЕД | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C011` | 11 | UPPER_LEFT | panel 1 | BODY_TEXT | dog body-language panel | gaze value | morbido, attento all'ambiente | T | мек, внимателен към средата | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C012` | 12 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | dog body-language panel | muzzle label | MUSO | T | МУЦУНА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C013` | 13 | UPPER_LEFT | panel 1 | BODY_TEXT | dog body-language panel | muzzle value | rilassato, bocca chiusa o appena socchiusa | T | отпусната, устата е затворена или леко открехната | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C014` | 14 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | dog body-language panel | body label | CORPO | T | ТЯЛО | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C015` | 15 | UPPER_LEFT | panel 1 | BODY_TEXT | dog body-language panel | body value | rilassato ma presente | T | отпуснато, но събрано | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C016` | 16 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | dog body-language panel | tail label | CODA | T | ОПАШКА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C017` | 17 | UPPER_LEFT | panel 1 | BODY_TEXT | dog body-language panel | tail value | naturale, portata bassa o a sciabola | T | естествено положение, носена ниско или саблевидно | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C018` | 18 | UPPER_LEFT | panel 1 | BODY_TEXT | dog body-language panel | panel interpretation | Il cane è a suo agio, ricettivo e in equilibrio. Osserva, valuta e resta centrato. | T | Кане Корсо се чувства спокойно, възприемчиво и уравновесено. Наблюдава, преценява и запазва самообладание. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C019` | 19 | UPPER_RIGHT | panel 2 | HEADING_OR_LABEL | dog body-language panel | panel heading | 2 STRESS CRESCENTE | T | 2 НАРАСТВАЩ СТРЕС | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C020` | 20 | UPPER_RIGHT | panel 2 | HEADING_OR_LABEL | dog body-language panel | ears label | ORECCHIE | T | УШИ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C021` | 21 | UPPER_RIGHT | panel 2 | BODY_TEXT | dog body-language panel | ears value | più dritte, ruotate in avanti | T | по-изправени, завъртени напред | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C022` | 22 | UPPER_RIGHT | panel 2 | HEADING_OR_LABEL | dog body-language panel | gaze label | SGUARDO | T | ПОГЛЕД | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C023` | 23 | UPPER_RIGHT | panel 2 | BODY_TEXT | dog body-language panel | gaze value | fisso, occhi più aperti | T | фиксиран, очите са по-широко отворени | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C024` | 24 | UPPER_RIGHT | panel 2 | HEADING_OR_LABEL | dog body-language panel | muzzle label | MUSO | T | МУЦУНА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C025` | 25 | UPPER_RIGHT | panel 2 | BODY_TEXT | dog body-language panel | muzzle value | chiuso, labbra tese | T | устата е затворена, устните са напрегнати | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C026` | 26 | UPPER_RIGHT | panel 2 | HEADING_OR_LABEL | dog body-language panel | body label | CORPO | T | ТЯЛО | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C027` | 27 | UPPER_RIGHT | panel 2 | BODY_TEXT | dog body-language panel | body value | più rigido, incurvamento muscolare | T | по-сковано, с напрегната мускулатура | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C028` | 28 | UPPER_RIGHT | panel 2 | HEADING_OR_LABEL | dog body-language panel | tail label | CODA | T | ОПАШКА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C029` | 29 | UPPER_RIGHT | panel 2 | BODY_TEXT | dog body-language panel | tail value | più alta, rigida o ferma | T | носена по-високо, твърда или неподвижна | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C030` | 30 | UPPER_RIGHT | panel 2 | BODY_TEXT | dog body-language panel | panel interpretation | Il cane percepisce una pressione o una potenziale minaccia. L'attenzione si concentra e la tensione sale. | T | Кане Корсо усеща натиск или потенциална заплаха. Вниманието му се изостря и напрежението се покачва. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C031` | 31 | UPPER_RIGHT | panel 2 | CALLOUT | warning icon | warning callout | RISPETTA IL SUO SPAZIO | T | УВАЖАВАЙ ПРОСТРАНСТВОТО МУ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C032` | 32 | CENTER_LEFT | panel 3 | HEADING_OR_LABEL | dog body-language panel | panel heading | 3 DISAGIO | T | 3 ДИСКОМФОРТ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C033` | 33 | CENTER_LEFT | panel 3 | HEADING_OR_LABEL | dog body-language panel | ears label | ORECCHIE | T | УШИ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C034` | 34 | CENTER_LEFT | panel 3 | BODY_TEXT | dog body-language panel | ears value | arretrate o basse | T | дръпнати назад или ниско | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C035` | 35 | CENTER_LEFT | panel 3 | HEADING_OR_LABEL | dog body-language panel | gaze label | SGUARDO | T | ПОГЛЕД | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C036` | 36 | CENTER_LEFT | panel 3 | BODY_TEXT | dog body-language panel | gaze value | laterale, sbadiglia, occhi che si stringono | T | настрани; прозява се; очите се присвиват | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C037` | 37 | CENTER_LEFT | panel 3 | HEADING_OR_LABEL | dog body-language panel | muzzle label | MUSO | T | МУЦУНА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C038` | 38 | CENTER_LEFT | panel 3 | BODY_TEXT | dog body-language panel | muzzle value | leccamento del naso, labbra tese | T | облизване на носа, напрегнати устни | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C039` | 39 | CENTER_LEFT | panel 3 | HEADING_OR_LABEL | dog body-language panel | body label | CORPO | T | ТЯЛО | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C040` | 40 | CENTER_LEFT | panel 3 | BODY_TEXT | dog body-language panel | body value | abbassato, peso spostato indietro | T | снишено, тежестта е изнесена назад | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C041` | 41 | CENTER_LEFT | panel 3 | HEADING_OR_LABEL | dog body-language panel | tail label | CODA | T | ОПАШКА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C042` | 42 | CENTER_LEFT | panel 3 | BODY_TEXT | dog body-language panel | tail value | bassa, infilata tra le zampe o che si muove velocemente | T | ниско, прибрана между краката или се движи бързо | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C043` | 43 | CENTER_LEFT | panel 3 | BODY_TEXT | dog body-language panel | panel interpretation | Il cane si sente sotto pressione e cerca di ridurre la tensione. Potrebbe allontanarsi o congelarsi. | T | Кане Корсо се чувства под напрежение и се опитва да го намали. Може да се отдалечи или да замръзне на място. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C044` | 44 | CENTER_RIGHT | panel 4 | HEADING_OR_LABEL | dog body-language panel | panel heading | 4 DISTANZA | T | 4 ДИСТАНЦИЯ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C045` | 45 | CENTER_RIGHT | panel 4 | HEADING_OR_LABEL | dog body-language panel | ears label | ORECCHIE | T | УШИ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C046` | 46 | CENTER_RIGHT | panel 4 | BODY_TEXT | dog body-language panel | ears value | indietro o appiattite | T | назад или прилепнали | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C047` | 47 | CENTER_RIGHT | panel 4 | HEADING_OR_LABEL | dog body-language panel | gaze label | SGUARDO | T | ПОГЛЕД | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C048` | 48 | CENTER_RIGHT | panel 4 | BODY_TEXT | dog body-language panel | gaze value | evita lo sguardo diretto | T | избягва пряк зрителен контакт | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C049` | 49 | CENTER_RIGHT | panel 4 | HEADING_OR_LABEL | dog body-language panel | muzzle label | MUSO | T | МУЦУНА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C050` | 50 | CENTER_RIGHT | panel 4 | BODY_TEXT | dog body-language panel | muzzle value | chiuso, profilo distante | T | устата е затворена, изражението е дистанцирано | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C051` | 51 | CENTER_RIGHT | panel 4 | HEADING_OR_LABEL | dog body-language panel | body label | CORPO | T | ТЯЛО | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C052` | 52 | CENTER_RIGHT | panel 4 | BODY_TEXT | dog body-language panel | body value | di lato o girato, pronto a muoversi via | T | обърнато встрани, готово да се отдалечи | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C053` | 53 | CENTER_RIGHT | panel 4 | HEADING_OR_LABEL | dog body-language panel | tail label | CODA | T | ОПАШКА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C054` | 54 | CENTER_RIGHT | panel 4 | BODY_TEXT | dog body-language panel | tail value | bassa, tra le zampe o che batte velocemente | T | ниско, между краката или маха бързо | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C055` | 55 | CENTER_RIGHT | panel 4 | BODY_TEXT | dog body-language panel | panel interpretation | Il cane sceglie la distanza per sentirsi più sicuro. È una richiesta di spazio, non di sfida. | T | Кане Корсо избира дистанция, за да се чувства по-сигурно. Това е молба за пространство, а не предизвикателство. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C056` | 56 | CENTER_RIGHT | panel 4 | CALLOUT | warning callout | behavioral instruction | NON INSEGUIRLO, NON FORZARE IL CONTATTO | T | НЕ ГО ПРЕСЛЕДВАЙ, НЕ ГО ПРИНУЖДАВАЙ КЪМ КОНТАКТ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C057` | 57 | LOWER_LEFT | panel 5 | HEADING_OR_LABEL | context strip | section heading | 5 OSSERVARE IL CONTESTO | T | 5 НАБЛЮДАВАЙ КОНТЕКСТА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C058` | 58 | LOWER_LEFT | panel 5 / environment | HEADING_OR_LABEL | context strip | environment label | AMBIENTE | T | СРЕДА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C059` | 59 | LOWER_LEFT | panel 5 / environment | BODY_TEXT | context strip | environment body | Rumori, spazi ristretti, presenza di estranei possono aumentare lo stress. | T | Шумове, тесни пространства и присъствие на непознати могат да увеличат стреса. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C060` | 60 | LOWER_LEFT | panel 5 / people and dogs | HEADING_OR_LABEL | context strip | people-and-dogs label | PERSONE E CANI | T | ХОРА И КУЧЕТА | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C061` | 61 | LOWER_LEFT | panel 5 / people and dogs | BODY_TEXT | context strip | people-and-dogs body | Distanza, postura e interazioni precedenti influenzano le reazioni. | T | Дистанцията, стойката и предишните взаимодействия влияят на реакциите. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C062` | 62 | LOWER_CENTER | panel 5 / prior experiences | HEADING_OR_LABEL | context strip | prior-experience label | ESPERIENZE PREGRESSE | T | ПРЕДИШЕН ОПИТ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C063` | 63 | LOWER_CENTER | panel 5 / prior experiences | BODY_TEXT | context strip | prior-experience body | Ogni cane porta con sé storia, educazione e sensibilità diverse. | T | Всяко куче носи със себе си различна история, възпитание и чувствителност. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C064` | 64 | LOWER_CENTER | panel 5 / subtle signals | HEADING_OR_LABEL | context strip | subtle-signals label | SEGNALI SOTTILI | T | ФИНИ СИГНАЛИ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C065` | 65 | LOWER_CENTER | panel 5 / subtle signals | BODY_TEXT | context strip | subtle-signals body | Sono i piccoli dettagli a fare la differenza: impariamo a notarli prima che sia tardi. | T | Малките детайли правят разликата: нека се научим да ги забелязваме, преди да е станало късно. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C066` | 66 | LOWER_LEFT | panel 5 footer | CALLOUT | context strip | leadership motto | Osservare, comprendere e rispettare: questa è la vera leadership. | T | Наблюдавай, разбирай и уважавай: това е истинското лидерство. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C067` | 67 | LOWER_RIGHT | synthesis panel | HEADING_OR_LABEL | named synthesis panel | panel heading | SINTESI | T | ОБОБЩЕНИЕ | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C068` | 68 | LOWER_RIGHT | synthesis panel | BODY_TEXT | named synthesis panel | message 1 | Il comportamento non è mai “giusto” o “sbagliato”: è una comunicazione. | T | Поведението никога не е просто „правилно“ или „грешно“: то е форма на общуване. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C069` | 69 | LOWER_RIGHT | synthesis panel | BODY_TEXT | named synthesis panel | message 2 | Leggere i segnali prima di giudicare ci permette di agire nel modo giusto, al momento giusto. | T | Разчитането на сигналите, преди да съдим, ни позволява да действаме правилно в точния момент. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C070` | 70 | LOWER_RIGHT | synthesis panel | BODY_TEXT | named synthesis panel | message 3 | Rispetto, empatia e consapevolezza trasformano ogni relazione in un legame solido e duraturo. | T | Уважението, емпатията и осъзнатостта превръщат всяка връзка в здрава и трайна. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C071` | 71 | FOOTER | bottom-left signature | FIXED_MARK | signature/credit | signature name | Stefano De Tanini | R | Retain personal name unchanged. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C072` | 72 | FOOTER | bottom-left signature | FIXED_MARK | signature/credit | role and brand line | Allevatore — UNICO SUO GENERE | T | РАЗВЪДЧИК — UNICO SUO GENERE | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C073` | 73 | FOOTER | bottom-center medallion | ARTWORK | bottom medallion | medallion artwork |  | G | No source text; preserve medallion artwork. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C074` | 74 | FOOTER | inside bottom-center medallion | FIXED_MARK | bottom medallion | center mark | USG | R | Retain canonical USG mark. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C075` | 75 | FOOTER | inside bottom-center medallion | FIXED_MARK | bottom medallion | upper perimeter | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |
| `P133-GA-C076` | 76 | FOOTER | inside bottom-center medallion | FIXED_MARK | bottom medallion | lower perimeter | CANE CORSO | R | Retain visible canonical seal text. | `P133_SEGNALI_CORPOREI_E_DI_STRESS_TARGET.png` |

## PAGE 134 — P134-GA

- Visual target: `references/source_text/sf05_visual_targets/P134_TEMPERAMENTO_TARGET.png`
- Target SHA-256: `A7E2578E64D78093168CDDA5B880B653F689F9DD80B2A88FBD8C713E3DC09418`
- Reading-order rule: crest/brand → title/subtitle/introduction → panels 1–3 left column → panels 4–5 right column → panel 6 lower center → note panel → signature and medallion.
- V1 range: `P134-GA-C001`–`P134-GA-C033` (33 contiguous IDs)
- Arithmetic: **33 = 25 T + 6 R + 0 N + 2 G + 0 U**

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P134-GA-C001` | 1 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C002` | 2 | HEADER | inside top-center crest | FIXED_MARK | top crest | central monogram | USG | R | Retain canonical USG mark. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C003` | 3 | HEADER | inside top-center crest | FIXED_MARK | top crest | lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C004` | 4 | HEADER | top | TITLE | named poster frame | main title | TEMPERAMENTO | T | ТЕМПЕРАМЕНТ | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C005` | 5 | HEADER | below title | TITLE | named poster frame | subtitle | ORIENTAMENTO PER IL PROPRIETARIO | T | НАСОКИ ЗА СОБСТВЕНИКА | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C006` | 6 | HEADER | below subtitle | BODY_TEXT | named poster frame | introduction | Il Cane Corso è un cane equilibrato, leale e protettivo. Ha bisogno di una guida sicura, coerente e rispettosa. | T | Кане Корсо е уравновесено, лоялно и защитнически настроено. Нуждае се от сигурно, последователно и уважително водене. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C007` | 7 | UPPER_LEFT | panel 1 | HEADING_OR_LABEL | security panel | panel heading | 1 SICUREZZA | T | 1 СИГУРНОСТ | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C008` | 8 | UPPER_LEFT | panel 1 | BODY_TEXT | security panel | panel explanation | Il Cane Corso è naturalmente protettivo e attento al suo ambiente. Si affida al proprietario per capire quando e come intervenire. | T | Кане Корсо е естествено защитнически настроено и внимателно към средата си. Обръща се към стопанина, за да разбере кога и как да се намеси. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C009` | 9 | UPPER_LEFT | panel 1 | CALLOUT | security panel | owner guidance | Offrigli regole chiare e coerenti: è così che si sente sicuro. | T | Давай му ясни и последователни правила: така се чувства сигурно. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C010` | 10 | CENTER_LEFT | panel 2 | HEADING_OR_LABEL | observation panel | panel heading | 2 OSSERVAZIONE | T | 2 НАБЛЮДЕНИЕ | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C011` | 11 | CENTER_LEFT | panel 2 | BODY_TEXT | observation panel | panel explanation | È un cane attento, riflessivo e ricettivo. Osserva prima di agire e valuta ogni situazione. | T | То е внимателно, разсъдливо и възприемчиво. Наблюдава преди да действа и преценява всяка ситуация. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C012` | 12 | CENTER_LEFT | panel 2 | CALLOUT | observation panel | owner guidance | Evita di esporlo inutilmente a stimoli eccessivi o confusione. | T | Не го излагай без нужда на прекомерни стимули или хаос. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C013` | 13 | LOWER_LEFT | panel 3 | HEADING_OR_LABEL | self-control panel | panel heading | 3 AUTOCONTROLLO | T | 3 САМОКОНТРОЛ | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C014` | 14 | LOWER_LEFT | panel 3 | BODY_TEXT | self-control panel | panel explanation | Il Cane Corso ha un forte autocontrollo quando è mentalmente equilibrato e correttamente guidato. | T | Кане Корсо има силен самоконтрол, когато е психически уравновесено и правилно водено. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C015` | 15 | LOWER_LEFT | panel 3 | CALLOUT | self-control panel | owner guidance | Lavora sulla calma, sulla gestione dell'impulso e sulla pazienza. | T | Работи върху спокойствието, управлението на импулсите и търпението. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C016` | 16 | UPPER_RIGHT | panel 4 | HEADING_OR_LABEL | human-bond panel | panel heading | 4 RAPPORTO CON L'UOMO | T | 4 ВРЪЗКА С ЧОВЕКА | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C017` | 17 | UPPER_RIGHT | panel 4 | BODY_TEXT | human-bond panel | panel explanation | È molto legato alla sua famiglia e cerca la vicinanza con le persone di riferimento. Non è invadente, ma sensibile e fedele. | T | То е силно привързано към семейството си и търси близост с хората, на които се доверява. Не е натрапчиво, а чувствително и вярно. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C018` | 18 | UPPER_RIGHT | panel 4 | CALLOUT | human-bond panel | owner guidance | Costruisci un legame basato su fiducia, rispetto e comunicazione. | T | Изграждай връзка, основана на доверие, уважение и общуване. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C019` | 19 | CENTER_RIGHT | panel 5 | HEADING_OR_LABEL | physical-function panel | panel heading | 5 FUNZIONALITÀ FISICA | T | 5 ФИЗИЧЕСКА ФУНКЦИОНАЛНОСТ | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C020` | 20 | CENTER_RIGHT | panel 5 | BODY_TEXT | physical-function panel | panel explanation | È un cane atletico, resistente e potente. Ha bisogno di movimento quotidiano, attività e stimoli adeguati. | T | То е атлетично, издръжливо и мощно. Нуждае се от ежедневно движение, подходящи занимания и стимули. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C021` | 21 | CENTER_RIGHT | panel 5 | CALLOUT | physical-function panel | owner guidance | Mantienilo in forma con esercizio, disciplina e attività mirate. | T | Поддържай го във форма с упражнения, дисциплина и целенасочени занимания. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C022` | 22 | LOWER_CENTER | panel 6 | HEADING_OR_LABEL | social-life panel | panel heading | 6 VITA SOCIALE | T | 6 СОЦИАЛЕН ЖИВОТ | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C023` | 23 | LOWER_CENTER | panel 6 | BODY_TEXT | social-life panel | panel explanation | Con una corretta socializzazione è equilibrato e rispettoso. Si relaziona in modo stabile con altri cani e persone. | T | При правилна социализация е уравновесено и уважително. Общува стабилно с други кучета и хора. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C024` | 24 | LOWER_CENTER | panel 6 | CALLOUT | social-life panel | owner guidance | Socializzazione precoce, esperienza positiva e gestione consapevole sono fondamentali. | T | Ранната социализация, положителният опит и осъзнатото управление са основополагащи. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C025` | 25 | FOOTER | note panel | HEADING_OR_LABEL | note panel | panel heading | NOTA BENE | T | ВАЖНО | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C026` | 26 | FOOTER | note panel | BODY_TEXT | note panel | note explanation | Questa pagina è un orientamento per comprendere il temperamento del Cane Corso e accompagnarlo in modo corretto nella vita quotidiana. | T | Тази страница е ориентир за разбиране на темперамента на Кане Корсо и за правилното му водене в ежедневието. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C027` | 27 | FOOTER | note panel | BODY_TEXT | note panel | disclaimer | Non costituisce né sostituisce un certificato ufficiale di carattere. | T | Тя не представлява и не замества официален сертификат за характер. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C028` | 28 | FOOTER | bottom-left signature | FIXED_MARK | signature/credit | signature name | Stefano De Tanini | R | Retain personal name unchanged. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C029` | 29 | FOOTER | bottom-left signature | FIXED_MARK | signature/credit | role and brand line | Allevatore — UNICO SUO GENERE | T | РАЗВЪДЧИК — UNICO SUO GENERE | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C030` | 30 | FOOTER | bottom-right medallion | ARTWORK | bottom medallion | medallion artwork |  | G | No source text; preserve medallion artwork. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C031` | 31 | FOOTER | inside bottom-right medallion | FIXED_MARK | bottom medallion | center mark | USG | R | Retain canonical USG mark. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C032` | 32 | FOOTER | inside bottom-right medallion | FIXED_MARK | bottom medallion | upper perimeter | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `P134_TEMPERAMENTO_TARGET.png` |
| `P134-GA-C033` | 33 | FOOTER | inside bottom-right medallion | FIXED_MARK | bottom medallion | lower perimeter | CANE CORSO | R | Retain visible canonical seal text. | `P134_TEMPERAMENTO_TARGET.png` |

## V1 aggregate

- Canonical units: **109**
- T/R/N/G/U: **93 / 12 / 0 / 4 / 0**
- Text-bearing units: **81**
- Artwork-preservation units: **4**
- Contiguous IDs: **2/2 graphics**
- Duplicate IDs: **0**
- Missing ordinals: **0**
- T units with Bulgarian targets: **69/69**
- R units retained: **12/12**
- U: **0**

## Translation notes

Two visible Italian phrases are awkward in the source graphic but legible:

- `CORPO — più rigido, incurvamento muscolare`
- `MUSO — chiuso, profilo distante`

The Bulgarian targets follow `BG_TRANSLATION_RULES.md`: preserve the supported meaning while producing natural Bulgarian rather than reproducing awkward Italian syntax word-for-word.

No source wording has been silently rewritten in the `Exact Italian source` column.
