# Shared parts: frozen
Frozen 2026-11-05 by the shared-parts owner (build/COORDINATION.md, gate 2). **The shared parts are final for the rebuild, on one condition below.** This file is the word gate 2 waits for.

## What this means
- Nobody edits a file on the list below directly from here on. Shared changes go through build/requests/, one at a time, in number order. A request closes only when its affected pages still pass (build/COORDINATION.md).
- **Updated 2026-11-05, after Varun's approval: requests 001 to 013 are applied and closed. Request 014 is ready but not applied, and stays open until every page has moved in.** Each request's last section has what changed and what was checked. "Changes after freeze" below lists every shared change. Frozen means stable: shared changes from here still go through build/requests/.
- **The one condition is met.** Varun saw the homepage, approved it and gave his notes (design/choices.md, "Homepage approval and instruction to finish"). They are applied.
- **Starting P2:** nothing here holds it up now. See "What P2 needs now" at the end of this file.

## Shared files
**Tokens and global code**
- design/tokens.css
- site/assets/global.css. The new look, then the OLD INNER PAGES block under `.t-legacy` until request 014 deletes it.
- site/assets/global.js. Same arrangement.

**Fonts, trucks, media**
- site/assets/fonts/: biosans-light.otf, biosans-regular.otf, biosans-semibold.otf, biosans-extrabold.otf, robotomono-latin.woff2, robotomono-latin-ext.woff2
- site/assets/trucks/: 20 SVGs, byte-identical to prototype/revision/assets/trucks/. Written by tools/build_trucks.py.
- site/assets/images/: 170 files. Cut by tools/images.py from data/images.json, never by hand. New crops are a request.
- site/assets/fx/: footer-joists-1400.webp; grain.svg (old pages only, goes with request 014)
- site/assets/icons/: apple-touch-icon.png, favicon-32.png, favicon-48.png
- site/src/stock/: the 21 originals

**Partials**
- site/src/partials/head.html, header.html, footer.html
- site/src/partials/trucks/: truck-sprite, truck-hero, truck-gauge, truck-banner, truck-row-1 to 4. Written by tools/build_trucks.py.
- Old-page art, kept only until request 014 deletes it: banner-art.html, banner-art-items.html, commercial-art.html, contact-art.html, faq-art-calendar.html, faq-art-items.html, faq-art-payment.html, ticket.html

**Data and tools**
- site/data/: faq.json, image-manifest.json (written by tools/images.py), images.json, prices.json, reviews.json, towns.json
- site/tools/: build.py, build_trucks.py, check.py, images.py, qa.py
- site/sitemap.xml and site/robots.txt (written by tools/build.py)

**Homepage**
- site/src/pages/index.body.html
- site/src/schema/index.json, and site/src/schema/page.json, which several pages share

**Logs the owner keeps**
- build/progress.md, content/placeholders.md, review-log.md

## Not shared
The pages session's own: site/src/pages-v2/ until each page moves in, then that page's site/src/pages/<slug>.body.html, site/src/templates/town.body.html, and the page's own schema (services.json, faq.json, contact.json, town.json). Its notes go to build/progress-pages-v2.md, content/placeholders-add-pages.md and logs/review-pages-v2.md. Built HTML at the site root is generated: never edit it.

## What P2 needs to know
- A page moves in by coming off `LEGACY_PAGES` in tools/build.py (`LEGACY_TOWNS` for the town template). That edit is shared, so it goes in as part of the page's request.
- The header's number is now hidden until global.js has run its block (`is-callReady`), so it no longer flashes on first paint. Nothing is needed on a page: the first `data-call-here` on the page still decides, and a page without one shows the number once the script has run.
- `.o-homeProof__stage`'s 1500px cap and `.o-homeTowns`'s column sizing are Home only. They don't reach `.m-compare` or `.m-promo` on other pages. If a page's promo headline must hold its rows on narrow phones, it needs the same column sizing: tools/qa.py doesn't catch a wrapped row, only a clipped one.
- tools/qa.py's image check only runs at 1440 and 390. Other pages' photos can be stretched on big screens, because the root grows past 1440. Check at 2560 as well.
- The preview line is off (`PREVIEW_LABEL` in tools/build.py). Set it True, or gate the preview, before any deploy-preview (brief; choices.md).

## State at the freeze
- tools/check.py PASS on 24 pages. tools/build.py --check up to date, 26 files.
- Home: tools/qa.py clean, flow_home.py no problems, every headline row one line at 24 widths from 320 to 2560. Full numbers: build/qa-report.md, last section.
- Old inner pages: smoke check clean at 1440 and 390, mixed look as expected. Their own flow tests were last run before the final footer, image and number changes.
- Backup: build/site-v1-backup/, 209 files, untouched.
- **Critic score of record: round 2, 7.9, FAIL by 0.1** (design 8, originality 8, craft 7 capped, functionality 9, no tells). Both allowed rounds are used. The defect behind the cap and the later fixes are not re-scored, so no one has scored the page as it stands. Round 1's 8.1 was withdrawn in effect by the Critic itself: it said many of its images hadn't loaded.

## Fingerprints at the freeze
First 16 characters of each file's SHA-256 (`sha256sum`), from projects/quickhaul/. A later mismatch means a shared file changed, which should trace to a request or a line below.

