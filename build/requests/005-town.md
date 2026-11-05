# Request 005: town template, the closing strip and the swap
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs requests 001 (`price-row`) and 002 (`truck-banner-quarter`, `.a-hero.-long`). Template source: site/src/pages-v2/_templates/town.body.html.

## What is needed
1. One page-only rule for the closing strip, and `.t-town` in the page scope rule.
2. The template moved to `src/templates/town.body.html`, not `src/pages/`. build.py would otherwise make a `town.html` page with unfilled tokens.
3. LEGACY_TOWNS off.

Everything else on the template already exists: `.o-homeHaul`, `.m-tile` and `.o-svcPrice` are reused as they are. I kept their names rather than rename a Home block for one page.

## Why
- revision.md, Town pages: "Banner with the town name, one line, one Book in Town pill. What we haul: heading, one line, shared photo tiles. The price row with four trucks. Cut: Ticket. Map. Paragraphs."
- **The strip is my call, and it adds a slim band.** On Services the row of four parks on the cream band rising over it. On a town page the next band is the estimate band, which is slate too, so the trucks would have no fold and the two slate bands would run together. copy.md's "See other towns" had no obvious home, so the strip holds it. The band count stays as revision.md's table in spirit: a strip, no new subject. If Varun would rather not have it, drop the strip and move the link into the price band's `.m-head`, and the trucks stand in slate with no fold.
- Tile order is copy.md's (Junk removal, Clean outs, Furniture, Appliances, Mattresses, Yard waste, Demo), which differs from Home's. I gave each its size so the crops still suit: tile-garage (1.3) in the five, tile-mattress in a four with `-right`, tile-yard (square) in the five. P2 should look at these three crops, since these slots are new for them.

## Exact change

### site/assets/global.css: in "Inner pages", after the Services rules
```css
/* ---- town pages: the strip the row of four parks on. o-svcIndex is the same slim rising band; its link needs no gap above it ---- */
.t-town .o-svcIndex .m-rowActions { margin-top: 0; }
```

### site/assets/global.css: the page scope rule
Add `.t-town`.

### site/tools/build.py
- `LEGACY_TOWNS = False`.
- The `{{TOWN_QUERY}}` replace stays: the pill uses it.

### Moving in
Copy `_templates/town.body.html` over `src/templates/town.body.html`. Build, then read one page at 1440 and 390 for each of: a short name (Derry, NH), the longest (Londonderry, NH).

## Checks P2 has to run
- Every path gets its `../` from prefix_paths, including `book.html?load=...&amp;town=...` from `price-row`. Open a "Book this load" link from a town page and confirm Book has both the load and the town filled in.
- check.py's duplicate ids: `#pricing` and `#page-title` are per page, so fine.
- Geometry on Londonderry, NH (request 002).

## Other pages this touches
None. The old `ticket`, `town-options` and `banner-art-live` blocks and the old ticket JS lose their last user here; they go in request 014.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied: the page-only rule and `.t-town` in the scope rule. **Copying the template to src/templates/ and `LEGACY_TOWNS = False` are the move-in's and were not done.** Everything else the template needs is already there.
- Real site: check.py PASS, build.py --check up to date. Home and old Lowell unchanged in full-page shots at 1440 and 390.
- Staged template in a scratch copy, with staged Book: build and check.py PASS. Londonderry, NH, the longest name, tools/qa.py without the tab pass: no overflow, console or reveal problems, 132 words. Its headline holds two rows at 1440 by eye. Every `price-row` link has its `../` and the town; a "Book this load" link opened Book with `quarter` picked, the town filled and "Yes, we come to Londonderry, NH." showing.
- qa.py's copy check lists the town's name in the lines, as expected for a template written for Lowell.
- Not run here, for P2: Derry at both widths, the three new tile crops read closely, the geometry sweep (request 002).
