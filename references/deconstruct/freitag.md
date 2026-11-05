# Deconstruction: FREITAG (https://www.freitag.ch)
Scope: header, and mission block (Donate donor). Measured: 2026-11-03, at 1440 and 390.

Role: section donor only. The primary reference is Truewerk. Nothing outside the header and the mission / circular-economy material was measured.

Notes on the capture
- /en redirected to /en_IN (the India English store). All values come from en_IN pages. The Swiss store may differ in copy and promos, not in the components.
- Screenshots: `projects/quickhaul/references/deconstruct/freitag/`. Scrollbar hidden, full scroll pass before capture, mouse parked, chat launcher and back-to-top button hidden for section shots. `home-1440-first-screen.png` keeps them visible (what a visitor sees).
- 390 is a 390px viewport in desktop Chromium, not a phone (hover and mouse scripts still run).
- No cookie banner appeared. A OneTrust container exists but stayed hidden. I never accepted or rejected anything, and submitted nothing.
- Pages used: home (en_IN), /mission (overview), /mission/circular-services/take-back (the reuse page, closest match to Quick Haul's Donate page), /mission/impact-statements.

## Layout

Page frame and grid (all pages)
- Page shell: `main` has 20px side padding at 1440 and about 10.8px at 390. Inside it is one 12-column grid, 1400 wide at 1440 (12 x 116.6px), 369.6 wide at 390 (12 x 30.8px). Gutters are 0. Every "gutter" is a hairline.
- Hairline: 0.8px solid rgb(202,202,202) (#cacaca). Cells draw only a top and a right border; the grid wrapper draws the left border. So the lines are shared, never doubled. The outer right frame line sits at about x=1419 and runs the full page height, through full-bleed photos too (faint over images).
- Cell padding is set per cell, not by the grid: 28px for the intro statement cell, 24px for the page-title cell, 12px for dense text cells and photo-tile cells.
- Column spans at desktop: full width (12), halves (6 x 699.6), thirds (4 x 466.4), quarters (3 x 349.8). At 390 everything collapses to 12 (one column).
- Rows are fully ruled: the cell above supplies the line under it, so the grid reads as a sheet of graph paper with content set in it.

Header at 1440 (total reserved height 69px: 4.3125rem)
- Stack, top to bottom, all `position: fixed`, solid white:
  1. Utility row: 0 to 20.8px (20px plus a 0.8px bottom hairline). Left: breadcrumb trail (FREITAG, then the path) in the mono face. Right: "LANGUAGE (EN)" and "DELIVER TO (CHF)" text buttons. Side padding about 20px.
  2. Nav bar: y=20 to 68, 48px tall (3rem), plus a 0.8px top and bottom rule, so the framed row measures 49px (3.0625rem).
  3. On mission pages only, a second fixed bar: y=69, 64px tall, white, holding a row of tab pills.
- Frame stubs: at the far left and right of the nav bar are two empty cells, 21.3px wide x 49px, with border-y plus a right border (left stub) or left border (right stub). They continue the page's outer frame lines up into the header, so the frame is unbroken from utility row to footer.
- Left cluster: starts at x=33 (21px stub + 12px margin). Two pills, gap 4px.
- Centre: the logo, 144 x 48, centred with left:50% and translateX(-50%).
- Right cluster: three icon circles, gap 2px, ending at x=1406.7 (12px margin from the right stub). The icons are bag, account, search.
- Sticky: yes, fixed, never hides. Scrolled to 600, 1100, 1500 and 2700px: position, size, fill and every rule were identical. No shrink, no shadow, no colour change, no hide on scroll down, no reveal on scroll up. A 56px round back-to-top button appears bottom centre once scrolled.

Header at 390
- Same three fixed layers. Heights unchanged: utility row 20.8, nav bar 48 (49 framed). The logo stays 144 x 48. Frame stubs shrink to 10.9px wide.
- Left: a 32px hamburger circle at x=15 and a 32px language-globe circle next to it. The PRODUCTS and MISSION pills are gone from the bar (they move into the menu). Right: bag and account circles, 32px each. Search moves into the menu.
- Utility row at 390 shows only the breadcrumb (long trails truncate with a leading "..."). The language and delivery buttons are hidden.
- The second tab bar on mission pages did not show at 390 (not in the screenshots).

Mobile menu (390, `menu-390-open.png`)
- A fixed white panel, inset-x 0, from y=68 to the bottom of the viewport (390 x 776), z-index 2000, scrollable inside. Page scroll is locked (body overflow hidden). The header stays visible above it.
- Opens with no animation (transition-duration 0s measured). The hamburger glyph did not change to a close icon in the screenshot.
- Top: search row (circle search icon plus placeholder in grey caps).
- Then section groups, each introduced by a square-bullet label row (PRODUCTS, MISSION) and followed by grey pill links, one per 49px ruled row. Rows are 49px tall, 24px left padding, 0.8px #cacaca bottom rule, edge to edge. Items that open a sub-list carry a thin outline arrow at the right edge (24px from the edge).

Mission block on the homepage (the "cycles" block)
- Sits directly under the full-bleed hero slider. Intro cell: x=20.8 to 1420, 223.9px tall at 1440, padding 28px, top and right hairlines.
- Contents, top to bottom: bullet plus mono label (16px gap below), statement (48px), pill link pinned to the bottom-left of the cell (absolutely positioned, 24px from the bottom, aligned to the text edge at x=48.8).
- Below it, one row of three ruled square cells (col-span 4, each 466.4 x 466.4 at 1440). Inside each cell: 12px padding, then a rounded photo tile 441.6 square, radius 12px. On the tile: a bottom-up black scrim (rgba 0.5 at the bottom, 0.4 at 20%, 0.1 at the top), a white title, and a white pill link. Overlay padding 16px. Title and pill hug the bottom-left.
- At 390: the intro cell is 369.6 x 287.9 with the same 28px padding. The three tiles stack, each full-width 369.6 square, rule between them, same 12px inner pad and 12px radius.

Mission overview page (/mission) and circular-services pages
- Row 1: a 6-column text cell ("OUR MISSION" label plus two short paragraphs, 643px measure) sharing the row with two 3-column photo tiles. Then rows of four 3-column photo tiles (349.8 square cells) with a mono category label (white, square bullet) at the top-left of the tile and title plus pill at the bottom.
- Tab pills (OVERVIEW, PRODUCT STORIES, CIRCULAR SERVICES, ABOUT FREITAG, IMPACT STATEMENTS) in the second fixed bar. Same pill spec as the header. The current page's pill is black with white text.

Take-back page (/mission/circular-services/take-back), the Donate analog
- Order: full-bleed photo (about 720px tall) then page-title cell (24px padding), then a full-width statement cell (28px padding), then a two-column ruled area, 6 + 6 columns (699.6 each). Left column stacks short cells, each cell = square-bullet mono label then body, 12px padding, a hairline between cells. Right column holds one rounded photo tile with white title and pill.
- Body text for each labelled block is short (3 to 6 lines at 1440). Bulleted lists use small solid square bullets.
- At 390 every cell is full width and stacks in reading order. The labels wrap onto two lines with the square bullet staying on the first line.

Impact statements page (/mission/impact-statements)
- Page ground changes to a pale yellow-cream (body background rgb(247,246,212)). Hairlines stay #cacaca.
- Text rows use a 3 + 6 + 3 split: empty ruled cell, a 699.6px text cell, empty ruled cell. This gives a narrow centred measure with visible empty margins that are part of the ruling.
- A third fixed bar holds anchor links (small caps, 32px tall) for the chapters.
- Chapter titles are full-width cells with a 48px regular-weight caps title. Between chapters, a centred pull-statement band in a dot-matrix display face (see Type).

## Type (with the licence of each family)

Families
- AkkStdRg (Akkurat Std Regular), file name AkkStdRg.otf: the whole UI and all display text. Commercial (Lineto). Also loaded but unused in scope: AkkStdLg, AkkStdBd. Only weight 400 is used in everything measured. Even the 48 to 76px headlines are regular weight.
- AkkStdMn (Akkurat Mono), AkkStdMn.otf: labels, breadcrumbs, product meta. Commercial (Lineto).
- FRg ("F-Regular.otf", plus FBd and FLg): FREITAG's own face. It is used on the white pill buttons. It also draws the arrow: the page text contains a "greater-than-or-equal" character and this font renders it as a short arrow. Unknown / proprietary, not a public foundry name I can verify. Treat as not available.
- FHandjet (Handjet Light, file Handjet-Light.ttf): the dot-matrix pull-statements on the impact page. Handjet is an open-licence (SIL OFL) Google Fonts family. Free.
- Third-party widget fonts (Open Sans, Inter, DM Sans, Work Sans): loaded by embedded widgets, not part of the design.

Scale as measured (1440 / 390). The scale is fluid: values land on odd decimals, and the big sizes shrink at 390 while the label and button sizes stay fixed.
- Page title (h1, take-back): AkkStdRg 400, 76.1px / lh 73.9 (0.97) / tracking -1.52px (-0.02em) at 1440; 48px / lh 46.6 / -0.48px at 390. Case: typed in caps in the content (no text-transform).
- Statement (the "cycles" line and the take-back lead): AkkStdRg 400, 48px / lh 46.56 (0.97) / tracking -0.48px (-0.01em) at 1440; 32.4px / lh 31.4 / -0.324px at 390. Typed in caps on the homepage, sentence case on the take-back page (see `reuse-1440-headline-statement.png`).
- Section title cell (impact chapters): 48px, same spec as the statement.
- Lead paragraph / tile title: 23.98px / lh 23.3 to 26.4 / tracking -0.12px for tile titles (white), normal for lead text; lead drops to 18.3px / 20.1 at 390.
- Body: 15.5px / lh 17.05 (1.1) / tracking +0.31px (+0.02em) at 1440; 11.3px / lh 13 / +0.23px at 390. Very small on mobile.
- Mono label (square-bullet label): AkkStdMn 400, 11.28px / lh 13 / tracking +0.2256px (+0.02em), uppercase, black. Same at 390.
- Pill and button label: AkkStdRg (header and tab pills) or FRg (white action pills), 9.904px / lh 7.36 / tracking +0.4952px (+0.05em), uppercase, weight 400. Same at 390.
- Utility row: breadcrumb AkkStdMn 8.46px, tracking +0.34px, uppercase; language and delivery buttons AkkStdRg 8px, tracking +0.32px, uppercase.
- Dot-matrix pull-statement: Handjet Light, 101.3px / lh 99.6 / tracking -1.01px, uppercase, centred, black, in a band 188px tall.
- Inline links in body copy: sage rgb(190,200,175), underlined. Low contrast on white (a weakness, not worth copying).

## Color system
- Ground: white. Impact page ground: pale yellow-cream rgb(247,246,212).
- Text: pure black.
- Hairlines: #cacaca (rgb 202,202,202), 0.8px. One value for every rule, frame line and cell edge.
- Pill fill: #f1f1f1 (rgb 241,241,241) with black text. Current / active pill: black fill, white text. White action pills (on photos and on the intro cell): white fill, black text, soft shadow 2px 2px 10px rgba(0,0,0,0.12).
- Logo tile: black with a white wordmark.
- Icon circles: #f1f1f1 resting, black on hover with a white glyph stroke.
- Photos carry all the colour. A black scrim gradient sits under white tile text. Accent colour beyond that: sage links only.
- Recorded as evidence, not for reuse.

## Motion
- Hover transitions measured at 0s on pills, icon circles, white action pills and the menu panel. Nothing eases: state changes are instant.
- Pill hover (header PRODUCTS / MISSION): no change at all. Computed styles before and after hover are identical (fill, colour, shadow, transform, outline, underline). No ::before or ::after content exists on the pill. Confirmed with the default/hover pair `header-1440-pill-default.png` and `header-1440-pill-hover.png`. State is carried by the active (black) pill, not hover. The same holds for the white action pills (`mission-button-default.png` / `mission-button-hover.png`) and for the photo tiles (`mission-tile-default.png` / `mission-tile-hover.png`): no zoom, no shift, no colour change.
- Icon circle hover (bag / account / search): fill goes from #f1f1f1 to black and the glyph turns white, instantly. Pair: `header-1440-icons-default.png` / `header-1440-icons-hover.png`.
- Scroll: no header change, no reveal animations seen on the mission block or take-back and impact pages while scrolling (I only observed; no timing capture).
- Hero slider on home: auto-advancing slides with three thin progress bars along the top edge and prev / next circles (48px, shown on hover at desktop). Not timed.
- Libraries: Next.js site styled with Tailwind utility classes. No scroll-hijack library (scroll-behavior auto).
- Reduced motion: not checked.

## Interactions
- Header: PRODUCTS and MISSION are plain links to /products and /mission (no hover flyout appeared). Icon buttons open dialogs (cart, account, search). Language and delivery buttons open selectors (not opened).
- Mobile menu: hamburger opens the full-height white panel described above. Pills in it are links; rows with arrows expand a sub-list (not opened). Search sits at the top of the panel.
- Pills with arrows: the white action pills (38px tall, full radius, 22px side padding, arrow glyph then label, 2px gap between them) are buttons inside link wrappers. The arrow points right and is part of the label font.
- Tabs on mission pages are real links; the current one is black.
- No custom cursor seen. No video in the in-scope blocks.
- Chat launcher: a 56px dark round button at the bottom right (x 1354, y 819 at 1440x900), fixed, above content. It overlaps the right end of the tile row and the intro cell at 390. Hidden for section shots.

## Section anatomy
- Header 1440: fixed white stack of utility row (20.8) over a framed 48px nav bar with two grey pills left (82.2 x 31.4 and 72.4 x 31.4), a 144 x 48 black logo tab centred, three 32px grey circles right, plus 21px frame stubs on both ends.
- Header 390: same stack and heights; left becomes hamburger plus globe circles, right keeps bag and account; logo unchanged at 144 x 48; menu opens a 776px-tall white panel of ruled 49px rows with grey pills.
- Homepage mission block 1440: one 223.9px ruled cell (bullet label, 48px caps statement, white pill link pinned bottom-left) over a row of three 466.4px ruled square cells holding rounded 441.6px photo tiles with scrim, title and pill.
- Homepage mission block 390: same cell at 287.9px with a 32.4px statement and a static pill; tiles stack one per row at 369.6 square.
- Mission overview: 12-col ruled grid of a 6-col text cell plus 3-col photo tiles with mono category labels; second fixed bar of tab pills above.
- Take-back page (reuse): full-bleed photo, 76px title cell, 48px statement cell, then a 6 / 6 ruled area of mono-labelled short text cells beside a rounded photo tile with white pill.
- Impact statements: cream ground, 3 / 6 / 3 ruled text rows, 48px chapter title cells, centred dot-matrix pull-statement bands, an anchor-link bar.
- Numbers: no big numeral stats on any page in scope. "33 statements" and similar counts appear only inside body sentences. Impact is carried by statements and ruled text, not counters. (A mass of hidden "0" counters sits in the page for a third-party widget; ignore.)

## Signature techniques (3 to 5, rebuildable from scratch)

1. Boxed raster logo as a header tab. The logo is a flat JPG (531 x 177 natural, 3:1), black background with a white wordmark, shown at 144 x 48 with no CSS padding. The padding is inside the image: the wordmark is roughly 110 to 115px wide inside the 144px box, so about 15px of black on each side and about 18px above and below (estimated from the screenshot, not measured in the file). The nav bar is exactly as tall as the tile (48px), so the tile fills the bar top to bottom and sits over the bar's top and bottom rules, like a tab hung in the row. Rebuild: a fixed link at left 50%, translateX(-50%), width 144, aspect 3:1, above the bar (higher z-index than the bar); bar height equal to the tile height; the tile's black does the "framing", so the logo never has to be cut out. This is the technique that fits an uncut logo mockup: crop the logo mockup to a 3:1 slab of its own slate and let the bar carry the same hairline weight.
2. Hairline-ruled 12-column sheet. A single 0.8px #cacaca value for all rules, drawn as top and right borders on cells so lines are shared; 12 columns with no gutters; the outer frame is a left border on the grid plus a right border on the cells, inset 20px from the viewport (10.8px at 390) and continued into the header as two empty 21px stub cells. Content sits 12 to 28px inside the lines. Cells collapse to one column at 390 while keeping the same rules.
3. One grey pill component used everywhere. 31.4px tall, padding 12 / 14, radius 16px (reads as a full pill), fill #f1f1f1, black 9.9px uppercase label with +0.05em tracking, 4px gap between pills. The same part serves as header nav, mission tabs and mobile menu items. State is by inversion (active = black fill, white text), not by hover. Icon actions use 32px circles in the same grey that flip to black on hover with no transition.
4. Square-bullet mono label over a very large regular-weight caps statement. A solid 8.3px black square (0.52rem), 8px gap, then 11.3px mono caps with +0.02em tracking, sitting 16px above a 48px (32.4px at 390) regular-weight statement with line-height 0.97 and tracking -0.01em, typed in caps. The tight leading and single weight give the block its "set in type" feel; the bullet and mono label supply the small, technical counterpoint. The same label pattern repeats on every text cell on the reuse page, one per cell, so a page of text reads as a form of labelled entries.
5. Rounded photo tiles inside ruled square cells with a bottom scrim. Square cell (ruled), 12px inner pad, 12px-radius photo, bottom-up black gradient (0.5 / 0.4 at 20% / 0.1), white title at about 24px, a white 38px pill with a soft 2px 2px 10px shadow pinned underneath. The ruled cell plus rounded photo mix (sharp lines, soft corners) is a large part of the look. No hover motion on any of it.

## Not measured
- Reduced-motion handling, and hero slider timing and easing.
- The Products and Mission pills' dropdown behaviour on click (they are links; no hover flyout appeared; I did not click through to check for a megamenu).
- The language, delivery, cart, account and search dialogs (not opened). The mobile menu's expandable sub-lists (not opened). The hamburger's open-state icon beyond the screenshot.
- The logo wordmark's exact inner padding (estimated from the screenshot; I did not save or analyse the image file).
- Real touch behaviour: 390 was a desktop Chromium viewport, no touch emulation.
- The second fixed tab bar at 390 on mission pages: not seen in the screenshots and not confirmed either way.
- FRg's licence and origin: unknown; I found no public foundry source.
- Cookie banner: none appeared; the cookie dialog's content and behaviour were not checked.
- The Swiss store (freitag.ch/en redirected to en_IN). Nothing was compared with the CH locale.
- Page load transitions between routes.
- Scratch files `_probe.png`, `_m*.png`, `_t*.png`, `_i*.png` remain in the screenshot folder because this session cannot delete files. They are discard-able contact sheets, not part of the record.

## Screenshots (folder: freitag/)
- Header 1440: `home-1440-first-screen.png`, `header-1440-scrolled.png`, `header-1440-scrolled-sticky.png`
- Header hover pairs: `header-1440-pill-default.png` / `header-1440-pill-hover.png`; `header-1440-icons-default.png` / `header-1440-icons-hover.png`
- Header 390 and menu: `home-390-first-screen.png`, `menu-390-open.png`
- Mission block 1440: `mission-block-1440.png`; hover pairs `mission-button-default.png` / `mission-button-hover.png`, `mission-tile-default.png` / `mission-tile-hover.png`
- Mission block 390: `mission-block-390.png`
- Reuse page 1440: `reuse-1440-headline-statement.png`, `reuse-1440-ruled-blocks.png`
- Reuse page 390: `reuse-390-headline.png`, `reuse-390-statement.png`, `reuse-390-labelled-blocks.png`
- Impact page 1440: `impact-1440-top.png`, `impact-1440-ruled-text-3-6-3.png`, `impact-1440-dotmatrix-statement.png`
- Scout's earlier shots in `references/screens/` were viewed, not redone.
