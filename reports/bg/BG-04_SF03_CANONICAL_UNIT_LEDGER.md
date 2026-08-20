# BG-04 SF-03 CANONICAL UNIT LEDGER — CORRECTION PASS V2

Status: **ACTIVE SF-03 CONSTRUCTION AUTHORITY — V2**
Supersedes: V1 603-unit canonical ledger
Scope: surgical closure of Independent Canonical Acceptance Audit V2 findings
OCR authority: **NO**
Legacy policy: the original 216 ordinal U records remain immutable audit history and are not mapped to wording.

## Anchor schema

Each row records `READING_ORDER`, `REGION`, `PANEL`, `ELEMENT_ROLE`, `ASSOCIATED_VISUAL`, and `RELATIVE_POSITION`. BBOX_NORM is omitted where these fields uniquely identify the visible block.

## PAGE 101 — P101-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-1(20260810-073754).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title, subtitle; numbered stages 1–6 top-to-bottom, each left text then right time panel; right-side summary panels; bottom advice; crest/footer.
- V2 range: `P101-GA-C001`–`P101-GA-C043` (43 contiguous IDs)
- Arithmetic: 43 = 35 T + 6 R + 0 N + 2 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P101-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | SVILUPPO DELLA GRAVIDANZA | T | РАЗВИТИЕ НА БРЕМЕННОСТТА | `image-gen-1(20260810-073754).png` |
| `P101-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | DALLA FECONDAZIONE AL PARTO | T | ОТ ОПЛОЖДАНЕТО ДО РАЖДАНЕТО | `image-gen-1(20260810-073754).png` |
| `P101-GA-C003` | 3 | CENTER_LEFT | stage 1 left | HEADING_OR_LABEL | table/grid | stage heading | 1 FECONDAZIONE | T | 1 ОПЛОЖДАНЕ | `image-gen-1(20260810-073754).png` |
| `P101-GA-C004` | 4 | CENTER_LEFT | stage 1 left | BODY_TEXT | table/grid | stage explanation | Gli spermatozoi raggiungono l’ovulo nella tuba uterina e avviene la fecondazione. | T | Сперматозоидите достигат яйцеклетката в маточната тръба и настъпва оплождане. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C005` | 5 | CENTER_RIGHT | stage 1 right | HEADING_OR_LABEL | table/grid | time heading | GIORNI 0–3 | T | ДНИ 0–3 | `image-gen-1(20260810-073754).png` |
| `P101-GA-C006` | 6 | CENTER_RIGHT | stage 1 right | BODY_TEXT | table/grid | time explanation | Avviene l’incontro tra ovulo e spermatozoo. L’embrione inizia le prime divisioni cellulari mentre si sposta verso l’utero. | T | Яйцеклетката и сперматозоидът се срещат. Ембрионът започва първите клетъчни деления, докато се придвижва към матката. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C007` | 7 | CENTER_LEFT | stage 2 left | HEADING_OR_LABEL | table/grid | stage heading | 2 IMPIANTO | T | 2 ИМПЛАНТАЦИЯ | `image-gen-1(20260810-073754).png` |
| `P101-GA-C008` | 8 | CENTER_LEFT | stage 2 left | BODY_TEXT | table/grid | stage explanation | L’embrione raggiunge l’utero e si impianta nella mucosa uterina per iniziare il suo sviluppo. | T | Ембрионът достига матката и се имплантира в маточната лигавица, за да започне развитието си. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C009` | 9 | CENTER_RIGHT | stage 2 right | HEADING_OR_LABEL | table/grid | time heading | GIORNI 4–12 | T | ДНИ 4–12 | `image-gen-1(20260810-073754).png` |
| `P101-GA-C010` | 10 | CENTER_RIGHT | stage 2 right | BODY_TEXT | table/grid | time explanation | L’impianto avviene tra il 17° e il 20° giorno. Si formano la placenta e il sacco gestazionale. | T | Имплантацията настъпва между 17-ия и 20-ия ден. Образуват се плацентата и гестационният сак. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C011` | 11 | CENTER_LEFT | stage 3 left | HEADING_OR_LABEL | table/grid | stage heading | 3 SVILUPPO PRECOCE | T | 3 РАННО РАЗВИТИЕ | `image-gen-1(20260810-073754).png` |
| `P101-GA-C012` | 12 | CENTER_LEFT | stage 3 left | BODY_TEXT | table/grid | stage explanation | Gli organi principali iniziano a formarsi: cuore, sistema nervoso, arti e organi interni. Il feto cresce rapidamente. | T | Започват да се формират основните органи: сърце, нервна система, крайници и вътрешни органи. Плодът расте бързо. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C013` | 13 | CENTER_RIGHT | stage 3 right | HEADING_OR_LABEL | table/grid | time heading | SETTIMANE 3–5 | T | СЕДМИЦИ 3–5 | `image-gen-1(20260810-073754).png` |
| `P101-GA-C014` | 14 | CENTER_RIGHT | stage 3 right | BODY_TEXT | table/grid | time explanation | Il battito cardiaco è visibile ecograficamente. Si formano le ossa, i muscoli e i tratti somatici principali. | T | Сърдечният ритъм се вижда при ехографско изследване. Формират се костите, мускулите и основните телесни черти. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C015` | 15 | CENTER_LEFT | stage 4 left | HEADING_OR_LABEL | table/grid | stage heading | 4 SVILUPPO FETALE | T | 4 РАЗВИТИЕ НА ПЛОДА | `image-gen-1(20260810-073754).png` |
| `P101-GA-C016` | 16 | CENTER_LEFT | stage 4 left | BODY_TEXT | table/grid | stage explanation | I cuccioli continuano a crescere, la madre aumenta di peso e il latte inizia a svilupparsi. I movimenti fetali diventano più evidenti. | T | Малките продължават да растат, майката наддава на тегло и започва образуването на мляко. Движенията на плодовете стават по-осезаеми. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C017` | 17 | CENTER_RIGHT | stage 4 right | HEADING_OR_LABEL | table/grid | time heading | SETTIMANE 6–7 | T | СЕДМИЦИ 6–7 | `image-gen-1(20260810-073754).png` |
| `P101-GA-C018` | 18 | CENTER_RIGHT | stage 4 right | BODY_TEXT | table/grid | time explanation | Crescita rapida del feto. Si sviluppano i polmoni, il sistema digestivo e la pigmentazione. La madre ha bisogno di più energia e riposo. | T | Плодът расте бързо. Развиват се белите дробове, храносмилателната система и пигментацията. Майката се нуждае от повече енергия и почивка. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C019` | 19 | CENTER_LEFT | stage 5 left | HEADING_OR_LABEL | table/grid | stage heading | 5 ULTIME SETTIMANE | T | 5 ПОСЛЕДНИ СЕДМИЦИ | `image-gen-1(20260810-073754).png` |
| `P101-GA-C020` | 20 | CENTER_LEFT | stage 5 left | BODY_TEXT | table/grid | stage explanation | I cuccioli completano la maturazione degli organi e si posizionano per il parto. La madre si prepara fisicamente e ormonalmente. | T | Малките завършват съзряването на органите и се разполагат за раждането. Майката се подготвя физически и хормонално. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C021` | 21 | CENTER_RIGHT | stage 5 right | HEADING_OR_LABEL | table/grid | time heading | SETTIMANE 7–9 | T | СЕДМИЦИ 7–9 | `image-gen-1(20260810-073754).png` |
| `P101-GA-C022` | 22 | CENTER_RIGHT | stage 5 right | BODY_TEXT | table/grid | time explanation | I cuccioli accumulano peso e grasso corporeo. La temperatura corporea della madre può diminuire nelle ultime 24–48 ore prima del parto. | T | Малките натрупват тегло и телесни мазнини. Телесната температура на майката може да спадне през последните 24–48 часа преди раждането. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C023` | 23 | CENTER_LEFT | stage 6 left | HEADING_OR_LABEL | table/grid | stage heading | 6 PREPARAZIONE AL PARTO | T | 6 ПОДГОТОВКА ЗА РАЖДАНЕТО | `image-gen-1(20260810-073754).png` |
| `P101-GA-C024` | 24 | CENTER_LEFT | stage 6 left | BODY_TEXT | table/grid | stage explanation | La madre mostra segnali specifici e si prepara all’arrivo dei cuccioli. | T | Майката проявява характерни признаци и се подготвя за появата на малките. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C025` | 25 | CENTER_RIGHT | stage 6 right | HEADING_OR_LABEL | table/grid | time heading | ULTIME 48 ORE | T | ПОСЛЕДНИТЕ 48 ЧАСА | `image-gen-1(20260810-073754).png` |
| `P101-GA-C026` | 26 | CENTER_RIGHT | stage 6 right | BODY_TEXT | table/grid | time explanation | Nidificazione, irrequietezza, diminuzione dell’appetito, possibile abbassamento della temperatura (sotto 37°C). Il parto può iniziare. | T | Подготвяне на гнездо, неспокойствие, намален апетит, възможен спад на температурата (под 37°C). Раждането може да започне. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C027` | 27 | CENTER_RIGHT | right middle | HEADING_OR_LABEL | named panel/frame | /1of2 | DURATA DELLA GRAVIDANZA | T | ПРОДЪЛЖИТЕЛНОСТ НА БРЕМЕННОСТТА | `image-gen-1(20260810-073754).png` |
| `P101-GA-C028` | 28 | CENTER_RIGHT | right middle | BODY_TEXT | named panel/frame | /2of2 | La gravidanza del Cane Corso dura in media 63 giorni, con un intervallo normale da 58 a 68 giorni. | T | Бременността при Кане Корсо продължава средно 63 дни, с нормален диапазон от 58 до 68 дни. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C029` | 29 | LOWER_CENTER | right lower | HEADING_OR_LABEL | named panel/frame | /1of2 | COSA OSSERVARE NELLA MADRE | T | КАКВО ДА НАБЛЮДАВАМЕ ПРИ МАЙКАТА | `image-gen-1(20260810-073754).png` |
| `P101-GA-C030` | 30 | LOWER_CENTER | right lower | BODY_TEXT | named panel/frame | /2of2/item1of4 | Aumento del peso e dell’addome. | T | Увеличаване на теглото и корема. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C031` | 31 | LOWER_CENTER | right lower | BODY_TEXT | named panel/frame | /2of2/item2of4 | Aumento dell’appetito dalla 4ª–5ª settimana. | T | Повишен апетит от 4-тата–5-ата седмица. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C032` | 32 | LOWER_CENTER | right lower | BODY_TEXT | named panel/frame | /2of2/item3of4 | Controllo della temperatura nelle ultime 48 ore. | T | Следене на температурата през последните 48 часа. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C033` | 33 | LOWER_CENTER | right lower | BODY_TEXT | named panel/frame | /2of2/item4of4 | Visite veterinarie ed ecografie per monitorare lo sviluppo. | T | Ветеринарни прегледи и ехографии за проследяване на развитието. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C034` | 34 | LOWER_LEFT | bottom left | CALLOUT | named panel/frame | /1of2 | CONSIGLIO IMPORTANTE | T | ВАЖЕН СЪВЕТ | `image-gen-1(20260810-073754).png` |
| `P101-GA-C035` | 35 | LOWER_LEFT | bottom left | CALLOUT | named panel/frame | /2of2 | Garantire alla madre un’alimentazione di qualità, esercizio moderato e un ambiente tranquillo. Evitare stress, sforzi intensi e cambiamenti improvvisi. | T | Осигурете на майката качествено хранене, умерено движение и спокойна среда. Избягвайте стрес, силно натоварване и внезапни промени. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C036` | 36 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C037` | 37 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C038` | 38 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C039` | 39 | LOWER_CENTER | bottom-center medallion | ARTWORK | bottom medallion | bottom medallion artwork |  | G | No source text; preserve medallion artwork. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C040` | 40 | LOWER_CENTER | inside bottom-center medallion, center | FIXED_MARK | bottom medallion | bottom medallion USG | USG | R | Retain canonical USG mark. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C041` | 41 | LOWER_CENTER | inside bottom-center medallion, upper perimeter | FIXED_MARK | bottom medallion | bottom medallion upper text | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C042` | 42 | LOWER_CENTER | inside bottom-center medallion, lower perimeter | FIXED_MARK | bottom medallion | bottom medallion lower text | CANE CORSO | R | Retain visible canonical seal text. | `image-gen-1(20260810-073754).png` |
| `P101-GA-C043` | 43 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-1(20260810-073754).png` |

