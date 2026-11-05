# Deconstruction: Muval (https://www.muval.com.au)
Scope: section donor only. Three parts: (1) the hero "What are you moving?" selector bar, (2) the per-city price cards band, (3) the header phone plus primary-button pairing and the 390 drawer. Not the whole site. Primary reference for Quick Haul is Truewerk (see truewerk.md).
Measured: 2026-11-03, at 1440 and 390. The 390 captures are desktop Chromium resized to 390 wide (not a phone): hover media queries and mouse scripts still run, there is no touch emulation, no safe-area inset and no browser chrome.
Screenshots: projects/quickhaul/references/deconstruct/muval/ (listed at the end).
All values are computed styles read from the live page. Colors are evidence, not for reuse.

## Layout

Page frame
- Bootstrap 5 grid on a 1296px content column at 1440 (72px side margins; the selector bar and orange testimonial panel share this width). At 390 the side margin is 12px.
- Header: full-width white bar, `position: sticky; top: 0`, z-index 1020, no shadow and no border. 72px tall at 1440 (16px vertical padding), 54px tall at 390.
- Hero: a rounded photo panel inset 10px from each viewport edge at 1440 (1420 wide, 472 tall, radius 16px from 1400 up, 8px below). Starts at y 80, directly under the header, so there is an 8px white strip between header and photo. The photo has a large orange brand squiggle drawn over it.
- Hero text is centred: h1 64px / 64px line height, weight 700, white, no tracking change; sub line 20px weight 300. At 390 the h1 is 37.3px / 37.3px line height.

1. Selector bar ("launcher")
- One white pill straddling the bottom edge of the hero: 1296 x 92 at 1440, x 72, y 502 to 594. The hero ends at y 552, so the bar hangs 42px below the photo and 50px sits inside it. Hero photo and bar overlap by design.
- Bar: padding 16px, radius 150px (from 1200 up; 8px below that), shadow `0 8px 16px rgba(0,0,0,0.15)`, no border. It carries `margin-bottom: -90px`, which pulls the next section up under it.
- Inside, one Bootstrap row, 6 units in a line at 1440: label, four chips, button. Gutter is 8px (gx-2). Chip width 204, button width 204, label about 188. Every cell is 60px tall.
  - Label "What are you moving?": 17.6px, weight 700, colour #212529, vertically centred on the chips.
  - Four chips: x 300, 512, 724, 936, each 204 wide, 8px gap between them (212 pitch).
  - Primary button: x 1148, 204 wide, same 60px height.
- At 390 the bar becomes a white rounded card (radius 8px, padding 16px, same shadow), 366 wide at x 12, 293 tall, with the label on top, chips in a 2 x 2 grid (each 163 wide, 8px gutter), and the button full width (334 x 57.6) underneath. The card sits at y 387 in the 844 viewport, so the grid and button are all in the lower half of the first screen, within thumb reach.
- At 390 the chip labels do not all fit: "A few rooms" wraps to two lines (the chip grows to 81.6 tall against 57.6 for the others, so the grid goes uneven) and "Something else" swaps to a shorter "Other" label (a second span shown only under 1200). Do not copy the wrap; pick labels that fit 163px.
- Under 387px the type steps down to 14.4px and the chip icons shrink to 16px; under 370px the icons are hidden.

2. City price cards band
- No band heading of its own. It is the carousel directly under the first section's h2 and Google rating line ("Find, compare & book..."). Section padding-top 16px, `mb-5` below.
- Owl Carousel (jQuery 3.7.1) with 8 cards. Wrapper 1272 wide at x 84; the stage has 50px side padding, so the first card starts at x 134 and the last visible card is cropped at the right edge (a peek that signals more). 4 cards fully visible at 1440, then a partial fifth.
- Card: 281.2 wide x 430 tall, 15px gap between cards (marginRight 15, pitch 296.2). At 390: 226.7 wide x 430 tall, one card visible plus a 50px peek of the next; 15px gap.
- Navigation: two 50px circles under the grid, right aligned, 14px apart (x 1235 and 1299 at 1440). Fill `rgba(255,92,0,0.05)`, chevron in the brand orange, no border, no shadow. Prev is at 50% opacity when disabled. No autoplay (the stage transform did not change over 4 seconds).
- At 390 the same nav sits at x 245 and 309, 50px each.

