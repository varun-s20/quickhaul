# Request 013: Privacy, the reading column
Filed by the pages session, phase P1, 2026-11-05. Status: open. Page source: site/src/pages-v2/privacy.body.html.

## What is needed
1. CSS for the plain page (`.o-privacy*`).
2. `.t-privacy` in the page scope rule.

CSS values are not measured. P2 checks them.

## Why
- revision.md, Privacy: "legal copy keeps its length, same type, no art, plain heading instead of a photo banner." The old `.m-privacyCell` was a ruled cell, which is retired.
- No photo banner, so no truck, no fold and no preload_picture. It's the only page with no banner: the heading sits on cream under the bar, so the band's top padding has to clear the logo's overhang.
- Revision.md disagrees with itself about the estimate band: its table says one band, its section 7 says every page but Book, Commercial and 404. I left it off, as copy-changes.md suggests and as the footer partial's own comment already says. No words depend on it.

## Exact change

### site/assets/global.css: in "Inner pages", a new section
```css
/* ---- Privacy: a reading column on the page's one axis, with the body's own type. No reveals: text to read shows at once ---- */
.o-privacy { max-width: 76rem; margin: 0 auto; box-sizing: content-box; }
.o-privacy__item { margin-top: var(--s-6); }
.o-privacy__title { font: var(--w-semi) 2rem/1.25 var(--f-body); }
.o-privacy__text { margin-top: var(--s-2); text-wrap: pretty; }
```
`box-sizing: content-box` keeps 760px of text inside the band's gutters. It must sit after `.b-band`, which sets the padding.

### site/assets/global.css: the page scope rule
Add `.t-privacy`.

### When Privacy moves in
Take `privacy` off LEGACY_PAGES. Delete the `banner-art-plain` block in the cleanup (request 014).

## Checks P2 has to run
- At 390 and 1440: the logo's overhang stays clear of the heading at every scroll position (rulings, R0 A1), and the heading is not undersized at 390 (R0 A14).
- Print: `.t-page { padding-top: 0 }` is already there; check that the policy prints clean.

## Other pages this touches
None.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written (CSS lifted from this file by script), with one undo line for the old page. Taking Privacy off LEGACY_PAGES stays with the move-in.
- **Found: the old Privacy page uses the same class.** `.o-privacy` is on its grid of cells, so the new reading column squeezed its two columns to 380px (build/tmp/v3/leak.py, 4 differences). `.t-legacy .o-privacy { box-sizing: border-box; max-width: none; }` joined the undo rules at the end of OLD INNER PAGES, and goes with that block. Leak check now 0 differences.

Checks:
- Real site: check.py PASS on 24 pages, build.py --check up to date. Home and old 404 0.0% changed in full-page shots at 1440 and 390. Old Privacy differs only in the header pill, 0.06% and 0.13%, which is the known timing noise (box at the pill, nowhere else).
- Staged Privacy in a scratch copy: build and check.py PASS. tools/qa.py without the tab pass: no overflow, console or reveal problems, 184 words, heading order 1 then 2s.
- build/tmp/v3/flow_trial_privacy.py, 0 failures. At rest the logo's foot clears the heading's line box by 95px at 1440, 63px at 390 and 76px at 320. Heading 64px at 1440, 47px at 390, 38px at 320, so it isn't undersized at 390. Reading column 760px at 1440, no sideways scroll at any of the three.
- Print emulated and written to PDF (build/shots/v3-trial/privacy-flow/privacy.pdf): chrome off, all seven sections on, top padding 0. Reads clean by eye.
- Not tried: a real print dialog. Not run here, for P2: the page's tab pass and Critic round.