| File | SHA-256 |
|---|---|
| design/tokens.css | d9a5b3da1c1896f4 |
| site/assets/global.css | 19bb758717820902 |
| site/assets/global.js | f85ebb428cff03ca |
| site/src/partials/head.html | a908e0be50841c35 |
| site/src/partials/header.html | b5a4bf87948734ff |
| site/src/partials/footer.html | 943cba5a34268cd0 |
| site/src/partials/trucks/truck-sprite.html | da7790a1bf28bff3 |
| site/src/pages/index.body.html | 1d6c77824a515bc4 |
| site/src/schema/index.json | 4504b329024ea99b |
| site/src/schema/page.json | 4ee84bdff9bc6542 |
| site/data/faq.json | 84fc7eb208c97b02 |
| site/data/images.json | d1a9791c04b4e0ec |
| site/data/image-manifest.json | fdf324f17d1bdbc0 |
| site/data/prices.json | fc8fdd874baf17ef |
| site/data/reviews.json | 7bb7ca8c82846100 |
| site/data/towns.json | 007bd35965d22ea3 |
| site/tools/build.py | e5a79bac532a53b4 |
| site/tools/build_trucks.py | b8ca97528a5ba58b |
| site/tools/check.py | 50ba6bf8c7454e7c |
| site/tools/images.py | 2129947497584761 |
| site/tools/qa.py | 02ca7dd5040760ea |
| site/sitemap.xml | be5477a48c00bc9d |
| site/robots.txt | 9cc6c41f99c526fd |

## Changes after freeze
Varun's approval note (design/choices.md, "Homepage approval and instruction to finish") was the one condition above. These are the changes since, newest last. The fingerprints above are the freeze's; a mismatch now traces to a line here.