## PAGE 103 — P103-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-2(20260810-073758).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title, subtitle and introduction; numbered phases 1–4 top-to-bottom, left narrative then right observations; warning column; timing strip; advice strip; crest/footer.
- V2 range: `P103-GA-C001`–`P103-GA-C060` (60 contiguous IDs)
- Arithmetic: 60 = 56 T + 3 R + 0 N + 1 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P103-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | IL PROCESSO DEL PARTO | T | ПРОЦЕСЪТ НА РАЖДАНЕ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | Fasi, segnali e attenzione | T | Етапи, признаци и внимание | `image-gen-2(20260810-073758).png` |
| `P103-GA-C003` | 3 | HEADER | below subtitle | BODY_TEXT | named panel/frame | introduction | Il parto della Cane Corso è un processo naturale che si svolge in più fasi. Conoscere ogni passaggio e i segnali da osservare permette di tutelare la salute della madre e dei cuccioli. | T | Раждането при Кане Корсо е естествен процес, който протича на няколко етапа. Познаването на всеки етап и признаците за наблюдение помага да се опази здравето на майката и малките. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C004` | 4 | CENTER_LEFT | main left | HEADING_OR_LABEL | named panel/frame | section heading | LE FASI DEL PARTO | T | ЕТАПИ НА РАЖДАНЕТО | `image-gen-2(20260810-073758).png` |
| `P103-GA-C005` | 5 | CENTER_LEFT | phase 1 left | HEADING_OR_LABEL | named panel/frame | /1of3 | 1 FASE PREPARATORIA | T | 1 ПОДГОТВИТЕЛЕН ЕТАП | `image-gen-2(20260810-073758).png` |
| `P103-GA-C006` | 6 | CENTER_LEFT | phase 1 left | HEADING_OR_LABEL | named panel/frame | /2of3 | 6–24 ORE PRIMA | T | 6–24 ЧАСА ПРЕДИ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C007` | 7 | CENTER_LEFT | phase 1 left | BODY_TEXT | named panel/frame | /3of3 | La cagna si prepara al parto. Possono comparire irrequietezza, ricerca del nido, diminuzione dell’appetito e lieve calo della temperatura. | T | Женската се подготвя за раждането. Може да се появят неспокойствие, търсене на място за гнездо, намален апетит и лек спад на температурата. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C008` | 8 | CENTER_RIGHT | phase 1 right | BODY_TEXT | named panel/frame | /1of4 | Nido sicuro e tranquillo | T | Безопасно и спокойно гнездо | `image-gen-2(20260810-073758).png` |
| `P103-GA-C009` | 9 | CENTER_RIGHT | phase 1 right | BODY_TEXT | named panel/frame | /2of4 | Osservare senza interferire | T | Наблюдавайте, без да се намесвате | `image-gen-2(20260810-073758).png` |
| `P103-GA-C010` | 10 | CENTER_RIGHT | phase 1 right | BODY_TEXT | named panel/frame | /3of4 | Temperatura normale 38,0–39,0°C | T | Нормална температура 38,0–39,0°C | `image-gen-2(20260810-073758).png` |
| `P103-GA-C011` | 11 | CENTER_RIGHT | phase 1 right | BODY_TEXT | named panel/frame | /4of4 | Breve calo a 37,0–37,5°C nelle ore precedenti il parto. | T | Кратък спад до 37,0–37,5°C в часовете преди раждането. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C012` | 12 | CENTER_LEFT | phase 2 left | HEADING_OR_LABEL | named panel/frame | /1of3 | 2 FASE DI DILATAZIONE | T | 2 ЕТАП НА РАЗШИРЯВАНЕ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C013` | 13 | CENTER_LEFT | phase 2 left | HEADING_OR_LABEL | named panel/frame | /2of3 | 3–12 ORE | T | 3–12 ЧАСА | `image-gen-2(20260810-073758).png` |
| `P103-GA-C014` | 14 | CENTER_LEFT | phase 2 left | BODY_TEXT | named panel/frame | /3of3 | Iniziano le contrazioni uterine. La cagna può ansimare, tremare, vomitare, rifiutare il cibo e assumere posizioni di sollievo. | T | Започват маточните контракции. Женската може да диша учестено, да трепери, да повръща, да отказва храна и да заема облекчаващи пози. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C015` | 15 | CENTER_RIGHT | phase 2 right | BODY_TEXT | named panel/frame | /1of5 | Contrazioni irregolari | T | Нерегулярни контракции | `image-gen-2(20260810-073758).png` |
| `P103-GA-C016` | 16 | CENTER_RIGHT | phase 2 right | BODY_TEXT | named panel/frame | /2of5 | Ansimazione | T | Учестено дишане | `image-gen-2(20260810-073758).png` |
| `P103-GA-C017` | 17 | CENTER_RIGHT | phase 2 right | BODY_TEXT | named panel/frame | /3of5 | Posizioni frequenti | T | Честа смяна на позата | `image-gen-2(20260810-073758).png` |
| `P103-GA-C018` | 18 | CENTER_RIGHT | phase 2 right | BODY_TEXT | named panel/frame | /4of5 | Maggior bisogno di privacy | T | По-голяма нужда от уединение | `image-gen-2(20260810-073758).png` |
| `P103-GA-C019` | 19 | CENTER_RIGHT | phase 2 right | BODY_TEXT | named panel/frame | /5of5 | Possibili perdite vaginali chiare o leggermente rosate. | T | Възможно прозрачно или леко розово вагинално течение. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C020` | 20 | CENTER_LEFT | phase 3 left | HEADING_OR_LABEL | named panel/frame | /1of3 | 3 FASE DI ESPULSIONE | T | 3 ЕТАП НА ИЗГОНВАНЕ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C021` | 21 | CENTER_LEFT | phase 3 left | HEADING_OR_LABEL | named panel/frame | /2of3 | 15–60 MINUTI | T | 15–60 МИНУТИ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C022` | 22 | CENTER_LEFT | phase 3 left | BODY_TEXT | named panel/frame | /3of3 | Nascita di ogni cucciolo. Le contrazioni diventano più forti e regolari. La cagna espelle un cucciolo alla volta, con le sue membrane. | T | Раждане на всяко малко. Контракциите стават по-силни и ритмични. Женската ражда малките едно по едно с техните обвивки. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C023` | 23 | CENTER_RIGHT | phase 3 right | BODY_TEXT | named panel/frame | /1of4 | Contrazioni forti e regolari | T | Силни и ритмични контракции | `image-gen-2(20260810-073758).png` |
| `P103-GA-C024` | 24 | CENTER_RIGHT | phase 3 right | BODY_TEXT | named panel/frame | /2of4 | Nascita di un cucciolo alla volta | T | Раждане на едно малко | `image-gen-2(20260810-073758).png` |
| `P103-GA-C025` | 25 | CENTER_RIGHT | phase 3 right | BODY_TEXT | named panel/frame | /3of4 | Ogni cucciolo con placenta | T | Всяко малко с плацента | `image-gen-2(20260810-073758).png` |
| `P103-GA-C026` | 26 | CENTER_RIGHT | phase 3 right | HEADING_OR_LABEL | named panel/frame | /4of4/label | Intervallo tra i cuccioli | T | Интервал между малките | `image-gen-2(20260810-073758).png` |
| `P103-GA-C027` | 27 | CENTER_RIGHT | phase 3 right | BODY_TEXT | named panel/frame | /4of4/value | 15–60 minuti. | T | 15–60 минути. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C028` | 28 | CENTER_LEFT | phase 4 left | HEADING_OR_LABEL | named panel/frame | /1of3 | 4 FASE DI SECONDAMENTO | T | 4 ЕТАП НА ОТДЕЛЯНЕ НА ПЛАЦЕНТАТА | `image-gen-2(20260810-073758).png` |
| `P103-GA-C029` | 29 | CENTER_LEFT | phase 4 left | HEADING_OR_LABEL | named panel/frame | /2of3 | FINO A 6 ORE DOPO L’ULTIMA NASCITA | T | ДО 6 ЧАСА СЛЕД ПОСЛЕДНОТО РАЖДАНЕ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C030` | 30 | CENTER_LEFT | phase 4 left | BODY_TEXT | named panel/frame | /3of3 | Espulsione delle placente residue e recupero della madre. La cagna pulisce i cuccioli e inizia l’allattamento. | T | Изхвърляне на останалите плаценти и възстановяване на майката. Женската почиства малките и започва кърменето. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C031` | 31 | CENTER_RIGHT | phase 4 right | BODY_TEXT | named panel/frame | /1of4 | Espulsione di tutte le placente | T | Изхвърляне на всички плаценти | `image-gen-2(20260810-073758).png` |
| `P103-GA-C032` | 32 | CENTER_RIGHT | phase 4 right | BODY_TEXT | named panel/frame | /2of4 | La cagna cura e nutre i cuccioli | T | Женската се грижи за малките и ги храни | `image-gen-2(20260810-073758).png` |
| `P103-GA-C033` | 33 | CENTER_RIGHT | phase 4 right | BODY_TEXT | named panel/frame | /3of4 | Riposo e idratazione | T | Почивка и прием на вода | `image-gen-2(20260810-073758).png` |
| `P103-GA-C034` | 34 | CENTER_RIGHT | phase 4 right | BODY_TEXT | named panel/frame | /4of4 | Monitorare il benessere generale. | T | Наблюдение на общото състояние. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C035` | 35 | CENTER_RIGHT | right column | HEADING_OR_LABEL | named panel/frame | warning heading | SEGNALI DI ALLARME | T | ТРЕВОЖНИ ПРИЗНАЦИ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C036` | 36 | CENTER_RIGHT | right column | WARNING_ITEM | named panel/frame | warning | Contrazioni forti senza nascita di cuccioli da oltre 2 ore | T | Силни контракции без раждане на малко повече от 2 часа | `image-gen-2(20260810-073758).png` |
| `P103-GA-C037` | 37 | CENTER_RIGHT | right column | WARNING_ITEM | named panel/frame | warning | Perdite vaginali verdi o maleodoranti | T | Зелено или неприятно миришещо вагинално течение | `image-gen-2(20260810-073758).png` |
| `P103-GA-C038` | 38 | CENTER_RIGHT | right column | WARNING_ITEM | named panel/frame | warning | Cagna molto debole, apatica o collassata | T | Много слаба, апатична или колабирала женска | `image-gen-2(20260810-073758).png` |
| `P103-GA-C039` | 39 | CENTER_RIGHT | right column | WARNING_ITEM | named panel/frame | warning | Distanza tra i cuccioli superiore a 2 ore | T | Интервал между малките над 2 часа | `image-gen-2(20260810-073758).png` |
| `P103-GA-C040` | 40 | CENTER_RIGHT | right column | WARNING_ITEM | named panel/frame | warning | Perdita di sangue abbondante | T | Обилна кръвозагуба | `image-gen-2(20260810-073758).png` |
| `P103-GA-C041` | 41 | LOWER_CENTER | right lower | HEADING_OR_LABEL | named panel/frame | /1of2 | QUANDO CHIAMARE IL VETERINARIO | T | КОГА ДА СЕ ОБАДИТЕ НА ВЕТЕРИНАРЯ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C042` | 42 | LOWER_CENTER | right lower | BODY_TEXT | named panel/frame | /2of2 | Contatta immediatamente il veterinario se noti uno dei segnali di allarme o in caso di dubbio. Meglio un controllo in più, che un rischio in più. | T | Свържете се незабавно с ветеринаря, ако забележите някой от тревожните признаци или се съмнявате. По-добре един допълнителен преглед, отколкото един допълнителен риск. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C043` | 43 | LOWER_CENTER | bottom strip | HEADING_OR_LABEL | named panel/frame | section heading | TEMPI DI RIFERIMENTO | T | ОРИЕНТИРОВОЧНИ СРОКОВЕ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C044` | 44 | LOWER_CENTER | bottom strip | BODY_TEXT | named panel/frame | timing | Dall’inizio delle contrazioni alla nascita del primo cucciolo: 15 minuti–2 ore | T | От началото на контракциите до раждането на първото малко: 15 минути–2 часа | `image-gen-2(20260810-073758).png` |
| `P103-GA-C045` | 45 | LOWER_CENTER | bottom strip | HEADING_OR_LABEL | named panel/frame | /label | Intervallo tra un cucciolo e l’altro | T | Интервал между две малки | `image-gen-2(20260810-073758).png` |
| `P103-GA-C046` | 46 | LOWER_CENTER | bottom strip | BODY_TEXT | named panel/frame | /value | 15–60 minuti | T | 15–60 минути | `image-gen-2(20260810-073758).png` |
| `P103-GA-C047` | 47 | LOWER_CENTER | bottom strip | HEADING_OR_LABEL | named panel/frame | /label | Espulsione delle placente | T | Изхвърляне на плацентите | `image-gen-2(20260810-073758).png` |
| `P103-GA-C048` | 48 | LOWER_CENTER | bottom strip | BODY_TEXT | named panel/frame | /value | una per ogni cucciolo | T | по една за всяко малко | `image-gen-2(20260810-073758).png` |
| `P103-GA-C049` | 49 | LOWER_CENTER | bottom strip | HEADING_OR_LABEL | named panel/frame | /label | Durata complessiva del parto | T | Обща продължителност на раждането | `image-gen-2(20260810-073758).png` |
| `P103-GA-C050` | 50 | LOWER_CENTER | bottom strip | BODY_TEXT | named panel/frame | /value | generalmente 4–12 ore | T | обикновено 4–12 часа | `image-gen-2(20260810-073758).png` |
| `P103-GA-C051` | 51 | FOOTER | bottom | HEADING_OR_LABEL | named panel/frame | section heading | CONSIGLI IMPORTANTI | T | ВАЖНИ СЪВЕТИ | `image-gen-2(20260810-073758).png` |
| `P103-GA-C052` | 52 | FOOTER | bottom | CALLOUT | named panel/frame | /1of5 | Predisponi il nido in un luogo caldo, pulito e tranquillo | T | Подгответе гнездото на топло, чисто и спокойно място | `image-gen-2(20260810-073758).png` |
| `P103-GA-C053` | 53 | FOOTER | bottom | CALLOUT | named panel/frame | /2of5 | Osserva con discrezione e intervieni solo se necessario | T | Наблюдавайте дискретно и се намесвайте само при необходимост | `image-gen-2(20260810-073758).png` |
| `P103-GA-C054` | 54 | FOOTER | bottom | CALLOUT | named panel/frame | /3of5 | Lavati sempre le mani prima di toccare i cuccioli | T | Винаги мийте ръцете си, преди да докосвате малките | `image-gen-2(20260810-073758).png` |
| `P103-GA-C055` | 55 | FOOTER | bottom | CALLOUT | named panel/frame | /4of5 | Mantieni la temperatura ideale: 26–28°C per i cuccioli | T | Поддържайте идеална температура 26–28°C за малките | `image-gen-2(20260810-073758).png` |
| `P103-GA-C056` | 56 | FOOTER | bottom | CALLOUT | named panel/frame | /5of5 | Annota orari e nascite per monitorare il processo. | T | Записвайте часовете и ражданията, за да следите процеса. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C057` | 57 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C058` | 58 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C059` | 59 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-2(20260810-073758).png` |
| `P103-GA-C060` | 60 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-2(20260810-073758).png` |

## PAGE 105 — P105-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-3(20260810-073802).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title and subtitle; development rows from birth through week 8, top-to-bottom; within each row: age, eyes, teeth, socialization, play, feeding, movement; bottom note, rules, crest/footer.
- V2 range: `P105-GA-C001`–`P105-GA-C134` (134 contiguous IDs)
- Arithmetic: 134 = 126 T + 6 R + 0 N + 2 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P105-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | TAPPE DI SVILUPPO DEL CUCCIOLO | T | ЕТАПИ В РАЗВИТИЕТО НА МАЛКОТО | `image-gen-3(20260810-073802).png` |
| `P105-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | SETTIMANA DOPO SETTIMANA | T | СЕДМИЦА СЛЕД СЕДМИЦА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C003` | 3 | CENTER | birth row | TABLE_CELL | table/grid | age block | NASCITA 0 SETTIMANA | T | РАЖДАНЕ 0 СЕДМИЦА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C004` | 4 | CENTER | birth row | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C005` | 5 | CENTER | birth row | TABLE_CELL | table/grid | /2of7/value | Chiusi. | T | Затворени. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C006` | 6 | CENTER | birth row | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C007` | 7 | CENTER | birth row | TABLE_CELL | table/grid | /3of7/value | Nessuno. | T | Няма. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C008` | 8 | CENTER | birth row | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C009` | 9 | CENTER | birth row | TABLE_CELL | table/grid | /4of7/value | Legame esclusivo con la madre. | T | Изключителна връзка с майката. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C010` | 10 | CENTER | birth row | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C011` | 11 | CENTER | birth row | TABLE_CELL | table/grid | /5of7/value | Nessuno. | T | Няма. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C012` | 12 | CENTER | birth row | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C013` | 13 | CENTER | birth row | TABLE_CELL | table/grid | /6of7/value | Esclusivamente latte materno. | T | Само майчино мляко. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C014` | 14 | CENTER | birth row | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C015` | 15 | CENTER | birth row | TABLE_CELL | table/grid | /7of7/value | Si muove strisciando. | T | Придвижва се с пълзене. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C016` | 16 | CENTER | week 1 | TABLE_CELL | table/grid | age block | 1ª SETTIMANA 7 GIORNI | T | 1-ВА СЕДМИЦА 7 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C017` | 17 | CENTER | week 1 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C018` | 18 | CENTER | week 1 | TABLE_CELL | table/grid | /2of7/value | Restano chiusi. | T | Остават затворени. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C019` | 19 | CENTER | week 1 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C020` | 20 | CENTER | week 1 | TABLE_CELL | table/grid | /3of7/value | Nessuno. | T | Няма. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C021` | 21 | CENTER | week 1 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C022` | 22 | CENTER | week 1 | TABLE_CELL | table/grid | /4of7/value | Dipendenza totale dalla madre. | T | Пълна зависимост от майката. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C023` | 23 | CENTER | week 1 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C024` | 24 | CENTER | week 1 | TABLE_CELL | table/grid | /5of7/value | Nessuno. | T | Няма. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C025` | 25 | CENTER | week 1 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C026` | 26 | CENTER | week 1 | TABLE_CELL | table/grid | /6of7/value | Latte materno frequente. | T | Често сучене. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C027` | 27 | CENTER | week 1 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C028` | 28 | CENTER | week 1 | TABLE_CELL | table/grid | /7of7/value | Striscia verso il calore. | T | Пълзи към топлината. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C029` | 29 | CENTER | week 2 | TABLE_CELL | table/grid | age block | 2ª SETTIMANA 14 GIORNI | T | 2-РА СЕДМИЦА 14 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C030` | 30 | CENTER | week 2 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C031` | 31 | CENTER | week 2 | TABLE_CELL | table/grid | /2of7/value | Ancora chiusi. | T | Все още затворени. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C032` | 32 | CENTER | week 2 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C033` | 33 | CENTER | week 2 | TABLE_CELL | table/grid | /3of7/value | Inizio eruzione dei denti da latte. | T | Започва пробивът на млечните зъби. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C034` | 34 | CENTER | week 2 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C035` | 35 | CENTER | week 2 | TABLE_CELL | table/grid | /4of7/value | Risponde alla voce e al contatto. | T | Реагира на глас и допир. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C036` | 36 | CENTER | week 2 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C037` | 37 | CENTER | week 2 | TABLE_CELL | table/grid | /5of7/value | Primi movimenti e tentativi di interazione. | T | Първи движения и опити за взаимодействие. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C038` | 38 | CENTER | week 2 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C039` | 39 | CENTER | week 2 | TABLE_CELL | table/grid | /6of7/value | Latte materno. Inizio scoperta dell’ambiente. | T | Майчино мляко. Започва да опознава средата. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C040` | 40 | CENTER | week 2 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C041` | 41 | CENTER | week 2 | TABLE_CELL | table/grid | /7of7/value | Cammina incerto sulle zampe. | T | Стъпва несигурно на краката си. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C042` | 42 | CENTER | week 3 | TABLE_CELL | table/grid | age block | 3ª SETTIMANA 21 GIORNI | T | 3-ТА СЕДМИЦА 21 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C043` | 43 | CENTER | week 3 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C044` | 44 | CENTER | week 3 | TABLE_CELL | table/grid | /2of7/value | Iniziano ad aprirsi. | T | Започват да се отварят. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C045` | 45 | CENTER | week 3 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C046` | 46 | CENTER | week 3 | TABLE_CELL | table/grid | /3of7/value | Dentini da latte in crescita. | T | Млечните зъбки растат. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C047` | 47 | CENTER | week 3 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C048` | 48 | CENTER | week 3 | TABLE_CELL | table/grid | /4of7/value | Prime reazioni a suoni e stimoli esterni. | T | Първи реакции към звуци и външни стимули. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C049` | 49 | CENTER | week 3 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C050` | 50 | CENTER | week 3 | TABLE_CELL | table/grid | /5of7/value | Inizia il gioco con i fratelli e la madre. | T | Започва да играе с останалите малки и майката. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C051` | 51 | CENTER | week 3 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C052` | 52 | CENTER | week 3 | TABLE_CELL | table/grid | /6of7/value | Inizio svezzamento: pappa morbida oltre al latte. | T | Начало на отбиването: мека храна наред с млякото. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C053` | 53 | CENTER | week 3 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C054` | 54 | CENTER | week 3 | TABLE_CELL | table/grid | /7of7/value | Cammina con più sicurezza. | T | Ходи по-уверено. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C055` | 55 | CENTER | week 4 | TABLE_CELL | table/grid | age block | 4ª SETTIMANA 28 GIORNI | T | 4-ТА СЕДМИЦА 28 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C056` | 56 | CENTER | week 4 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C057` | 57 | CENTER | week 4 | TABLE_CELL | table/grid | /2of7/value | Aperti del tutto. | T | Напълно отворени. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C058` | 58 | CENTER | week 4 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C059` | 59 | CENTER | week 4 | TABLE_CELL | table/grid | /3of7/value | Dentini da latte completi. | T | Пълен комплект млечни зъбки. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C060` | 60 | CENTER | week 4 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C061` | 61 | CENTER | week 4 | TABLE_CELL | table/grid | /4of7/value | Esplora l’ambiente, curioso e attento. | T | Изследва средата с любопитство и внимание. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C062` | 62 | CENTER | week 4 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C063` | 63 | CENTER | week 4 | TABLE_CELL | table/grid | /5of7/value | Gioco attivo con i fratelli. Prime regole. | T | Активна игра с останалите малки. Първи правила. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C064` | 64 | CENTER | week 4 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C065` | 65 | CENTER | week 4 | TABLE_CELL | table/grid | /6of7/value | Svezzamento avanzato. Pasti frequenti. | T | Напреднало отбиване. Чести хранения. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C066` | 66 | CENTER | week 4 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C067` | 67 | CENTER | week 4 | TABLE_CELL | table/grid | /7of7/value | Percorre brevi distanze con sicurezza. | T | Изминава уверено кратки разстояния. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C068` | 68 | CENTER | week 5 | TABLE_CELL | table/grid | age block | 5ª SETTIMANA 35 GIORNI | T | 5-А СЕДМИЦА 35 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C069` | 69 | CENTER | week 5 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C070` | 70 | CENTER | week 5 | TABLE_CELL | table/grid | /2of7/value | Vista completa e reattiva. | T | Зрението е пълноценно и реагиращо. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C071` | 71 | CENTER | week 5 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C072` | 72 | CENTER | week 5 | TABLE_CELL | table/grid | /3of7/value | Morsi affinato in sviluppo. | T | Захапванията се усъвършенстват в хода на развитието. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C073` | 73 | CENTER | week 5 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C074` | 74 | CENTER | week 5 | TABLE_CELL | table/grid | /4of7/value | Periodo chiave: accetta novità e persone. | T | Ключов период: приема нови неща и хора. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C075` | 75 | CENTER | week 5 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C076` | 76 | CENTER | week 5 | TABLE_CELL | table/grid | /5of7/value | Gioco vivace e interazioni complesse. | T | Жива игра и сложни взаимодействия. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C077` | 77 | CENTER | week 5 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C078` | 78 | CENTER | week 5 | TABLE_CELL | table/grid | /6of7/value | Pasti solidi 3–4 volte al giorno. | T | Твърда храна 3–4 пъти дневно. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C079` | 79 | CENTER | week 5 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C080` | 80 | CENTER | week 5 | TABLE_CELL | table/grid | /7of7/value | Esplora, corre e supera piccoli ostacoli. | T | Изследва, тича и преодолява малки препятствия. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C081` | 81 | CENTER | week 6 | TABLE_CELL | table/grid | age block | 6ª SETTIMANA 42 GIORNI | T | 6-А СЕДМИЦА 42 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C082` | 82 | CENTER | week 6 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C083` | 83 | CENTER | week 6 | TABLE_CELL | table/grid | /2of7/value | Coordinazione visiva ottima. | T | Отлична зрителна координация. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C084` | 84 | CENTER | week 6 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C085` | 85 | CENTER | week 6 | TABLE_CELL | table/grid | /3of7/value | Cambio denti in arrivo. | T | Предстои смяна на зъбите. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C086` | 86 | CENTER | week 6 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C087` | 87 | CENTER | week 6 | TABLE_CELL | table/grid | /4of7/value | Fase d’oro: nuove esperienze sono fondamentali. | T | Златен период: новите преживявания са основополагащи. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C088` | 88 | CENTER | week 6 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C089` | 89 | CENTER | week 6 | TABLE_CELL | table/grid | /5of7/value | Apprende limiti, ruoli e autocontrollo. | T | Усвоява граници, роли и самоконтрол. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C090` | 90 | CENTER | week 6 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C091` | 91 | CENTER | week 6 | TABLE_CELL | table/grid | /6of7/value | Pasti solidi completi. Acqua fresca. | T | Пълноценна твърда храна. Прясна вода. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C092` | 92 | CENTER | week 6 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C093` | 93 | CENTER | week 6 | TABLE_CELL | table/grid | /7of7/value | Movimenti sicuri, salti e giochi. | T | Уверени движения, скокове и игри. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C094` | 94 | CENTER | week 7 | TABLE_CELL | table/grid | age block | 7ª SETTIMANA 49 GIORNI | T | 7-А СЕДМИЦА 49 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C095` | 95 | CENTER | week 7 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C096` | 96 | CENTER | week 7 | TABLE_CELL | table/grid | /2of7/value | Perfettamente reattivi. | T | Реагират напълно. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C097` | 97 | CENTER | week 7 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C098` | 98 | CENTER | week 7 | TABLE_CELL | table/grid | /3of7/value | Dentizione mista in corso. | T | Протича смесено съзъбие. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C099` | 99 | CENTER | week 7 | HEADING_OR_LABEL | table/grid | /4of7/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C100` | 100 | CENTER | week 7 | TABLE_CELL | table/grid | /4of7/value | Sicurezza in crescita, coraggio naturale. | T | Нарастваща увереност, естествена смелост. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C101` | 101 | CENTER | week 7 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C102` | 102 | CENTER | week 7 | TABLE_CELL | table/grid | /5of7/value | Gioco strutturato, estremo piacere nell’interazione. | T | Структурирана игра, силно удоволствие от взаимодействието. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C103` | 103 | CENTER | week 7 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C104` | 104 | CENTER | week 7 | TABLE_CELL | table/grid | /6of7/value | Pasti solidi 2–3 volte al giorno. | T | Твърда храна 2–3 пъти дневно. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C105` | 105 | CENTER | week 7 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C106` | 106 | CENTER | week 7 | TABLE_CELL | table/grid | /7of7/value | Resistente, esplora ampi spazi. | T | Издръжливо, изследва големи пространства. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C107` | 107 | CENTER | week 8 | TABLE_CELL | table/grid | age block | 8ª SETTIMANA 56 GIORNI | T | 8-А СЕДМИЦА 56 ДНИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C108` | 108 | CENTER | week 8 | HEADING_OR_LABEL | table/grid | /2of7/label | OCCHI | T | ОЧИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C109` | 109 | CENTER | week 8 | TABLE_CELL | table/grid | /2of7/value | Sguardo vivo e attento. | T | Жив и внимателен поглед. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C110` | 110 | CENTER | week 8 | HEADING_OR_LABEL | table/grid | /3of7/label | DENTI | T | ЗЪБИ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C111` | 111 | CENTER | week 8 | TABLE_CELL | table/grid | /3of7/value | Dentizione mista completata progressivamente. | T | Смесеното съзъбие постепенно завършва. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C112` | 112 | CENTER | week 8 | HEADING_OR_LABEL | table/grid | /4of7/1of2/label | SOCIALIZZAZIONE | T | СОЦИАЛИЗАЦИЯ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C113` | 113 | CENTER | week 8 | TABLE_CELL | table/grid | /4of7/1of2/value | Pronto al mondo | T | Готово за света | `image-gen-3(20260810-073802).png` |
| `P105-GA-C114` | 114 | CENTER | week 8 | TABLE_CELL | table/grid | /4of7/2of2 | continua socializzazione e costruzione del legame. | T | социализацията и изграждането на връзка продължават. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C115` | 115 | CENTER | week 8 | HEADING_OR_LABEL | table/grid | /5of7/label | GIOCO | T | ИГРА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C116` | 116 | CENTER | week 8 | TABLE_CELL | table/grid | /5of7/value | Gioco libero e adattamento all’ambiente. | T | Свободна игра и адаптиране към средата. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C117` | 117 | CENTER | week 8 | HEADING_OR_LABEL | table/grid | /6of7/label | ALIMENTAZIONE | T | ХРАНЕНЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C118` | 118 | CENTER | week 8 | TABLE_CELL | table/grid | /6of7/value | Alimentazione completa e bilanciata. | T | Пълноценно и балансирано хранене. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C119` | 119 | CENTER | week 8 | HEADING_OR_LABEL | table/grid | /7of7/label | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-3(20260810-073802).png` |
| `P105-GA-C120` | 120 | CENTER | week 8 | TABLE_CELL | table/grid | /7of7/value | Ben coordinato, forte e pieno di energia. | T | Добре координирано, силно и изпълнено с енергия. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C121` | 121 | LOWER_LEFT | bottom left | CALLOUT | named panel/frame | note | Le prime 8 settimane sono fondamentali per la salute, la socializzazione e il carattere del tuo Cane Corso. Amore, stimoli positivi e coerenza oggi, per un compagno equilibrato domani. | T | Първите 8 седмици са основополагащи за здравето, социализацията и характера на вашето Кане Корсо. Любов, положителни стимули и последователност днес — за уравновесен спътник утре. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C122` | 122 | LOWER_RIGHT | bottom right | CALLOUT | named panel/frame | /1of2 | REGOLE D’ORO | T | ЗЛАТНИ ПРАВИЛА | `image-gen-3(20260810-073802).png` |
| `P105-GA-C123` | 123 | LOWER_RIGHT | bottom right | CALLOUT | named panel/frame | /2of2/1of4 | Sicurezza e ambiente sereno | T | Безопасност и спокойна среда | `image-gen-3(20260810-073802).png` |
| `P105-GA-C124` | 124 | LOWER_RIGHT | bottom right | CALLOUT | named panel/frame | /2of2/2of4 | Stimoli graduali e positivi | T | Постепенни и положителни стимули | `image-gen-3(20260810-073802).png` |
| `P105-GA-C125` | 125 | LOWER_RIGHT | bottom right | CALLOUT | named panel/frame | /2of2/3of4 | Routine costante e amore coerente | T | Постоянен режим и последователна обич | `image-gen-3(20260810-073802).png` |
| `P105-GA-C126` | 126 | LOWER_RIGHT | bottom right | CALLOUT | named panel/frame | /2of2/4of4 | Rispetto dei tempi del cucciolo | T | Уважение към темпото на малкото | `image-gen-3(20260810-073802).png` |
| `P105-GA-C127` | 127 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C128` | 128 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C129` | 129 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C130` | 130 | LOWER_CENTER | bottom-center medallion | ARTWORK | bottom medallion | bottom medallion artwork |  | G | No source text; preserve medallion artwork. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C131` | 131 | LOWER_CENTER | inside bottom-center medallion, center | FIXED_MARK | bottom medallion | bottom medallion USG | USG | R | Retain canonical USG mark. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C132` | 132 | LOWER_CENTER | inside bottom-center medallion, upper perimeter | FIXED_MARK | bottom medallion | bottom medallion upper text | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C133` | 133 | LOWER_CENTER | inside bottom-center medallion, lower perimeter | FIXED_MARK | bottom medallion | bottom medallion lower text | CANE CORSO | R | Retain visible canonical seal text. | `image-gen-3(20260810-073802).png` |
| `P105-GA-C134` | 134 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-3(20260810-073802).png` |

