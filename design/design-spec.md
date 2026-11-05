# Design spec: Quick Haul
Primary reference: Truewerk (references/deconstruct/truewerk.md). Section donors: FREITAG (header logo cell, ruled sheet, mission block for Donate), Muval (load selector chips, per-town price cards), Piece of Cake (quote-plus-call pairing, hours under the phone, review-score row, date-first phone form). Donor sections were not named by Varun; these are the defaults from design/choices.md.
Varun's choices (design/choices.md): concept 1, The work order; type A, Bio Sans with Roboto Mono; palette 1, Slate wall.
Art Director, phase B, 2026-11-03. Hero prototype: prototype/index.html. Tokens: design/tokens.css.

## 1. Concept
Every Quick Haul job comes down to four facts on a ticket: the town, how much junk, the day and the price. The site is that ticket. Truewerk's system is a spec sheet for workwear: heavy and light caps, mono labels, hairline rules, a hazard edge, slats and a halftone band. Here the same parts become a crew's dispatch sheet, in the logo's own chrome and slate instead of Truewerk's lime. The hero states the promise in two caps rows, then hands the visitor the work order: type a town, pick a load (the price changes and a hairline drawing of the logo's dump truck fills to that level), pick a day, book or call. FREITAG's ruled sheet holds every later section the same way, so services, prices, towns and reviews all read as lines on one document. With no client photos yet, the drawing, the type and the ruling carry the site; Shawn's own job photos slot into square ruled frames under one grade as they arrive.

## 2. Source map
| Section (from the brief) | Structure from | Technique taken | What changes for this client | Client assets used |
|---|---|---|---|---|
| Top bar | Truewerk announcement bar | Slim dark mono caps bar, sticky | Carries Shawn's line "Need help booking or have questions? Give us a call" and the number on every page; hours on the right (Piece of Cake's hours beside the phone) | Shawn's words (brief 4) |
| Header | Truewerk sticky header, FREITAG logo cell | Caps nav at about 32px spacing; logo as a ruled cell in the centre | Slimmed to 60px (Truewerk 100); logo cropped from the unchanged mockup file by CSS; call circle plus chrome Book now pill | assets/logo.png |
| Menu (phones, tablets) | Truewerk mobile menu | Panel inset 8px, big caps rows on hairlines, hexagon close | Cream panel, ink hexagon; ends with Piece of Cake's two closing pills and the hours | none |
| Hero | Truewerk banner | Live rebuild of stripe edge, speck grain, registration hairlines, slats; light plus heavy caps | Chrome stripe instead of lime; type-led with a custom hairline truck drawing instead of a photo | logo palette |
| Ticket strip | Truewerk strip under hero, FREITAG ruled cells, Muval selector, Piece of Cake pairing | Ruled cells with no gutters; load chips; button plus text call link of near-equal weight | Real radio chips with checked and focus states; price figure loudest (Muval's figure-over-label); call link is tel: | placeholders (towns, prices, days) |
| Halftone bands | Truewerk | Staggered 5.5px dot grid thinning downward | CSS gradients instead of an image tile; ink on cream | none |
| Services overview (home) | Truewerk category tile grid | One large plus two stacked tiles, labels bottom-left | Six services as ruled cells: large cell for junk removal, then clean outs, then four item cells | job photos when they arrive; hairline item drawings until then |
| Price and service area (home) | Muval city price cards | Card per town with a loud figure and quiet label, carousel with a peek | Square ruled cards, no photo, a "from" price per town; "Can't see your town? Call us" closing card | placeholder towns and prices |
| Featured reviews (home) | Piece of Cake review row, Truewerk product row | Source logo plus score and count, no stars or card; horizontal row with progress line and square arrows | Facebook only, linked out to verify; reviews quoted exactly; row hidden until real reviews exist | Shawn's Facebook reviews (missing) |
| Trust indicators (home) | FREITAG labelled cells | Square-bullet mono label then a short body, in ruled cells | Only claims Shawn confirms (licensed, insured, guarantee are all unconfirmed) | none yet |
| How it works (home) | FREITAG impact rows (3 + 6 + 3) | Narrow centred measure with empty ruled margins | Three stacked ticket lines, not three cards in a row, no numbering | none |
| Before and after (home, gallery) | Truewerk split bands | Square image (54.6% of width) beside a 504px text column, alternating grounds | A native range-input slider in a square ruled frame; Shawn's pairs only | job photo pairs (missing) |
| Estimate band and footer | V10 (Varun), Truewerk footer and halftone | Halftone band above a dark footer; heavy two-line caps tagline | Estimate band on slate with a faint giant arrow-ring glyph from the logo; big phone first | logo glyph; socials (handles missing) |
| Services page | Truewerk split bands | Alternating square image and text column, one per service | Six service sections plus demo, each with "What we take" checklist (Piece of Cake's "what's included") and Book now | job photos when they arrive |
| Booking page | Piece of Cake date-first form, Muval step flow | Date first, then load, then address and details; progress line | Request-then-confirm wording pending Varun's answer; call line beside every step | none |
| Reviews page | Truewerk collection page | Plain text header, filter column plus grid | Review cards as ruled cells quoting Facebook exactly, linked out | Facebook reviews (missing) |
| Donate page | FREITAG take-back page | Title cell, statement cell, 6 + 6 labelled blocks with one photo tile | What can be donated, where it goes once Shawn confirms | none yet |
| About, FAQ, Contact | Truewerk statement block, FREITAG ruled rows | Big light statement; accordion rows on hairlines | Shawn's story; details-based FAQ; map plus hours plus form | none yet |
| Service-area pages | Muval price cards, Truewerk statement | One template per town | Town name in the hero rows, the ticket pre-filled with the town | placeholder towns |
| Commercial enquiry, 404, Privacy | Truewerk collection header | Plain text header | Enquiry form in the ticket's ruling; 404 shows the empty truck bed | none |

## 2b. Section compositions
Grid at 1440: 48px page margins (Truewerk), content 1344 wide, ruled like FREITAG: cells share 1px hairlines, no gutters, cell padding 24px (20 at tablet, 16 at 390). Frame lines run down both page margins through every band. At 390: 20px margins, everything one column.

- Top bar. 32px, full width, ink. Left: Shawn's line plus the number link at x 72; right: hours, ending at 1368. 390: one centred line, "Questions? Give us a call (603) 555-0142". The phone link's hit area is extended to 44px. Sticky from 641px; on phones it scrolls away and only the header sticks (critic r1: fixed chrome took 149 of 844px).
- Header. 60px, slate, hairline under it. Three-column grid: nav left from x 48 (five links, 32px apart, ending near x 440), logo cell centred (88 by 60 between two hairlines, mark 54px tall), call circle and Book now pill right, ending at 1392. 390: Menu pill left, logo cell 64 by 56, Book now pill right.
- Hero. 484px banner at 1440 (Truewerk 515). Copy column 660px from x 48 with 24px cell padding, so text starts at x 72; headline top 72px below the header, two rows; lede 24px under it, 52ch measure. Drawing: 600 by 275, right edge on the right frame line, bottom 48px above the hero edge, its ground line running to the frame line. Stripe on the left edge, 1.75vw wide, top 52%. Slats along the bottom edge from 43% across. No image slot. 390: headline, lede, then the drawing full width bleeding off the right edge, then slats from 28% across.
- Ticket. Directly under the hero, cream, one row of five ruled cells at 1440 (1.15 / 1.6 / 1 / .8 / 1.05 fr): Town, How much junk, Pick a day, Price from, then Book now with the call link under it. Each cell: square-bullet label, 12px gap, a 56px control. The same one row holds from 1025px: between 1025 and 1366 the cells tighten (1 / 1.45 / .95 / .8 / 1.2 fr, 16px padding, load chips with the glyph over the label, 40px figure, 12px call line) so the price and Book now stay on the first screen at 1366x768 and 1100x800 (critic r2). The town field's helper keeps two lines reserved so the strip never jumps, and the town suggestions are a styled listbox in the ticket ruling, not the browser's datalist popup. Tablet: two columns, the action row full width with button and call side by side (Piece of Cake). 390: one column; load chips four across, day chips three across, the button full width with the call link centred under it.
- Halftone band. 40px at 1000 and up, 20px below, full bleed.
- Services overview. Truewerk's tile grid as ruled cells: 4 columns at 1440, the first cell spanning 2 columns and 2 rows (junk removal), two stacked cells right of it (garage and basement clean outs, demo), then a row of four cells (furniture, appliances, mattresses, yard waste). Each cell: square image slot 1:1 with 12px inner padding (FREITAG), label bottom-left 24px in Bio Sans 800 caps, one Book now pill per section, not per cell. 390: large cell first, then a 2-column grid of the rest.
- Price and service area. Section statement (Bio Sans light plus heavy caps, left at x 72), then Muval's row: square ruled cards, 4 visible plus a peek at 1440, one plus a peek at 390; each card holds the town (Bio Sans 800 24px caps), state label, and "from" figure (Bio Sans 800 40px) with the unit in mono 12px; the last card is "Can't see your town? Call us". Square arrows under the row, right-aligned, with a progress hairline (Truewerk product row).
- Featured reviews. Piece of Cake's score row first (Facebook logo, score and count, linked out, no stars) once a real rating exists; then a horizontal row of ruled quote cells (Truewerk product row pitch, 314 wide at 1440, 289 at 390), each quote exact with the reviewer's name and date as given. The section is not built until real reviews arrive.
- Trust indicators. A single ruled row inside the reviews section, cells of square-bullet label plus two lines of body. Only confirmed claims; with none confirmed the row is left out.
- How it works. FREITAG 3 + 6 + 3: the outer cells are empty ruled margins, the middle 6-column cell holds three stacked ticket lines (a mono label for the stage, one Bio Sans 600 line, one mono sentence), hairline between each. No numbers, no icons. 390: full width.
- Before and after. Truewerk split band: a square frame 786 wide (54.6%) beside a 524 column with 20px inner padding, alternating cream and white grounds; the frame holds a native range slider over one pair. 390: square frame 350 over the text.
- Estimate band (V10). Slate, centred heading in light plus heavy caps, one Book now pill and the call line under it, a faint giant arrow-ring glyph redrawn from the logo at 7% behind it. Padding 160 above and below at 1440, 96 at 390.
- Footer. Halftone band, then ink with grain: left column with the big tappable phone (26px/700, underlined) and email, then a heavy two-line caps tagline (Truewerk footer), four short link columns right, social pills, a fact line once Shawn gives one, Back to top, "Created with love by Digital Heroes". 390: phone first, link columns as accordion rows (Truewerk 390), never a long centred list.
- Inner banner (all inner pages). Compact slate banner 440px at 1440, the stripe and slats kept, headline rows sized off the column, no breadcrumbs (anti-slop), one line of lede.
- Services page. One Truewerk split band per service, image side alternating, square frame 786 and a 504 text measure; inside the text column: heading in light plus heavy caps, a mono paragraph, a "What we take" checklist with small square bullets (FREITAG) in two columns, Book now plus the call link. Demo gets its own band on slate.
- Booking page. Ruled ticket at full width: date first (inline calendar under the field, 39px day cells as Piece of Cake), then load chips, then address, junk details and photo upload, then contact. A progress hairline across the top (Muval). The call line sits in a fixed right cell at 1440 and under every step at 390.
- Reviews page. Truewerk collection layout: text header, a 300px filter column (stars, service) on hairline rows, a 3-column grid of ruled quote cells. 390: filters collapse into one row of chips.
- Donate page. FREITAG take-back order: title cell, full-width statement cell, then 6 + 6: left a stack of labelled cells (what we can donate, what we can't, where it goes, how to ask), right one square photo tile. 390: all stacked in reading order.
- About. Truewerk statement block (light 42px sentence across the full measure) then one split band with Shawn's photo once he sends one.
- FAQ. Accordion rows on hairlines (Truewerk filter rows with a plus), questions in Bio Sans 600 caps, answers in mono, `<details>` elements.
- Contact. Split band: map at the square frame size, contact cells (phone, hours, area) and the quote form in ticket ruling.
- Service-area pages. Inner banner with the town name in the heavy row, the ticket below it with the town pre-filled, then the price cards and reviews from that town.
- Commercial enquiry. Inner banner, ticket-ruled form. 404: inner banner with the empty truck bed drawing and one Book now.
Compositions invented without deconstruction support: the truck drawing (no reference has one; it stands in for the missing photo), the ticket's five-cell split (reference cells are 12-column spans; the fr split is mine), and the How it works stacked lines (FREITAG's 3 + 6 + 3 row is measured, the stacked content inside it is mine).

## 2c. Image direction
- Crop by focal point. Every photo slot is square 1:1 (Truewerk's split-band and tile crops). The hero has no photo slot. Within a section, every image uses the same ratio.
- Full-bleed is kept for the strongest single job photo when it exists (the before-and-after split band can go full-bleed at 390). Never a small image floating in a large empty area: an image fills its ruled cell to the 12px inner padding.
- One grade for every photo: a slight cool shift toward the slate (hue 219), saturation down about 15%, contrast up about 10%, and the same speck grain as the hero at reduced opacity. Phone photos of real jobs, imperfect is fine (brief, proposal term 06). Before and after pairs share the same crop and the same grade.
- Until Shawn's photos arrive: no stock (brief) and no visible placeholder labels (anti-slop). Image slots show hairline drawings in the truck drawing's style (1.25px chrome lines on slate, halftone fills): a sofa, a fridge, a mattress, yard bags, a garage shelf. The before-and-after section and the photo tiles are left out of the build until real pairs exist, rather than drawn. Varun to confirm (decision 3).
- Logo: the unchanged mockup file, shown only as the cropped mark in the header cell, at a quarter of its native pixels or less (mark 56px tall at 1440, 50px at phone sizes), clipped to a hard circle at the badge edge so none of the screenshot's wall shows (critic r2). The menu shows the same circle on cream. It cannot be shown larger until Shawn sends the original file.

## 3. Tokens
Values live in design/tokens.css (pasted into the first :root block of global.css).
- Palette, from the logo's pixels (phase A sampling): slate #343D4E (wall: hero, header, dark bands), ink #0F141C (mark shadow: top bar, text on light), chrome #D5D4D3 (accent: stripe, CTA pill on dark, focus on dark, lede), chrome mid #81858C (outlined pill and circle borders on dark, registration marks; never text). The truck drawing's strokes are chrome at 75% (4.93:1 on slate), raised from chrome mid after critic r1 found the drawing too faint, cream #F7EFEC (headline on dark, ticket and light bands), steel #4A5263 (secondary text on cream, derived by darkening the slate toward ink).
- Contrast: cream on slate 9.62; chrome on slate 7.38; ink on chrome 12.48 (CTA pill); ink on cream 16.28; slate on cream 9.62 (slate pill and chip text); cream on ink 16.28; chrome on ink 12.48 (top bar); steel on cream 6.91; chrome mid is 2.95 on slate and 3.27 on cream, so it is never text. Measured over the rendered hero ground (text hidden, 6 zones each): headline worst 9.62, lede worst 7.38. The grain only darkens the slate, so no scrim is needed.
- Type: Bio Sans (Dharma Type), weights 300, 600 and 800, loaded as .otf; Varun's decision to use it; web licence not confirmed; woff2 conversion not yet decided (needs a package install). Roboto Mono (Apache 2.0) 400, 500, 600 for body, labels and buttons; loaded from Google Fonts in the prototype only, to be self-hosted as woff2 in the site build. Hero headline min(12rem, 17cqi) at .9 line height; section statements min(7.2rem, 11cqi); price figure 48px (40 at 390); day numbers 22px; menu rows 24px; nav 13px Bio Sans 600 caps, tracking .04em; body 16px/1.625 (15/1.6 at 390); buttons 14px/600; labels 11px caps, tracking .08em; top bar 12px caps (11 at 390).
- Spacing: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Margins 20 / 32 / 48. Cell padding 16 / 20 / 24. Bar 32, header 56 / 60, control 56, button 44, halftone 20 / 40.
- Radii: pills 44 (buttons), chips 30; every frame, tile, image, card and the ticket square (0).
- Motion: Truewerk's curve cubic-bezier(.22,1,.36,1) for every long move; ease-in-out for state changes. UI 150ms, nudge 400ms, breathe 1000ms, rise 700ms, reveal 1100ms, stagger 90ms, fill 1200ms, menu 500ms.

## 4. Components
- Top bar: Truewerk's announcement bar, static (no message swap, no endless motion). Sticky with the header.
- Header: Truewerk's sticky header, slimmed; never changes on scroll (Truewerk and FREITAG both hold still). The logo cell is FREITAG's. Headline stays the largest thing on screen (quiet-nav rule): tallest header piece 60px of 900.
- Menu: Truewerk's inset panel and hexagon close, a real dialog (inert page, focus trap, Escape, focus return). The panel is always opaque and wipes down (clip, 500ms), the links rise in after it lands; the client's mark sits top right in place of a text title.
- Phone action bar: brief's mobile Book and Call bar; appears only after the ticket's own buttons scroll away (Muval's floating button timing), never on the first screen.
- Hero: Truewerk banner devices rebuilt live; V1 light plus heavy caps headline, no full stop, no colour change, no italics.
- Buttons: V9 pills, Roboto Mono 600 sentence case, arrow, hover breathes 8px each side, arrow nudges 8px, sheen to 10%, press .97. Chrome on dark, slate on cream.
- Chips: V3 outlined pills as real radios (Muval chips rebuilt with states); checked fills slate; hover outlines solid (Muval hover).
- Call link: Piece of Cake's text-only secondary with a phone glyph, tel: only.
- Labels: mono caps with FREITAG's square bullet, for field names and fact labels only, never as section eyebrows.
- Cards: square ruled cells (FREITAG), never rounded, no shadows.
- Footer: V10 content order on Truewerk's dark footer with the halftone band above.

## 5. Motion
- Load, once: headline rows rise out of their masks (108% to 0, 1100ms, Truewerk curve, 90ms apart, from 150ms); the lede and each ticket cell fade and rise 15px (700ms, from 350ms, 90ms apart); the drawing fades in (900ms from 500ms) and the load inside the bed rises to the 1/8 line (1200ms from 900ms). Starts when Bio Sans is loaded, 700ms failsafe.
- On interaction: picking a load slides the bed fill and the dashed level line to that level (1200ms). Buttons, chips and links as in section 4.
- In-view reveals for later sections: fade and rise 15px (700ms), cards staggered 90ms (Truewerk's 80ms card stagger, lengthened). Image tiles push in to 1.06 on hover over 1.5s (Truewerk). No parallax, no scroll-linked motion, no endless loops.
- Reduced motion: everything shows at once, the fill sits at its level, no breathing pills, no menu slide. Hover changes become instant colour changes.

## 6. Mobile (390)
- Top bar: one short line that scrolls away. Header (sticky): Menu pill, logo circle, Book now pill, all 44px; the call circle moves to the top bar and the action bar. Header Book now stays visible while the action bar shows (brief: always in the header), so Book now appears twice once the visitor is past the ticket (a decision for Varun in design/handover.md).
- Hero: headline about 54px in two rows, lede 15px, drawing full width under the lede with the gauge labels hidden (too small to read), slats from 28%. No stripe (Truewerk drops it at 390).
- Ticket: one column in the order Town, Load, Day, Price, Book plus call. First screen shows the headline, lede, drawing and the top of the ticket; Book now is always in the header.
- Later sections: one column; tile grid becomes large cell then 2 across; price cards one plus a peek; split bands stack image over text; footer link columns become accordion rows.

## 7. Asset plan
- assets/logo.png: header logo cell (prototype/assets/images/brand/quickhaul-logo.png, a byte-identical copy). Gap: the original PNG or a vector, needed for any logo larger than about 110px wide, for the favicon and for the footer glyph.
- Bio Sans .otf (Light, SemiBold, ExtraBold): prototype/assets/fonts/. Gap: woff2 conversion and the web licence.
- Job photos, before-and-after pairs, Shawn's photo: none. Note to the client through Varun: phone photos of real jobs, before and after from the same spot. Until then, hairline drawings in the services cells, and the before-and-after section left out.
- Facebook reviews and rating, social handles: none. Reviews row and social pills wait for them.
- Facts (phone, hours, towns, prices, trust claims): placeholders, all in content/placeholders.md.

## 8. Anti-slop check
- Breadcrumbs: none on the homepage or inner banners.
- Heading left, body right as the default layout: not used; split bands pair an image with text, the ticket is a ruled strip, statements run full measure.
- Italics or serif accent words: none; the italic Bio Sans files are not loaded.
- Generic typography: Bio Sans and Roboto Mono are both the reference's own faces (Truewerk), chosen by Varun.
- Purple gradients; three icon cards in a row: neither. How it works is three stacked lines, not cards.
- AI attribution: none in code, comments or meta.
- The AI eyebrow: labels are field names on the ticket and fact labels on cards, never a line plus caps above every section.
- Full-stop headlines: none; working headline "Junk out / Space back".
- Em dashes: none in copy, comments or this spec.
- Generic AI copy phrases: none in the working copy.
- Dot-separated keywords and numbered labels: none; no step numbers.
- Off-brand accent CTA with glow: CTAs are chrome or slate pills, no glow, no shadow.
- Invented logo: none; the real file is used unchanged. The footer glyph is redrawn from the logo's own arrow ring, not a new mark (to confirm with Varun when built).
- Outlined footer wordmark: none.
- Robot chat icon: none.
- Visible placeholder labels: none; missing media becomes a hairline drawing or the section waits.

## 9. Conflicts resolved
1. Header: Varun's floating three-piece header (V4, "V+R, unsplit") is allowed only where the reference supports it; Truewerk has a bar, so the primary wins on layout with a slimmed bar (92px of chrome, against Truewerk's 145) to meet the quiet-nav cap.
2. Hero media: V5 wants full-screen footage of the client's work; none exists. Type-led Truewerk banner (484px, primary's proportion) with a custom drawing in place of the photo.
3. Buttons: Truewerk's square mono-caps blocks lose to V9 pills in sentence case. Square corners stay on every frame, tile and the ticket.
4. Headline weights: V1's values are 300 plus 600; Truewerk mixes 300 and 900. The primary's contrast wins (type is not a V-priority area), at 800, the heaviest weight supplied.
5. Motion: Truewerk's motion is short and quiet; the finish pass and V12 ask for masked line reveals and long ease-outs. One load sequence with masked rows, on Truewerk's own curve; everything else stays at Truewerk's tempo. No scroll-linked effects.
6. Ticket placement: Muval's bar straddles the hero edge. Truewerk's slats already cut the hero's bottom edge from 43%, and a straddling strip would cover them. Truewerk wins on layout: the ticket fills the strip under the hero and the slats bite up from it, which keeps the hinge between hero and page.
7. Muval's chips are links with no selected or reliable focus state; ours are radios with both. Piece of Cake's button has no focus ring and its phone target is 20px; ours has a ring and 44px targets (accessibility is never traded).
8. Call pairing: Piece of Cake sets button and call link side by side; the 1440 ticket cell is 204px wide inside, so they stack there and sit side by side at tablet. At 390 stacked, as Piece of Cake does.
9. Palette: Truewerk's lime is not in the logo (V6), so the stripe and accents are chrome. The site is quieter than Truewerk by design.
10. Media gaps: the brief says to use clearly marked image placeholders; anti-slop forbids visible placeholder labels. Anti-slop wins: drawings or no section.
11. Type files: conventions want self-hosted woff2. Bio Sans ships as .otf by Varun's decision (no package install for conversion), and Roboto Mono comes from Google Fonts in the prototype only.
12. Top bar link: the bar is 32px, under the 44px tap target; the link's hit area is extended to 44px instead of making the bar taller.
13. Never taken from Truewerk or the donors: em dash tails on headings, full-stop headlines, two-colour headline lines (Truewerk, Piece of Cake, Muval); Muval's tada wobble; Piece of Cake's accessibility overlay widget.
14. Header Book now on phones (critic r1 asked to hide it while the action bar shows; critic r2 then found the header lopsided): the brief's "sticky header keeps Book Now always visible" is stated by the client, so it stays. Listed for Varun.
15. Ticket one row at every desktop width: the reference (Truewerk) only shows its strip at 1440; tightening the cells below 1367 is mine, to keep the concept's "where, how much, book" on the first screen of common laptops.

## 10. Decisions for Varun (at most 5)
1. Bio Sans: confirm the web licence, and approve fontTools (a package install) to convert the .otf files to woff2, or keep .otf.
2. Body copy in Roboto Mono (pairing A as chosen) on long pages such as Services and FAQ, or Bio Sans 300 for long reading and mono for labels only.
3. Until Shawn sends photos: hairline item drawings in the service cells and no before-and-after section, as proposed here? Or hold those sections empty in the build.
4. The hero ticket shows a "from" price on the first screen. If Shawn will not publish prices, the price cell becomes a "Get a price" step in booking and the drawing stays as the load gauge only.
5. Ask Shawn for the original logo file (the 2.6 MB PNG from Fiverr, or a vector). The mark cannot go above about 110px wide today, and the favicon and footer glyph need it.
