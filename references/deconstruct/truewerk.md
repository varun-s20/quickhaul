# Deconstruction: TRUEWERK (https://truewerk.com)
Scope: whole site for Quick Haul (homepage first screen and every homepage section, header, mega menu, open menu at 390, one collection page, footer). Measured: 2026-11-03, at 1440 and 390. Primary reference.
Screenshots: `truewerk/` folder next to this file. Names: home-1440-*, home-390-*, detail-*, nav-1440-*, menu-390-*, button-dark-shopnow-default/hover, tile-outerwear-default/hover, collection-1440-*.
Method note: computed styles and live DOM for everything that is live. The hero art is a flat image, so its values come from pixel measurement of the image, converted to CSS pixels at 1440. The 390 view is desktop Chromium at 390 wide, not a phone (hover media queries and mouse scripts still run). Values marked "est" are estimates.

## The most important finding
The whole hero is one flat PNG. The hazard stripe, the white slats, the grain, the three-line headline and the lime SHOP NOW block are all baked into a single 2803x1002 image (desktop) and a separate 1200x1600 portrait image (mobile). The hero DOM holds no text, no button, no overlay layer and no pseudo-element art. The whole slide is one link, the image has empty alt text, and there is no hover state on it. So nothing in the hero is live type or CSS. Quick Haul should rebuild these as live CSS and SVG, which is also better for accessibility, sharpness and editing. The numbers below say what to rebuild.

The halftone band is also an image (a repeating PNG tile), not CSS. Everything else (bands, buttons, cards, menu, hex close button) is live HTML and CSS.