## PAGE 106 — P106-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-4(20260810-073804).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title/subtitle; upper explanatory, anatomy and importance panels left-to-right; recommended and avoid cards left-to-right; lower guidance panels; motto and footer.
- V2 range: `P106-GA-C001`–`P106-GA-C047` (47 contiguous IDs)
- Arithmetic: 47 = 43 T + 3 R + 0 N + 1 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P106-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | CARTILAGINI DI ACCRESCIMENTO ED ESERCIZIO | T | РАСТЕЖНИ ХРУЩЯЛИ И УПРАЖНЕНИЯ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | Crescere senza forzare | T | Растеж без претоварване | `image-gen-4(20260810-073804).png` |
| `P106-GA-C003` | 3 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of2 | COSA SONO LE CARTILAGINI DI ACCRESCIMENTO | T | КАКВО ПРЕДСТАВЛЯВАТ РАСТЕЖНИТЕ ХРУЩЯЛИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C004` | 4 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /2of2 | Le cartilagini di accrescimento sono aree di tessuto cartilagineo situate alle estremità delle ossa lunghe. Consentono l’allungamento progressivo delle ossa durante la crescita del cucciolo. Sono più delicate dell’osso maturo e sensibili a sollecitazioni eccessive. Proteggerle significa garantire uno sviluppo armonico e sano. | T | Растежните хрущяли са участъци от хрущялна тъкан в краищата на дългите кости. Те позволяват постепенното удължаване на костите по време на растежа на малкото. По-деликатни са от зрялата кост и са чувствителни към прекомерно натоварване. Защитата им осигурява хармонично и здравословно развитие. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C005` | 5 | CENTER | upper center | HEADING_OR_LABEL | diagram | anatomy heading | PRINCIPALI CARTILAGINI DI ACCRESCIMENTO | T | ОСНОВНИ РАСТЕЖНИ ХРУЩЯЛИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C006` | 6 | CENTER | dog diagram | BODY_TEXT | dog illustration | /1of6 | Spalla (omero prossimale) | T | Рамо (проксимална раменна кост) | `image-gen-4(20260810-073804).png` |
| `P106-GA-C007` | 7 | CENTER | dog diagram | BODY_TEXT | dog illustration | /2of6 | Anca (femore prossimale) | T | Тазобедрена става (проксимална бедрена кост) | `image-gen-4(20260810-073804).png` |
| `P106-GA-C008` | 8 | CENTER | dog diagram | BODY_TEXT | dog illustration | /3of6 | Gomito (omero distale) | T | Лакът (дистална раменна кост) | `image-gen-4(20260810-073804).png` |
| `P106-GA-C009` | 9 | CENTER | dog diagram | BODY_TEXT | dog illustration | /4of6 | Ginocchio (tibia prossimale) | T | Коляно (проксимална голямопищялна кост) | `image-gen-4(20260810-073804).png` |
| `P106-GA-C010` | 10 | CENTER | dog diagram | BODY_TEXT | dog illustration | /5of6 | Carpo (radio distale) | T | Карпус (дистална лъчева кост) | `image-gen-4(20260810-073804).png` |
| `P106-GA-C011` | 11 | CENTER | dog diagram | BODY_TEXT | dog illustration | /6of6 | Garretto (tibia distale) | T | Скакателна става (дистална голямопищялна кост) | `image-gen-4(20260810-073804).png` |
| `P106-GA-C012` | 12 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | PERCHÉ È IMPORTANTE RISPETTARLE | T | ЗАЩО Е ВАЖНО ДА ГИ ЩАДИМ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C013` | 13 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /2of2 | Sollecitazioni eccessive o traumi possono danneggiare le cartilagini di accrescimento, causando alterazioni strutturali, deformità e problemi articolari nell’età adulta. Crescita sana oggi, forza duratura domani. | T | Прекомерното натоварване или травмите могат да увредят растежните хрущяли и да причинят структурни изменения, деформации и ставни проблеми в зряла възраст. Здравословен растеж днес, трайна сила утре. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C014` | 14 | CENTER_LEFT | middle left | HEADING_OR_LABEL | named panel/frame | section heading | MOVIMENTO CONSIGLIATO | T | ПРЕПОРЪЧИТЕЛНО ДВИЖЕНИЕ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C015` | 15 | CENTER | recommended 1 | HEADING_OR_LABEL | named panel/frame | /1of2 | PASSEGGIATE QUOTIDIANE | T | ЕЖЕДНЕВНИ РАЗХОДКИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C016` | 16 | CENTER | recommended 1 | BODY_TEXT | named panel/frame | /2of2 | Passeggiate su superfici regolari, al guinzaglio, alla portata di attenzione e non eccessivamente lunghe. | T | Разходки по равни настилки, на повод, съобразени с вниманието и без прекомерна продължителност. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C017` | 17 | CENTER | recommended 2 | HEADING_OR_LABEL | named panel/frame | /1of2 | ESPLORAZIONE LIBERA CONTROLLATA | T | КОНТРОЛИРАНО СВОБОДНО ИЗСЛЕДВАНЕ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C018` | 18 | CENTER | recommended 2 | BODY_TEXT | named panel/frame | /2of2 | Lascia che il cucciolo esplori, annusi e conosca l’ambiente in sicurezza e senza stress. | T | Оставете малкото да изследва, души и опознава средата безопасно и без стрес. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C019` | 19 | CENTER | recommended 3 | HEADING_OR_LABEL | named panel/frame | /1of2 | GIOCO MODERATO CON COETANEI | T | УМЕРЕНА ИГРА С ВРЪСТНИЦИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C020` | 20 | CENTER | recommended 3 | BODY_TEXT | named panel/frame | /2of2 | Interazioni sociali brevi e positive aiutano lo sviluppo comportamentale e motorio in modo naturale. | T | Кратките положителни социални взаимодействия подпомагат естественото поведенческо и двигателно развитие. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C021` | 21 | CENTER | recommended 4 | HEADING_OR_LABEL | named panel/frame | /1of2 | SUPERFICI AMICHEVOLI | T | ЩАДЯЩИ НАСТИЛКИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C022` | 22 | CENTER | recommended 4 | BODY_TEXT | named panel/frame | /2of2 | Terreni morbidi e regolari favoriscono il movimento senza sovraccaricare le articolazioni. | T | Меките и равни терени подпомагат движението, без да претоварват ставите. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C023` | 23 | CENTER_RIGHT | middle right | HEADING_OR_LABEL | named panel/frame | section heading | DA EVITARE | T | ДА СЕ ИЗБЯГВА | `image-gen-4(20260810-073804).png` |
| `P106-GA-C024` | 24 | CENTER | avoid 1 | HEADING_OR_LABEL | named panel/frame | /1of2 | SCALE FREQUENTI | T | ЧЕСТО КАЧВАНЕ ПО СТЪЛБИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C025` | 25 | CENTER | avoid 1 | BODY_TEXT | named panel/frame | /2of2 | Salire e scendere ripetutamente affatica ginocchia e garretti ancora in crescita. | T | Многократното качване и слизане натоварва коленете и все още растящите скакателни стави. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C026` | 26 | CENTER | avoid 2 | HEADING_OR_LABEL | named panel/frame | /1of2 | SALTI ALTI E OSTACOLI | T | ВИСОКИ СКОКОВЕ И ПРЕПЯТСТВИЯ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C027` | 27 | CENTER | avoid 2 | BODY_TEXT | named panel/frame | /2of2 | Salti, divani, auto e giochi troppo dinamici possono sovraccaricare le articolazioni. | T | Скокове, дивани, автомобили и прекалено динамични игри могат да претоварят ставите. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C028` | 28 | CENTER | avoid 3 | HEADING_OR_LABEL | named panel/frame | /1of2 | CORSE INTENSE E PROLUNGATE | T | ИНТЕНЗИВНО И ПРОДЪЛЖИТЕЛНО ТИЧАНЕ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C029` | 29 | CENTER | avoid 3 | BODY_TEXT | named panel/frame | /2of2 | L’attività intensa e prolungata può sovraccaricare le cartilagini e affaticare muscoli e tendini. | T | Интензивното и продължително натоварване може да претовари хрущялите и да измори мускулите и сухожилията. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C030` | 30 | CENTER | avoid 4 | HEADING_OR_LABEL | named panel/frame | /1of2 | SUPERFICI SCIVOLOSE | T | ХЛЪЗГАВИ НАСТИЛКИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C031` | 31 | CENTER | avoid 4 | BODY_TEXT | named panel/frame | /2of2 | Pavimenti scivolosi possono causare cadute e movimenti innaturali pericolosi. | T | Хлъзгавите подове могат да причинят падания и опасни неестествени движения. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C032` | 32 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | PERCHÉ LA CRESCITA NON È UNA GARA | T | ЗАЩО РАСТЕЖЪТ НЕ Е СЪСТЕЗАНИЕ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C033` | 33 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2/item1of4 | Ogni cucciolo ha i propri tempi di crescita. | T | Всяко малко има собствен темп на растеж. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C034` | 34 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2/item2of4 | Forzare il corpo oggi può compromettere la salute di domani. | T | Претоварването на тялото днес може да застраши здравето утре. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C035` | 35 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2/item3of4 | Un movimento graduale e adeguato costruisce forza, equilibrio e resistenza in modo armonico. | T | Постепенното и подходящо движение изгражда хармонично сила, равновесие и издръжливост. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C036` | 36 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2/item4of4 | La pazienza è il miglior investimento per un Cane Corso sano, forte e longevo. | T | Търпението е най-добрата инвестиция за здраво, силно и дълголетно Кане Корсо. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C037` | 37 | LOWER_CENTER | lower center | FIXED_MARK | bottom medallion | medallion | RADICI FORTI, FUTURO SOLIDO. | T | СИЛНИ КОРЕНИ, СТАБИЛНО БЪДЕЩЕ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C038` | 38 | LOWER_RIGHT | lower right | HEADING_OR_LABEL | named panel/frame | /1of2 | LINEE GUIDA GENERALI | T | ОБЩИ НАСОКИ | `image-gen-4(20260810-073804).png` |
| `P106-GA-C039` | 39 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item1of4 | Segui sempre l’età, la taglia e la condizione del tuo cucciolo. | T | Винаги се съобразявайте с възрастта, размера и състоянието на малкото. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C040` | 40 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item2of4 | Aumenta gradualmente durata e intensità delle attività. | T | Увеличавайте постепенно продължителността и интензивността на дейностите. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C041` | 41 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item3of4 | Osserva il tuo Cane Corso: stanchezza, zoppia o riluttanza a muoversi sono segnali da non ignorare. | T | Наблюдавайте своето Кане Корсо: умората, куцотата или нежеланието за движение са признаци, които не бива да се пренебрегват. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C042` | 42 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item4of4 | In caso di dubbi, consulta il tuo medico veterinario. | T | При съмнение се консултирайте с ветеринарен лекар. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C043` | 43 | FOOTER | above footer | FIXED_MARK | named panel/frame | motto | UN CUCCIOLO PROTETTO OGGI, UN GIGANTE EQUILIBRATO DOMANI. | T | ЗАЩИТЕНО МАЛКО ДНЕС, УРАВНОВЕСЕН ГИГАНТ УТРЕ. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C044` | 44 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C045` | 45 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C046` | 46 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-4(20260810-073804).png` |
| `P106-GA-C047` | 47 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-4(20260810-073804).png` |

## PAGE 108 — P108-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-5(9).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title/subtitle; growth columns left-to-right; table row labels and cells left-to-right; observation cards; warning strip; motto and footer.
- V2 range: `P108-GA-C001`–`P108-GA-C077` (77 contiguous IDs)
- Arithmetic: 77 = 69 T + 6 R + 0 N + 2 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P108-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | MONITORAGGIO DELLA CRESCITA | T | ПРОСЛЕДЯВАНЕ НА РАСТЕЖА | `image-gen-5(9).png` |
| `P108-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | NEI PRIMI MESI | T | ПРЕЗ ПЪРВИТЕ МЕСЕЦИ | `image-gen-5(9).png` |
| `P108-GA-C003` | 3 | CENTER | upper table | HEADING_OR_LABEL | table/grid | section heading | PROGRESSIONE DI CRESCITA | T | РАЗВИТИЕ НА РАСТЕЖА | `image-gen-5(9).png` |
| `P108-GA-C004` | 4 | CENTER | table columns | TABLE_CELL | table/grid | /1of8 | 2 MESI | T | 2 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C005` | 5 | CENTER | table columns | TABLE_CELL | table/grid | /2of8 | 3 MESI | T | 3 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C006` | 6 | CENTER | table columns | TABLE_CELL | table/grid | /3of8 | 4 MESI | T | 4 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C007` | 7 | CENTER | table columns | TABLE_CELL | table/grid | /4of8 | 5 MESI | T | 5 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C008` | 8 | CENTER | table columns | TABLE_CELL | table/grid | /5of8 | 6 MESI | T | 6 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C009` | 9 | CENTER | table columns | TABLE_CELL | table/grid | /6of8 | 8 MESI | T | 8 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C010` | 10 | CENTER | table columns | TABLE_CELL | table/grid | /7of8 | 12 MESI | T | 12 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C011` | 11 | CENTER | table columns | TABLE_CELL | table/grid | /8of8 | 18 MESI | T | 18 МЕСЕЦА | `image-gen-5(9).png` |
| `P108-GA-C012` | 12 | CENTER | weight | TABLE_CELL | table/grid | /1of8/1of2 | PESO | T | ТЕГЛО | `image-gen-5(9).png` |
| `P108-GA-C013` | 13 | CENTER | weight | TABLE_CELL | table/grid | /1of8/2of2 | Valori indicativi | T | Ориентировъчни стойности | `image-gen-5(9).png` |
| `P108-GA-C014` | 14 | CENTER | weight | TABLE_CELL | table/grid | /2of8 | 4–8 kg | T | 4–8 кг | `image-gen-5(9).png` |
| `P108-GA-C015` | 15 | CENTER | weight | TABLE_CELL | table/grid | /3of8 | 8–15 kg | T | 8–15 кг | `image-gen-5(9).png` |
| `P108-GA-C016` | 16 | CENTER | weight | TABLE_CELL | table/grid | /4of8 | 15–24 kg | T | 15–24 кг | `image-gen-5(9).png` |
| `P108-GA-C017` | 17 | CENTER | weight | TABLE_CELL | table/grid | /5of8 | 25–40 kg | T | 25–40 кг | `image-gen-5(9).png` |
| `P108-GA-C018` | 18 | CENTER | weight | TABLE_CELL | table/grid | /6of8 | 30–48 kg | T | 30–48 кг | `image-gen-5(9).png` |
| `P108-GA-C019` | 19 | CENTER | weight | TABLE_CELL | table/grid | /7of8 | 38–55 kg | T | 38–55 кг | `image-gen-5(9).png` |
| `P108-GA-C020` | 20 | CENTER | weight | TABLE_CELL | table/grid | /8of8 | 45–60+ kg | T | 45–60+ кг | `image-gen-5(9).png` |
| `P108-GA-C021` | 21 | CENTER | proportions | TABLE_CELL | table/grid | /1of8/1of2 | PROPORZIONI | T | ПРОПОРЦИИ | `image-gen-5(9).png` |
| `P108-GA-C022` | 22 | CENTER | proportions | TABLE_CELL | table/grid | /1of8/2of2 | Crescita armonica | T | Хармоничен растеж | `image-gen-5(9).png` |
| `P108-GA-C023` | 23 | CENTER | proportions | TABLE_CELL | table/grid | /2of8 | Corpo compatto, testa rotonda, arti corte | T | Компактно тяло, закръглена глава, къси крайници | `image-gen-5(9).png` |
| `P108-GA-C024` | 24 | CENTER | proportions | TABLE_CELL | table/grid | /3of8 | Inizio allungamento del corpo | T | Начало на удължаването на тялото | `image-gen-5(9).png` |
| `P108-GA-C025` | 25 | CENTER | proportions | TABLE_CELL | table/grid | /4of8 | Torace si apre, dorso stabile | T | Гръдният кош се разширява, гърбът е стабилен | `image-gen-5(9).png` |
| `P108-GA-C026` | 26 | CENTER | proportions | TABLE_CELL | table/grid | /5of8 | Proporzioni più equilibrate, massa in aumento | T | По-балансирани пропорции, увеличаваща се маса | `image-gen-5(9).png` |
| `P108-GA-C027` | 27 | CENTER | proportions | TABLE_CELL | table/grid | /6of8 | Struttura in definizione, muscolatura in sviluppo | T | Структурата се оформя, мускулатурата се развива | `image-gen-5(9).png` |
| `P108-GA-C028` | 28 | CENTER | proportions | TABLE_CELL | table/grid | /7of8 | Proporzioni quasi adulte, petto profondo | T | Почти зрели пропорции, дълбок гръден кош | `image-gen-5(9).png` |
| `P108-GA-C029` | 29 | CENTER | proportions | TABLE_CELL | table/grid | /8of8 | Struttura completa e armonica | T | Завършена и хармонична структура | `image-gen-5(9).png` |
| `P108-GA-C030` | 30 | CENTER | movement | TABLE_CELL | table/grid | /1of8/1of2 | MOVIMENTO | T | ДВИЖЕНИЕ | `image-gen-5(9).png` |
| `P108-GA-C031` | 31 | CENTER | movement | TABLE_CELL | table/grid | /1of8/2of2 | Osserva e valuta | T | Наблюдавайте и оценявайте | `image-gen-5(9).png` |
| `P108-GA-C032` | 32 | CENTER | movement | TABLE_CELL | table/grid | /2of8 | Movimenti incerti, andatura corta | T | Несигурни движения, къса крачка | `image-gen-5(9).png` |
| `P108-GA-C033` | 33 | CENTER | movement | TABLE_CELL | table/grid | /3of8 | Più sicuro, inizia l’esplorazione | T | По-уверено, започва да изследва | `image-gen-5(9).png` |
| `P108-GA-C034` | 34 | CENTER | movement | TABLE_CELL | table/grid | /4of8 | Passo sciolto, coordinazione in crescita | T | Свободна крачка, подобряваща се координация | `image-gen-5(9).png` |
| `P108-GA-C035` | 35 | CENTER | movement | TABLE_CELL | table/grid | /5of8 | Spinta posteriore in sviluppo, passo ampio | T | Развиващ се тласък от задните крайници, широка крачка | `image-gen-5(9).png` |
| `P108-GA-C036` | 36 | CENTER | movement | TABLE_CELL | table/grid | /6of8 | Andatura sciolta, equilibrata, senza rigidità | T | Свободна и балансирана походка без скованост | `image-gen-5(9).png` |
| `P108-GA-C037` | 37 | CENTER | movement | TABLE_CELL | table/grid | /7of8 | Movimento armonico, forza in aumento | T | Хармонично движение, нарастваща сила | `image-gen-5(9).png` |
| `P108-GA-C038` | 38 | CENTER | movement | TABLE_CELL | table/grid | /8of8 | Andatura potente e fluida | T | Мощна и плавна походка | `image-gen-5(9).png` |
| `P108-GA-C039` | 39 | CENTER | body condition | TABLE_CELL | table/grid | /1of8/1of2 | CONDIZIONE CORPOREA | T | ТЕЛЕСНО СЪСТОЯНИЕ | `image-gen-5(9).png` |
| `P108-GA-C040` | 40 | CENTER | body condition | HEADING_OR_LABEL | table/grid | row label and value | Ideale: 4–5/9 | T | Идеално: 4–5/9 | `image-gen-5(9).png` |
| `P108-GA-C041` | 41 | CENTER | body condition | TABLE_CELL | table/grid | /2of8 | 4/9 | T | 4/9 | `image-gen-5(9).png` |
| `P108-GA-C042` | 42 | CENTER | body condition | TABLE_CELL | table/grid | /3of8 | 4/9 | T | 4/9 | `image-gen-5(9).png` |
| `P108-GA-C043` | 43 | CENTER | body condition | TABLE_CELL | table/grid | /4of8 | 4–5/9 | T | 4–5/9 | `image-gen-5(9).png` |
| `P108-GA-C044` | 44 | CENTER | body condition | TABLE_CELL | table/grid | /5of8 | 4–5/9 | T | 4–5/9 | `image-gen-5(9).png` |
| `P108-GA-C045` | 45 | CENTER | body condition | TABLE_CELL | table/grid | /6of8 | 4–5/9 | T | 4–5/9 | `image-gen-5(9).png` |
| `P108-GA-C046` | 46 | CENTER | body condition | TABLE_CELL | table/grid | /7of8 | 4–5/9 | T | 4–5/9 | `image-gen-5(9).png` |
| `P108-GA-C047` | 47 | CENTER | body condition | TABLE_CELL | table/grid | /8of8 | 4–5/9 | T | 4–5/9 | `image-gen-5(9).png` |
| `P108-GA-C048` | 48 | LOWER_CENTER | lower cards | HEADING_OR_LABEL | named panel/frame | section heading | SEGNALI DA OSSERVARE | T | ПРИЗНАЦИ ЗА НАБЛЮДЕНИЕ | `image-gen-5(9).png` |
| `P108-GA-C049` | 49 | LOWER_CENTER | lower 1 | HEADING_OR_LABEL | named panel/frame | /1of2 | CRESCITA EQUILIBRATA | T | БАЛАНСИРАН РАСТЕЖ | `image-gen-5(9).png` |
| `P108-GA-C050` | 50 | LOWER_CENTER | lower 1 | BODY_TEXT | named panel/frame | /2of2 | Aumento graduale di peso e altezza. Mantieni una crescita armoniosa senza eccessi. | T | Постепенно увеличаване на теглото и височината. Поддържайте хармоничен растеж без крайности. | `image-gen-5(9).png` |
| `P108-GA-C051` | 51 | LOWER_CENTER | lower 2 | HEADING_OR_LABEL | named panel/frame | /1of2 | STRUTTURA CORRETTA | T | ПРАВИЛНА СТРУКТУРА | `image-gen-5(9).png` |
| `P108-GA-C052` | 52 | LOWER_CENTER | lower 2 | BODY_TEXT | named panel/frame | /2of2 | Torace ampio, dorso forte, arti dritti. Le proporzioni devono migliorare con l’età. | T | Широк гръден кош, здрав гръб, прави крайници. Пропорциите трябва да се подобряват с възрастта. | `image-gen-5(9).png` |
| `P108-GA-C053` | 53 | LOWER_CENTER | lower 3 | HEADING_OR_LABEL | named panel/frame | /1of2 | MOVIMENTO NATURALE | T | ЕСТЕСТВЕНО ДВИЖЕНИЕ | `image-gen-5(9).png` |
| `P108-GA-C054` | 54 | LOWER_CENTER | lower 3 | BODY_TEXT | named panel/frame | /2of2 | Passo sciolto, nessuna zoppia o rigidità. Il cane si muove con facilità. | T | Свободна крачка без куцота или скованост. Кучето се движи с лекота. | `image-gen-5(9).png` |
| `P108-GA-C055` | 55 | LOWER_CENTER | lower 4 | HEADING_OR_LABEL | named panel/frame | card heading | MUSCOLATURA IN SVILUPPO | T | РАЗВИВАЩА СЕ МУСКУЛАТУРА | `image-gen-5(9).png` |
| `P108-GA-C056` | 56 | LOWER_CENTER | lower 4 | BODY_TEXT | named panel/frame | card body | Massa muscolare che cresce in modo uniforme, mai troppo né troppo poco. | T | Мускулна маса, която нараства равномерно — нито прекалено много, нито прекалено малко. | `image-gen-5(9).png` |
| `P108-GA-C057` | 57 | LOWER_CENTER | lower 5 | HEADING_OR_LABEL | named panel/frame | /1of2 | ALIMENTAZIONE DI QUALITÀ | T | КАЧЕСТВЕНО ХРАНЕНЕ | `image-gen-5(9).png` |
| `P108-GA-C058` | 58 | LOWER_CENTER | lower 5 | BODY_TEXT | named panel/frame | /2of2 | Dieta bilanciata per sostenere la crescita sana di ossa, muscoli e articolazioni. | T | Балансирана диета за здравословния растеж на костите, мускулите и ставите. | `image-gen-5(9).png` |
| `P108-GA-C059` | 59 | LOWER_CENTER | lower 6 | HEADING_OR_LABEL | named panel/frame | /1of2 | SALUTE COSTANTE | T | ПОСТОЯННА ГРИЖА ЗА ЗДРАВЕТО | `image-gen-5(9).png` |
| `P108-GA-C060` | 60 | LOWER_CENTER | lower 6 | BODY_TEXT | named panel/frame | /2of2 | Controlli regolari, vaccinazioni e sverminazioni secondo il piano veterinario. | T | Редовни прегледи, ваксинации и обезпаразитяване според ветеринарния план. | `image-gen-5(9).png` |
| `P108-GA-C061` | 61 | LOWER_CENTER | bottom box | HEADING_OR_LABEL | named panel/frame | /1of6/label | ATTENZIONE A | T | ВНИМАВАЙТЕ ЗА | `image-gen-5(9).png` |
| `P108-GA-C062` | 62 | LOWER_CENTER | bottom box | WARNING_ITEM | named panel/frame | /1of6/value | Aumento di peso troppo rapido | T | Прекалено бързо наддаване | `image-gen-5(9).png` |
| `P108-GA-C063` | 63 | LOWER_CENTER | bottom box | WARNING_ITEM | named panel/frame | /2of6 | Difficoltà a salire scale o a correre | T | Трудност при изкачване на стълби или тичане | `image-gen-5(9).png` |
| `P108-GA-C064` | 64 | LOWER_CENTER | bottom box | WARNING_ITEM | named panel/frame | /3of6 | Zampe divaricate o andatura rigida | T | Разкрачени лапи или скована походка | `image-gen-5(9).png` |
| `P108-GA-C065` | 65 | LOWER_CENTER | bottom box | WARNING_ITEM | named panel/frame | /4of6 | Dolore al tatto su articolazioni o schiena | T | Болка при допир по ставите или гърба | `image-gen-5(9).png` |
| `P108-GA-C066` | 66 | LOWER_CENTER | bottom box | WARNING_ITEM | named panel/frame | /5of6 | Stanchezza eccessiva durante l’attività | T | Прекомерна умора по време на активност | `image-gen-5(9).png` |
| `P108-GA-C067` | 67 | LOWER_CENTER | bottom box | WARNING_ITEM | named panel/frame | /6of6 | Mancanza di appetito o apatia | T | Липса на апетит или апатия | `image-gen-5(9).png` |
| `P108-GA-C068` | 68 | HEADER | above crest | HEADING_OR_LABEL | top crest | /label | Ogni Cane Corso è unico | T | Всяко Кане Корсо е уникално | `image-gen-5(9).png` |
| `P108-GA-C069` | 69 | HEADER | above crest | FIXED_MARK | top crest | /value | osserva, misura e accompagna la crescita con pazienza e costanza. | T | наблюдавайте, измервайте и подкрепяйте растежа с търпение и постоянство. | `image-gen-5(9).png` |
| `P108-GA-C070` | 70 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-5(9).png` |
| `P108-GA-C071` | 71 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-5(9).png` |
| `P108-GA-C072` | 72 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-5(9).png` |
| `P108-GA-C073` | 73 | LOWER_CENTER | bottom-center medallion | ARTWORK | bottom medallion | bottom medallion artwork |  | G | No source text; preserve medallion artwork. | `image-gen-5(9).png` |
| `P108-GA-C074` | 74 | LOWER_CENTER | inside bottom-center medallion, center | FIXED_MARK | bottom medallion | bottom medallion USG | USG | R | Retain canonical USG mark. | `image-gen-5(9).png` |
| `P108-GA-C075` | 75 | LOWER_CENTER | inside bottom-center medallion, upper perimeter | FIXED_MARK | bottom medallion | bottom medallion upper text | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-5(9).png` |
| `P108-GA-C076` | 76 | LOWER_CENTER | inside bottom-center medallion, lower perimeter | FIXED_MARK | bottom medallion | bottom medallion lower text | CANE CORSO | R | Retain visible canonical seal text. | `image-gen-5(9).png` |
| `P108-GA-C077` | 77 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-5(9).png` |

