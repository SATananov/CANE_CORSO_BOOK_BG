# CANE CORSO BOOK BG — AGENT GOVERNANCE

All agents working in this repository must follow these rules.

## Authority order

1. Human owner decision
2. `BG_STYLE_LOCK.md`
3. `BG_TRANSLATION_RULES.md`
4. `BG_MASTER_PLAN.md`
5. `BG_PHASE_STATE.json`
6. phase-specific report/evidence

If instructions conflict, the higher authority wins.

## Immutable source

`references/PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf`

Required SHA-256:
`A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170`

No agent may modify, overwrite, rename as output, rasterize in place, or save changes into this reference.

## General safety

- Work only inside `CANE_CORSO_BOOK_BG`.
- Never write into `CANE_CORSO_BOOK_IT`.
- Never skip phases.
- Never advance phase state after FAIL.
- REPORT ONLY phases may not modify book content.
- Produce new output filenames; do not overwrite approved inputs during experimental work.
- Create page-specific evidence before high-risk visual changes.
- Preserve 143 pages unless human owner explicitly authorizes otherwise.
- Stop when the reference hash does not match.
- Stop when unexpected pages change.

## Translation safety

- Natural Bulgarian.
- No invented facts.
- No silent historical correction.
- Preserve speaker attribution.
- Follow the terminology lock once BG-02 is approved.

## Visual safety

- Italian Phase 7I FINAL is visual authority.
- Page 78 is master identity for decorative Cane Corso head.
- Preserve frames, footer, numbering and imagery.
- Do not use patch-on-patch ghost overlays as a normal construction method.
- Rebuild language-dependent graphics cleanly.

## Agent roles

### `bg-orchestrator`
Owns phase progression and gates. Does not override guardians.

### `translation-guardian`
Checks Bulgarian language, terminology and attribution.

### `visual-master-guardian`
Checks visual equivalence to the Italian master.

### `image-text-guardian`
Checks language-dependent text embedded in graphics.

### `final-qa-guardian`
Performs final 1–143 audit. REPORT ONLY by default and must not silently fix findings.

## Mandatory stop conditions

Stop and report if:
- IT reference hash changes;
- page count changes unexpectedly;
- an unapproved page is modified;
- a phase prerequisite is missing;
- a visual correction would require redesign rather than translation/reconstruction;
- source meaning is uncertain enough that translation would be speculative.
