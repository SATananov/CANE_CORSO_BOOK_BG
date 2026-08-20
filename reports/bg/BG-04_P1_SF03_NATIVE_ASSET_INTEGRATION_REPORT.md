# BG-04 P1 SF-03 NATIVE ASSET INTEGRATION REPORT

Final result: **PASS WITH REMAINING SOURCE GAPS**

BG-04 remains ACTIVE. The nine native Italian PNGs were compared directly with fresh 400-dpi renders of the immutable Italian PDF and with the embedded full-page raster evidence. No OCR library, OCR API, or automated text recognition was used.

## Immutable reference

- SHA-256 before: A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170 — PASS
- SHA-256 after: A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170 — PASS
- Reference byte-identical: YES
- Required page count: 143; PDF not rewritten

## Correspondence method

Each candidate was checked for exact title and subtitle, illustration identity, panel count/order, icons, relative text positions, footer, crest position, decorative structure, crop and scale. All nine preserve the same complete composition and are embedded with scaling/resampling; none shows a content crop or derived panel rearrangement. Classification: SCALED_NATIVE.

Fresh renders: reports/bg/diagnostics/bg04_p1_sf03_native_asset_integration/page{PAGE}_400dpi.png. Extracted page-raster evidence is stored in the same diagnostic directory.

## Per-graphic results

| Page | Graphic | Native asset | Initial U | Correspondence | T | R | N | G | U remaining | BG targets | Unsupported | Terminology violations | Ready | Remaining blocker |
|---:|---|---|---:|:---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 101 | P101-GA | image-gen-1(20260810-073754).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 103 | P103-GA | image-gen-2(20260810-073758).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 105 | P105-GA | image-gen-3(20260810-073802).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 106 | P106-GA | image-gen-4(20260810-073804).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 108 | P108-GA | image-gen-5(9).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 110 | P110-GA | image-gen-6(7).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 113 | P113-GA | image-gen-7(4).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 116 | P116-GA | image-gen-8(4).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |
| 117 | P117-GA | image-gen-9(4).png | 24 | SCALED_NATIVE | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | NO | Legacy Unit IDs have no surviving spatial anchors/order; native wording cannot safely be assigned to a specific ID. |

## Final totals

- Graphics processed: 9/9
- Initial SF-03 U count: 216
- U resolved: 0
- U remaining: 216
- T/R/N/G produced: 0/0/0/0
- Construction-ready before: 0/9
- Construction-ready after: 0/9
- Duplicate Unit IDs: 0
- Missing Unit IDs: 0
- Unsupported Bulgarian targets: 0
- Terminology violations: 0
- OCR authority violations: 0
- P117 proven against image-gen-9(4).png: YES — SCALED_NATIVE

## Why units remain U

The recovered assets solve graphic identity and make the Italian artwork readable. They do not restore the association between the current anonymous Unit IDs and specific panels. The ledger-rebuild checkpoint created each ID as an unanchored ordinal and no predecessor file in Git contains the lost position map. A new deterministic order cannot be imposed silently because that would manufacture Unit-ID correspondence.

Required next evidence: a human-approved mapping convention (for example, top-to-bottom and left-to-right with named panels) explicitly assigning the existing 24 IDs per graphic, or the original ledger evidence containing coordinates/bounding boxes.

## Safety

- SF-05 and SF-02 processed: NO
- Page 16 reopened: NO
- PDFs, production graphics, BG-03 page masters, BG_PHASE_STATE.json modified: NO
- BG-05 started: NO
- Commit performed: NO