## Layout
- Platform: Shopify theme (custom sections), web components, no jQuery, no GSAP, no Lenis, no Swiper. Native scroll.
- Page margin / container: 48px left and right at 1440, content spans full 1344px (x 48 to 1392). No max-width cap seen at 1440; it is a fluid full-width page with 48px margins. At 390 the margin is 20px.
- Section rhythm at 1440 (top to bottom, px): announcement 45, header 100, hero image 515 plus a 40 strip (#F2F2F2) below it, halftone band 40, statement text block 364, product row 876, category tile grid 682, three split bands 866 each, second product row 926, halftone band 40, footer 621. Total page 6848.
- Vertical padding is not a uniform token. Text-only sections have around 90px above the first line (statement block: band top at 740, first text line at 836). Split bands have 40px padding all round (866 band height = 786 image + 2 x 40).
- Split bands (media-with-text): the band is a 2-column grid, 786px column then 524px column, 30px gap, 40px padding, left padding 59.9px. Image is a perfect square 786x786 (54.6% of the 1440 width, 1296x1296 source), object-fit cover, radius 0, no border. Text column is 524px wide with 20px inner padding (504px text measure), vertically centred.
- Band order and alternation: image left on #F5F2ED, then image right on white, then image left on #F5F2ED. The off-white fills the full 1440 width of the band, not just the card. At 390 the band stacks: square image 350x350 over text, 20px padding, off-white and white alternate the same way.
- Category tile grid: 4 equal columns of 328.5px, 2 rows of 288px, 10px gap. Tile 1 spans 2 columns and 2 rows (667x586), tiles 2 and 3 are 667x288 stacked on the right. Label sits 48px from the left and 40px from the bottom of each tile. A soft drop shadow shows under the whole grid in the capture. At 390 it stacks to 350 wide: 310 tall tile, then two 150 tall tiles, 10px gaps.
- Product row: CSS grid used as a horizontal scroller, auto columns 314.25px, gap 24px (row gap 48px), 18 cards in the first row. A thin scroll progress line sits under the cards, plus two 41x41 square arrow buttons with a 1px dark border on the right of that line. At 390 the cards are 289 wide with 20px margin, 309px pitch.
- Collection page (/collections/workwear-pants-shorts-bibs): plain text header, no banner image. H1 at x 48, 60px. Below it a 300px filter column on the left (accordion rows with a plus icon, hairline rules) and a 3-column product grid (315px columns, 24px column gap, 48px row gap) on the right. Product image tiles are #F5F2ED with the product on it. A Filters button (outlined) and a Sort select (outlined) sit above the grid.
- Stacking and overlap: no overlaps in the normal flow. The only overlap is the sticky header over scrolling content, and the hero slats overlapping the strip below them (they are part of the image).

## Type (with the licence of each family)
Families in use:
- BioSans (self-hosted woff2; faces declared at 300 normal, 300 italic, 500, 900). Licence: unknown, treat as commercial (self-hosted custom or purchased face; no open licence found). A bold request (700) falls to the 900 face, so every "bold" caps heading is the 900 cut. Heavy, slightly squared caps grotesque with tight fit.
- Roboto Mono (400, 500, 700; self-hosted). Licence: free (open licence, Apache 2.0). This is the mono body and the button and label face.
- Roboto (400, 500, 700; self-hosted). Licence: free (open licence, Apache 2.0). Used for the generic UI text (footer links, announcements wrapper, rewards link, view-all wrapper).
- Barlow (declared, not loaded on the pages measured). Licence: free (SIL OFL). Ignore.
- Caveat, Kanit, Poppins, Montserrat, Open Sans: loaded by third-party apps (reviews, email popups), not part of the design.

Measured values (1440 / 390):
- Hero headline (raster, est): caps height 38px at 1440, line pitch about 51px, so roughly 54px type at about 0.95 line height. Lines 1 and 2 are the light weight in lime (#D0FD00), line 3 is the heavy weight in white. A small heavy white eyebrow above them has 17px caps height. Tracking and word spacing cannot be read from a raster; visually near-normal tracking and normal word spacing. At 390 the same lockup is centred.
- Statement lead (BioSans 300, none case): 42px / 50px line height, letter spacing -0.42px (-0.01em), colour #1D1D1D. 390: 28px / 34px, -0.28px.
- Section heading (BioSans bold cut, uppercase): 32px / 38px, tracking normal, followed by an em dash glyph as a graphic tail. 390: 24px / 29px.
- Band heading (H3): 36px / 43.2px, uppercase, #1A1A1A. 390: 24px / 28.8px.
- Collection H1: 60px / 66px, letter spacing -1.2px (-0.02em), uppercase. This is the biggest type on the whole site.
- Category tile label: 32px / 38px, uppercase, white.
- Mono body: Roboto Mono 400, 16px / 26px, letter spacing -0.08px (-0.005em), colour #1A1A1A, 504px measure. 390: 14px / 22.4px, -0.07px. Collection intro is the same mono.
- Nav top level: BioSans bold cut, 15px, uppercase, tracking 0.08px (about 0.005em). Mega menu column heads 16px / 20px same style, items 14px BioSans light (weight 200 requested, capitalize), red SALE (#FF0000).
- Announcement bar text: Roboto Mono 12px / 17px, uppercase, tracking 0.24px (0.02em), white on #1D1D1D.
- Product card: badge Roboto Mono 13px / 500 uppercase (white on #1D1D1D, padding 1px 7px, no radius); title BioSans bold cut uppercase; price and attribute lines Roboto Mono 13px / 500; Quick add Roboto Mono 14px / 700 uppercase, tracking 0.7px.
- Buttons (dark): Roboto Mono 700, 16px / 22.4px, uppercase, tracking normal. 390: 14px, tracking 0.56px.
- Mobile category row: Roboto Mono 13px / 500, uppercase, 5px side padding on each item.
- Mobile menu items: BioSans bold cut, 24px / 29px, uppercase.
- Footer: tagline heading BioSans 900 32px / 38px uppercase white, second paragraph BioSans 600 28px / 36.4px, tracking -0.14px, colour #C2BDB8; column heads BioSans bold 16px uppercase (#F4F2EB); links Roboto 13px / 15.6px, 0.26px tracking, #C2BDB8. Legal line Roboto Mono uppercase.
- Case: nearly everything is uppercase. Sentence-style type only in the product links and footer links.
- Weight mixing: the contrast is between light (300) and heavy (900) of one family, plus mono for reading text. The hero mixes light lime lines with a heavy white line.

## Color system
Values are evidence, not for reuse.
- Ink / dark ground: #1D1D1D (announcement bar, text, dark buttons, badges). Footer ground #282827.
- Warm off-white: #F5F2ED (alternate band grounds, product image tiles, halftone strip ground, hero slats). White #FFFFFF is the main page ground.
- Hero strip under the image: #F2F2F2 (cool light grey, a different value from the off-white).
- Accent lime: #D0FD00 for the hero stripe, the hero lime button and the lime headline lines (a previous A/B override on the site used #D6FF00 and #EDFF00 for a real button, but no such button exists on the page now). Lime appears only in the hero art and in a menu promo image; it is not used on any live UI element.
- Red (#FF0000) only for the SALE link and discount lines.
- Mid grey #C2BDB8 for footer text on dark.
- Photo grounds: warm tans, olives and dark denim from the photography do most of the colour work. The UI itself is near black, off-white and white.
- Calls to action: dark #1D1D1D blocks with off-white text. The lime block appears only inside the hero art.

## Motion
Little and quiet. Libraries: none (no GSAP, Lenis, AOS). Web Animations API and CSS transitions only. Reduced motion is handled: the page-transition fade and the scroll-reveal start states sit inside a (prefers-reduced-motion: no-preference) block.
- Load: page sections fade in over 200ms ease-in-out (an A/B test tool's anti-flicker fade). Nothing else on load. The hero does not animate and has one slide (no controls, no autoplay).
- Announcement bar: two messages swap with an opacity and 5px vertical translate, 400ms linear, on a loop of roughly 5s (est, cycle not timed precisely).
- Scroll reveal: product cards fade and rise 15px to 0 over 350ms ease, staggered about 80ms per card. Section headings, text blocks and band images use an opacity reveal (marked reveal-on-scroll, ends at opacity 1). There is no parallax or scroll-linked movement on the home page. (The theme contains a scroll-driven image-reveal block with clip-path, but it is not used on the home page.)
- Hover, image tiles: the photo scales to 1.06 over 1.5s with cubic-bezier(0.22, 1, 0.36, 1), only where the pointer is fine. Label stays put. Pair captured (tile-outerwear-default/hover); the scale reads as a slow push-in.
- Hover, dark button: background and border go to #CFCCC7 and the label to black over 0.15s ease-in-out. No movement, no shadow. Pair captured (button-dark-shopnow-default/hover).
- Header: no scroll state change (no shrink, no shadow, no colour swap).
- Mega menu: opens on hover with the chevron flipping and the active label underlined 1px; the page behind dims. Open state captured.
- No cursor effects, no marquee on the home page, no smooth scroll.

## Interactions
- Header: both the announcement bar (sticky at top 0) and the header (sticky at top 45px, z-index 10) stay pinned at all scroll positions, so 145px of chrome is always visible at 1440. Header is solid white with a 1px hairline (#1D1D1D at 12% opacity) beneath it. At 390: bar 35px plus header 61px, both sticky (96px total).
- Desktop header layout: logo is an SVG image 150x20 at x 48. Nav starts at x 238. Item left edges: MEN 238, WOMEN 334, GEAR 452, WORKWEAR SYSTEM 553, CREW STORE 758, SALE 891, so about 40px between items. Right cluster: Rewards text at 1176, then search icon (23px), account icon (23px), cart icon (30x24) at 1268, 1315 and 1362, about 24px apart, ending at the 1392 margin.
- Mega menu (Men, 1440): full-width white panel about 470px tall below the header with two text columns (FEATURED, WORKWEAR) and two 360x360 square promo images with a bold caption each, aligned to the right half. One of the promo images repeats the lime-and-white diagonal stripe motif in its art.
- Mobile header (390): hamburger (27px) and search (23px) on the left, logo centred at 140x18, account and cart on the right. Below the header sits the horizontal category row (see section anatomy).
- Mobile menu (390): a white panel inset 8px from the left, right and bottom (374 wide, 836 tall), opens over the page with a transparent gap showing the page behind. Top-level rows are BioSans 24px uppercase with a chevron on the right and hairline dividers (row height about 57px). Then a row of 6 social icons (27px), hairline, then Account and Rewards as small Roboto links. SALE is in red.
- Hexagon close button: a 40x40 button (at x 32, y 32) holding an SVG on a 60x65 canvas. The hexagon is a single path, pointy-top, vertices at (30,10), (50,21.06), (50,43.19), (30,54.26), (10,43.19), (10,21.06). Visible hexagon is 40px wide by 44px tall, white fill, with a soft drop-shadow filter inside the SVG. A 24px X icon (two 1.5px-ish strokes, from 6.3 to 17.7 in a 24 box, currentColor #1D1D1D) is centred on it. The hexagon is not clip-path; it is an SVG path with filter shadow.
- Mobile category row: 7 text links (best sellers, pants and shorts, shirts and hoodies, jackets and vests, bibs and overalls, all men's, all women's) in a horizontal scroller, scroll-snap x mandatory, 10px gap, 20px vertical padding, 63px tall total. The row is wider than the screen (953px of content in 390), so the third item is cut off at the right edge to signal scrolling. It is not sticky. It exists only at mobile width (zero height at desktop).
- Product cards: Quick add button on each card, colour swatches, second image on hover (class flag present; the hover image swap was not captured).
- Footer email field: underline only, no box, arrow submit icon. Not submitted.
- Chat widget: a fixed 182x62 pill at the bottom right (about 1238,668 at 1440x900) that overlaps content. It was hidden for section shots and left on in the first-screen and full-page shots.

## Section anatomy
1. Announcement bar (45px, #1D1D1D): centred mono caps message that swaps vertically; sticky. 390: 35px, 15px type.
2. Header (100px, white): logo, six nav items with chevrons, Rewards, three icons. 390: 61px, hamburger layout.
3. Mobile category row (390 only): scroll-snap row of mono labels under the header.
4. Hero (515px image plus 40px grey strip): one clickable flat image with the stripe on the left, headline and lime button baked in, slats along the bottom. 390: separate portrait image 390x521 (3:4), headline and button centred, no left stripe, slats along the bottom.
5. Halftone band (40px, 20px under 1000px wide): tiled halftone image on off-white, full width.
6. Statement block (364px, white): a small caps heading then a very large light-weight sentence at 42px, full 1344px measure. 390: 28px, wraps to about 7 lines.
7. Product row 1 (876px, white): caps heading with an em dash, "view all" mono link with underline on the right, horizontal row of cards on #F5F2ED tiles, progress line and square arrows below. 390: 289px cards, view all drops under the heading.
8. Category tile grid (682px): one tall and two short photo tiles with caps labels. 390: stacked.
9. Split band 1 (866px, #F5F2ED): image left, caps heading, mono paragraph, dark button.
10. Split band 2 (866px, white): image right, small eyebrow label above the heading, same stack.
11. Split band 3 (866px, #F5F2ED): image left, eyebrow, heading, paragraph, dark button.
12. Product row 2 (926px, white): same pattern as row 1.
13. Footer halftone band (40px): same tile image on off-white, then footer.
14. Footer (621px, #282827): left column with a heavy two-line caps tagline, a lighter grey paragraph, an underline email field, 6 social icons, language selector and legal line; right 4 link columns (Resources, Community, Shop, Featured) with small caps heads. 390: link columns collapse into accordion rows with plus icons.
15. Collection page: text header with H1 and mono intro, filters and sort bar, filter column plus 3-column product grid, same footer.

## Signature techniques (3 to 5, rebuildable from scratch)
Build these as live CSS or SVG. The original uses images for all of 1 to 3.

1. Hazard-stripe edge (left of hero). What it is: a flat lime block, 25px wide at 1440 (1.75% of the width), running from the top of the image down to about 268px (52% of the image height), with a hard vertical right edge at 25px. The block is cut into diagonal bars by thin gaps of the underlying photo showing through. Bar geometry at 1440: the gap lines run at about 29 degrees from horizontal, rising to the right. Measured along the vertical, one bar plus its gap repeats every 68.5px, bar 53.5px, gap 15px. Measured square to the stripes: period about 60px, bar about 47px, gap about 13px (lime is about 78% of each period). Colour #D0FD00 (208,253,0). Baked-in extras: a few hairline crosshair rules and registration ticks run across the stripe and photo (1px, dark, partly transparent), and the grain covers the stripe too. How to build: a 25px wide absolutely placed block with `repeating-linear-gradient` at roughly 61 degrees (CSS angle measured from the vertical axis, so 90 minus 29), lime 47px then transparent 13px, clipped to the 25px width and the top 52% of the hero. Or as an SVG with parallelograms so the angle stays exact when the hero scales; since the original scales with the image, size the stripe with vw units (25px = 1.75vw) so the proportions hold.
2. White slats along the bottom edge. What it is: a row of off-white (#F5F2ED, the same value as the next band's ground) parallelograms sitting on the bottom edge of the hero, so the photo reads as cut away by a row of angled planks and the bottom edge blends into the ground below. At 1440: each slat is 29px tall, 164px wide at the flat top edge, with a 46px gap between slats (pitch 210.6px). The first slat starts at x 625 (43% across) and the row runs to the right edge (5 slats, the last cut by the photo). The slat sides lean about 29 degrees from vertical (the top edge is the flat, wider edge, the sides slant down to the right). Through the gaps you see the photo. At 390: slats are about 16px tall, 56px wide, 16px gap, pitch about 72px, first slat at x 109 (28% across), same lean (about 28 degrees). How to build: absolutely placed row at the bottom of the hero, each slat a `clip-path: polygon()` parallelogram or an SVG, in the colour of the next section so they merge. Scale heights and pitches with vw.
3. Halftone band between hero and content (and again above the footer). What it is: an image, not CSS. A 652px wide tile (PNG, 1264x120 source shown at 652 wide) repeats horizontally in a flex row on #F5F2ED; the band height is 40px at 1000px wide and up, 20px below that, and it shows only the top 40px (or 20px) of the tile (object-fit cover, object-position top). Dots are near-black #1D1D1D. Pattern: a staggered (offset-row, roughly 45 degree) dot grid with about 5.5px between dots along a row and about 2.8px between rows. The dots shrink downward: ink coverage runs from about 51% at the top of the tile to about 38% at the 40px crop line and 30% at the tile bottom, with dot diameter roughly 3.1px at the top falling to about 2.7px by the crop line, so it is a gentle gradient halftone, not uniform. The dots are antialiased circles, so it reads as dense grey texture at a glance and individual dots when near. How to build: either an SVG pattern tile or `radial-gradient(circle, #1D1D1D 1.55px, transparent 1.7px)` with `background-size: 5.5px 5.5px` plus a second offset copy for the stagger, then a `mask-image: linear-gradient(black, rgba(0,0,0,.6))` to thin it downward. Same band reused above the footer.
4. Photo-less proof: baked grain and ink-speck texture on the hero. It is not a separate layer. No overlay element, no blend mode, no opacity layer, no filter on the image; the grain is inside the PNG. It looks like dark irregular specks 1 to 3px across plus fine noise, scattered over the sky, the photo and also over the lime stripe, with density fading toward the lower half. Other band photos are clean, so the treatment is only on selected art. To rebuild with a live layer: an SVG `feTurbulence` noise or a tiled 200px noise PNG at `mix-blend-mode: multiply`, opacity about 0.25 to 0.35, over the hero or over flat colour blocks. This is how Quick Haul can get the worn, job-site feel on flat slate and lime areas with no photo.
5. Hard-edged job-site system. Zero radius everywhere (buttons, badges, cards, images, arrows), 2.4px solid same-colour button borders, hairline rules at 12% ink, heavy caps with a light-weight counterpart, mono for reading text, and an em dash after section headings. Dark buttons are plain blocks (#1D1D1D, off-white label, 176x51 at 1440, padding 12px 47px, 2.4px border) that invert to #CFCCC7 with black text in 0.15s. No shadows, no gradients, no rounded anything. Reads as stencilled gear tag, not polished retail.

Other things that add to the hard-wearing feel: product images on warm off-white tiles with tool-room colours (olive, tan, black); mono prices and attribute lines like a spec sheet; square image crops with no frames; sticky 145px dark-and-white chrome that never changes; the hexagon (nut shaped) close button on mobile.

## Buttons, measured
- Lime SHOP NOW (hero): baked into the image, so it is not a button. In-image size 256x44px at 1440 (x 134 to 390, y 496 to 541), flat #D0FD00, square corners, mono caps label with a thin right arrow, label about 13px tall caps, tracking wide (est about 0.1em). No hover state exists (hover tested over the button: no change at all). Rebuild live: 256x44, no radius, lime fill, black mono bold caps, arrow glyph; hover can follow the dark button pattern (invert in 0.15s).
- Dark SHOP NOW (bands): live link. 175.6x51.2px, padding 12px 47px, 2.4px solid #1D1D1D border, radius 0, bg #1D1D1D, label #F5F2ED, Roboto Mono 700 16px / 22.4px uppercase, tracking normal, no arrow, no icon, no pseudo-elements. Hover: bg and border #CFCCC7, label black, 0.15s ease-in-out, size unchanged. 390: label 14px, tracking 0.56px, 171x48.
- Other button styles on the site: outlined small buttons (Filters, Sort) in mono caps, black-stroke 1px; Quick add as bare mono text with a plus; square arrow buttons 41x41 with 1px border.

## Not measured
- Hero art values (headline size, weights, label tracking, button label size) come from pixel measurement of the image, not from fonts. Headline font family inside the image cannot be proven; it looks like the same BioSans light and heavy cuts but this is unverified.
- Exact announcement-bar swap interval (about 5s, est) and exact fade/translate easing beyond the 400ms linear reading.
- Product card hover (second image) not captured; Quick add flow not clicked; cart, search drawer, account, filters drawer, sort dropdown and any product page not opened (no forms submitted, nothing added to cart).
- Only the Men mega menu was opened; Women, Gear and Workwear System panels were not. The 390 collection page and 390 per-section crops were not captured separately (full-page and first-screen shots only at 390). The 390 footer accordions were not opened.
- 390 view is desktop Chromium at 390 wide, not touch emulation: real phone behavior (touch scroll-snap feel, hover removal) not tested.
- No cookie or consent banner appeared and nothing was accepted. Tracking and A/B scripts are present (a visual A/B tool touches the hero); the hero art may vary by visitor or date (the file name shows an April T-line campaign).
- The soft shadow under the category grid is visible in the capture but computed box-shadow reads none on the tiles; the source of that shadow was not traced.
- Reduced-motion behavior was read from the stylesheet, not tested by emulating the setting.
- Licence of BioSans not verified with a foundry. Not checked: line-by-line pixel diff between the 1440 and 390 hero art beyond the stripe, slats and lime measurements above.
