# Deconstruction: Piece of Cake Moving & Storage (https://mypieceofcakemove.com)
Scope: section donor only, four named parts of the homepage (hero quote block, header phone and Instant price, review-score row, and at 390 the date-first form plus the mobile menu's closing pills). Not the rest of the site. Measured: 2026-11-03, at 1440 and 390. Primary reference for the project is Truewerk (truewerk.md); this file only adds sections to it.
Screenshots: `pieceofcake/` folder next to this file.
Method note: computed styles and live DOM for everything. The 390 view is desktop Chromium at 390 wide, not a phone (hover media queries and mouse scripts still run, no touch events). The fixed accessibility widget (left edge, ids starting INDmenu) is hidden in every per-section shot; the two shots named `*-with-widget.png` keep it, as a visitor sees it on load. No text was typed and nothing was submitted. Platform: Avada (WordPress) with WPForms, jQuery, flatpickr. No GSAP, Lenis or Swiper.

## Layout
- Page frame at 1440: announcement bar 36.3px tall, header 125px (pink), hero 629px, review row 124px (white). First screen at 1440x900 therefore ends inside the review row: you see the whole quote block and the review row together.
- Header at 1440: full-width bar, no container cap. Logo box 175x83 at x 34. Six nav words (Montserrat 16px/700, white, caps typed into the text) with 25px between them, starting x 250. Two navy pills on the right: Instant price 197.1x66 at x 996.6 and phone 196.3x66 at x 1218.7, 25px apart, the phone pill ending 25px from the viewport edge. Both pills are 66px high and 197px wide by tuning, so they read as a matched pair. Header is not sticky: it scrolls away (checked at scroll 700).
- Hero quote block at 1440: right column x 806 to 1374 (568 wide), inner measure 538 (x 821 to 1359). Stack from the top, in px: H1 at y 224 (189.75 tall, three lines, 10px margin below), two-line subline at y 424 (45 tall), input 1 at y 497, input 2 at y 568 (45 high each, 71px pitch, so a 26px visible gap), button at y 636 (52 high). Form is 505 wide (x 821 to 1326), narrower than the 538 text measure, so the form edge sits 33px inside the text edge.
- Quote and call row: the Get quote button is flush left at x 821 (212.3x52). The call link is flush right at x 1111.6 to 1326 (214.4x28.9), so its right edge lines up with the right edge of the inputs. Its vertical centre (662.5) matches the button's centre (662). The two items are almost the same width (212 vs 214), so the row reads as two balanced halves with empty space between them.
- Review row at 1440: container 1170 (x 135 to 1305) with 15px gutters, 30px above and below the 60px logos (section is 124 tall). Two columns: lead-in claim in a 3/12 column (292px, x 150) and the four scores in a 9/12 column (x 427.5, 877 wide). Inside, a 750px flex row, space-between, starting at x 540 (97.5px left margin). Items 175, 168, 175, 155 wide, so uneven widths with equal-ish gaps (about 26px).
- Review row at 390: heading centred over a 2x2 grid. Wrap is 394px wide with -17px side margins (flex, wrap, centre). Items 167x41 at x 13 and x 210, rows 71px apart. Logo box shrinks to 40x60 (the 60px SVG is letterboxed). No horizontal scroll (scrollWidth 390).
- Mobile hero at 390: header 80px (pink), then a navy section (30px top and bottom, 15px sides) holding one white card (radius 10, padding 18, x 15 to 375, 729 tall) that replaces the photo hero entirely. The 1440 form (id 6585) is `d-none d-lg-block` and a second, different form (id 9020) is `d-block d-lg-none`. These are two forms, not one reflowed.

## Type (with the licence of each family)
- Montserrat, weights 400, 500, 600, 700, 800 (served from the site's own domain as woff, plus Montserrat-Medium woff2). Licence: free (SIL OFL). Record as evidence only.
- MPCM-Icons (custom icon font, the arrow glyph in the buttons), icomoon, Font Awesome 5 (phone glyph is an inline SVG with the Font Awesome path): icon fonts, not a text face. MPCM-Icons licence unknown; do not reuse.
- Measured at 1440:
  - Announcement bar: 13px/16.25, 400, centred, navy on #FFE3E8, 10px 16px padding.
  - H1: 55px/63.25px, 800, normal tracking, sentence case, 10px bottom margin, three lines on a 538px measure, text white (the h1 box itself computes navy, the visible words are white spans). Ends in a full stop.
  - Subline: 18px/22.5px, 700. Line 1 navy, line 2 white, with the closing full stop navy again.
  - Input text and placeholder: 16px/20.8, 400, text #333, placeholder grey.
  - Get quote button: 16px/16px, 800, normal tracking, label typed in caps ("GET QUOTE", not text-transform), white on navy, plus an up-right arrow glyph.
  - Call link: 17px/28.9px, 700, white, sentence case ("Or get a call from us").
  - Nav: 16px/16px, 700, white, caps typed in.
  - Instant price label: 14px/16.8px, 700 (inline style, so it is smaller than the phone number); phone number 16px/16px, 700.
  - Hours line: 12px/12px, 700, white, centred, no tracking.
  - Review lead-in H4: 20px/30px, 800, pink. Score: 24px/30px, 600, navy. Count: 14px/17.5px, 400, navy.
- Measured at 390:
  - Card H3: 26px/34.58px, 800, navy, with a pink span on "free quote within minutes".
  - Card description: 15px/21.6px, 600.
  - Field labels: 16px/20.8px, 700, navy, red asterisk. Field text 16px, 400.
  - Get quote: 14px/14px, 800, white on pink. Call link 17px/28.9px, 700, navy text.
  - Review lead-in: 20px/30px, 800, pink, centred. Score 20px/25px, 600. Count 13px, 400.
  - Menu top level: 16px/19.2px, 700, navy. Menu pills: 16px/16px, 800, uppercase, white. Hours: 12px, 800, uppercase, navy.

## Color system
- Two colours plus white, used as grounds. Hot pink #FF399A (255,57,154) is the header and hero ground at 1440, and the button and accent colour on white at 390. Navy #1C1C57 (28,28,87; the header pills read #1D1C57) is text, the buttons on pink, the header pills, and the ground behind the 390 card. White is field fill, card, and review row ground. Light pink #FFE3E8 is only the announcement bar.
- The same button flips with its ground: navy on pink at 1440, pink on white at 390 (menu: navy phone pill and pink Get quote pill side by side on white). The accent is never used for two things at once on one ground.
- Review logos keep their brand colours (Google multicolour, Yelp red, Trustpilot green, Thumbtack blue). Evidence only, not for reuse.

## Motion
- Hover: the Get quote button fades to opacity 0.7 over 300ms (transition "all 0.3s ease"). Because the ground is pink, the faded navy reads as a purple and the white label as light pink. Computed background stays navy; the effect is the opacity transition only (confirmed from the running CSSTransition: opacity 1 to 0.7, 300ms).
- Header pills, nav links, the call link and the review logos: no visible hover. Header links run a 200ms border-colour transition on an invisible border, so nothing shows. The call link has no transition at all.
- Nothing animates on load or scroll in the four scoped sections. Libraries: jQuery, flatpickr (date field), WPForms. Reduced motion: three `prefers-reduced-motion` rules exist in the sheets; what they cover was not read.
- Mobile menu: opens as a white panel under the header (absolute, 739px tall, scrolls inside, 17px top padding). The open transition was not timed.

## Interactions
- Get quote (1440): submit button of the two-field form (Moving from, Moving to; both Google Places address inputs, required). Not submitted. Mobile menu Get quote is a plain link to /free-moving-quote/.
- Or get a call from us: a link to /callback/ (the href has a trailing space), not tel:. It goes to a page, so it is a request-a-callback path, not a dial. The page behind it was not opened.
- Instant price: link to /instantquote/ in the header and the mobile header and drawer.
- Phone: tel:2126517273 in the header pill, the mobile header icon, the drawer pill and the footer.
- Review row: each of the four logos is wrapped in an external link (target _blank, rel nofollow noopener). The Google link goes to the "write a review" form (search.google.com/local/writereview), not to the listing; Yelp, Trustpilot and Thumbtack go to the business profile. Only the 60px logo is the link: the score and count text beside it is not clickable, and the logos carry no alt or aria-label. No stars drawn anywhere in the row; the only stars are inside the Trustpilot logo.
- Focus (keyboard): the text inputs show only a 0.8px border that changes from grey to pink at 63% alpha, which is near invisible on the pink ground. The Get quote button has outline style none, so it shows no focus ring at all. The call link shows the browser default double ring (dark and white, 0.8px, 0.8px offset). Tab order is from address, to address, a hidden input, Get quote, the call link.
- Mobile form (390): date field first (flatpickr, text input not native date, calendar icon at left inside the field, 40px left padding). Tapping opens an inline calendar under the field: 308px wide, navy month bar, pink weekday letters, 39x39px day cells, past days greyed out. Then Type of move (select, pink chevron), Moving from, Moving to (both "Enter a location", Google Places). Date focus shows a pink border. Two further fields (home size select, a number input) exist in the form markup but stay hidden; what triggers them was not tested.
- Mobile header: the phone is an icon link of only 20x20px, the hamburger link is 24x17px. The Instant price pill is 146x52.

## Section anatomy
1. Hero quote block, 1440: right-hand column of a pink hero (photo of two people with branded bins fills the left; not scoped). H1, two-line navy and white subline, two stacked inputs, then one row: navy Get quote block on the left, white text call link on the right.
2. Hero quote block, 390: becomes a white card on a navy band under a pink header. Order: three-line H3 with a pink phrase, a two-line description, Date, Type of move, From, To, a full-width pink Get quote (324x50), and the centred call link under it with a 26px pink phone glyph.
3. Header, 1440: logo left, six nav words, then Instant price pill and phone pill, with the hours line hanging under the phone pill.
4. Header, 390: logo (110x52), Instant price pill (146x52), phone icon (20x20), hamburger. The hours line is not shown in the bar; it is only in the open menu.
5. Review row, 1440: lead-in claim at the left, a single row of four logo plus score plus count items across the right.
6. Review row, 390: lead-in centred, items in a 2x2 grid; same logo, score, count pattern with smaller sizes.
7. Mobile menu, 390: white panel, six rows 54px apart with hairline grey rules and chevrons (Storage has none). It ends with two side-by-side 49px pills, a navy phone pill (174x49, with arrow glyph) and a pink Get quote pill (160x49, with arrow glyph), 16px apart, and the hours in small navy caps centred under the phone pill only. The pills follow the list; they are not pinned to the foot of the panel, leaving about 250px of blank white below.

## Signature techniques (3 to 5, rebuildable from scratch)
1. Quote plus call as a weighted pair, not two buttons. A solid block button (52px high, radius 4, padding 18px 45px, one-weight label plus an arrow) sits flush left of the form. A text-only link (a 26px phone glyph in the dark colour and a 17px bold label in white or dark, no fill, no border) sits flush right, edge-aligned with the right edge of the inputs and vertically centred on the button. Make the two items roughly the same width (212 vs 214) so the row feels balanced. The block button is the primary, the glyph plus words is the secondary, and no second colour is needed. Hover fades only the primary (opacity 1 to 0.7, 300ms). At narrow width the button goes full width and the call link is centred under it. For Quick Haul, add a real visible focus ring to both, which this site lacks.
2. Hours as an attached pseudo-element, not a second line of layout. The phone pill is a 66px block. The hours text lives in a ::before on the pill's wrapper: position absolute, left 0, width of the pill, top 7px below the pill's bottom edge, 12px bold, centred. It takes no height in the header, so the header stays 125px, and it cannot drift away from the number. Reuse the same pill in the drawer, where the hours go uppercase navy 12px, 12px under a smaller pill. Pair it with an equal-height, equal-width secondary pill (Instant price) at 25px apart so the header ends in two matched blocks.
3. One component, inverted by ground. The same button spec (radius 4, 800 weight, up-right arrow glyph) is navy on the pink ground and pink on a white card. Build one button with a ground-aware colour token and the page keeps one accent while every button stays high contrast.
4. A logo-led proof row with no stars and no card chrome. A claim lead-in at the left (20px, 800, accent) and four items at the right: a 60px logo mark, an 8px gap, a 24px/600 score and a 14px/400 count stacked beside it. Items are distributed with space-between inside a 750px row. At 390 the same items drop to a centred 2x2 grid with 20px scores and 13px counts. The logo is the link out to the review page (open in a new tab, nofollow). For Quick Haul rebuild with only the platforms that are real (Facebook), keep the link out to verify, and make the whole item (logo and text) the link, not just the logo.
5. A date-first mobile form in a white card. One column, label above every field (16px bold), 56px-high fields at full card width (324px), 26px of visible space between fields, the date first with a calendar icon inside the field and an inline calendar that opens under it (39px day cells), then the type select, then the two addresses, then a full-width 50px button and the call link under it. It is a separate form from the desktop one, so the mobile version can be shorter and put the date (the thing a mover needs first) at the top. Rebuild it as "Pick a day" then "How much junk?".

## Anti-slop tells inside the scoped sections
- Full-stop sentence headline: the 1440 H1 ends "best reviews." and the subline sentences end in full stops. Do not copy.
- Accent-coloured words inside a headline: the 390 card H3 colours "free quote within minutes" pink. The review lead-in is all pink, so it has no word-level change.
- Two colours inside one text block: the 1440 subline is navy on line 1, white on line 2.
- Em dashes: none found in the scoped sections (an ampersand and a hyphen in "7AM-9PM" only).
- Every button carries the same up-right arrow glyph, including the header pills and the menu pills. Consistent, but it is a pattern to ration.
- Accessibility problems to avoid when rebuilding: no focus ring on the button, near-invisible input focus, 20x20 phone tap target, unlabelled review logo links, trailing space in the callback href.

## Not measured
- The /callback/ and /free-moving-quote/ pages (links only; I did not follow them), so I do not know whether the call option opens a form or a modal.
- The two hidden mobile fields (home size, number) and what reveals them; validation and error states; the Google Places suggestion list.
- The open and close timing of the mobile menu, and the submenu open state (only the closed rows and the closing pills were captured).
- The touch hover and tap states: 390 was desktop Chromium, so hover on the mobile pills was not tested.
- What the three reduced-motion rules cover.
- The hero photograph and the pink ground source (which element paints the pink behind the header and hero); not scoped.
- Focus states on the header pills and review logos; hover on the mobile Get quote pill.
- Screenshot caveats: `reviews-390.png` is a viewport capture that also shows the start of the video-testimonial cards below the row (out of scope). `header-1440-scrolled.png` shows the page at scroll 700 to prove the header is not sticky, so it shows content, not the header.
- Screenshot list: home-1440-first-screen-with-widget, hero-1440-first-screen, header-1440-default, header-1440-scrolled, quote-block-1440-default, reviews-row-1440, getq-default and getq-hover, call-default and call-hover, instant-default and instant-hover, phone-default and phone-hover, review-default and review-hover, input-focus-1440, getq-focus-1440, call-focus-1440, home-390-first-screen-with-widget, home-390-first-screen, form-390-top, form-390-bottom, form-390-card-full, form-390-date-open, reviews-390, menu-390-open-top, menu-390-closing-pills. The call-hover, instant-hover and phone-hover pairs look identical to default, which matches the measurements (no visible hover).
