# Request 007: About, the call pill on narrow phones
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs requests 002 (`truck-banner-eighth`) and 003 (`.m-factRow`). Page source: site/src/pages-v2/about.body.html.

## What is needed
1. Two small rules for the call pill, so it fits a phone.
2. `.t-about` in the page scope rule.
3. A decision on the photo (see the end).

Everything else is existing: `.m-promo`, `.m-fact`, `.a-num`, and `.o-svcBand` for its top padding.

## Why
`.a-button` doesn't wrap. "Call Shawn (603) 555-0142" with its icon, at the large pill's padding, is about 300px wide. A promo card's words are 302px wide at 390 and 232px at 320 (worked out from the tokens, not measured).

## Exact change

### site/assets/global.css: in "Inner pages", a new section
```css
/* ---- About: the call pill. Its label and number run about 300px at the large pill's padding, and the promo's words are 302px wide at 390. Tighter on phones; number and icon alone under 380, the aria-label still says "Call Shawn" ---- */
.m-promo__callLabel { display: inline; }
@media (max-width: 640px) { .t-about .m-promo__action { padding: 0 1.6rem; font-size: 1.5rem; } }
@media (max-width: 379px) { .m-promo__callLabel { display: none; } }
```
`.t-about .m-promo__action` and `.a-button.-large` tie at (0,2,0), so this has to sit after the atoms, which it does here.

### site/assets/global.css: the page scope rule
Add `.t-about`.

### When About moves in
Take `about` off LEGACY_PAGES.

## Checks P2 has to run
- Header number and call bar with the pill in and out of view (`data-call-here` on a mid-page pill): the number should show once per screen, with no flash on load.
- Pill width at 390 and 320.

## Decision for Varun: the photo
copy.md names old-pickup-driveway for this slot, so I used it. It shows a large Chevrolet bowtie on the grille, a second on the plate frame and a "Custom Deluxe" badge on the fender. Revision.md keeps "the no-brands rule", and cropping can't lose them without losing the truck. It's also an Arizona gravel yard on a page that says "local". Options, logged in content/placeholders-add-pages.md: paint out the badges (revision.md allowed "one retouch, the only one", so this needs his say), download a better stock photo, or wait for Shawn's own. I did not change or re-crop it.

## Other pages this touches
None.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written. Taking About off LEGACY_PAGES stays with the move-in.
- Real site: check.py PASS, build.py --check up to date. Home and old About unchanged in full-page shots at 1440 and 390 (one 390 shot differs 0.09% in the header pill, the baseline's own timing noise).
- Staged About in a scratch copy: build and check.py PASS. The pill fits on one row at 320 with number and icon only, and shows "Call Shawn (603) 555-0142" at 1440. The band reads fine by eye.
- **The photo decision stays open.** Varun told the Studio Lead not to be asked, and choices.md keeps the staged defaults, so it is built as copy.md names it, with no retouch. At 1440 the Chevrolet bowtie on the grille and on the plate frame are readable. The Critic capped Home's craft for a badge earlier (review-log.md), so expect the same on this page in P2. The fix then is a better stock photo.
- Banner measured, scrim and geometry: see the note under request 002's checks in build/progress.md. At 320x640 the sentence is 3.82:1, under 4.5.
- Not run here, for P2: the header number with the pill in and out of view, the page's QA and Critic round.

## P2 batch b (2026-11-05)
Moved in. The photo decision is closed: old-pickup-driveway is gone, replaced with a house and drive with no vehicle or person, must-replace by Shawn's own (content/placeholders.md, About). The checks above were run: build/qa-report.md, "P2 batch b: About". At 320 the pill keeps number and icon, 183 by 56.
