# Request 008: Donate, the one band
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs request 002 (`truck-banner-donate`, `.a-hero.-long`, `.o-pageBanner__truck.-wide`). Page source: site/src/pages-v2/donate.body.html.

## What is needed
1. CSS for the band (`.o-donateBand*`), and a page rule for its list.
2. A narrower banner truck on this page, so the wide drawing clears the words.
3. `.t-donate` in the page scope rule.

CSS values are not measured. P2 checks them.

## Why
- revision.md, Donate: "One band: big photo, Can as a plain line (.m-takes) and Can't as a marked list (.m-notList). Merge: 'Where it goes' and 'How to ask' into two small facts."
- `.m-notList` opens into two and three columns for Services' wide seated card. In this column it has to stay one column, flush left.
- Donate keeps its own estimate band in the page body, with `estimate: no` in its meta, so the footer partial doesn't change and no shared words move. Its markup is the partial's, so if the glyph changes, change both. Nothing to apply for this.

## Exact change

### site/assets/global.css: in "Inner pages", a new section
```css
/* ---- Donate: the one band. A big photo beside the words. Heading on the axis above, so it's not a heading-left, body-right band. Photo first when stacked ---- */
.o-donateBand { display: grid; gap: var(--s-6); max-width: 134.4rem; margin: 0 auto; }
.o-donateBand__media { overflow: hidden; border-radius: var(--r-image); background: var(--c-slate); }
.o-donateBand__img { display: block; width: 100%; height: auto; aspect-ratio: 1; object-fit: cover; }
.o-donateBand__words { display: grid; gap: var(--s-5); align-content: center; }
.o-donateBand__not .m-fact__title { margin-bottom: var(--s-3); }
.o-donateBand__facts { display: grid; gap: var(--s-4); }
/* One column, flush left: its two and three columns are for Services' wide card */
.t-donate .m-notList { grid-template-columns: minmax(0, 1fr); width: auto; margin: 0; }
.t-donate .m-notList__item { font-size: 1.7rem; }
@media (min-width: 1025px) {
  .o-donateBand { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: var(--s-8); }
  .o-donateBand__facts { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .o-donateBand .m-takes { font-size: 1.8rem; }
}
/* The drawing is 1.376 times the truck's width (request 002), and the words run long here, so the truck comes down a little to keep clear of them. Set from the prototype's numbers: measure it */
@media (min-width: 1025px) { .t-donate .o-pageBanner { --truckW: min(38vw, 60vh, 72rem); } }
```
`.m-notList` has media-query rules at 641 and 1025 with one class; `.t-donate .m-notList` (0,2,0) beats them.

### site/assets/global.css: the page scope rule
Add `.t-donate`.

### When Donate moves in
Take `donate` off LEGACY_PAGES.

## Checks P2 has to run
- Geometry: the words against the dresser and bike at the windows in revision.md section 11. This is the banner most likely to collide: the longest row, a 22-word line and the widest drawing.
- The drawing itself: inline with `<use>` it should look like assets/trucks/truck-donate.svg.
- The estimate band: both its own link and the button by keyboard, and that the menu's inert list (it uses `.o-estimate`) still catches it now it's inside main.

## Other pages this touches
None.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written, with one value changed after measuring. Taking Donate off LEGACY_PAGES stays with the move-in.
- **`--truckW` is 57vh, not 60vh.** At 60vh the words cleared the plant by 10px at 1440x900; at 57vh, 36px. Measured on painted pixels from 1026x700 to 2560x1300 (build/tmp/v3/banner_check.py), smallest gap 34 to 36px. Below 1025 the shared rule applies: 14px at 1024x768, 34px at 844x390, 44px at 768x1024.
- Real site: check.py PASS, build.py --check up to date. Home and old Donate unchanged in full-page shots at 1440 and 390.
- Staged Donate in a scratch copy: build and check.py PASS. Banner and band read fine by eye at 1440; the drawing matches assets/trucks/truck-donate.svg.
- **Copy v3 adds a third small fact ("If it can't be donated").** `.o-donateBand__facts` is two columns from 1025, so that fact lands alone on a second row. That's fine for the copy's length, but the pages step should look at it when it applies v3 to this page.
- At 390x844 the sentence is 4.29:1 and at 320x640 3.73:1, under the 4.5 target. Handled in the banners pass after request 013 (build/progress.md).
- Not run here, for P2: the estimate band by keyboard and the menu's inert list, the page's QA and Critic round.

## P2 batch b (2026-11-05)
Moved in. The checks above were run: build/qa-report.md, "P2 batch b: Donate". `--truckW` is now min(33vw, 54vh, 72rem), because 38vw touched on tall windows. The third fact no longer lands alone: stacked from 1025, in a row at tablets.