## PAGE 110 — P110-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-6(7).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title/subtitle; numbered panels 1–6 in visual reading order with central panel after left/right upper groups; callouts; motto and footer.
- V2 range: `P110-GA-C001`–`P110-GA-C057` (57 contiguous IDs)
- Arithmetic: 57 = 48 T + 7 R + 0 N + 2 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P110-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | CRESCITA E ALIMENTAZIONE SICURA | T | БЕЗОПАСЕН РАСТЕЖ И ХРАНЕНЕ | `image-gen-6(7).png` |
| `P110-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | Nutrizione, equilibrio e responsabilità | T | Хранене, баланс и отговорност | `image-gen-6(7).png` |
| `P110-GA-C003` | 3 | CENTER_LEFT | left 1 | HEADING_OR_LABEL | named panel/frame | /1of2 | 1 QUALITÀ DELL’ALIMENTO | T | 1 КАЧЕСТВО НА ХРАНАТА | `image-gen-6(7).png` |
| `P110-GA-C004` | 4 | CENTER_LEFT | left 1 | BODY_TEXT | named panel/frame | /2of2 | Scegli un alimento completo, bilanciato e specifico per cuccioli di taglia grande. Deve contenere ingredienti di alta qualità, proteine animali di valore, grassi buoni, vitamine e minerali in equilibrio. | T | Изберете пълноценна, балансирана храна, предназначена за малки от едри породи. Тя трябва да съдържа висококачествени съставки, ценни животински протеини, полезни мазнини, витамини и минерали в баланс. | `image-gen-6(7).png` |
| `P110-GA-C005` | 5 | CENTER_LEFT | left 1 icons | HEADING_OR_LABEL | adjacent icon | /1of4 | PROTEINE DI QUALITÀ | T | КАЧЕСТВЕНИ ПРОТЕИНИ | `image-gen-6(7).png` |
| `P110-GA-C006` | 6 | CENTER_LEFT | left 1 icons | HEADING_OR_LABEL | adjacent icon | /2of4 | GRASSI BUONI | T | ПОЛЕЗНИ МАЗНИНИ | `image-gen-6(7).png` |
| `P110-GA-C007` | 7 | CENTER_LEFT | left 1 icons | HEADING_OR_LABEL | adjacent icon | /3of4 | VITAMINE E MINERALI | T | ВИТАМИНИ И МИНЕРАЛИ | `image-gen-6(7).png` |
| `P110-GA-C008` | 8 | CENTER_LEFT | left 1 icons | HEADING_OR_LABEL | adjacent icon | /4of4 | EQUILIBRIO COMPLETO | T | ПЪЛЕН БАЛАНС | `image-gen-6(7).png` |
| `P110-GA-C009` | 9 | CENTER_LEFT | left 2 | HEADING_OR_LABEL | named panel/frame | /1of2 | 2 QUANTITÀ | T | 2 КОЛИЧЕСТВО | `image-gen-6(7).png` |
| `P110-GA-C010` | 10 | CENTER_LEFT | left 2 | BODY_TEXT | named panel/frame | /2of2 | Rispetta le dosi consigliate in base al peso, all’età e al livello di attività. Evita gli eccessi: nutrire troppo oggi significa compromettere la salute domani. | T | Спазвайте препоръчаните количества според теглото, възрастта и нивото на активност. Избягвайте излишъка: прекомерното хранене днес застрашава здравето утре. | `image-gen-6(7).png` |
| `P110-GA-C011` | 11 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /1of3 | INDICAZIONI GENERALI GIORNALIERE | T | ОБЩИ ДНЕВНИ НАСОКИ | `image-gen-6(7).png` |
| `P110-GA-C012` | 12 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /2of3 | ETÀ DEL CUCCIOLO / PASTI AL GIORNO | T | ВЪЗРАСТ НА МАЛКОТО / ХРАНЕНИЯ ДНЕВНО | `image-gen-6(7).png` |
| `P110-GA-C013` | 13 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /3of3/1of4 | 2–3 mesi / 4 pasti | T | 2–3 месеца / 4 хранения | `image-gen-6(7).png` |
| `P110-GA-C014` | 14 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /3of3/2of4 | 3–6 mesi / 3 pasti | T | 3–6 месеца / 3 хранения | `image-gen-6(7).png` |
| `P110-GA-C015` | 15 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /3of3/3of4 | 6–12 mesi / 2–3 pasti | T | 6–12 месеца / 2–3 хранения | `image-gen-6(7).png` |
| `P110-GA-C016` | 16 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /3of3/4of4 | 12–18 mesi / 2 pasti | T | 12–18 месеца / 2 хранения | `image-gen-6(7).png` |
| `P110-GA-C017` | 17 | CENTER_LEFT | left 2 | HEADING_OR_LABEL | table/grid | /label | Le quantità variano in base al prodotto | T | Количествата варират според продукта | `image-gen-6(7).png` |
| `P110-GA-C018` | 18 | CENTER_LEFT | left 2 | TABLE_CELL | table/grid | /value | segui sempre le indicazioni del produttore e consulta il tuo allevatore o veterinario. | T | винаги следвайте указанията на производителя и се консултирайте с развъдчика или ветеринарния лекар. | `image-gen-6(7).png` |
| `P110-GA-C019` | 19 | CENTER_RIGHT | right 3 | HEADING_OR_LABEL | named panel/frame | /1of2 | 3 REGOLARITÀ | T | 3 РЕДОВНОСТ | `image-gen-6(7).png` |
| `P110-GA-C020` | 20 | CENTER_RIGHT | right 3 | BODY_TEXT | named panel/frame | /2of2 | Mantieni orari regolari per i pasti e un ambiente tranquillo durante l’alimentazione. La routine favorisce la digestione, il benessere mentale e una crescita serena. | T | Поддържайте редовни часове за хранене и спокойна обстановка. Режимът подпомага храносмилането, психичното благополучие и спокойния растеж. | `image-gen-6(7).png` |
| `P110-GA-C021` | 21 | CENTER_RIGHT | right 3 | CALLOUT | named panel/frame | /1of2 | ACQUA SEMPRE FRESCA | T | ВИНАГИ ПРЯСНА ВОДА | `image-gen-6(7).png` |
| `P110-GA-C022` | 22 | CENTER_RIGHT | right 3 | CALLOUT | named panel/frame | /2of2 | Lascia sempre a disposizione acqua pulita e fresca. | T | Винаги осигурявайте чиста и прясна вода. | `image-gen-6(7).png` |
| `P110-GA-C023` | 23 | CENTER_RIGHT | right 4 | HEADING_OR_LABEL | named panel/frame | /1of2 | 4 RISCHI DELL’ECCESSO | T | 4 РИСКОВЕ ОТ ПРЕКОМЕРНОТО ХРАНЕНЕ | `image-gen-6(7).png` |
| `P110-GA-C024` | 24 | CENTER_RIGHT | right 4 | BODY_TEXT | named panel/frame | /2of2/1of5 | Un’alimentazione sbilanciata o eccessiva può causare problemi seri: Crescita troppo rapida | T | Небалансираното или прекомерно хранене може да причини сериозни проблеми: Прекалено бърз растеж | `image-gen-6(7).png` |
| `P110-GA-C025` | 25 | CENTER_RIGHT | right 4 | BODY_TEXT | named panel/frame | /2of2/2of5 | Sovraccarico articolare e osseo | T | Претоварване на ставите и костите | `image-gen-6(7).png` |
| `P110-GA-C026` | 26 | CENTER_RIGHT | right 4 | BODY_TEXT | named panel/frame | /2of2/3of5 | Displasia e problemi ortopedici | T | Дисплазия и ортопедични проблеми | `image-gen-6(7).png` |
| `P110-GA-C027` | 27 | CENTER_RIGHT | right 4 | BODY_TEXT | named panel/frame | /2of2/4of5 | Obesità e malattie metaboliche | T | Затлъстяване и метаболитни заболявания | `image-gen-6(7).png` |
| `P110-GA-C028` | 28 | CENTER_RIGHT | right 4 | BODY_TEXT | named panel/frame | /2of2/5of5 | Riduzione della longevità | T | Съкращаване на продължителността на живота | `image-gen-6(7).png` |
| `P110-GA-C029` | 29 | CENTER_RIGHT | right 4 | CALLOUT | named panel/frame | /1of2 | MEGLIO POCO E GIUSTO | T | ПО-ДОБРЕ УМЕРЕНО И ПРАВИЛНО | `image-gen-6(7).png` |
| `P110-GA-C030` | 30 | CENTER_RIGHT | right 4 | CALLOUT | named panel/frame | /2of2 | È più importante la qualità e l’equilibrio della quantità. | T | Качеството и балансът са по-важни от количеството. | `image-gen-6(7).png` |
| `P110-GA-C031` | 31 | CENTER_LEFT | left 5 | HEADING_OR_LABEL | named panel/frame | /1of2 | 5 OSSERVAZIONE DEL CANE | T | 5 НАБЛЮДЕНИЕ НА КУЧЕТО | `image-gen-6(7).png` |
| `P110-GA-C032` | 32 | CENTER_LEFT | left 5 | BODY_TEXT | named panel/frame | introductory paragraph | Osserva il tuo cucciolo ogni giorno: il suo corpo racconta molto. | T | Наблюдавайте малкото си всеки ден: тялото му разказва много. | `image-gen-6(7).png` |
| `P110-GA-C033` | 33 | CENTER_LEFT | left 5 | BODY_TEXT | named panel/frame | /2of2/1of4 | Peso e forma corporea adeguati | T | Подходящо тегло и телесна форма | `image-gen-6(7).png` |
| `P110-GA-C034` | 34 | CENTER_LEFT | left 5 | BODY_TEXT | named panel/frame | /2of2/2of4 | Coste facilmente palpabili | T | Лесно напипващи се ребра | `image-gen-6(7).png` |
| `P110-GA-C035` | 35 | CENTER_LEFT | left 5 | BODY_TEXT | named panel/frame | /2of2/3of4 | Addome leggermente raccolto | T | Леко прибран корем | `image-gen-6(7).png` |
| `P110-GA-C036` | 36 | CENTER_LEFT | left 5 | BODY_TEXT | named panel/frame | /2of2/4of4 | Energia, vitalità e pelo sano | T | Енергия, жизненост и здрава козина | `image-gen-6(7).png` |
| `P110-GA-C037` | 37 | CENTER_LEFT | left 5 | CALLOUT | named panel/frame | /1of2 | OGNI CUCCIOLO È UNICO | T | ВСЯКО МАЛКО Е УНИКАЛНО | `image-gen-6(7).png` |
| `P110-GA-C038` | 38 | CENTER_LEFT | left 5 | CALLOUT | named panel/frame | /2of2 | Adatta sempre alimentazione e gestione alle sue esigenze reali. | T | Винаги приспособявайте храненето и грижите към действителните му нужди. | `image-gen-6(7).png` |
| `P110-GA-C039` | 39 | CENTER | center | HEADING_OR_LABEL | named panel/frame | /1of2 | CRESCITA ARMONIOSA | T | ХАРМОНИЧЕН РАСТЕЖ | `image-gen-6(7).png` |
| `P110-GA-C040` | 40 | CENTER | center | BODY_TEXT | named panel/frame | /2of2 | Una crescita corretta è graduale e costante. L’obiettivo non è farlo crescere in fretta, ma farlo crescere bene. Una nutrizione equilibrata sostiene lo sviluppo di ossa forti, muscoli sani e un sistema immunitario solido. | T | Правилният растеж е постепенен и постоянен. Целта не е малкото да расте бързо, а да расте добре. Балансираното хранене подпомага развитието на здрави кости, силни мускули и устойчива имунна система. | `image-gen-6(7).png` |
| `P110-GA-C041` | 41 | CENTER | center icons | HEADING_OR_LABEL | adjacent icon | /1of4 | OSSA FORTI | T | ЗДРАВИ КОСТИ | `image-gen-6(7).png` |
| `P110-GA-C042` | 42 | CENTER | center icons | HEADING_OR_LABEL | adjacent icon | /2of4 | MUSCOLI SANI | T | СИЛНИ МУСКУЛИ | `image-gen-6(7).png` |
| `P110-GA-C043` | 43 | CENTER | center icons | HEADING_OR_LABEL | adjacent icon | /3of4 | DIFESE FORTI | T | СИЛНА ЗАЩИТА | `image-gen-6(7).png` |
| `P110-GA-C044` | 44 | CENTER | center icons | HEADING_OR_LABEL | adjacent icon | /4of4 | BENESSERE COMPLETO | T | ЦЯЛОСТНО БЛАГОПОЛУЧИЕ | `image-gen-6(7).png` |
| `P110-GA-C045` | 45 | CENTER_RIGHT | right 6 | HEADING_OR_LABEL | named panel/frame | /1of2 | 6 RESPONSABILITÀ | T | 6 ОТГОВОРНОСТ | `image-gen-6(7).png` |
| `P110-GA-C046` | 46 | CENTER_RIGHT | right 6 | BODY_TEXT | named panel/frame | /2of2 | Nutrire bene il tuo Cane Corso è un atto d’amore e responsabilità. Significa garantirgli salute, forza e una vita lunga e armoniosa. | T | Доброто хранене на вашето Кане Корсо е проява на любов и отговорност. То означава да му осигурите здраве, сила и дълъг, хармоничен живот. | `image-gen-6(7).png` |
| `P110-GA-C047` | 47 | CENTER_RIGHT | right 6 | CALLOUT | named panel/frame | callout | UN BUON INIZIO È LA BASE DI UN FUTURO ECCEZIONALE | T | ДОБРОТО НАЧАЛО Е ОСНОВАТА НА ИЗКЛЮЧИТЕЛНО БЪДЕЩЕ | `image-gen-6(7).png` |
| `P110-GA-C048` | 48 | FOOTER | bottom | FIXED_MARK | named panel/frame | motto | Alimenta con saggezza, osserva con attenzione, ama con responsabilità. Il tuo Cane Corso crescerà forte, equilibrato e fiero. | T | Хранете разумно, наблюдавайте внимателно, обичайте отговорно. Вашето Кане Корсо ще израсне силно, уравновесено и гордо. | `image-gen-6(7).png` |
| `P110-GA-C049` | 49 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-6(7).png` |
| `P110-GA-C050` | 50 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-6(7).png` |
| `P110-GA-C051` | 51 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-6(7).png` |
| `P110-GA-C052` | 52 | LOWER_CENTER | bottom-center medallion | ARTWORK | bottom medallion | bottom medallion artwork |  | G | No source text; preserve medallion artwork. | `image-gen-6(7).png` |
| `P110-GA-C053` | 53 | LOWER_CENTER | inside bottom-center medallion, center | FIXED_MARK | bottom medallion | bottom medallion USG | USG | R | Retain canonical USG mark. | `image-gen-6(7).png` |
| `P110-GA-C054` | 54 | LOWER_CENTER | inside bottom-center medallion, upper perimeter | FIXED_MARK | bottom medallion | bottom medallion upper text | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-6(7).png` |
| `P110-GA-C055` | 55 | LOWER_CENTER | inside bottom-center medallion, lower perimeter | FIXED_MARK | bottom medallion | bottom medallion lower text | CANE CORSO | R | Retain visible canonical seal text. | `image-gen-6(7).png` |
| `P110-GA-C056` | 56 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-6(7).png` |
| `P110-GA-C057` | 57 | CENTER | central puppy feeding illustration | FIXED_MARK | food bowl | inside bowl face | USG | R | Retain visible canonical USG mark. | `image-gen-6(7).png` |