3. Header and drawer
- 1440: logo left at x 72. A row of four plain text links with small caret dropdowns (16px, weight 300, colour `rgba(0,0,0,0.65)`, 8px padding, no pills), then at the right end the phone and button. Phone: x 1082 to 1217, y 20.7, 135 x 30.6. Button: x 1233 to 1368, 135 x 30.6. 16px between them (`ms-3` plus 1px borders). Button right edge lands on the same 72px margin as the selector bar.
- 390: header is the logo left and a 54 x 38 hamburger at the right (x 324 to 378). No phone or button in the bar. See Interactions for the drawer and the floating button.

## Type (with the licence of each family)

- GT Haptik (loaded as `GTHaptik`, fallback `arial, sans-serif`), Grilli Type. COMMERCIAL, believed licensed per seat or per site; evidence only, no file saved. The page loads two faces (400 and 600). Weights 300, 500 and 700 are used in CSS but only 400 and 600 files were seen loading, so the other weights are the browser picking or synthesising the nearest. Treat the visual weight steps as approximate.
- No other families seen in scope. Booking subdomain (book.muval.com.au) uses a different, plain sans for body text (looks like Roboto); not measured.
- Scale in scope (all GT Haptik, letter spacing normal, case as written, sentence case, no uppercase anywhere):
  - Hero h1: 64 / 64, 700 (390: 37.3 / 37.3)
  - Hero sub: 20, 300
  - Section h2: 32 / 38.4, 600, colour #212529
  - Selector label: 17.6 / 26.4, 700 (16px under 1400 wide). At 390: 16, 700
  - Chip text: 17.6 / 26.4, 500 for the first chip and 400 for the rest (the first chip has a medium weight class; the others do not). Under 1400 the chips drop to 16px.
  - Get prices button: 17.6, 700
  - City name on card: 24 / 28.8, 700, white (390: 21.6 / 25.9)
  - Price figure: 21.6 / 21.6, 700, white
  - Price unit ("/half hour", "/m3 average"): 12.8, 400, white at 78% opacity
  - Row label ("Local removalists X"): 12.8 / 16.6, 600, white at 85% opacity
  - Header links: 16, 300. Phone and header button: 14 / 21, 400
  - Drawer links: 20, 600 (nav links), 20, 400 (phone and button)

How price is set against the city name: the city name is the largest line on the card (24px, bold). Each row below has a small bold label (12.8px) over a figure that is bigger than the label (21.6px) with the unit tucked beside it at the small size, baseline aligned. So the number is the loudest thing in each row, the label and unit are quiet. The figure and unit share one baseline, with `line-height: 1` on the figure.

## Color system