**2026-11-05, Home from copy v3 and Varun's notes (not a request)**
- site/src/pages/index.body.html: copy v3 (content/copy-changes.md). Reviews band is five cards and one Facebook link.
- site/data/reviews.json: `home` is a list of five; no `source` on samples; `reviews_page` has v3's six, `who` "Sample review", `initials` added. `filter` stays until the old Reviews page moves. The staged site/src/pages-v2/_data/reviews.json is older than this file: request 006's note says how they combine.
- site/data/prices.json: `_note` lists where a price is typed by hand.
- site/tools/build.py: `block_review_home` prints five cards through a new `quote_foot` (source, date and post link print only when a real review has them). New blocks `facebook-url` (was request 006's) and `price-from`. `block_load_picker` prints the visible "How full?" label, a wrapper `.o-homePrice__loads`, and the legend "How full is the truck". **The fieldset no longer carries `.o-homePrice__loads`.**
- site/assets/global.css: `.m-loadPicker` is now a small control, 296 by 36px with a 44px target per stop (was the band's full width, 64px tall). This is global, so Book's picker follows when it moves (request 003's note). `.a-choice__unit` hidden at every width. New: `.m-quote.-card`, `.o-homeReview__grid`, `.o-homeProof__takes`, `.o-homePrice__loadsLabel`.
- site/tools/qa.py: `--port`, because each session has its own (qa.py defaulted to 8820). `.a-choice__unit` no longer reads as overflowing text.

**2026-11-05, requests, applied in number order. Each request file's last section has what differs from it and the checks.**
- 001: build.py `block_price_row`, blocks `truck-banner`, `price-row`. global.css `.t-services` in the scope rule.
- 002: build_trucks.py five more banner trucks, and five new partials from running it. build.py five blocks. global.css `.a-hero.-long`, `.o-pageBanner.-short`, `.-noTruck`, `.o-pageBanner__truck.-wide`, `.o-pageBanner__callLabel`.
- 003: global.css reset gains h3, ol, dl, dd, legend, textarea; `.a-choice.-light`, `.m-loadPicker.-light`, `.m-fact`, `.m-factRow`, the form parts, Book's sheet, `.t-book`; an undo block at the end of OLD INNER PAGES. build.py `load_radios`, block `load-radios`. global.js gauge block's `readout`, Book block (prefill sends change, no-price summary, default town note, Try again), `fieldError`, `showFieldError`, `setupUploads` with Remove.
- 004: build.py `block_town_list` new, `block_town_list_old`, `CURRENT_LEGACY` (a rewritten block prints its old markup on a page still on LEGACY_PAGES). `block_town_map` runs the state, line and river past the square. global.css `.a-chip.is-lit`, `.m-promo__group`, `.m-promo__label`, `.m-promo__media.-map` and its map rules, `.t-area`.
- 005: global.css `.t-town .o-svcIndex .m-rowActions`, `.t-town`.
- 006: build.py `block_review_grid` new, `block_review_grid_old`. data/reviews.json gains photo items, in a new order. global.css `.o-reviewGrid*`, `.o-reviewPairs*`, `.t-reviews`. global.js before and after runs per slider.
- 007: global.css `.m-promo__callLabel`, `.t-about .m-promo__action`, `.t-about` in the scope rule.
- 008: global.css `.o-donateBand*`, `.t-donate .m-notList*`, `.t-donate .o-pageBanner` (`--truckW` 57vh, was 60vh in the request), `.t-donate` in the scope rule.
- 009: build.py `block_faq_groups` new, `block_faq_groups_old`, `OLD_FAQ_ART`. data/faq.json is the staged file. global.css `.o-faqList*` (with `display: flow-root`, not in the request), `.m-faq*` new rules, `.t-faq` in the scope rule, three transition names in the reduced-motion block, `.t-legacy .m-faq__title` undo. global.js FAQ block moved above the OLD INNER PAGES banner, unchanged.
- 010: global.css `.m-field__label`, `.m-form` with `.m-form[hidden]` (not in the request: the grid outranked `hidden`), `.m-form__chips`, `__help`, `__foot`, `.m-formState` with a scroll margin (not in the request), `.o-contactFacts`, `.o-contactMore`, `.t-contact` in the scope rule. global.js focusin handler finds `.m-field__label`.
- 011: global.css `.m-form__rhythm`, `.m-form__often`, `.t-commercial` in the scope rule.
- 012: global.css `.t-notFound` in the scope rule, `.t-notFound .a-chip` under 380 (not in the request).
- 013: global.css `.o-privacy*`, `.t-privacy` in the scope rule, `.t-legacy .o-privacy` undo.
- Banners pass after 013 (not a request; it answers the checks request 002 left open): global.css `.o-pageBanner__scrim` phone stops, `.o-pageBanner.-noTruck .o-pageBanner__scrim`. No page on the real site prints either yet.
- 014: NOT applied, still open (its last section says why). Nothing in shared files changed for it, apart from one word: global.css drops `.m-header` from the reduced-motion transition list, because it gave the header a 1ms transition on every property.

**2026-11-05, after the Critic's round on Home (8.4 PASS, not re-scored after these). Not requests.**
- global.css `.m-quote.-card` is slate with cream text (was the seated card's pale ground), so the staged Reviews cards follow. `.m-quote.-card .m-quote__avatar` and `__source` follow the ground.
- global.css `.o-estimate__glyph` turned -40deg, on every page with the band.
- global.css `.o-homePrice__note` capped at 28rem from 1025.
- global.css `:focus-visible` has a 4px radius, and pills, tiles and cards keep their own. `.m-menu__link` is `width: fit-content`, so its ring fits the word.
- global.css `.o-homeHero__scrim` from 641 in landscape gains one small faint ellipse behind JUNK OUT's last letters. `.o-homeProof__takes` balanced.
- global.css `.m-footerCol.-wide` and footer.html: on phones the last list takes the row, its links on two columns. Every page's footer is 88px shorter at 390.

**2026-11-05, P2 batch a: Services moved in (not requests; the P2 builder owns shared files now). Rechecked: Home first (tools/qa.py clean, flow_home.py no problems), then Services. Old pages only take the header and the reset's line.**
- site/tools/build.py: `COVER_SIZES`, the `sizes` for the two full-bleed photos, used by both `picture()` and the preload, so they can't differ. Banners and Home's hero asked for a file narrower than the picture on tall windows (1000px file shown at 1346 at 768x1024, Home's at 1666). Staged pages need no edit: any `page-street` picture gets it.
- site/src/pages/index.body.html: `sizes` only, on four pictures. Same fault at 640 and at 1026 to 1100. Looks the same, sharper.
- site/data/images.json: `page-street` 2400, `svc-junk` 2380, `svc-yard` and `svc-shed` 1600.
- site/tools/images.py: retouch mode `ink`, and paint-outs for the pickup's door and the trimmer's cover. Recut tile-junk, og-home, svc-junk, pickup-trash-bags, compare-before, svc-garage, garage-clutter-before, so Home's photos changed by those marks only.
- global.css, header: 641 to 820 drops "Questions? Give us a call"; 641 to 767 also has an 88px logo, no arrow on the pill, a tighter pill and a 14px number. The logo stood over the number there, on every page. Book now's breathing on hover is off to 820. build/tmp/p2/header_check.py measures it.
- global.css, reset: `scroll-padding-bottom: 72px` under 641, so focus clears the call bar on every page.
- global.js, call bar: `blocked()` also counts the booking links inside `:target`, so a jump chip's service wins over the bar. Listens on any page with `.m-jump`, and on `hashchange`.
- global.js, new block: a jump chip reached by keyboard scrolls to the row's centre. Keyboard only.
- global.css, banners: `.o-pageBanner__img` sits at `50% 100%` from 1025 up (was 62%), and the small wash behind the sentence goes .25 and .19 (was .2 and .15), every banner. Every later page must re-measure its own.
- global.css, Services and cards: `.m-svcCards.-two` is a checkerboard from 1025 up, with `.m-svcCard__words` (new, in the two cards' markup); its heading is 6.4vw at tablets. Text padding in cards. `.m-svcCard:target` underline. `.t-services` one-row lead heading, photo 2.85, promo columns 7.5 and 4.5 from 1367, promo picture 1.65 on phones. `.o-svcNot` art on the axis, card 112rem. `.m-notList` equal columns from 1241 (was auto from 1025). Donate overrides it.

**2026-11-05, P2 batch a: Book moved in. Rechecked: Home first (flow_home.py no problems), Services (flow_services.py no problems).**
- site/tools/build.py: `book` off LEGACY_PAGES.
- global.js, gauge block (Home too): pieces land by level, lowest first, so the bed fills before the heap. Was drawing order.
- global.js, header states (every page): any number of `data-call-here` elements. Each is watched and any one in view counts. Home, Contact and About still have one each.
- global.js, Book block: card lands 20px under the bar, was flush. Town check rewritten: as you type, full stops ignored, a typed state must match, a listed town written out on leaving. **build/tmp/v3/r014.py lost the one replacement that targeted the old town lines** (request 014's note). Day error moves beside what's missing and focus goes there. Up and Down go by week. Progress line shows the visitor's answers. Optional chips clear on a second press or Space. The end states add `is-finished`, and the done state parks a copy of the gauge truck.
- global.css, Book only: `.o-book__chips` own width, 44px, Regular (was grid, 56px, Semibold; `-five`, `-seven`, `-lead` gone); `.-stack` three across at 641 to 1024. Calendar faces 44px circles, lighter ring. `.o-book` no fixed height. `.o-book__cells.-single`, `.o-book__cell.-load`, `.o-book__readout`, `.o-book__progressAnswer`, `.o-book__dayError`, `.o-book__townNote`, `.o-book__doneBody`, `.o-book__doneTruck`, `.o-book.is-finished`. `.o-book__summaryRow[hidden]`. `.t-book .m-field__error + .m-field__note` hidden with an error up. Facts tighter on phones. `.o-book__stateFoot` on the axis on phones.

**2026-11-05, P2 batch a: hub and town template moved in. Rechecked: Home first (tools/qa.py clean, flow_home.py no problems), then Services, Book, the hub and 12 towns (their flows no problems), old pages smoke-checked (no console, network, overflow or h1 problems).**
- site/tools/build.py: `service-area` off LEGACY_PAGES, `LEGACY_TOWNS = False`. `block_town_map`: viewBox 800 by 700, its empty foot cropped, state and river running on past it; state names inside their states; round dots (`rx`); `MAP_LABEL_LIFT`, more in `MAP_LABEL_DROP`; `MAP_HIT_SHIFT` gains Derry and Londonderry; `MAP_BORDER` and `MAP_RIVER` each move one point, so no town sits on a line. **Staged Contact uses this map, so it gets all of it.**
- site/data/images.json: `tile-yard` 1200.
- global.css, map (every `.m-promo__media.-map`): labels in the drawing's own units, 26, 22 and 20 (px in an SVG, because in rem they grew past 1440 while the map's spacing didn't). 8/7 on phones, 4/3 on tablets. Ground slate 2%, north 11% (was 0 and 8). River a 9-unit soft band. Lit label is a slate tag. Hairline round the slot, on `::after`.
- global.css, `.t-area` only: map half the card from 1025, words before the map under 1025, chips `max-width: 46rem`.
- global.css, `.t-town` only: `--t-section` lower, so the H1 is the page's biggest line; `.a-hero.-long` 11.2cqi; "What we haul" sized off its column. The pattern is usable by Donate if its H1 has the same problem: set `--t-section` on the page wrapper.
- global.css, every page: `.m-header__link[aria-current]` and `.m-menu__link[aria-current]`, any value. `.o-estimate__glyph` -30deg at 1024 and under, because the band's edge cut an arrowhead; -40deg stays above that.
- global.js: town pages mark Towns as current (`aria-current="true"`). Any `[data-town-query]` wrapper adds the town to every plain Book link on the page, header and estimate band too.
- build/tmp/v3/r014.py: tried on a scratch copy with the remaining staged pages overlaid (build/tmp/p2/r014_try.py): it still runs to the end.

**2026-11-05, P2 batch b: Reviews moved in. Rechecked: Home first, then Reviews (see the end of this block).**
- site/tools/build.py: `reviews` off LEGACY_PAGES.
- global.css: `.o-reviewPairs__end`, copy v3's line under the pairs, on the axis.
- site/tools/images.py: `ImageChops`; new retouch mode `flat`, one colour with the columns' shading kept, for a printed label on something round; RETOUCH entries for cellar-shelves.jpg and service-truck-street.jpg.
- site/data/images.json: `basement-boxes-before` out. In: `storage-room-before`, `cellar-shelves` (folder reviews), `service-truck-street`. `garage-clutter-before`, `garage-after`, `basement-empty-after`, `yard-branches-before`, `yard-lawn-after`, `shed-old-before`, `shed-gone-after` recut at 4:3, the frame's own ratio; the last-but-one and last also swap sources. Reviews' garage pair is off Home's compare-before and compare-after, which are unchanged. site/src/stock/ gains three originals.
- site/tools/images.py, RETOUCH: `garage-after.jpg` gains the wider crop's marks. Home's crop leaves them out and wasn't recut. `storage-room-clutter.jpg` is new.
- site/tools/build.py: `block_review_grid` prints a wrapper per column and reads `col`, `lead`, `tone`, `art` from data/reviews.json. Its `if CURRENT_LEGACY` lines stay for request 014.
- site/data/reviews.json: `reviews_page` gains those keys, a new photo order and no yard photo. `home` and `filter` unchanged.
- global.css, sliders on every page (Home too): `.m-compare__tag.is-covered` fades a tag as the divider reaches it, chevrons spread on hover, no ring after a mouse drag (`.m-compare.is-pointer`). Same in global.js's block, which adds the two classes.
- global.css, every page: `.a-skip` is solid cream with a slate ring (was chrome, with nav text showing at its corners).
- global.css, Reviews: `.o-reviewGrid__col`, real columns from 1025, groups of two cards and a photo at 641 to 1024, photos fill what the cards leave; `.m-quote.-card.-soft`, `.m-quote__item`, two seated cards; `.o-reviewPanel`, before and after on a soft rising panel (was `.o-svcBand`).
- global.css, every banner: `.o-pageBanner .a-hero` 3px left at 1440, for the letters' side bearing. Every later banner gets it.
- site/tools/images.py, RETOUCH: `backyard-lawn-deck.jpg` new. Home's hero shares that original and wasn't recut.
- build/tmp/v3/r014.py: pickup-trash-bags, garage-clutter-before and garage-after off GONE_JOBS, because Reviews uses them (note at the end of request 014).
- Not touched: request 006 says to delete the old Reviews filter block and the `.t-legacy [data-compare]` block from global.js at this move-in. They stay until request 014, because build/tmp/v3/r014.py removes them by exact match and fails if they've gone.

**2026-11-05, P2 batch b: About moved in. Rechecked: Home first, then About.**
- site/tools/build.py: `about` off LEGACY_PAGES.
- site/data/images.json: `old-pickup-driveway` out, its cuts deleted. site/src/stock/old-pickup-driveway.jpg has no job now.
- global.css, About only: `.t-about .o-pageBanner__scrim` from 1025, a taller, lower small wash for a sentence of four rows (was 4.34:1 at 1440, now 5.45). `.o-aboutWork*`, the seated card.
- global.js, every page with `data-call-here`: coming up the screen, the header's number and the phone's bar wait until 60% of a call pill is in view, or 40px of something taller like Book's rail (was any sliver). Going under the header, the pill counts until it has gone.
- global.css, every banner but Donate's: `--truckW` min(38vw, 50vh) on landscape tablets at least 501 tall (was 40vh, so 307px at 1024x768). FAQ, Contact, Commercial and 404 still have to be measured against it.
- site/data/images.json, images.py: `fall-house-drive` new. `service-truck-street` tried and gone.

**2026-11-05, P2 batch b: Donate moved in. Rechecked: Home first (tools/qa.py clean, flow_home.py no problems), then Services, Book, hub and towns, Reviews, About, Donate (their flows no problems), old pages smoke-checked (no console, network, overflow or h1 problems).**
- site/tools/build.py: `donate` off LEGACY_PAGES.
- site/tools/build_trucks.py: `banner_donate_svg` wraps the truck in `.m-truck__rig` and the dresser and bike in `.m-truck__curb`. Rerun: only that partial changes, assets/trucks/ byte-identical.
- site/data/images.json: `dresser-on-street` zoom 2.3, focus 0.5, 0.79, widths to the crop's 1156. Its 1200 and 1600 files deleted.
- global.css, every page: `.m-header__book` from 821 up, on hover margins take back what the padding adds, so the number stays still (was pushed 16px). Its transition gains `margin`.
- global.css, About and Reviews: the taller small wash from 1025 is now both pages' (`.t-about .o-pageBanner__scrim, .t-reviews .o-pageBanner__scrim`). Reviews read 4.47 at 1400x1050, now 5.7.
- global.css, Donate only: `.o-donateBand*` and the page's `.m-notList` rewritten: Yes as the lead, refusals lighter, facts stacked from 1025, photo filling the words' height from 1025, tablets 3 by 2 with Yes beside the list and facts in a row. `--truckW` min(33vw, 54vh, 72rem) from 1025. `--t-section` lower on `.t-donate`. On landscape tablets at least 501 tall: the old truck width, a 7.4rem H1, 32px more under the words. `.t-donate .m-truck__rig`, `.m-truck__curb` under 641.
- build/tmp/p2/banner_check.py: `--gutter N`, the page laid out as if a scrollbar took N px.

**2026-11-05, P2 batch c: the Studio Lead's Donate ruling, then FAQ moved in. Rechecked: Donate (flow_donate.py no problems). FAQ's rules are its own, so no other page was affected.**
- site/tools/build_trucks.py: `DONATE_LOAD = 2`. Donate's truck carries a quarter load, was the high heap less the dresser, bike and lamp. Rerun: only truck-banner-donate.html and assets/trucks/truck-donate.svg change. **assets/trucks/truck-donate.svg no longer matches prototype/revision/,** the first truck file that doesn't. No page prints that file.
- site/tools/build.py: `faq` off LEGACY_PAGES.
- site/data/faq.json: `_note` says v3. Words unchanged, checked against copy.md by script (build/tmp/p2/move_faq.py).
- global.css, FAQ only: `.t-faq .o-pageBanner__scrim` from 1025, its small wash where the sentence is (3.74:1 at 1440, now 4.85; 4.78 or better at every window from 1026 up). `.o-faqList__group:nth-child(even) .m-seatCard__art`, items right and left by turn. `.o-faqList__item.-fridge` 5.2rem, was 5.6, so it stands 23px under the card above, was 14. `.m-faq__title` inline-block, because its hover underline ran the whole row. `.m-faq__a` no right padding under 1025.
- global.css, Donate: the note on `--truckW` only.

**2026-11-05, P2 batch c: FAQ after its Critic rounds. Rechecked: Home first (flow_home.py no problems), then About, Donate, Reviews (flows no problems), FAQ.**
- site/tools/build_trucks.py: `box`, `fridge`, `dresser` take `slab`, on by default, so the load in the sprite is unchanged and Home's truck too. Off for items standing alone, with a soft contact shadow: item-boxes, item-fridge, item-dresser, and the bags, bike, TV, branches and mattress gain one. Donate's curb dresser loses its slab. `mattress` takes `stain` and `soft`. item-mattress.svg leans 5 degrees, new shape. **New file: item-dresser-tv.svg. item-* files no longer match prototype/revision/.** About's and Reviews' cards show the new items.
- site/tools/build.py: `block_faq_groups` rewritten, with `faq_rows`, `faq_heading`, `faq_item`. Its first lines stay as build/tmp/v3/r014.py expects (tried: runs to the end).
- site/data/faq.json: `rows`, `band`, `split`, `lineup`, `art`, one `open`. Words unchanged.
- global.js, every page: the header's number and the phone's bar now wait for the footer's own number (`.o-footer__phone`), not the footer's top edge.
- global.js, FAQ block: `showWhole`, an opened answer comes into view; with reduced motion too.
- global.css, FAQ only: the block is new (`.o-faqBand`, `.o-faqSet*`, `.o-faqRows*`, `.o-faqLoad*`, `.o-faqPair`, `--c-rowLine`), `.o-faqList*` gone; `.t-faq` scrims at three widths; `.m-faq*` as logged in the block.

**2026-11-05, P2 batch c: Contact moved in. Rechecked: Home first (flow_home.py no problems), Book (flow_book4.py no problems), the hub (flow_area.py no problems), Contact.**
- site/tools/build.py: `contact` off LEGACY_PAGES. `block_town_map`: state and line run -2400 to 2400 (was -800 to 1600), for a full-width band. Hub's markup changes, what it shows doesn't.
- global.js, every form: `sendForm` holds one send at a time with `aria-busy`, so a double click or second Enter can't send twice.
- global.css, every form: `[aria-busy="true"] .a-button` steps back. `.m-field__error` carries a round mark, Book too. `.m-upload__remove` ends on the field's edge; `.m-upload__files` 44rem. `.m-field:has([data-either]) .m-field__error` runs under two columns from 641. `.m-form .m-formState` 24px above; `.m-formState` scroll margin 48px, was 32. `.m-form.m-seatCard` fields and chips cream.
- global.css, every page with the band: `.o-estimate__glyph` 96vw on phones, was 170vw, so the ring is whole. Home's band included.
- global.css, Contact and its form: `.o-pageBanner__callLabel` hidden under 380, every banner with a pill; `.t-contact` scrims at three widths, 480px banner; `.o-contactAsk`, `.o-contactMap*`, `.m-form__item`, `.a-section.-oneRow`, `.o-contactMore .m-takes`; `.o-svcBand` no longer on this page. `body:has(.m-formState.is-sent) .o-estimate` hides the band after a send, the only rule of its kind.
- site/src/pages-v2/contact.body.html is now stale. Don't copy it back.

**2026-11-05, P2 batch c: Commercial moved in. Rechecked: Home first, then every moved-in page's flow, old pages smoke-checked (see the end of build/qa-report.md).**
- site/tools/build.py: `commercial` off LEGACY_PAGES. Left on it: 404, privacy.
- site/tools/build_trucks.py: `banner_full_svg`, a full body with no heap, replaces the level-4 truck for `truck-banner-full`, which only this page uses. `sofa`, `armchair` take `ground`; standing alone they get the soft foot and the sofa's cushion notch is filled. Home's review card shows the new item files. The sprite and every load in a truck are unchanged.
- global.js, every form: `clearable` is now shared, moved out of Book's block; request forms mark chips `data-clearable`. Commercial's How often asks the group, so a cleared chip closes it.
- global.css, every form: `.m-field__input.-area` no resize grip, `field-sizing: content`. `.m-upload__file` Remove beside its file. `.m-form .m-formState` left-aligned, smaller, and it now sits above `.m-form__foot` in both pages' markup. `.m-field:has([data-either][aria-invalid="true"]) ~ .m-form__help` hidden.
- global.css, every page: `.m-header__call:focus-visible` offset 6px.
- global.css, Commercial only: `.t-commercial` scrims (phones and landscape tablets share Contact's rules), `.m-form__item.-sofa`, `-armchair`, `-bags`, 120rem card, strip cut to the load.
- site/src/pages-v2/ faq, contact and commercial are stale now. build/tmp/p2/r014_try.py leaves them out. build/tmp/v3/trial.py would copy them back.

## What P2 needs now
- **Trying a page before it moves in:** build/tmp/v3/trial.py <slugs> builds a scratch copy, and build/tmp/v3/serve.py serves it at /_trial/ on the integrator's port. Tests already written for the staged pages, in build/tmp/v3/: flow_trial_book.py, flow_trial_contact.py, flow_trial_commercial.py, flow_trial_404.py, flow_trial_privacy.py, flow_trial_misc.py, faq_rows.py, banner_check.py. Their URLs say /_trial/, so point them at the real page after move-in.
- **All 13 page types build and run clean with everything moved in** (scratch copy): check.py PASS, full-page shots at 1440 and 390 with no overflow, console, network or reveal problems. So the shared parts are enough. What's left on each page is its own.
- **Copy v3 is not on the staged pages yet.** Reviews, Donate, About and Book still have v2 lines (content/copy-changes.md lists them; request 006's note names the Reviews ones). This run was told not to touch pages-v2.
- **Don't copy site/src/pages-v2/_data/reviews.json over.** It's older than site/data/reviews.json and would undo Home's five cards. data/faq.json is already the staged file.
- **Banners:** every staged banner measured at 12 windows. Sentence 4.59:1 or better at phone and tablet windows after the scrim fix, headline 3:1 or better, words clear of the truck. banner_check.py flags "logo" on Contact at 1026 to 1920: that's the line box against the logo's foot, and the painted letters clear it.
- **Open on pages, not shared:** About's photo shows Chevrolet badges (request 007's decision; expect the Critic to cap it). Donate's third fact lands alone on a row (request 008's note).
- **Request 014 last:** build/tmp/v3/r014.py, how to run it is in the request's last section. Keep that file.
- **Screenshots:** the first full-page capture of a short page can miss a photo that's still decoding. regress.py now takes a viewport capture first; do the same in any new script.

- **From P2 batch a, for the next batches.** Serving: the long-lived server on 8841 reached its 2-hour limit in this run and, having the longest limit allowed, wasn't restarted. Scripted checks run through `python build/tmp/p2/with_server.py <command>`, a server for that command's life. A Critic round uses `python build/tmp/p2/serve_until.py <seconds> <file>` in the foreground, at most 10 minutes: tell the Critic its time limit and to save a last screenshot as that file. Tools: build/tmp/p2/sweep.py (17 windows: overflow, stretched photos, wrapped rows, hidden reveals, unloaded images), banner_check.py (scrim and words against the truck, 12 windows), header_check.py, map_measure.py, shot.py, measure.py. All default to 8841. Each page's move-in script is a pattern: move_book.py, move_area.py. Note that `sizes` is often wrong on cover-cropped photos: sweep.py catches it, and `max(40vw, 580px)` works in `sizes`. The Critic can't open `file:` addresses; its browser tool blocks them.
- **Stale now:** site/src/pages-v2/ copies of services, book, service-area and _templates/town. The live sources have moved on, so never copy those over again. build/tmp/v3/trial.py would.
- **Each banner re-measures after the lower crop** (`.o-pageBanner__img` 50% 100% from 1025): Reviews, About, Donate, FAQ, Contact, Commercial, 404. Old numbers in the section above are from before it.

- **From P2 batch b, for the next batches.** Serving: `python build/tmp/p2/serve_until.py 1500 <folder>/last.png` as a background command for a Critic round, and tell the Critic to save that file last and not to open image files directly (it downloads them). Wait in the foreground with build/tmp/p2/wait_for.py. Scripted checks through with_server.py as before.
- **Measure banners on tall windows and with a scrollbar:** `banner_check.py <page> --gutter 15 --sizes 1280x1024,1400x1050,1600x1200,1920x1200,1440x900,1400x900`. Words hang off the left and the truck off the right, and vw counts the bar, so a real scrollbar takes 15px from the gap. Donate's words touched its plant on tall windows and no earlier check saw it. Home's hero, About, Reviews, Services, hub and Londonderry hold on those windows (30px or more).
- **Every banner now has a bigger truck on landscape tablets,** `--truckW` min(38vw, 50vh), 384px at 1024x768. FAQ, Contact, Commercial and 404 still have to be measured against it. Lowell and Londonderry read 2.99 and 4.36 at 700x520, a rare window, not fixed.
- **The header's number:** a `data-call-here` pill counts once 60% of it shows coming up the screen (40px of something taller), and until it has gone under the header going up. flow_book4.py's test follows this. Contact's pill should be checked with build/tmp/p2/m_number.py.
- **Book now's hover** no longer moves its neighbours from 821 up. Any new header piece: check it stays still.
- **tools/qa.py's --section:** pass a leading newline in bash (`$'\n## Reviews'`), or it matches Home's `### Reviews`.
- **Stale now, as well as batch a's:** site/src/pages-v2/ copies of reviews, about, donate, and _data/reviews.json. build/tmp/v3/trial.py would copy them back; build/tmp/p2/r014_try.py leaves them out.
- **FAQ's staged page** may meet `--t-section` trouble no earlier check saw: read H1 against H2 at phone widths (flow_donate.py has a loop to reuse). The old Reviews filter and `.t-legacy [data-compare]` blocks in global.js stay for request 014.

- **From P2 batch c, for the next batches.** 404 and Privacy are the last two staged pages. Serving: as batch b's entry, with one change: **a Critic works from the repository root, so give it full relative names (projects/quickhaul/build/shots/...), or its shots and the file that stops the server land in the wrong folder.** Forms: it may not press Send, so give it a script's captures of the states and tell it so; build/tmp/p2/flow_forms.py takes a page and a folder for them, and works for any page with `data-request`. Warn it off coordinate clicks near the phone's call bar: one clicked the tel: link there by accident. Banners: build/tmp/p2/banner_check.py now prints the 99.5th percentile and the worst pixel, because Critics sample the worst pixel. The three short banners here each needed their own scrim, so 404's will want measuring. sweep.py's `outOfWindow` caught a pill cut off at 320 that no other check saw.
- **What moved the Critic this batch:** FAQ's and Contact's first rounds both failed for the same reason, a stack of plain rounded cards on cream. What worked: a slate band or a full-width picture in the middle of the page, group names in the headline system, the load standing on a fold, the page's lead action in cream. Field wells of the page's cream on a seated card lifted both forms.
- **Noted for the whole-site pass:** on phones on their side the estimate band's 88px heading is bigger than the H1 (52px) on every page whose band sits outside the wrapper. Under 1025 every banner's crop shows mostly barn wall, and two Critics have now said so; the road only reaches the truck from 1025 up. About and Reviews still carry the old form of the small wash.

## Fingerprints at the end of the shared-parts run (2026-11-05)
First 16 characters of each file's SHA-256, from projects/quickhaul/. These replace the freeze's table above as the current state.

| File | SHA-256 |
|---|---|
| design/tokens.css | d9a5b3da1c1896f4 |
| site/assets/global.css | 5eada148efa2137e |
| site/assets/global.js | 9179bc3277452aeb |
| site/src/partials/head.html | a908e0be50841c35 |
| site/src/partials/header.html | b5a4bf87948734ff |
| site/src/partials/footer.html | 2fef41641b6bc38b |
| site/src/partials/trucks/truck-sprite.html | da7790a1bf28bff3 |
| site/src/pages/index.body.html | 9fbdedd9e9227a25 |
| site/src/schema/index.json | 4504b329024ea99b |
| site/src/schema/page.json | 4ee84bdff9bc6542 |
| site/data/faq.json | 9425bbc6b22120d0 |
| site/data/images.json | d1a9791c04b4e0ec |
| site/data/image-manifest.json | fdf324f17d1bdbc0 |
| site/data/prices.json | 7ee1d327c593e44d |
| site/data/reviews.json | de8de734ca7f0e88 |
| site/data/towns.json | 007bd35965d22ea3 |
| site/tools/build.py | 7a81396d1b6e94ea |
| site/tools/build_trucks.py | 9598c53f7e18843d |
| site/tools/check.py | 50ba6bf8c7454e7c |
| site/tools/images.py | 2129947497584761 |
| site/tools/qa.py | a716ef1e33872e8d |
| site/sitemap.xml | be5477a48c00bc9d |
| site/robots.txt | 9cc6c41f99c526fd |

## Fingerprints at the end of P2 batch a (2026-11-05)
First 16 characters of each file's SHA-256, from projects/quickhaul/. These replace the tables above as the current state.

| File | SHA-256 |
|---|---|
| design/tokens.css | d9a5b3da1c1896f4 |
| site/assets/global.css | b1f25632f3f2205f |
| site/assets/global.js | ac6dd710bfae01ed |
| site/src/partials/head.html | a908e0be50841c35 |
| site/src/partials/header.html | b5a4bf87948734ff |
| site/src/partials/footer.html | 2fef41641b6bc38b |
| site/src/partials/trucks/truck-sprite.html | da7790a1bf28bff3 |
| site/src/pages/index.body.html | 13039e5699c8b131 |
| site/src/pages/services.body.html | 5099380a8419e7bb |
| site/src/pages/book.body.html | acc67b2a40977e93 |
| site/src/pages/service-area.body.html | f1272e7519cd374f |
| site/src/templates/town.body.html | b854059f1c0bf392 |
| site/src/schema/index.json | 4504b329024ea99b |
| site/src/schema/page.json | 4ee84bdff9bc6542 |
| site/data/faq.json | 9425bbc6b22120d0 |
| site/data/images.json | 93698230ce626769 |
| site/data/image-manifest.json | 5e962ecf0a566cfe |
| site/data/prices.json | 7ee1d327c593e44d |
| site/data/reviews.json | de8de734ca7f0e88 |
| site/data/towns.json | 007bd35965d22ea3 |
| site/tools/build.py | b09d477fb65fa97e |
| site/tools/build_trucks.py | 9598c53f7e18843d |
| site/tools/check.py | 50ba6bf8c7454e7c |
| site/tools/images.py | 716fba4ef97d4cf9 |
| site/tools/qa.py | a716ef1e33872e8d |
| site/sitemap.xml | be5477a48c00bc9d |
| site/robots.txt | 9cc6c41f99c526fd |

## Fingerprints at the end of P2 batch b (2026-11-05)
First 16 characters of each file's SHA-256, from projects/quickhaul/. These replace the tables above as the current state.

| File | SHA-256 |
|---|---|
| design/tokens.css | d9a5b3da1c1896f4 |
| site/assets/global.css | 475dcc59910734ba |
| site/assets/global.js | 4cd5bf3ed56ace74 |
| site/src/partials/head.html | a908e0be50841c35 |
| site/src/partials/header.html | b5a4bf87948734ff |
| site/src/partials/footer.html | 2fef41641b6bc38b |
| site/src/partials/trucks/truck-sprite.html | da7790a1bf28bff3 |
| site/src/partials/trucks/truck-banner-donate.html | 6708117af5fac400 |
| site/src/pages/index.body.html | 13039e5699c8b131 |
| site/src/pages/services.body.html | 5099380a8419e7bb |
| site/src/pages/book.body.html | acc67b2a40977e93 |
| site/src/pages/service-area.body.html | f1272e7519cd374f |
| site/src/pages/reviews.body.html | ff1989d9fd935bdc |
| site/src/pages/about.body.html | 856a47042bd1e685 |
| site/src/pages/donate.body.html | bb8d5f49e6fbdf9d |
| site/src/templates/town.body.html | b854059f1c0bf392 |
| site/src/schema/index.json | 4504b329024ea99b |
| site/src/schema/page.json | 4ee84bdff9bc6542 |
| site/data/faq.json | 9425bbc6b22120d0 |
| site/data/images.json | 95bd5be74661f7c5 |
| site/data/image-manifest.json | 42ef290e1821aefc |
| site/data/prices.json | 7ee1d327c593e44d |
| site/data/reviews.json | ac28f9b12a7a09d6 |
| site/data/towns.json | 007bd35965d22ea3 |
| site/tools/build.py | 9743f79357d9d851 |
| site/tools/build_trucks.py | fb155be1c8a96e2f |
| site/tools/check.py | 50ba6bf8c7454e7c |
| site/tools/images.py | 7321065a4a2c9a31 |
| site/tools/qa.py | a716ef1e33872e8d |
| site/sitemap.xml | be5477a48c00bc9d |
| site/robots.txt | 9cc6c41f99c526fd |

## Fingerprints at the end of P2 batch c (2026-11-05)
First 16 characters of each file's SHA-256, from projects/quickhaul/. These replace the tables above as the current state.

| File | SHA-256 |
|---|---|
| design/tokens.css | d9a5b3da1c1896f4 |
| site/assets/global.css | 89b0e093c8760902 |
| site/assets/global.js | 9543871e68fb1f43 |
| site/src/partials/head.html | a908e0be50841c35 |
| site/src/partials/header.html | b5a4bf87948734ff |
| site/src/partials/footer.html | 2fef41641b6bc38b |
| site/src/partials/trucks/truck-sprite.html | da7790a1bf28bff3 |
| site/src/partials/trucks/truck-banner-donate.html | 5e0fd8a1e97ced16 |
| site/src/partials/trucks/truck-banner-full.html | 50da0523fcf8184c |
| site/src/pages/index.body.html | 13039e5699c8b131 |
| site/src/pages/services.body.html | 5099380a8419e7bb |
| site/src/pages/book.body.html | acc67b2a40977e93 |
| site/src/pages/service-area.body.html | f1272e7519cd374f |
| site/src/pages/reviews.body.html | ff1989d9fd935bdc |
| site/src/pages/about.body.html | 856a47042bd1e685 |
| site/src/pages/donate.body.html | bb8d5f49e6fbdf9d |
| site/src/pages/faq.body.html | bece9cf1b6f874f1 |
| site/src/pages/contact.body.html | 487d96bab675af29 |
| site/src/pages/commercial.body.html | 129eefde1a99a0ff |
| site/src/templates/town.body.html | b854059f1c0bf392 |
| site/src/schema/index.json | 4504b329024ea99b |
| site/src/schema/page.json | 4ee84bdff9bc6542 |
| site/data/faq.json | a5893247b9fd7a0b |
| site/data/images.json | 95bd5be74661f7c5 |
| site/data/image-manifest.json | 42ef290e1821aefc |
| site/data/prices.json | 7ee1d327c593e44d |
| site/data/reviews.json | ac28f9b12a7a09d6 |
| site/data/towns.json | 007bd35965d22ea3 |
| site/tools/build.py | 5bcf8d8eadcaa714 |
| site/tools/build_trucks.py | 78926dd079618b0b |
| site/tools/check.py | 50ba6bf8c7454e7c |
| site/tools/images.py | 7321065a4a2c9a31 |
| site/tools/qa.py | a716ef1e33872e8d |
| site/sitemap.xml | be5477a48c00bc9d |
| site/robots.txt | 9cc6c41f99c526fd |