## PAGE 113 — P113-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-7(4).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title/subtitle; internal and external parasite panels top-to-bottom; lower control, environment and veterinarian panels left-to-right; prevention line and footer.
- V2 range: `P113-GA-C001`–`P113-GA-C057` (57 contiguous IDs)
- Arithmetic: 57 = 49 T + 6 R + 0 N + 2 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P113-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | CONTROLLO DEI PARASSITI | T | КОНТРОЛ НА ПАРАЗИТИТЕ | `image-gen-7(4).png` |
| `P113-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | Prevenzione, sverminazione e ambiente | T | Превенция, обезпаразитяване и среда | `image-gen-7(4).png` |
| `P113-GA-C003` | 3 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of2 | PARASSITI INTERNI | T | ВЪТРЕШНИ ПАРАЗИТИ | `image-gen-7(4).png` |
| `P113-GA-C004` | 4 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /2of2 | I più comuni e i rischi principali. | T | Най-често срещаните и основните рискове. | `image-gen-7(4).png` |
| `P113-GA-C005` | 5 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of2 | ASCARIDI | T | АСКАРИДИ | `image-gen-7(4).png` |
| `P113-GA-C006` | 6 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /2of2 | Vermi intestinali che possono causare problemi digestivi e crescita rallentata. | T | Чревни червеи, които могат да причинят храносмилателни проблеми и забавен растеж. | `image-gen-7(4).png` |
| `P113-GA-C007` | 7 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of2 | ANCHILOSTOMI | T | АНКИЛОСТОМИ | `image-gen-7(4).png` |
| `P113-GA-C008` | 8 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /2of2 | Si nutrono di sangue e possono causare anemia e debolezza. | T | Хранят се с кръв и могат да причинят анемия и слабост. | `image-gen-7(4).png` |
| `P113-GA-C009` | 9 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of2 | TENIE | T | ТЕНИИ | `image-gen-7(4).png` |
| `P113-GA-C010` | 10 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /2of2 | Possono provocare disturbi intestinali e perdita di peso. | T | Могат да причинят чревни разстройства и загуба на тегло. | `image-gen-7(4).png` |
| `P113-GA-C011` | 11 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of2 | GIARDIA | T | ГИАРДИЯ | `image-gen-7(4).png` |
| `P113-GA-C012` | 12 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /2of2 | Protozoo che causa diarrea e cattivo assorbimento. | T | Протозой, който причинява диария и нарушено усвояване. | `image-gen-7(4).png` |
| `P113-GA-C013` | 13 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | PARASSITI ESTERNI | T | ВЪНШНИ ПАРАЗИТИ | `image-gen-7(4).png` |
| `P113-GA-C014` | 14 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /2of2 | Proteggi la pelle e il benessere del tuo Cane Corso. | T | Защитете кожата и благополучието на своето Кане Корсо. | `image-gen-7(4).png` |
| `P113-GA-C015` | 15 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | PULCI | T | БЪЛХИ | `image-gen-7(4).png` |
| `P113-GA-C016` | 16 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /2of2 | Causano prurito, allergie e possono trasmettere tenie. | T | Причиняват сърбеж и алергии и могат да пренасят тении. | `image-gen-7(4).png` |
| `P113-GA-C017` | 17 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | ZECCHE | T | КЪРЛЕЖИ | `image-gen-7(4).png` |
| `P113-GA-C018` | 18 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /2of2 | Possono trasmettere malattie gravi come ehrlichiosi e babesiosi. | T | Могат да пренасят сериозни заболявания като ерлихиоза и бабезиоза. | `image-gen-7(4).png` |
| `P113-GA-C019` | 19 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | ACARI DELLA ROGNA | T | КРАСТНИ АКАРИ | `image-gen-7(4).png` |
| `P113-GA-C020` | 20 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /2of2 | Provocano prurito intenso, lesioni cutanee e perdita di pelo. | T | Причиняват силен сърбеж, кожни лезии и загуба на козина. | `image-gen-7(4).png` |
| `P113-GA-C021` | 21 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | ZANZARE E PAPPATACI | T | КОМАРИ И ФЛЕБОТОМИ | `image-gen-7(4).png` |
| `P113-GA-C022` | 22 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /2of2 | Possono trasmettere filariosi e leishmaniosi. | T | Могат да пренасят дирофилариоза и лайшманиоза. | `image-gen-7(4).png` |
| `P113-GA-C023` | 23 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | CONTROLLO PERIODICO | T | ПЕРИОДИЧЕН КОНТРОЛ | `image-gen-7(4).png` |
| `P113-GA-C024` | 24 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | La costanza è la miglior protezione. | T | Постоянството е най-добрата защита. | `image-gen-7(4).png` |
| `P113-GA-C025` | 25 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | VERMIFUGO REGOLARE | T | РЕДОВНО ОБЕЗПАРАЗИТЯВАНЕ | `image-gen-7(4).png` |
| `P113-GA-C026` | 26 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Segui un piano di sverminazione adatto all’età, allo stile di vita e al territorio. | T | Следвайте план за обезпаразитяване, съобразен с възрастта, начина на живот и района. | `image-gen-7(4).png` |
| `P113-GA-C027` | 27 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | ANTIPARASSITARI ADEGUATI | T | ПОДХОДЯЩИ ПРОТИВОПАРАЗИТНИ СРЕДСТВА | `image-gen-7(4).png` |
| `P113-GA-C028` | 28 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Usa prodotti specifici consigliati dal veterinario per la prevenzione di pulci, zecche e altri parassiti. | T | Използвайте конкретни продукти, препоръчани от ветеринарния лекар за превенция на бълхи, кърлежи и други паразити. | `image-gen-7(4).png` |
| `P113-GA-C029` | 29 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | OSSERVA IL TUO CANE | T | НАБЛЮДАВАЙТЕ КУЧЕТО | `image-gen-7(4).png` |
| `P113-GA-C030` | 30 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Controlla regolarmente pelle, mantello, feci e comportamento. Ogni cambiamento può essere un segnale. | T | Проверявайте редовно кожата, козината, изпражненията и поведението. Всяка промяна може да бъде признак. | `image-gen-7(4).png` |
| `P113-GA-C031` | 31 | LOWER_CENTER | lower center | HEADING_OR_LABEL | named panel/frame | /1of2 | GESTIONE DELL’AMBIENTE | T | ПОДДЪРЖАНЕ НА СРЕДАТА | `image-gen-7(4).png` |
| `P113-GA-C032` | 32 | LOWER_CENTER | lower center | BODY_TEXT | named panel/frame | /2of2 | Un ambiente pulito riduce il rischio. | T | Чистата среда намалява риска. | `image-gen-7(4).png` |
| `P113-GA-C033` | 33 | LOWER_CENTER | lower center | HEADING_OR_LABEL | named panel/frame | /1of2 | PULIZIA REGOLARE | T | РЕДОВНО ПОЧИСТВАНЕ | `image-gen-7(4).png` |
| `P113-GA-C034` | 34 | LOWER_CENTER | lower center | BODY_TEXT | named panel/frame | /2of2 | Lava cucce, coperte e tappeti con frequenza. | T | Перете често леглата, одеялата и килимите. | `image-gen-7(4).png` |
| `P113-GA-C035` | 35 | LOWER_CENTER | lower center | HEADING_OR_LABEL | named panel/frame | /1of2 | ASPIRAZIONE FREQUENTE | T | ЧЕСТО ПОЧИСТВАНЕ С ПРАХОСМУКАЧКА | `image-gen-7(4).png` |
| `P113-GA-C036` | 36 | LOWER_CENTER | lower center | BODY_TEXT | named panel/frame | /2of2 | Rimuovi peli, uova di pulci e polvere da pavimenti, divani e tappeti. | T | Отстранявайте козина, яйца на бълхи и прах от подове, дивани и килими. | `image-gen-7(4).png` |
| `P113-GA-C037` | 37 | LOWER_CENTER | lower center | HEADING_OR_LABEL | named panel/frame | /1of2 | ELIMINA I PARASSITI NELL’AMBIENTE | T | ПРЕМАХВАЙТЕ ПАРАЗИТИТЕ ОТ СРЕДАТА | `image-gen-7(4).png` |
| `P113-GA-C038` | 38 | LOWER_CENTER | lower center | BODY_TEXT | named panel/frame | /2of2 | Utilizza prodotti specifici sicuri per eliminare uova e larve. | T | Използвайте специални безопасни продукти за унищожаване на яйца и ларви. | `image-gen-7(4).png` |
| `P113-GA-C039` | 39 | LOWER_CENTER | lower center | HEADING_OR_LABEL | named panel/frame | /1of2 | GESTISCI GLI SPAZI ESTERNI | T | ПОДДЪРЖАЙТЕ ВЪНШНИТЕ ПРОСТРАНСТВА | `image-gen-7(4).png` |
| `P113-GA-C040` | 40 | LOWER_CENTER | lower center | BODY_TEXT | named panel/frame | /2of2 | Taglia l’erba, elimina ristagni d’acqua e tieni pulite le aree di riposo. | T | Косете тревата, премахвайте застоялата вода и поддържайте чисти местата за почивка. | `image-gen-7(4).png` |
| `P113-GA-C041` | 41 | LOWER_RIGHT | lower right | HEADING_OR_LABEL | named panel/frame | /1of2 | QUANDO SERVE IL VETERINARIO | T | КОГА Е НЕОБХОДИМ ВЕТЕРИНАР | `image-gen-7(4).png` |
| `P113-GA-C042` | 42 | LOWER_RIGHT | lower right | HEADING_OR_LABEL | named panel/frame | /2of2/label | Non aspettare | T | Не чакайте | `image-gen-7(4).png` |
| `P113-GA-C043` | 43 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/value | agire presto fa la differenza. | T | ранната реакция има значение. | `image-gen-7(4).png` |
| `P113-GA-C044` | 44 | LOWER_RIGHT | lower right | WARNING_ITEM | named panel/frame | body/item1of5 | Diarrea, vomito o perdita di peso inspiegabile. | T | Необяснима диария, повръщане или загуба на тегло. | `image-gen-7(4).png` |
| `P113-GA-C045` | 45 | LOWER_RIGHT | lower right | WARNING_ITEM | named panel/frame | body/item2of5 | Pelo spento, prurito, arrossamenti o ferite sulla pelle. | T | Безжизнена козина, сърбеж, зачервяване или рани по кожата. | `image-gen-7(4).png` |
| `P113-GA-C046` | 46 | LOWER_RIGHT | lower right | WARNING_ITEM | named panel/frame | body/item3of5 | Presenza di pulci, zecche o parassiti visibili. | T | Наличие на видими бълхи, кърлежи или паразити. | `image-gen-7(4).png` |
| `P113-GA-C047` | 47 | LOWER_RIGHT | lower right | WARNING_ITEM | named panel/frame | body/item4of5 | Stanchezza, tosse o difficoltà respiratorie. | T | Умора, кашлица или затруднено дишане. | `image-gen-7(4).png` |
| `P113-GA-C048` | 48 | LOWER_RIGHT | lower right | WARNING_ITEM | named panel/frame | body/item5of5 | Dopo viaggi o contatti con altri animali. | T | След пътуване или контакт с други животни. | `image-gen-7(4).png` |
| `P113-GA-C049` | 49 | LOWER_CENTER | bottom box | FIXED_MARK | named panel/frame | motto | La prevenzione è il gesto più importante per la salute del tuo Cane Corso. Un controllo regolare protegge oggi e previene problemi domani. | T | Превенцията е най-важната грижа за здравето на вашето Кане Корсо. Редовният контрол предпазва днес и предотвратява проблеми утре. | `image-gen-7(4).png` |
| `P113-GA-C050` | 50 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-7(4).png` |
| `P113-GA-C051` | 51 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-7(4).png` |
| `P113-GA-C052` | 52 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-7(4).png` |
| `P113-GA-C053` | 53 | LOWER_CENTER | bottom-center medallion | ARTWORK | bottom medallion | bottom medallion artwork |  | G | No source text; preserve medallion artwork. | `image-gen-7(4).png` |
| `P113-GA-C054` | 54 | LOWER_CENTER | inside bottom-center medallion, center | FIXED_MARK | bottom medallion | bottom medallion USG | USG | R | Retain canonical USG mark. | `image-gen-7(4).png` |
| `P113-GA-C055` | 55 | LOWER_CENTER | inside bottom-center medallion, upper perimeter | FIXED_MARK | bottom medallion | bottom medallion upper text | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-7(4).png` |
| `P113-GA-C056` | 56 | LOWER_CENTER | inside bottom-center medallion, lower perimeter | FIXED_MARK | bottom medallion | bottom medallion lower text | CANE CORSO | R | Retain visible canonical seal text. | `image-gen-7(4).png` |
| `P113-GA-C057` | 57 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-7(4).png` |