- Ground: white (#fff) for the page, header and selector bar. Body text #212529. A very light grey (#f8f9fa area, seen on the booking subdomain) for the booking page ground.
- One accent: brand orange `rgb(255,92,0)` (#FF5C00). Used for the primary buttons (solid), the outline button in the header, the phone link, the nav circles (as 5% tint plus orange chevron), the full-stop on the hero headline, the brand squiggle and the testimonial panel.
- Chips: white fill, 0.8px border `rgb(222,226,230)`, black text and black line icons. No colour on a chip until hover.
- Price cards: sit on photographic ground with a dark scrim, text white. Card base colour behind the photo `rgb(22,32,44)`. Scrim is a vertical gradient on a span: `rgba(0,0,0,0.2)` at top, 0.03 at 20%, 0 at 36%, 0.15 at 55%, 0.52 at 74%, 0.76 at the bottom. So the top of the photo stays clear and the lower 45% darkens enough to hold white type.
- Row divider on card: 0.8px line, white at 28%.
- CTA discipline: orange appears on actions only (plus brand marks). No orange on the chips.

## Motion

Library in use: Bootstrap 5 (offcanvas, modal, buttons), jQuery 3.7.1 with Owl Carousel, animate.css (`animate__tada`, `animate__slideInUp`). No GSAP, Lenis, AOS or WOW found. Document has `scroll-behavior: smooth` inside a `prefers-reduced-motion: no-preference` block. Other reduced-motion rules only turn off Bootstrap form-control transitions; the tada, slide-in and offcanvas slide have no reduced-motion override that I found.

- Selector bar on load: `animation: tada 1s ease 2s both` (animate.css tada). It waits 2 seconds after load and then plays once: a short scale and wobble of the whole bar to draw the eye. Standard animate.css keyframes presumably; I did not read the keyframe values.
- Chips and button hover: 0.15s ease-in-out on colour, background-color, border-color and box-shadow. No transform, no lift.
- City card hover: card translates up 3px (`transform 0.15s`, `box-shadow 0.2s` declared, but the shadow did not change in my read). The hovered row gets a `rgba(255,255,255,0.14)` fill (0.15s on background-color) and its arrow goes from 78% white to full white.
- Owl carousel: drag and click on the nav circles. Default Owl slide. No autoplay.
- Header: button fills on hover with 0.15s colour and background-color transition. The phone link has no hover change at all.
- Drawer (390): Bootstrap offcanvas, `transform 0.3s ease-in-out`, slides in from the right edge (translateX from 390 to 0). Sampled mid-flight at 70ms steps: 362, 217, 52, 0 px. Backdrop black at 50% opacity. Body scroll is locked while open (`overflow: hidden`). Close is the same slide in reverse (74, 211, 359, 390 sampled), same 0.3s, and focus returns to the hamburger (it showed a visible focus ring after closing by mouse click, which looks like an unwanted ring).
- Floating "Get instant moving quotes" button at 390: `animate__slideInUp`, 0.5s ease, delay 0. Hidden until the page has scrolled a few hundred px (hidden at 300px, visible at 500px; threshold is between). It enters from below the screen (y 828 to 780).
- "Get instant quotes" header button opens a Bootstrap modal: 800 wide, 8px radius, `transform 0.3s ease-out` on the dialog, backdrop black at 90%.

## Interactions

Selector chips (1440 and 390)
- Each chip is an `<a>` styled as a Bootstrap button (`btn btn-light btn-lg rounded-8 border btn-white`), not a radio or a toggle. There is no selected state on the home page. Clicking one is a navigation: it opens the booking app at `book.muval.com.au/new/<choice>` (whole_home, few_rooms, few_items; "Something else" and "Get prices" both go to `/new` with no choice) in a new tab. The choice is carried in the URL only.
- Default: white fill, 0.8px `rgb(222,226,230)` border, radius 8px, padding 16px, 204 x 60 at 1440, text black, icon 20 x 22 (about 22 wide for the rooms and items icons), line style, black. Icon to label gap is about 8px (read from the screenshot, not computed). Content is centred as one group.
- Hover: fill goes to `rgba(0,0,0,0.03)` and the border goes from light grey to solid black. Nothing else moves. This is the whole hover. See chip-default-1440.png and chip-hover-1440.png (and the 390 pair).
- Active (mouse down): the same as hover. No extra pressed state.
- Focus: inconsistent in my test. One chip reached by Tab showed the hover fill and border plus a `0 0 0 4px rgba(211,212,213,0.5)` ring (this is Bootstrap's focus-visible rule); the other chips I focused (script focus and Tab) showed no visible change. Treat the focus state as unreliable; do not copy it, build a proper 2px ring.
- Get prices: solid orange `rgb(255,92,0)`, white 700 text, radius 100px (full pill), padding 16px 24px, 204 x 60 at 1440, 334 x 57.6 at 390. Hover: fill goes to `rgb(255,116,38)` (lighter) with a matching border; no shadow, no lift. Tap target is 57.6px or larger everywhere.
- What a pick does: it opens a new tab on the booking subdomain, step "Where are you moving from?". That is one text field for the pickup address, a toggle for "discreet move", a Next button, and an orange progress bar under the header already filled to about 12%. The page has a reviews card at the right. Stopped there. I typed nothing and submitted nothing. Contact details come later and were not reached.
- Alternate entry: the header "Get instant quotes" button opens a modal with a single select ("What are you moving?") and a "Get instant prices" link, so the same question is available on any page without the bar.

Phone and button pair (1440 header)
- Phone: a ghost Bootstrap button (`btn-sm btn-link`), radius 50px, transparent 0.8px border, orange text, 14px, padding 4px 8px, `tel:` link. No hover change. It is not a button shape until you notice the label "Call:".
- Button: `btn-sm btn-outline-primary`, radius 50px, 0.8px orange border, orange text, padding 4px 8px. Hover: fills solid orange, text goes white, 0.15s.
- So the pair is a text link next to an outline pill, both small (30.6px tall), both in the one accent colour. The pair reads as "call or get quotes" without a heavy button. The solid orange pill is held back for the hero.

390 drawer
- Opens from the right as a full-width white sheet (390.4 x 844, no shadow), covering the page. Header row 62px tall: logo left, close X right (32 x 32 hit area, icon 16px at 50% opacity). Below: four dropdown nav items at 20px/600, each row 46px tall (rows at y 78, 124, 170, 216), then a big empty gap, then the pair at the bottom.
- Bottom pair: "Call: 1300 168 825" is a full-width ghost link button, 357.6 x 47.6, radius 50px, 20px orange text, at y 669. "Get instant quotes" is a full-width solid orange pill, 357.6 x 47.6, white 20px text, at y 732.4 to 780. 16px between them (`mb-3`). 16px side padding. The pair block runs y 669 to 780 (111px tall) and sits 64px above the bottom edge of the 844 viewport. The CTA centre is at y 756, in the bottom 13% of the screen.
- It is "pinned" by layout, not by `position: fixed`: the drawer body is a flex column with `justify-content: space-between`, the nav list takes the remaining height (`flex-grow-1`) and the pair sits at the end. On a short phone with the list taller than the space it would scroll. I did not test a short viewport.
- Separate from the drawer: once the visitor scrolls past roughly 300 to 500px, a solid orange floating pill ("Get instant moving quotes", `d-md-none`, so mobile only) is fixed to the bottom of the screen: left 16, right 16, bottom 16, 358.4 x 47.6, radius 100px, 20px text, z-index 99, no shadow. It sits over the page content (it overlaps the testimonial panel in citycards-390.png). So at 390 the primary action is reachable in the thumb zone both from the closed page (floating pill) and from the open drawer (bottom pair).

## Section anatomy

1. Selector bar: one pill that straddles the hero's bottom edge and holds the question, four option chips and a solid orange button in a single row at 1440, stacked as label, 2 x 2 chips, full-width button in a card at 390; chips are links to the booking app, not form controls.
2. Price cards: a draggable carousel of 8 city photo cards, 4 and a half visible at 1440 and 1 plus a 50px peek at 390, each card a full-bleed photo with a bottom scrim, the city name in large type, then two stacked tappable rows (interstate per-m3 average, local per-half-hour average) each with label, figure, unit and a right-aligned arrow; whole row is the link (stretched link).
3. Header pair: left-to-right logo, four text links with carets, ghost phone link and outline button at the far right, aligned to the page margin; at 390 collapsed to hamburger, with the pair moving to the foot of a full-width right-hand offcanvas and a separate floating solid pill appearing after scroll.

Card anatomy (1440, 281 x 430, radius 8px, overflow hidden, shadow `0 2px 4px rgba(0,0,0,0.075)`)
- Layer 1: photo, `object-fit: cover`, absolute, full card.
- Layer 2: scrim span with the gradient above.
- Layer 3: text stack pinned to the bottom (`margin-top: auto`): city name (px 16px, mb 4px), then a 140px links block with two 65.6 to 73.6px rows. Row padding 8px 16px, gap 8px, text left, arrow right in a 24px box with a 16px icon. Rows are separated by a 0.8px white-28% line (the first row has no top line; the second has one).
- Each row is a stretched link, so the click target is the full row (281 x 65.6 to 73.6).
- At 390, the first row's label wraps to two lines ("Interstate removalists" / "Brisbane") when the label is long, which pushes the row taller than the second; the card keeps its 430 height and the rows stay stuck to the bottom.

## Signature techniques (3 to 5, rebuildable from scratch)

1. A selector bar that straddles the hero edge. Build a white pill (radius 150px, padding 16, shadow 0 8px 16px at 15% black) the full content width, then pull it down over the bottom of the hero with a negative margin so about half of it sits on the photo and half on the white page (hero bottom at y 552, bar y 502 to 594). Add `margin-bottom: -90px` so the next section tucks under. At desktop it is a single row: bold label, four equal chips (200 wide, 60 tall, 8px gaps), one solid pill button. Below 1200 it becomes a 2 x 2 chip grid in an 8px-radius card with a full-width button. This one move puts the first conversion question on the first screen without a form block.
2. Chips as links, not controls. Four outline cards that are real links to the next step with the choice in the URL, so there is no selected state, no validation and no JS. Visual recipe: white fill, 0.8px light-grey border, radius 8, icon 20 x 22 line style at 8px from a medium-weight label, hover = fill to 3% black and the border to solid black over 0.15s ease-in-out, nothing else moves. The quiet hover is what keeps the orange button as the only loud thing in the bar.
3. A 2-second-delayed single "tada" on the bar. After load, wait 2s, then scale and wobble the whole selector once (1s) so the eye finds it after the hero has been read. One play only, never loops. Rebuild with a CSS keyframe on the bar, `animation: tada 1s ease 2s both`, and wrap it in a reduced-motion check (the original has none).
4. Price cards that carry the number as the loudest line. Photo card with a bottom-weighted scrim (clear on the top third, 15% by 55%, 52% by 74%, 76% at the bottom), city name in 24px bold, then two tappable rows each with a 12.8px label over a 21.6px bold figure plus a small unit on the same baseline and an arrow at the right. A hairline (white 28%) separates the rows. Whole card lifts 3px on hover and the hovered row washes white 14% with the arrow going full white. Carousel: 50px of stage padding so the next card peeks, 15px gaps, 50px tinted circle nav, no autoplay. Idea for Quick Haul: swap "per half hour" for "from $X per load" by town.
5. Phone as text, action as outline pill, then orange only at the bottom of the thumb zone. Desktop header: a ghost "Call: number" link and a small outline pill with a 16px gap, both orange, same height (30.6). Mobile: a full-width right-hand drawer where the nav list takes all spare height and the pair (ghost phone over solid orange pill, 47.6 tall each, 16px apart) is pushed to the bottom with flexbox, with a separate floating solid orange pill (16px inset left, right and bottom, slides up in 0.5s once the page has scrolled past roughly 300 to 500px) so the booking action is always within thumb reach.

## Not measured

- Keyframe values of the tada animation, and whether it is skipped under reduced motion (I found no override). Not checked in a browser set to reduced motion.
- The final state after the chip click beyond step 1 of the booking app. I stopped at "Where are you moving from?" on purpose, before any address or contact field. The booking tab opened at a 1054 wide viewport, not 1440, so its layout numbers are from that width and are only indicative; I measured nothing on it beyond field presence.
- Chip focus-visible styling: inconsistent across chips, so I could not say which behaviour is intended. No :active state beyond what is above.
- Touch behaviour. 390 is desktop Chromium, so touch scrolling, tap highlights, hover-less states, long press, drag on the carousel by touch and safe-area insets at the bottom of the drawer or floating pill are not checked. The 64px gap under the drawer's CTA and the floating pill's 16px bottom inset are what I read, not how they behave on a notched phone.
- Exact scroll threshold of the floating pill (between 300 and 500px; the script that sets it is not read) and whether it hides at the page bottom or over the footer.
- Header at widths between 1440 and 390 (the breakpoint where nav collapses is Bootstrap lg, 992px, by class name; not tested).
- Dropdown menus of the header links (not opened, out of scope).
- Hero image loading: the hero photo looked soft or low resolution in the 390 shot; I did not check whether it was a lazy placeholder.
- The font files and their licence terms. Only the family name and the two loaded weights were read. Licence is believed commercial (Grilli Type), unconfirmed.
- Whether "Whole home" having weight 500 and the others 400 is a deliberate default selected look or a class slip. It reads as a slip; nothing else distinguishes it.
- The price figures on the cards are the site's live data and may be rotating; not recorded as facts.

## Screenshots (all in projects/quickhaul/references/deconstruct/muval/)

1440
- hero-1440.png: first screen (header, hero, selector bar, start of the next section)
- chip-default-1440.png, chip-hover-1440.png: selector bar, "A few rooms" chip default and hover pair
- chip-focus-1440.png: keyboard focus state on a chip (looks the same as hover; see the focus note)
- getprices-hover-1440.png: Get prices hover
- citycards-1440.png: the price cards band in view under the sticky header
- pricecard-default-1440.png, pricecard-hover-1440.png: Brisbane card default and hover (card element crops; the hovered crop is shifted up by the 3px lift)
- pricecard-hover-1440-card.png: an alternate fixed-position crop of the same card on hover (a second copy of the hover pair; could not be deleted with the tools I had)
- header-default-1440.png, header-cta-hover-1440.png, header-call-hover-1440.png: header at the top of the page, button hover, phone hover (phone shows no change)
- quotes-modal-1440.png: the "Get instant quotes" modal
- after-chip-step1-1440.png: the booking app step reached after a chip click (1054 wide window, see Not measured)

390 (desktop Chromium at 390 x 844)
- hero-390.png: first screen with the selector card
- launcher-default-390.png, launcher-hover-390.png: selector card, "A few items" chip default and hover
- header-390.png: header bar with the hamburger
- drawer-open-390.png: the open drawer with the phone and button pair at the bottom
- citycards-390.png: the price card carousel with the floating "Get instant moving quotes" pill at the bottom
