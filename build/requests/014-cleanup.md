# Request 014: cleanup, once every staged page has moved in
Filed by the pages session, phase P1, 2026-11-05. Status: open. Apply last, after requests 001 to 013 and after every page is off LEGACY_PAGES. For the integration review (build/COORDINATION.md, gate 3).

## What is needed
The old build's parts lose their last user when the last page moves. Delete them, so the site ships without the temporary block global.css and global.js both promise to remove.

## Exact change

### site/tools/build.py
Delete:
- `LEGACY_PAGES`, `LEGACY_TOWNS` and the `.t-legacy` wrapper in build_page.
- `block_town_options`, `block_ticket`, `banner_art`, `block_price_cards`, `price_glyph`.
- From BLOCKS: `contact-art`, `town-options`, `price-cards`, `ticket`, `banner-art`, `banner-art-empty`, `banner-art-live`, `banner-art-donate`, `banner-art-commercial`, `banner-art-plain`.

In `block_town_map`, nothing prints a marked town now, since town pages lost their map:
- Delete `map_arms`, `MAP_ARM` and the `CURRENT_TOWN` branch, with `reg` and the `-here` sort.
- Delete the `<defs>` pattern and the `fill="url(#qh-map-dots)"` attribute. The halftone is retired, and CSS sets the fill (request 004).

Keep `CURRENT_TOWN` itself: `fill_head` and `block_price_row` read it.

### site/src/partials
Delete ticket.html, banner-art.html, banner-art-items.html, commercial-art.html, contact-art.html, faq-art-calendar.html, faq-art-items.html, faq-art-payment.html.

### site/data
- prices.json: drop `fill`, and its sentences in `_note` about the old price cards and the town ticket.
- towns.json: drop "the old town ticket's listbox" from `_note`.
- images.json: these crops have no page left, so drop them and their files: pickup-trash-bags (services folder), garage-clutter-before, garage-after, band-basement, band-tearout, band-sofa, band-fridge, band-man-mattress, band-yard-truck. Check with a search first: Home or a page may have picked one up meanwhile.
- content/placeholders.md: the same crops' "where used" rows are out of date. renovation-tearout, backyard-lawn-fence and others need their rows updated, not deleted.

### site/assets/global.css
- Delete the OLD INNER PAGES block, including the second `.t-legacy { ... }` rule at the very end of the file.
- Update the banner comment at the top of the file.
- Delete the "print" comment's reference to the block below.
- `.m-map` rules hang off `.m-promo__media.-map` (request 004). Once the old map is gone they could be single-class, as conventions prefer. Optional, and worth doing only if the converter's check asks for it.

### site/assets/global.js
- Delete the OLD INNER PAGES blocks with no page left: its in-view block, Ticket, the old before-and-after, Reviews filter. Forms, Book, Request forms, Commercial, FAQ and the map's lights stay: move them above the banner comment, and update the banners on those two comments.
- `reduceMotion` and `root` are the old blocks' names for `reduced` and `html`. Rename what's left, then drop the aliases.
- `is-ready` in the load sequence is the old pages' name for `is-loaded`. Drop it.

### Then
Run tools/build.py, tools/check.py and build.py --check on the whole site, and QA on every page. check.py is the test for this one: it fails on any class left with no rule.

## Other pages this touches
All of them, since it removes shared code. They should look exactly the same, because nothing kept should depend on what's deleted. So any visual change after this request is a bug.

## Result (shared-parts owner, 2026-11-05): ready, NOT applied, still open
**This request is not closed, and it was not applied to the real site.** Its own first line says it comes after every page is off LEGACY_PAGES. This run was told not to move staged pages in, and 11 old pages and 12 town pages still run on what it deletes, so applying it now would break all 23. A request closes only when its affected pages pass, and they couldn't. It belongs to the integration review (build/COORDINATION.md, gate 3).

**What's ready: build/tmp/v3/r014.py does the whole cleanup as one script.** It stops at once if any page is still on LEGACY_PAGES or LEGACY_TOWNS is True, and every replacement must match exactly once, or it stops rather than skip. So a later edit to one of these places is caught, not lost. Keep that file until this request is closed, even if build/tmp/ is tidied.

To apply at integration, once every page has moved in:
1. From build/tmp/v3/: `python -I r014.py ../../../site --delete`
2. From site/: `python tools/images.py`, `python tools/build.py`, `python tools/check.py`, `python tools/build.py --check`
3. QA on every page. Any visual change is a bug.
4. Update the "where used" rows in content/placeholders.md (renovation-tearout, backyard-lawn-fence and the others this request names). The script doesn't touch that file.

**It does more than this request lists, because later requests added old-page parts.** Also removed: `block_review_grid_old`, `block_town_list_old`, `block_faq_groups_old`, `OLD_FAQ_ART`, `CURRENT_LEGACY`; the `filter` keys in data/reviews.json; Book's `priceLine` and `setPrice`, the `.t-legacy` branch on calendar chips, the optional town-note default and the optional "Remove" word (request 003's note says this file lists those; it didn't until now); the `.t-legacy` filters on the before and after and in-view blocks; the undo rules, which go with the block; assets/fx/grain.svg.

**Tried on a scratch copy with all 12 staged sources moved in** (build/tmp/v3/trial, with its own copies of global.css and global.js; site/ untouched):
- check.py PASS on 24 pages, so no class is left without a rule. build.py --check up to date. global.css 203KB to 105KB, global.js 54KB to 38KB.
- Before and after, full-page shots at 1440 and 390, all 13 page types: 0.0% changed on 24 of 26, 0.07% in one header pill (the known timing noise). The 26th, the 404 at 1440, was a capture glitch on a page that links its CSS from the site root, so the trimmed files never reached it. Compared again with them routed in, the 404 differs only in the header pills, 0.16% and 0.18%.
- On the trimmed files, no failures in: Book's flow (21 lines), Contact's, Commercial's, Privacy's, Home's, FAQ's rows, Reviews' sliders, the hub's chips and map lighting together, a town's load links, the phone menu. No script errors.
- The 9 image jobs and 44 media files it will delete were checked against every staged page: none is used. It lists them; in this try nothing under assets/ was deleted.

**One real thing this try turned up, fixed on the real site:** the reduced-motion list gave `.m-header` a 1ms transition on every property though it has no transition of its own, so a full-page capture could catch the header between sizes. Removed from the list.

**Not known yet:** the staged pages will change during P2 (copy v3 on Reviews, Donate, About and Book, and whatever their Critic rounds ask). If they pick up an old class or a dropped image, the script or check.py will say so at integration.

## Note from P2 batch a, 2026-11-05
Book moved in, and its Critic found the town check wrong (Salem, MA got Salem, NH's yes), so global.js's town block is rewritten. build/tmp/v3/r014.py had one replacement on the old lines, which is removed: the new block has no optional default left to trim. Its other Book replacements (`priceLine`, `setPrice`, `noPrice`, the calendar's `.t-legacy` branch) still match. Rule rows in OLD INNER PAGES for `.t-legacy .o-book*` have had no user since Book moved; they go with the block.

## Note from P2 batch b (2026-11-05)
Reviews now uses three of the crops this request meant to drop: pickup-trash-bags (the grid, through data/reviews.json, which the script's page search can't see), garage-clutter-before and garage-after (the garage pair, recut at 4:3). They came off GONE_JOBS in build/tmp/v3/r014.py. Don't drop them.