## PAGE 116 — P116-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-8(4).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title/subtitle; anatomy panels left-to-right; summary; care panels left-to-right; alteration signs; veterinarian panel; motto and footer.
- V2 range: `P116-GA-C001`–`P116-GA-C059` (59 contiguous IDs)
- Arithmetic: 59 = 55 T + 3 R + 0 N + 1 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P116-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | CURA DI PELLE E MANTELLO | T | ГРИЖА ЗА КОЖАТА И КОЗИНАТА | `image-gen-8(4).png` |
| `P116-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | Segnali, equilibrio e osservazione | T | Признаци, баланс и наблюдение | `image-gen-8(4).png` |
| `P116-GA-C003` | 3 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | section | ANATOMIA DELLA PELLE E DEL MANTELLO | T | АНАТОМИЯ НА КОЖАТА И КОЗИНАТА | `image-gen-8(4).png` |
| `P116-GA-C004` | 4 | UPPER_LEFT | upper left 1 | HEADING_OR_LABEL | diagram | /1of2 | PELLE | T | КОЖА | `image-gen-8(4).png` |
| `P116-GA-C005` | 5 | UPPER_LEFT | upper left 1 | BODY_TEXT | diagram | /2of2 | La pelle è la base della salute del mantello. Protegge, regola la temperatura e ospita il follicolo pilifero. | T | Кожата е основата на здравата козина. Тя защитава, регулира температурата и съдържа космения фоликул. | `image-gen-8(4).png` |
| `P116-GA-C006` | 6 | UPPER_LEFT | upper left 2 | HEADING_OR_LABEL | diagram | /1of2 | PELO DI COPERTURA | T | ПОКРИВЕН КОСЪМ | `image-gen-8(4).png` |
| `P116-GA-C007` | 7 | UPPER_LEFT | upper left 2 | BODY_TEXT | diagram | /2of2 | Corto, fitto e lucente, protegge la pelle dagli agenti esterni e dona aspetto sano e uniforme. | T | Къс, гъст и лъскав, предпазва кожата от външни въздействия и придава здрав и равномерен вид. | `image-gen-8(4).png` |
| `P116-GA-C008` | 8 | UPPER_LEFT | upper left 3 | HEADING_OR_LABEL | diagram | /1of2 | SOTTOPELO | T | ПОДКОСЪМ | `image-gen-8(4).png` |
| `P116-GA-C009` | 9 | UPPER_LEFT | upper left 3 | BODY_TEXT | diagram | /2of2 | Morbido e denso, regola l’isolamento termico e si rinnova in modo stagionale. | T | Мек и гъст, регулира топлоизолацията и се обновява сезонно. | `image-gen-8(4).png` |
| `P116-GA-C010` | 10 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of2 | SINTESI | T | ОБОБЩЕНИЕ | `image-gen-8(4).png` |
| `P116-GA-C011` | 11 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /2of2 | Una pelle sana e un mantello equilibrato riflettono benessere interno, corretta gestione e attenzione costante. | T | Здравата кожа и балансираната козина отразяват вътрешното благополучие, правилните грижи и постоянното внимание. | `image-gen-8(4).png` |
| `P116-GA-C012` | 12 | CENTER | middle 1 | HEADING_OR_LABEL | named panel/frame | /1of2 | IGIENE | T | ХИГИЕНА | `image-gen-8(4).png` |
| `P116-GA-C013` | 13 | CENTER | middle 1 | BODY_TEXT | named panel/frame | /2of2/item1of4 | Spazzola regolarmente con strumenti adatti per rimuovere pelo morto e impurità. | T | Разресвайте редовно с подходящи инструменти, за да премахвате мъртвата козина и замърсяванията. | `image-gen-8(4).png` |
| `P116-GA-C014` | 14 | CENTER | middle 1 | BODY_TEXT | named panel/frame | /2of2/item2of4 | Bagni solo quando necessari, usando shampoo delicati specifici per cani. | T | Къпете само при необходимост с нежен шампоан за кучета. | `image-gen-8(4).png` |
| `P116-GA-C015` | 15 | CENTER | middle 1 | BODY_TEXT | named panel/frame | /2of2/item3of4 | Asciuga bene, soprattutto nelle pieghe cutanee. | T | Подсушавайте добре, особено кожните гънки. | `image-gen-8(4).png` |
| `P116-GA-C016` | 16 | CENTER | middle 1 | BODY_TEXT | named panel/frame | /2of2/item4of4 | Controlla frequentemente orecchie, pieghe e zampe. | T | Проверявайте често ушите, гънките и лапите. | `image-gen-8(4).png` |
| `P116-GA-C017` | 17 | CENTER | middle 2 | HEADING_OR_LABEL | named panel/frame | /1of2 | NUTRIZIONE | T | ХРАНЕНЕ | `image-gen-8(4).png` |
| `P116-GA-C018` | 18 | CENTER | middle 2 | BODY_TEXT | named panel/frame | /2of2/item1of4 | Alimentazione completa e bilanciata, ricca di proteine di alta qualità. | T | Пълноценно и балансирано хранене, богато на висококачествени протеини. | `image-gen-8(4).png` |
| `P116-GA-C019` | 19 | CENTER | middle 2 | BODY_TEXT | named panel/frame | /2of2/item2of4 | Acidi grassi Omega-3 (EPA e DHA) per sostenere la pelle e la lucentezza del mantello. | T | Омега-3 мастни киселини (EPA и DHA) за подкрепа на кожата и блясъка на козината. | `image-gen-8(4).png` |
| `P116-GA-C020` | 20 | CENTER | middle 2 | BODY_TEXT | named panel/frame | /2of2/item3of4 | Vitamine A, E, biotina e zinco per la salute della cute e del pelo. | T | Витамини A и E, биотин и цинк за здравето на кожата и косъма. | `image-gen-8(4).png` |
| `P116-GA-C021` | 21 | CENTER | middle 2 | BODY_TEXT | named panel/frame | /2of2/item4of4 | Acqua sempre fresca e pulita a disposizione. | T | Постоянен достъп до прясна и чиста вода. | `image-gen-8(4).png` |
| `P116-GA-C022` | 22 | CENTER | middle 3 | HEADING_OR_LABEL | named panel/frame | /1of2 | AMBIENTE E STILE DI VITA | T | СРЕДА И НАЧИН НА ЖИВОТ | `image-gen-8(4).png` |
| `P116-GA-C023` | 23 | CENTER | middle 3 | BODY_TEXT | named panel/frame | /2of2/item1of3 | Mantieni un ambiente pulito, asciutto e ben ventilato. | T | Поддържайте чиста, суха и добре проветрена среда. | `image-gen-8(4).png` |
| `P116-GA-C024` | 24 | CENTER | middle 3 | BODY_TEXT | named panel/frame | /2of2/item2of3 | Evita l’esposizione prolungata a sole intenso e umidità. | T | Избягвайте продължително излагане на силно слънце и влага. | `image-gen-8(4).png` |
| `P116-GA-C025` | 25 | CENTER | middle 3 | BODY_TEXT | named panel/frame | /2of2/item3of3 | Attività fisica regolare e gestione dello stress favoriscono l’equilibrio generale. | T | Редовната физическа активност и управлението на стреса подпомагат общия баланс. | `image-gen-8(4).png` |
| `P116-GA-C026` | 26 | CENTER | middle 4 | HEADING_OR_LABEL | named panel/frame | /1of2 | CURA STAGIONALE DEL SOTTOPELO | T | СЕЗОННА ГРИЖА ЗА ПОДКОСЪМА | `image-gen-8(4).png` |
| `P116-GA-C027` | 27 | CENTER | middle 4 | BODY_TEXT | named panel/frame | /2of2/item1of3 | Nei periodi di muta, spazzola più spesso per rimuovere il pelo morto. | T | По време на линеене разресвайте по-често, за да премахвате мъртвата козина. | `image-gen-8(4).png` |
| `P116-GA-C028` | 28 | CENTER | middle 4 | BODY_TEXT | named panel/frame | /2of2/item2of3 | Non radere il mantello: compromette la protezione naturale della pelle. | T | Не бръснете козината: това нарушава естествената защита на кожата. | `image-gen-8(4).png` |
| `P116-GA-C029` | 29 | CENTER | middle 4 | BODY_TEXT | named panel/frame | /2of2/item3of3 | Una corretta spazzolatura stimola la circolazione e mantiene il mantello sano e compatto. | T | Правилното разресване стимулира кръвообращението и поддържа козината здрава и плътна. | `image-gen-8(4).png` |
| `P116-GA-C030` | 30 | CENTER | middle 5 | HEADING_OR_LABEL | named panel/frame | /1of2 | CONTROLLO COSTANTE | T | ПОСТОЯНЕН КОНТРОЛ | `image-gen-8(4).png` |
| `P116-GA-C031` | 31 | CENTER | middle 5 | BODY_TEXT | named panel/frame | /2of2/item1of3 | Osserva regolarmente pelle e mantello. | T | Наблюдавайте редовно кожата и козината. | `image-gen-8(4).png` |
| `P116-GA-C032` | 32 | CENTER | middle 5 | BODY_TEXT | named panel/frame | /2of2/item2of3 | Intervieni subito in caso di alterazioni. | T | Реагирайте веднага при промени. | `image-gen-8(4).png` |
| `P116-GA-C033` | 33 | CENTER | middle 5 | BODY_TEXT | named panel/frame | /2of2/item3of3 | La prevenzione è la chiave per evitare problemi e favorire il benessere del Cane Corso. | T | Превенцията е ключът към избягването на проблеми и благополучието на Кане Корсо. | `image-gen-8(4).png` |
| `P116-GA-C034` | 34 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | section | SEGNALI COMUNI DI ALTERAZIONE | T | ЧЕСТИ ПРИЗНАЦИ НА ПРОМЯНА | `image-gen-8(4).png` |
| `P116-GA-C035` | 35 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | PRURITO ECCESSIVO | T | ПРЕКОМЕРЕН СЪРБЕЖ | `image-gen-8(4).png` |
| `P116-GA-C036` | 36 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Si gratta spesso, si morde o si lecca con insistenza. | T | Често се чеше, хапе се или се ближе настойчиво. | `image-gen-8(4).png` |
| `P116-GA-C037` | 37 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | ARROSSAMENTI | T | ЗАЧЕРВЯВАНЕ | `image-gen-8(4).png` |
| `P116-GA-C038` | 38 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Pelle arrossata, irritata o infiammata. | T | Зачервена, раздразнена или възпалена кожа. | `image-gen-8(4).png` |
| `P116-GA-C039` | 39 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | CADUTA DI PELO | T | КОСОПАД | `image-gen-8(4).png` |
| `P116-GA-C040` | 40 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Diradamento localizzato o perdita anomala di pelo. | T | Локално оредяване или необичайна загуба на козина. | `image-gen-8(4).png` |
| `P116-GA-C041` | 41 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | FORFORA E PELLE SECCA | T | ПЪРХОТ И СУХА КОЖА | `image-gen-8(4).png` |
| `P116-GA-C042` | 42 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Desquamazione, pelle secca e pruriginosa. | T | Лющене, суха и сърбяща кожа. | `image-gen-8(4).png` |
| `P116-GA-C043` | 43 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | ODORE SGRADEVOLE | T | НЕПРИЯТНА МИРИЗМА | `image-gen-8(4).png` |
| `P116-GA-C044` | 44 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Odore intenso o persistente, anche dopo il bagno. | T | Силна или постоянна миризма, включително след къпане. | `image-gen-8(4).png` |
| `P116-GA-C045` | 45 | LOWER_LEFT | lower left | HEADING_OR_LABEL | named panel/frame | /1of2 | ZONE UMIDE O LESIONI | T | ВЛАЖНИ ЗОНИ ИЛИ ЛЕЗИИ | `image-gen-8(4).png` |
| `P116-GA-C046` | 46 | LOWER_LEFT | lower left | BODY_TEXT | named panel/frame | /2of2 | Aree umide, croste, ferite o lesioni cutanee. | T | Влажни участъци, корички, рани или кожни лезии. | `image-gen-8(4).png` |
| `P116-GA-C047` | 47 | LOWER_RIGHT | lower right | HEADING_OR_LABEL | named panel/frame | /1of2 | QUANDO RIVOLGERSI AL VETERINARIO | T | КОГА ДА СЕ ОБЪРНЕТЕ КЪМ ВЕТЕРИНАР | `image-gen-8(4).png` |
| `P116-GA-C048` | 48 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item1of7 | Prurito persistente o autotraumatismo. | T | Постоянен сърбеж или самонараняване. | `image-gen-8(4).png` |
| `P116-GA-C049` | 49 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item2of7 | Lesioni, arrossamenti o infezioni ricorrenti. | T | Повтарящи се лезии, зачервявания или инфекции. | `image-gen-8(4).png` |
| `P116-GA-C050` | 50 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item3of7 | Caduta di pelo eccessiva o improvvisa. | T | Прекомерна или внезапна загуба на козина. | `image-gen-8(4).png` |
| `P116-GA-C051` | 51 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item4of7 | Odore intenso non associato a sporco. | T | Силна миризма, несвързана със замърсяване. | `image-gen-8(4).png` |
| `P116-GA-C052` | 52 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item5of7 | Cambiamenti improvvisi nella pelle o nel mantello. | T | Внезапни промени в кожата или козината. | `image-gen-8(4).png` |
| `P116-GA-C053` | 53 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item6of7 | Sintomi generali: letargia, perdita di appetito, dimagrimento. | T | Общи симптоми: летаргия, загуба на апетит, отслабване. | `image-gen-8(4).png` |
| `P116-GA-C054` | 54 | LOWER_RIGHT | lower right | BODY_TEXT | named panel/frame | /2of2/item7of7 | Una diagnosi tempestiva previene complicazioni e tutela la salute del tuo Cane Corso. | T | Навременната диагноза предотвратява усложнения и защитава здравето на вашето Кане Корсо. | `image-gen-8(4).png` |
| `P116-GA-C055` | 55 | FOOTER | bottom | FIXED_MARK | named panel/frame | motto | Osserva, previeni, rispetta. La bellezza del Cane Corso nasce da equilibrio e attenzione quotidiana. | T | Наблюдавайте, предотвратявайте, уважавайте. Красотата на Кане Корсо се ражда от баланса и ежедневната грижа. | `image-gen-8(4).png` |
| `P116-GA-C056` | 56 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-8(4).png` |
| `P116-GA-C057` | 57 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-8(4).png` |
| `P116-GA-C058` | 58 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-8(4).png` |
| `P116-GA-C059` | 59 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-8(4).png` |

## PAGE 117 — P117-GA

- Native source: `references/source_text/p1_sf03_native_source_assets/BG04_P1_SF03_NATIVE_SOURCE_ASSETS/image-gen-9(4).png`
- Correspondence: **SCALED_NATIVE**
- Reading-order rule: Title/subtitle; six cause panels in two rows left-to-right; warning-sign strip left-to-right; reminder; crest/footer.
- V2 range: `P117-GA-C001`–`P117-GA-C065` (65 contiguous IDs)
- Arithmetic: 65 = 57 T + 6 R + 0 N + 2 G + 0 U

| Canonical ID | READING_ORDER | REGION | PANEL | ELEMENT_ROLE | ASSOCIATED_VISUAL | RELATIVE_POSITION | Exact Italian source | Class | Bulgarian target / rationale | Source |
|---|---:|---|---|---|---|---|---|:---:|---|---|
| `P117-GA-C001` | 1 | HEADER | top | TITLE | named panel/frame | main title | CAUSE E SEGNALI DI PELLE E MANTELLO | T | ПРИЧИНИ И ПРИЗНАЦИ, СВЪРЗАНИ С КОЖАТА И КОЗИНАТА | `image-gen-9(4).png` |
| `P117-GA-C002` | 2 | HEADER | below title | TITLE | named panel/frame | subtitle | PRURITO, PARASSITI, ALIMENTAZIONE E AMBIENTE | T | СЪРБЕЖ, ПАРАЗИТИ, ХРАНЕНЕ И СРЕДА | `image-gen-9(4).png` |
| `P117-GA-C003` | 3 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | /1of3 | PARASSITI | T | ПАРАЗИТИ | `image-gen-9(4).png` |
| `P117-GA-C004` | 4 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | panel body | Pulci, zecche, acari (sarcoptes, demodex) e pidocchi possono causare forte prurito, arrossamento, croste e perdita di pelo. | T | Бълхи, кърлежи, акари (Sarcoptes, Demodex) и въшки могат да причинят силен сърбеж, зачервяване, корички и загуба на козина. | `image-gen-9(4).png` |
| `P117-GA-C005` | 5 | UPPER_LEFT | upper left | HEADING_OR_LABEL | named panel/frame | secondary heading | FATTORI DI RISCHIO | T | РИСКОВИ ФАКТОРИ | `image-gen-9(4).png` |
| `P117-GA-C006` | 6 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /3of3/1of3 | Contatti con altri animali | T | Контакт с други животни | `image-gen-9(4).png` |
| `P117-GA-C007` | 7 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /3of3/2of3 | Ambienti infestati | T | Заразена среда | `image-gen-9(4).png` |
| `P117-GA-C008` | 8 | UPPER_LEFT | upper left | BODY_TEXT | named panel/frame | /3of3/3of3 | Assenza di prevenzione stagionale | T | Липса на сезонна профилактика | `image-gen-9(4).png` |
| `P117-GA-C009` | 9 | CENTER | upper center | HEADING_OR_LABEL | named panel/frame | /1of3 | INFIAMMAZIONE | T | ВЪЗПАЛЕНИЕ | `image-gen-9(4).png` |
| `P117-GA-C010` | 10 | CENTER | upper center | BODY_TEXT | named panel/frame | panel body | Allergie a pollini, acari, muffe, prodotti chimici o contatto possono provocare dermatiti atopiche o da contatto, con prurito e lesioni. | T | Алергии към полени, акари, плесени, химически продукти или контакт могат да причинят атопичен или контактен дерматит със сърбеж и лезии. | `image-gen-9(4).png` |
| `P117-GA-C011` | 11 | CENTER | upper center | HEADING_OR_LABEL | named panel/frame | secondary heading | SEGNI TIPICI | T | ТИПИЧНИ ПРИЗНАЦИ | `image-gen-9(4).png` |
| `P117-GA-C012` | 12 | CENTER | upper center | BODY_TEXT | named panel/frame | /3of3/1of4 | Arrossamento | T | Зачервяване | `image-gen-9(4).png` |
| `P117-GA-C013` | 13 | CENTER | upper center | BODY_TEXT | named panel/frame | /3of3/2of4 | Leccamento e sfregamento | T | Близане и триене | `image-gen-9(4).png` |
| `P117-GA-C014` | 14 | CENTER | upper center | BODY_TEXT | named panel/frame | /3of3/3of4 | Otiti ricorrenti | T | Повтарящи се отити | `image-gen-9(4).png` |
| `P117-GA-C015` | 15 | CENTER | upper center | BODY_TEXT | named panel/frame | /3of3/4of4 | Infezioni secondarie | T | Вторични инфекции | `image-gen-9(4).png` |
| `P117-GA-C016` | 16 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | /1of3 | SQUILIBRI ALIMENTARI | T | ХРАНИТЕЛНИ ДИСБАЛАНСИ | `image-gen-9(4).png` |
| `P117-GA-C017` | 17 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | panel body | Diete povere di nutrienti essenziali o intolleranze possono causare pelle secca, forfora, pelo opaco e caduta eccessiva. | T | Диети, бедни на основни хранителни вещества, или непоносимости могат да причинят суха кожа, пърхот, безжизнена козина и прекомерен косопад. | `image-gen-9(4).png` |
| `P117-GA-C018` | 18 | UPPER_RIGHT | upper right | HEADING_OR_LABEL | named panel/frame | secondary heading | DA CONTROLLARE | T | ДА СЕ ПРОВЕРЯВА | `image-gen-9(4).png` |
| `P117-GA-C019` | 19 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /3of3/1of4 | Proteine di qualità | T | Качествени протеини | `image-gen-9(4).png` |
| `P117-GA-C020` | 20 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /3of3/2of4 | Acidi grassi Omega 3 e 6 | T | Омега-3 и омега-6 мастни киселини | `image-gen-9(4).png` |
| `P117-GA-C021` | 21 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /3of3/3of4 | Vitamine e minerali | T | Витамини и минерали | `image-gen-9(4).png` |
| `P117-GA-C022` | 22 | UPPER_RIGHT | upper right | BODY_TEXT | named panel/frame | /3of3/4of4 | Idratazione adeguata | T | Подходяща хидратация | `image-gen-9(4).png` |
| `P117-GA-C023` | 23 | CENTER_LEFT | middle left | HEADING_OR_LABEL | named panel/frame | /1of3 | PROBLEMI ENDOCRINI | T | ЕНДОКРИННИ ПРОБЛЕМИ | `image-gen-9(4).png` |
| `P117-GA-C024` | 24 | CENTER_LEFT | middle left | BODY_TEXT | named panel/frame | panel body | Ipotiroidismo, sindrome di Cushing e alterazioni ormonali possono compromettere la pelle e il mantello, riducendo la naturale protezione cutanea. | T | Хипотиреоидизмът, синдромът на Кушинг и хормоналните нарушения могат да увредят кожата и козината, като намалят естествената кожна защита. | `image-gen-9(4).png` |
| `P117-GA-C025` | 25 | CENTER_LEFT | middle left | HEADING_OR_LABEL | named panel/frame | secondary heading | INDIZI COMUNI | T | ЧЕСТИ ПРИЗНАЦИ | `image-gen-9(4).png` |
| `P117-GA-C026` | 26 | CENTER_LEFT | middle left | BODY_TEXT | named panel/frame | /3of3/1of4 | Pelo diradato e opaco | T | Оредяла и безжизнена козина | `image-gen-9(4).png` |
| `P117-GA-C027` | 27 | CENTER_LEFT | middle left | BODY_TEXT | named panel/frame | /3of3/2of4 | Cute ispessita o sottile | T | Удебелена или изтънена кожа | `image-gen-9(4).png` |
| `P117-GA-C028` | 28 | CENTER_LEFT | middle left | BODY_TEXT | named panel/frame | /3of3/3of4 | Intolleranza al freddo | T | Непоносимост към студ | `image-gen-9(4).png` |
| `P117-GA-C029` | 29 | CENTER_LEFT | middle left | BODY_TEXT | named panel/frame | /3of3/4of4 | Aumento di peso | T | Наддаване на тегло | `image-gen-9(4).png` |
| `P117-GA-C030` | 30 | CENTER | middle center | HEADING_OR_LABEL | named panel/frame | /1of3 | AMBIENTE | T | СРЕДА | `image-gen-9(4).png` |
| `P117-GA-C031` | 31 | CENTER | middle center | BODY_TEXT | named panel/frame | panel body | Polvere, umidità, muffe, smog, detergenti aggressivi e temperature estreme possono irritare la pelle e indebolire la barriera naturale. | T | Прах, влага, плесени, смог, агресивни почистващи препарати и крайни температури могат да раздразнят кожата и да отслабят естествената бариера. | `image-gen-9(4).png` |
| `P117-GA-C032` | 32 | CENTER | middle center | HEADING_OR_LABEL | named panel/frame | secondary heading | FATTORI DI RISCHIO | T | РИСКОВИ ФАКТОРИ | `image-gen-9(4).png` |
| `P117-GA-C033` | 33 | CENTER | middle center | BODY_TEXT | named panel/frame | /3of3/1of4 | Umidità e scarsa aerazione | T | Влага и лоша вентилация | `image-gen-9(4).png` |
| `P117-GA-C034` | 34 | CENTER | middle center | BODY_TEXT | named panel/frame | /3of3/2of4 | Pavimentazioni irritanti | T | Дразнещи настилки | `image-gen-9(4).png` |
| `P117-GA-C035` | 35 | CENTER | middle center | BODY_TEXT | named panel/frame | /3of3/3of4 | Bagni troppo frequenti | T | Прекалено често къпане | `image-gen-9(4).png` |
| `P117-GA-C036` | 36 | CENTER | middle center | BODY_TEXT | named panel/frame | /3of3/4of4 | Esposizione al sole intenso | T | Излагане на силно слънце | `image-gen-9(4).png` |
| `P117-GA-C037` | 37 | CENTER_RIGHT | middle right | HEADING_OR_LABEL | named panel/frame | /1of3 | SEGNALI DA NON IGNORARE | T | ПРИЗНАЦИ, КОИТО НЕ БИВА ДА СЕ ПРЕНЕБРЕГВАТ | `image-gen-9(4).png` |
| `P117-GA-C038` | 38 | CENTER_RIGHT | middle right | BODY_TEXT | named panel/frame | panel body | Riconoscere in tempo i segnali di disagio permette di intervenire subito e prevenire complicazioni. | T | Навременното разпознаване на признаците на дискомфорт позволява бърза намеса и предотвратяване на усложнения. | `image-gen-9(4).png` |
| `P117-GA-C039` | 39 | CENTER_RIGHT | middle right | HEADING_OR_LABEL | named panel/frame | secondary heading | REAGIRE IN TEMPO | T | РЕАГИРАЙТЕ НАВРЕМЕ | `image-gen-9(4).png` |
| `P117-GA-C040` | 40 | CENTER_RIGHT | middle right | BODY_TEXT | named panel/frame | /3of3/1of3 | Osservazione quotidiana | T | Ежедневно наблюдение | `image-gen-9(4).png` |
| `P117-GA-C041` | 41 | CENTER_RIGHT | middle right | BODY_TEXT | named panel/frame | /3of3/2of3 | Interventi mirati | T | Целенасочени действия | `image-gen-9(4).png` |
| `P117-GA-C042` | 42 | CENTER_RIGHT | middle right | BODY_TEXT | named panel/frame | /3of3/3of3 | Visita veterinaria quando necessario | T | Ветеринарен преглед при необходимост | `image-gen-9(4).png` |
| `P117-GA-C043` | 43 | LOWER_CENTER | lower strip | HEADING_OR_LABEL | named panel/frame | section | SEGNALI DA NON IGNORARE | T | ПРИЗНАЦИ, КОИТО НЕ БИВА ДА СЕ ПРЕНЕБРЕГВАТ | `image-gen-9(4).png` |
| `P117-GA-C044` | 44 | LOWER_CENTER | lower strip 1 | HEADING_OR_LABEL | named panel/frame | /1of2 | PRURITO PERSISTENTE | T | ПОСТОЯНЕН СЪРБЕЖ | `image-gen-9(4).png` |
| `P117-GA-C045` | 45 | LOWER_CENTER | lower strip 1 | BODY_TEXT | named panel/frame | /2of2 | Si gratta, si morde o si lecca spesso, soprattutto su fianchi, inguine, zampe e base della coda. | T | Често се чеше, хапе се или се ближе, особено по хълбоците, слабините, лапите и основата на опашката. | `image-gen-9(4).png` |
| `P117-GA-C046` | 46 | LOWER_CENTER | lower strip 2 | HEADING_OR_LABEL | named panel/frame | /1of2 | ARROSSAMENTI E LESIONI | T | ЗАЧЕРВЯВАНЕ И ЛЕЗИИ | `image-gen-9(4).png` |
| `P117-GA-C047` | 47 | LOWER_CENTER | lower strip 2 | BODY_TEXT | named panel/frame | /2of2 | Cute arrossata, puntini, escoriazioni o croste che non guariscono. | T | Зачервена кожа, точици, охлузвания или корички, които не заздравяват. | `image-gen-9(4).png` |
| `P117-GA-C048` | 48 | LOWER_CENTER | lower strip 3 | HEADING_OR_LABEL | named panel/frame | /1of2 | CATTIVO ODORE E FORFORA | T | НЕПРИЯТНА МИРИЗМА И ПЪРХОТ | `image-gen-9(4).png` |
| `P117-GA-C049` | 49 | LOWER_CENTER | lower strip 3 | BODY_TEXT | named panel/frame | /2of2 | Odore sgradevole della pelle o delle orecchie, forfora, pelle unta o secca e desquamata. | T | Неприятна миризма от кожата или ушите, пърхот, мазна или суха и лющеща се кожа. | `image-gen-9(4).png` |
| `P117-GA-C050` | 50 | LOWER_CENTER | lower strip 4 | HEADING_OR_LABEL | named panel/frame | /1of2 | CADUTA DI PELO ANOMALA | T | НЕОБИЧАЕН КОСОПАД | `image-gen-9(4).png` |
| `P117-GA-C051` | 51 | LOWER_CENTER | lower strip 4 | BODY_TEXT | named panel/frame | /2of2 | Diradamento, chiazze senza pelo o caduta eccessiva fuori dal periodo di muta. | T | Оредяване, обезкосмени петна или прекомерна загуба на козина извън периода на линеене. | `image-gen-9(4).png` |
| `P117-GA-C052` | 52 | LOWER_CENTER | lower strip 5 | HEADING_OR_LABEL | named panel/frame | /1of2 | CAMBIAMENTI GENERALI | T | ОБЩИ ПРОМЕНИ | `image-gen-9(4).png` |
| `P117-GA-C053` | 53 | LOWER_CENTER | lower strip 5 | BODY_TEXT | named panel/frame | /2of2 | Pelo opaco, pelle ruvida, apatia, perdita di appetito o aumento di peso inspiegabile. | T | Безжизнена козина, груба кожа, апатия, загуба на апетит или необяснимо наддаване. | `image-gen-9(4).png` |
| `P117-GA-C054` | 54 | LOWER_CENTER | lower strip 6 | HEADING_OR_LABEL | named panel/frame | /1of2 | INFEZIONI RICORRENTI | T | ПОВТАРЯЩИ СЕ ИНФЕКЦИИ | `image-gen-9(4).png` |
| `P117-GA-C055` | 55 | LOWER_CENTER | lower strip 6 | BODY_TEXT | named panel/frame | /2of2 | Otiti, hotspot, pustole o infezioni cutanee che si ripresentano frequentemente. | T | Отити, горещи точки, пустули или кожни инфекции, които често се появяват отново. | `image-gen-9(4).png` |
| `P117-GA-C056` | 56 | FOOTER | bottom | CALLOUT | named panel/frame | /1of2 | RICORDA | T | ПОМНЕТЕ | `image-gen-9(4).png` |
| `P117-GA-C057` | 57 | FOOTER | bottom | CALLOUT | named panel/frame | /2of2 | Una pelle sana è il riflesso del benessere generale del Cane Corso. Osservazione, prevenzione e cura costante fanno la differenza. | T | Здравата кожа е отражение на общото благополучие на Кане Корсо. Наблюдението, превенцията и постоянната грижа имат значение. | `image-gen-9(4).png` |
| `P117-GA-C058` | 58 | HEADER | top-center crest | ARTWORK | top crest | top crest artwork |  | G | No source text; preserve crest artwork. | `image-gen-9(4).png` |
| `P117-GA-C059` | 59 | HEADER | inside top-center crest, central monogram | FIXED_MARK | top crest | top crest USG | USG | R | Retain canonical USG mark. | `image-gen-9(4).png` |
| `P117-GA-C060` | 60 | HEADER | inside top-center crest, lower ribbon | FIXED_MARK | top crest | inside crest lower ribbon | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-9(4).png` |
| `P117-GA-C061` | 61 | LOWER_CENTER | bottom-center medallion | ARTWORK | bottom medallion | bottom medallion artwork |  | G | No source text; preserve medallion artwork. | `image-gen-9(4).png` |
| `P117-GA-C062` | 62 | LOWER_CENTER | inside bottom-center medallion, center | FIXED_MARK | bottom medallion | bottom medallion USG | USG | R | Retain canonical USG mark. | `image-gen-9(4).png` |
| `P117-GA-C063` | 63 | LOWER_CENTER | inside bottom-center medallion, upper perimeter | FIXED_MARK | bottom medallion | bottom medallion upper text | UNICO SUO GENERE | R | Retain canonical Italian brand text. | `image-gen-9(4).png` |
| `P117-GA-C064` | 64 | LOWER_CENTER | inside bottom-center medallion, lower perimeter | FIXED_MARK | bottom medallion | bottom medallion lower text | CANE CORSO | R | Retain visible canonical seal text. | `image-gen-9(4).png` |
| `P117-GA-C065` | 65 | FOOTER | bottom | FIXED_MARK | named panel/frame | brand line | USG · UNICO SUO GENERE | R | USG · UNICO SUO GENERE — запазва се като канонична марка. | `image-gen-9(4).png` |

## V2 aggregate

- Canonical units: **599**
- T/R/N/G/U: **538/46/0/15/0**
- Contiguous IDs: **9/9 graphics**
- Duplicate IDs: **0**
- Missing ordinals: **0**
- U: **0**
