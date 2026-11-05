# Revision direction: Quick Haul (Art Director, round 2, 2026-11-04)
Varun approved the direction at checkpoint R1 and gave notes (design/choices.md, "Checkpoint R1 result"). This file is what the Copywriter and the Developer work from. site/, design-spec.md, tokens.css and handover.md are untouched; the rebuild has not started.

Look at these first (serve projects/quickhaul on any port):
- Homepage: prototype/revision/index.html
- Inner-page pattern: prototype/revision/services.html
- Truck set: prototype/revision/trucks.html
- Without a server: prototype/revision/shots/r2-*.png

Critic results are in section 10.

## 1. How far to simplify
Measured on the built homepage at 1440: 779 words in main, 963 with the chrome, 7,529px tall, 8 bands. Round 1's prototype went to 133 words, which Varun called too little. Round 2 lands between them.

Seen on the client's two references, one look at each homepage, for feel and density only: EasyScrap about 767 words and 29 images, Junk Teens about 569 words and 52 images. What differs from the built site isn't the word count alone. A photo holds nearly every screen, words sit small beside it, corners are round, and the people and trucks look like someone you could call. No layout, image, text or code was taken from either.

**Decision: the work order stops being the site's visual system and becomes one thing, the Book page form.** The idea under it survives in the two places it earns its keep: "how full is the truck?" as the price question, and town, load, day as the booking steps.

**Retired site-wide** (these are what make it read as a sharp spec sheet):
- The five-cell ticket on Home and the town pages.
- The ruled sheet: hairline cells, frame lines down the margins, registration marks, square bullets with mono caps labels.
- The hazard stripe, the slats and the halftone bands.
- Square frames. Images and cards go to Varun's own round corners (V8: 24px; V7: a light band rising over a dark one, 32px).
- Roboto Mono as body text. Body goes to Bio Sans; mono keeps one small job (phone numbers, price units, the review caption).
- The speck grain over photos.

**Kept** (these are the brand, and they are Varun's):
- The palette: slate, ink, chrome, cream, from the logo. No new UI colour (2b decision 1). Colour comes from the photos and from the junk on the truck.
- V1 headlines: caps, light plus heavy, no full stop.
- V9 pills, V10 estimate band and footer, the sticky Book now, the call-only bar on phones.
- Long ease-out motion, one load sequence, a reduced-motion switch.

The site's one recurring character is the logo's truck, redrawn. It parks on the edge of a band, a move of our own, and how full it is answers the price question.

## 2. The new text level (Varun's note 1)
**The rule for every band: one short heading, one or two supporting lines, and at most one short list or three small facts. One picture, one action.** It replaces round 1's "at most one short line". If a band needs more than that, it becomes two bands or the extra goes.

Three kinds of text carry the extra words, so paragraphs don't come back:
- **The lede** (.a-lede): 15 to 30 words under a heading. Never two paragraphs.
- **One line under a photo** (.m-tile__line): 5 to 12 words, on the cream, so the photo stays clean.
- **Short lists and facts:** a list of things goes in one plain line with a bold lead (.m-takes: "We take couches, recliners and dressers"). Small facts (.m-fact, a short title and one line) say how something works. Fact chips (.a-factChip, V3) are for one row of two or three short facts on a page at most: a whole list of them read as a wall of buttons (critic r2-1). No icons, no numbers. Pills are links or actions; a fact chip is the one exception.

Homepage as built, words a visitor can see in main (screen-reader-only text left out, measured in the browser):

| Band | Words | What it holds |
|---|---|---|
| Hero | 30 | Heading, one sentence, two pills |
| What we haul | 104 | Heading, one line, seven photos with a name and one line each, a pill and a link |
| Priced by the load | 92 | Heading, one line, picker, price, note, pill, three small facts |
| Before and after | 36 | Heading, one line, slider with its two tags, a pill and a link |
| Reviews | 42 | Heading, one line, one sample quote in a seated card, who and a link |
| Towns | 50 | Heading, one line, 12 town names, one "can't see your town" line |
| **Main total** | **354** | Target 300 to 400. Was 133 in round 1, 779 built |
| Estimate band | 57 | Sits outside main: heading, one line, three steps, a pill. Main plus this band is 411 |

**Word targets per page.** Words now are read from the built files (text in main, hidden states and screen-reader text left out), so Home reads 712 here against 779 on screen. Only Home and Services are built at this level; the other targets are my judgment for the Copywriter, not measurements.

| Page | Built now | Target in main | Bands (with estimate band) |
|---|---|---|---|
| Home | 712 | **built: 354** (300 to 400) | 8 to 7 |
| Services | 1,005 | **built: 536** (about 500 to 550) | 8 to 8 |
| Book | 202 | about 170 | 2 to 2 |
| Reviews | 269 | about 120, plus the reviews | 4 to 4 |
| Donate | 212 | about 170 | 2 to 3 |
| About | 237 | about 180 | 4 to 3 |
| FAQ | 493 | about 350 | 6 to 3 |
| Contact | 125 | about 110 | 3 to 3 |
| Service area hub | 57 | about 80 | 2 to 3 |
| Town pages (12) | 198 | about 130 | 4 to 4 |
| Commercial | 82 | about 80 | 2 to 2 |
| 404 | 30 | about 25 | 1 to 1 |
| Privacy | 175 | legal copy stays | 1 to 1 |

Services stays the longest page because it holds seven services and the prices: its bands run 16, 11, 62, 51, 120, 101, 118 and 57 words, the long ones being rows of cards or prices. Words stand in for the Copywriter's final copy. They are trimmed from copy.md, prices.json and Shawn's own line, with no new facts. Every number, town and "we take" list is still a placeholder from content/placeholders.md. No trust claims: licensed, insured and guarantee stay on hold, unbuilt.

## 3. The hero and the price band (Varun's notes 2 and 3)
**Hero.** The words now sit on the hero's height and are set in from the left by 8.33vw (120px at 1440): the headline's top moved from y150 to y252 at 1440x900, its left edge from 48 to 120, and the block's middle sits at y470 in a hero whose middle is y486. The truck stays bottom right, at 52vw instead of 57vw, so the lower words clear it. The block is held at the optical centre, a little above the true middle, so the headline clears the load. On phones and portrait tablets the words centre in the space above the truck.
- My reading of "closer to the centre": mainly down to the middle of the height, and in from the edge. A stack on the page's true centre line (V5) would need the truck about 30% smaller to clear it under 900px tall. One value changes the inset (--heroInset). Decision 1.

**Priced by the load.** It now spans the whole band: heading on one row, one line, then the picker edge to edge as one long pill with a ring that slides along it, then price on the left, truck a little left of the middle, three small facts on the right. On phones: picker, truck, price and pill together on one screen, so the truck fills right under your thumb, with the small print last (critic r2-1).

## 4. Page by page, at this level
**Global chrome:** see section 7.

**Home** (built)
- Keep: Hero. What we haul (7 photos, now with one line each). Before and after. Do you come to my town. Estimate band.
- New from a merge: Priced by the load, replacing the ticket's load cell and the price on every town card.
- Reviews: heading, one line, one quote, in a seated card (section 5) with the load's sofa and chair on its edge, in a band of its own. Built with a slot for who wrote it and the date.
- Merge: How it works into the estimate band as three small facts (agreed scope, three steps). Home only.
- Cut: Ticket. Trust row (repeats the hero and Book; the claims stay on hold anyway). Town price cards and their carousel. All multi-sentence section paragraphs.

**Services** (built, and the pattern)
- Keep: Banner, heading and one line, no pills. Junk removal as the lead band. Clean outs as the slate promo. Each service has a "We take" line and its own way to book, as the brief asks: a pill on these two bands, a link naming the job on each card ("Book a furniture pickup").
- Add: jump chips under the banner (the built page's critic asked for an index).
- Merge: Furniture, Appliances and Mattresses into three cards with portrait photos. Yard waste and Demo into two cards; Demo keeps its own heading and anchor.
- Merge: "What we take and what we don't" into a "What we can't take" band: heading, one line, and a marked list in a seated card with a drawn paint can, propane tank and battery on its edge.
- Keep: Pricing, spanning the width, four trucks parked on the fold. Heavy loads, single items and demo pricing become one row of three fact chips (plain lines on phones). On phones each truck stands on its own price.
- Cut: The call line in every band (the number shows once per screen). The long body paragraphs. The banner's second sentence and pills. 45 static chips.

**Book** (the work order's new home)
- Keep: Date, load, address and details, contact, confirmation and error states. The ruling and mono labels can stay here, and only here.
- Add: the three steps as three small facts under the banner. The filling truck and the Home picker on the load step.
- Merge: long step notes into one helper line each.
- Cut: Banner truck (the load truck does that job). Keep Shawn's call line beside every step, word for word.

**Reviews**
- Keep: Banner. One line. Quotes mixed with photos in a loose grid. Before and after: heading, one line, the pairs.
- Merge: "Used us already?" becomes a line and a link at the end of the grid.
- Cut: Filter column (dead with few reviews; both its critic rounds said so).

**Donate**
- Keep: Banner with truck-donate, heading, one line from the statement. One band: big photo, Can as a plain line (.m-takes) and Can't as a marked list (.m-notList).
- Merge: "Where it goes" and "How to ask" into two small facts (destination stays a placeholder until Shawn confirms).
- Cut: The rest of the 74-word statement.

**About**
- Keep: Banner. Slate promo: big photo, "Pick up the phone", a short story of 40 to 60 words.
- Merge: How we work into three small facts, without repeating Home's lines.
- Cut: Statement block (the banner's line says it). Second paragraph. The second call to action.

**FAQ**
- Keep: Short banner (section 5). One list with four small group labels, 11 or 12 questions, each answer one or two lines. Estimate band. A band with no natural picture, so a seated card with one drawn item per group is the option if it reads flat.
- Cut: Repeated pricing answers. The close row (the estimate band under it asks the same thing). The line art.

**Contact**
- Keep: Short banner with the call pill on the first screen (one of the exceptions in section 5). Map with hours beside it. Short form.
- Merge: Commercial cell into one line and a link.
- Cut: Contact cells that repeat the footer. Line art.

**Service area hub**
- Keep: Banner, one line. Map beside town chips by state. "Can't see your town?" line.
- Cut: Repeated price lines.

**Town pages**
- Keep: Banner with the town name, one line, one Book in Town pill (one of the exceptions in section 5: these are landing pages from search). What we haul: heading, one line, shared photo tiles. The price row with four trucks.
- Cut: Ticket. Map (it's on the hub). Paragraphs.

**Commercial:** keep banner, one line and form. Cut the building line art and the form intro.
**404:** keep the empty truck, one line, Book now, three links.
**Privacy:** legal copy keeps its length, same type, no art, plain heading instead of a photo banner.

## 5. The inner-page pattern (set by services.html)
Every inner page is these parts, in this order. Pick the recipes the content needs, and never the same one twice in a row, so the page doesn't read as a template (the built Services page's top critic issue).

1. **Banner.** A colour photo of somewhere a truck could park. Two-row heading and one line (V5), no pills: the header's Book now and number are right there, and on phones the call bar. The words sit like the hero's: on the banner's height, set in by --heroInset. The truck parks on the fold at the right, carrying a load that suits the page. 520px tall at 1440x900, inside V5's 440 to 580, so the next band shows. No breadcrumb, no eyebrow, no tag (anti-slop over V5's list for inner pages: Services isn't a deep page). This is what keeps every page from opening as a smaller homepage (critic r2-1, r2-2).
   - *Short banner:* for utility pages (FAQ, Contact, Commercial), about 440px. My judgment from the Critic's note, not built yet.
   - *Exceptions that carry one pill:* town pages (Book in Town, they are landing pages from search) and Contact (the call pill, with data-call-here).
2. **A cream band rising over it (V7),** opening with jump chips only if the page has more than four sections. On phones the chips are one row you can swipe.
3. **Recipes for the bands:**
   - *Lead:* centred heading and line, one wide photo, then a "We take" line on the left and a filled pill on the right.
   - *Promo (V8):* a slate card, words and one big photo. When stacked, under 1025, the photo goes first.
   - *Cards:* three or two, each a photo, a two-row heading, one line, a "We take" line, and a link naming the job. Portrait photos in a row of three. They share rows, so everything lines up across the cards however each one wraps. A grouping for Services' five services, not a rule: other pages use it only if their content comes in twos or threes.
   - *Slate row:* heading on one row, one line, one row of fact chips, then a row spanning the width with the trucks parked on the fold.
   - *Seated card:* for a band with no photo to carry it. A soft card (slate at 8% on cream) with a few drawn things set down on its top edge, the same move as the truck on the fold. Built twice: Home's review, Services' "can't take". This is the plan for pages with few natural pictures.
4. **Close:** estimate band (heading, one line, one pill, no steps), then the footer. Skipped on Book, Commercial, 404 and Privacy (Privacy: conflict 21).

**Heading sizes, by the kind of band and nothing else:** 88px full-width bands, 64px slim bands, promos and rows of two, 52px rows of three, at 1440. Bold lands on the word a visitor is scanning for: **FURNITURE** removal, never furniture **REMOVAL**.

**Booking links per page:** the header's is always there. Services is the one page where every service gets its own, because the brief asks for it, and even there only the two big bands and the estimate band use a pill. Other pages: one action a band at most, usually the estimate band alone. Never a row of identical pills.

**Text balance:** as section 2. 30 to 60 words for a band with one subject, up to about 120 for a band of cards or prices.

**Truck art, where it belongs:**
- The banner, parked on the fold, standing still. Only Home's truck is piled high and backs in; a truck reversing on every page load would wear thin. Inner trucks just rise with the words, and the load varies: half on Services, and my suggestion for the rest is a quarter on Reviews and town pages, an eighth on FAQ, Contact and About, truck-donate on Donate, empty on 404.
- Prices: the row of four loads wherever prices are listed (Services, town pages). The interactive one on Home and Book only.
- The drawing stands outdoors. Never over an indoor photo. Banner photos are streets and yards for that reason.
- Not in the bands in between, except on a seated card, whose drawings are single items from the load. One truck per screen is the most you should ever see, except the price row.

**Motion:** the same as Home. Headline rows rise out of their masks, then the rest fades and rises 15px, once each. Everything has a reduced-motion off switch.

## 6. Colour photos and trucks
**Photos: no mono grade.** Remove the grade in site/tools/images.py: no desaturation, no tone map, no cool shift, no grain over photos. Crop and resize only, plus the usual small unsharp after a big downscale. Rebuild every derivative and the og image. prototype/revision/tools/build_assets.py is the working example. Unifying treatment: none. A dark wash only where words sit on a photo, sampled, as small as it can be (section 11). Keep the crop rules for plates and badges in placeholders.md. Replace the black and white mattress shot on Home. Every stock image stays must-replace. One retouch, the only one: the fridge's maker badge is painted out in build_assets.py (RETOUCH), under the same no-brands rule as the crops, so the crop can show a whole fridge. (Developer, 5 Nov: no longer the only one. Hover and the slider's ends showed more brand marks than the crops hid, including one the Critic capped the homepage for. Now in site/tools/images.py; listed in content/placeholders.md.)

**Trucks.** One drawing, built by prototype/revision/tools/build_trucks.py into assets/trucks/. It is the truck in the logo: cab-forward, slatted body, tandem rear axle, heap of junk, facing right. Metal like the logo, with the client's real mark on the door. The load is the only colour: Shawn's own list, in the same hand. Our own drawing, nothing traced.

| Where it appears | Built site | Goes to |
|---|---|---|
| Home hero | Hairline schematic with a gauge | truck-full, inline, backs in and parks on the fold |
| Home price, Book load step | Ticket's gauge, chip glyphs | One inline truck: the load lands piece by piece, the body sits lower |
| Services pricing, town pages | Bed-fill glyph | Row of four inline trucks parked on the fold (built on Services) |
| Load chips | 22 by 14 glyph | Cut: the long picker, the truck does that job |
| Inner banners (Services, Service area, FAQ, Reviews, About, Contact, town pages) | banner-art partial | A truck with a load that suits the page, parked on the band edge over a colour photo (built on Services at half a load; section 5 has the rest). Piled high is Home's alone. truck-nose on narrow or tall banners |
| 404 | Banner truck | truck-empty |
| Donate | Dashed drawing with dresser and bike | truck-donate |
| Commercial | Buildings line art | Cut; truck-full parked on a photo (Developer, 5 Nov: a full body with no heap, so "piled high" is Home's alone, as section 5 says. Studio Lead ruled so for Donate, whose row above now means a quarter load with the dresser and bike at the curb; this row follows its reason, and that's flagged in build/progress.md.) |
| Contact, FAQ section art | Line art | Cut on Contact. On FAQ, cut, or one colour item per group on a seated card (item-*.svg, 13 drawn) |
| Home review, Services "can't take" | None | Seated cards: item-sofa and item-armchair; item-paint, item-propane and item-battery (new) |

## 7. For the Developer: the shared parts that change
Round 2 keeps all of this in prototype/revision/assets/global.css and global.js. Lift them as they are.

**Tokens** (paste into tokens.css and the first :root block; each is marked "new" in the CSS)
- Added in round 1: --f-body (Bio Sans), --t-section and --t-body larger, --h-buttonLarge, --r-image, --r-band, --logo, --logoSmall, --e-drop.
- Added in round 2: --t-sectionSmall (6.4rem), --t-card (5.2rem), --t-lede. --c-soft is set on each band, not in :root: steel on cream, chrome on slate.
- New per-section value: --heroInset. New font file: Bio Sans Regular, from the same supplied set.
- Set by the script, not a token: --logoSettled, on the header.
- Colour tokens are unchanged. The seated card's ground is slate at 8%, not a new colour.

**Type:** .a-lede, .a-section with -small and -card, .a-hero with -banner. Three heading sizes only (section 5). Phone numbers are Roboto Mono everywhere (.a-num), the call bar and menu included.

**Header**
- Bar 88px above 1024, 72px on tablets, 64px on phones, capped in pixels past 1440. Five links: Services, Pricing, Towns, Reviews, Donate. About, FAQ and Contact sit in the menu and footer.
- Logo first: 108px round badge at the top of the page, 84px once scrolled. **Changed:** it settles over the first 32px of scroll, tied to the scroll position by global.js rather than a timer, so a hard flick can't catch it half way and sit it on a heading (Varun's confirmed ruling: no collision at any scroll position). Hover and press live on the mark inside it. Sharp ceiling: **a bigger logo needs Shawn's original file or a vector.**
- Top bar cut. Shawn's line and the number sit on the right. No design-preview line now, but **it must come back, or be gated, before any deploy-preview** (brief; choices.md). Its build markers are already in the header partial.
- **Changed in round 2:** the chrome is identical on every page, so Pricing always goes to services.html#pricing and Towns to service-area.html, never to a spot on Home. The current link comes from the address (aria-current, underlined), set in global.js.
- The number shows once per screen: any first-screen pill marked data-call-here hides the header's number and the phone bar while it's in view. Only Home's hero and Contact's banner carry one. Other banners have no call pill, so the header's number and the phone bar show from the start.

**Menu:** any link inside it now closes it, because a same-page link wouldn't otherwise.

**Call bar (phones):** still call-only. Shows once the first screen's pill has gone, or from the start on a page with none, and hides at the footer. **Changed:** the number is in Roboto Mono like everywhere else, so the markup gains a span. The menu's number too.

**Footer:** V10's order, three link columns, no halftone, a faint plain photo. Pricing goes to services.html#pricing. The phone's underline sits lower, so it doesn't cut through the brackets.

**Estimate band:** on every page except Book, Commercial, 404 and Privacy (conflict 21). Heading, one line (now .a-lede), one pill. **The three steps are Home's only:** give the footer partial a slot for them, since the band lives in that partial today.

**Buttons (V9):** -cream on any dark ground, -slate on cream for a band's main action, -line (outlined) in the menu, -glass as the second pill on photos (Home's hero and Contact), -large for hero, band and price pills. **Changed:** a row of service cards takes plain links naming the job (.a-link with .m-svcCard__book), not outlined pills.

**New parts:** .a-chip -light (link chips on cream), .a-factChip and .m-factChips (one row of facts at most on a page; plain lines on phones in the price band), .m-takes (the "We take" line), .m-notList (the marked list), .m-seatCard (the seated card, with .m-seatCard__art), .m-fact, .m-head (centred heading and line), .m-rowActions, .m-loadPicker (the long picker), .m-tile__line, .m-svcCards and .m-svcCard (shared rows from 1025 up, using subgrid), .m-load, .o-pageBanner, .o-svcBand, .o-svcIndex, .o-svcPrice, .o-svcNot. Reused from round 1: .m-promo (picture first when stacked, under 1025), .m-tile, .m-compare. .m-quote is now the words inside a seated card.

**Truck set:** assets/trucks/ and the 72 KB inline sprite (17 KB gzipped) go in the header partial. tools/build_trucks.py fills marked slots: sprite, truck-hero, truck-gauge, truck-banner (half a load on Services), truck-row-1 to 4. Inline with `<use>`, so a page with four trucks costs little more than a page with one. Three new single items: item-paint, item-propane, item-battery, as files used in `<img>`. WordPress blocks SVG uploads (conventions.md), so at conversion these go in the inline sprite or the plugin. The door decal is the logo at 132px inside the SVG: a logo swap means one rebuild.

**Photo treatment:** as section 6. New crops are in build_assets.py: page-street, page-street-phone, the svc- set (portrait in the row of three), towns-street, and new sources for tile-garage, tile-demo and compare-after. A banner photo must show ground the truck can stand on at its lower right. Each new banner needs its scrim sampled the way section 11 does; don't reuse Services' numbers.

**JS blocks changed:** logo settle (new, sets --logoSettled from the scroll position, replaces the is-scrolled class and its sentinel), current link (new), number-once-per-screen (uses data-call-here, works with none on a page), menu links close, load picker's data-level.

**Must log in content/placeholders.md at rebuild** (this round wrote only to prototype/revision/ and this file):
| Photo | Source | Licence | Used as | Alt on the page |
|---|---|---|---|---|
| portsmouth-street (new download, in prototype/revision/stock-new/) | Emi Mo, photo-1781819117983-1828a116f34f, https://unsplash.com/photos/historic-wooden-houses-line-a-sunny-street-with-shadows-j5TewHOqdpw, Portsmouth, NH | Page reads "Free to use under the Unsplash License", read 2026-11-04 | Services banner, Home towns; proposed for other inner banners | A sunny street of old wooden houses with a brick sidewalk |
| pickup-trash-bags (logged) | iridial | Logged | Services junk removal, new crop | A white pickup truck piled high with black trash bags |
| garage-clutter-before (logged) | Clay Banks | Logged | Services clean outs and Home before and after, new crops. "Cub Cadet" is small but readable on the mower | Services: A garage crowded with a ride-on mower, a workbench, shelving and gas cans. Home: Before: a garage crowded with a ride-on mower, a workbench, shelving and stacked gear |
| garage-after (logged) | Liz Crosswell | Logged | Home before and after, after side, new crop. "Rain Bird" is small but readable at the far end of the slider; the Yakima mark is cropped out | After: a garage with a clear concrete floor and tools hung tidily on the wall |
| basement-cleared (logged) | Point3D | Logged | Home clean-outs tile, new crop | An empty basement with white walls, square pillars and a clear wood floor |
| fridge-in-room (logged) | Raymond Petrik | Logged | Home appliances tile and Services appliances card, new crops, **maker badge painted out** | A pale green retro fridge freezer against a brick wall |
| sofa-by-door, man-carrying-mattress, yard-waste-truck (logged) | As logged | Logged | Services cards, new crops | As on the page |
| shed-weathered (logged) | Ries Bosch | Logged | Home demo tile and Services demo card (was Reviews only) | A weathered wooden garden shed with glazed double doors |
| Round 1, still unlogged: backyard-lawn-deck (Home hero), man-carrying-mattress (Home mattresses), basement-unfinished (footer) | As logged | Logged | As listed | As on the page |
| No longer used on these two pages: backyard-lawn-fence, renovation-tearout, basement-unfinished as the after side | | | Their round 1 notes no longer apply | |

## 8. What the prototype adds to the system
Own CSS in prototype/revision/assets/global.css, with the site's tokens pasted in and the additions marked "new". tokens.css is unchanged until the Developer takes them across (section 7). The header, menu, call bar and footer live once, in index.html, between chrome markers; tools/build_trucks.py copies them into services.html, so the two can't drift.

## 9. Conflicts resolved
1. **Concept 1 (Varun's pick at 2a) against his new feedback.** The feedback is later and specific, so it wins: the ticket goes to Book.
2. **Truewerk as primary against "casual, easy on the eye".** Truewerk wins on layout under the skill's order, but Varun's feedback ranks above it. What stays from Truewerk: caps pairing, tempo, the ease-out curve. Layout now leans on V7 and V8.
3. **V5's centred headline against the truck.** Round 2 moved the words to the middle of the hero's height and in from the edge, as Varun asked, but not onto the page's centre line: that leaves no room for the truck under 900px tall. Decision 1.
4. **V6's chrome CTA on dark against legibility.** Flat chrome beside cream read as disabled (critic r1). Cream on every dark ground, which is V9's "white on dark photos". Varun accepted this at R1.
5. **Ruling R0 A10, "a sketch among photos", against Varun's ask for trucks everywhere plus colour photos.** The truck is treated as a brand character, and it's a solid drawing, not a sketch. Varun kept it at R1.
6. **Quiet-nav guide (a tenth of viewport height) against "logo as the main thing".** At rest the badge is 12% of a 900px window. Varun's ask wins.
7. **Agreed scope against one idea per section.** How it works becomes three small facts on Home and the full steps on Book. Featured reviews stays as one quote in a slim band. Trust indicators stay on hold, unbuilt.
8. **Top bar in the approved spec.** Cut for calm. Shawn's agreed line stays next to the number. Varun accepted this at R1.
9. **Book now twice on the first screen** (header and hero). The header's is the client's "always visible"; the hero's is the booking prompt. Kept both on Home. Inner banners have only the header's (conflict 17).
10. **Skill's "one consistent colour grade" and spec 2c against Varun's point 1.** Colour wins; no grade.
11. **Accessibility stays whole:** skip link, visible focus, 44px targets, contrast sampled, reduced-motion off switch, a slider and picker that work by keyboard.
12. **V5's inner banner list (breadcrumb, tag) against anti-slop.** Anti-slop wins. Heading and one line.
13. **Anti-slop's "heading left, body right" against "spread across the width".** The price bands keep the heading and line centred on the axis, and spread only the picker, price, truck and facts below them.
14. **Round 1's "at most one short line" against Varun's note 1.** Varun's note wins; section 2 is the new rule.
15. **Brief's "demo as its own section" against fewer bands.** Demo shares a band with Yard waste but keeps its own heading, anchor, list and booking link. Listed for Varun.
16. **V3's facts in chips against the Critic's "too many chips".** V3 is a V move and stays, but as one row of two or three facts. Lists of things go in a plain line. On phones the price band's chips become plain lines, because stacked pills looked like filters.
17. **The brief's "click-to-call on every screen" and "Book Now always visible" against a banner with no pills.** V5 gives inner banners a title and one line, and the Critic twice read pills there as a second homepage hero. The header's Book now and number, and the phone's call bar, meet the brief on that screen. Town pages and Contact keep one pill. Listed for Varun.
18. **The brief's "Book Now on every section" against a row of identical pills.** Every service still has its own booking link. On the cards it's a text link naming the job.
19. **"No truck art in the bands in between", and ruling R0 A10 ("a sketch among photos"), against bands with no photo.** A stock job photo beside a review would borrow a job that isn't the writer's, and anti-slop asks for a custom illustration when real media is missing. So two bands use single solid drawings from the truck set. Listed for Varun.
20. **Stock left as it is against the no-brands crop rule.** The fridge's badge couldn't be cropped out without losing the fridge, so it's painted out. Must-replace regardless.
21. **Privacy's estimate band.** This file's table gave Privacy one band and section 7 ran the estimate band everywhere but Book, Commercial and 404. Resolved by Varun, 5 Nov: the lighter option, no band on Privacy (the page's critic called it a loud close after a legal page). Added by the Developer.

## 10. Critic
| Round | Page | Design | Originality | Craft | Functionality | Weighted | Verdict |
|---|---|---|---|---|---|---|---|
| R1, 1 | Home | 8 | 8 | 7 | 8 | 7.8 | FAIL |
| R1, 2 | Home | 8 | 8 | 7 | 9 | 7.9 | FAIL by 0.1 |
| R2, 1 | Home and Services | 8 | 8 | 7 (capped) | 9 | 7.9 | FAIL by 0.1 |
| R2, 2 | Home and Services | 8 | 8 | 8 | 9 | 8.1 | PASS, narrowly |

No copy or design tells in either round. All of Varun's notes were delivered in both. Round 1 asked for a ruling on Roboto Mono because it couldn't tell where the face came from; it's half of the pairing Varun picked at 2a, so round 2 was told and counted nothing.

**The pass has a condition.** Round 2 found the logo overlapping the headline for 3 to 6 frames under a scripted 2500 px/s flick, and said that if Varun counts it under his "any collision" ruling, craft falls to 7 and the total to 7.9. I fixed that afterwards (section 7, section 11). The skill stops the Critic at 2 rounds, so **everything below is checked by me in the browser and not re-scored.**

Fixed after round 2, its issue numbers in brackets:
- Logo tied to the scroll position [8].
- Before and after: a warm garage for the after side, cream wall to cream wall [1]. Still two rooms, so still the weakest band.
- Clean outs and every stacked promo: picture first; a shorter "We take" line [2].
- Banner: heading and one line, no pills, 520px [3].
- Cards: a link naming the job instead of five identical pills [4].
- Can't take: a seated card with a drawn paint can, propane tank and battery [5].
- Phone number in Roboto Mono in the call bar and menu [6].
- Services banner scrim on phones lighter over the headline and sky, darkest only behind the sentence [7]. Home's hero scrim on phones is unchanged: the Critic said it suffers less, and I didn't re-sample it.
- Home tiles: the cleared basement for clean outs, the old shed for demo. Towns: the New England street [9].
- Price band chips on phones are plain lines [10].

Left as they are: the review band still holds one sample quote, which only real reviews can change. The Critic also read the estimate ring running close behind small text at 1440 as still readable.

## 11. Measurements
Cream text over the photo, text and truck hidden, screenshot sampled by tools/sample_contrast.py. Worst case is the 99.5th percentile brightest pixel in each text zone. Target: headline 3:1, sentence 4.5:1. The soft text shadow is not counted, so real legibility is a little better.

Home hero, final scrim (measured earlier in this round; the hero hasn't changed since):
| Window | JUNK OUT | SPACE BACK | Sentence |
|---|---|---|---|
| 1920x1080 | 3.46 | 3.34 | 6.05 |
| 1440x900 | 3.63 | 3.46 | 6.23 |
| 1366x768 | 3.43 | 3.39 | 6.13 |
| 1100x800 | 3.54 | 3.42 | 4.57 |
| 1024x768 | 4.93 | 4.89 | 5.06 |
| 768x1024 | 5.39 | 5.31 | 4.67 |
| 390x844 | 6.38 | 6.10 | 5.57 |
| 320x640 | 7.14 | 6.51 | 5.65 |

Services banner, final scrim and final height:
| Window | OUR | SERVICES | Sentence |
|---|---|---|---|
| 2560x1300 | 4.23 | 4.42 | 5.82 |
| 1920x1080 | 4.11 | 4.45 | 5.81 |
| 1440x900 | 4.11 | 4.43 | 5.77 |
| 1366x768 | 4.01 | 4.39 | 5.78 |
| 1280x720 | 4.03 | 4.39 | 5.84 |
| 1240x700 | 4.03 | 4.36 | 5.91 |
| 1100x800 | 3.86 | 4.09 | 5.40 |
| 1026x700 | 3.81 | 4.06 | 5.67 |
| 1024x768 | 3.80 | 4.09 | 5.99 |
| 844x390 | 3.94 | 4.20 | 6.22 |
| 768x1024 | 5.19 | 5.30 | 5.66 |
| 390x844 | 3.41 | 3.64 | 4.89 |
| 320x640 | 3.50 | 3.58 | 4.68 |

Single bright specks (sky between leaves, sun on a window) fall under target at some widths: the brightest pixel in a headline zone is 1.92:1 at worst, at 1920x1080 on JUNK OUT. They sit under heavy capitals, and I judged that acceptable rather than darken the photos further. The Critic's own lowest reading, worked out from the image and scrim rather than from pixels, was 1.99:1 on the same words.

Geometry, Services: the whole drawing's box against the words, at the final banner, in 15 windows from 2560x1300 to 320x640. All clear. Smallest gaps: sentence to truck 62px at 320x640 and 67px at 844x390; SERVICES to truck 102px at 1026x700; logo to OUR 20px at 320x640 and 28px at 390x844.

Geometry, Home, measured earlier in this round and unchanged since: the words against the truck's load box, clear at 2560x1300, 1920x1080, 1440x900, 1366x768, 1280x720, 1240x700, 1100x700, 1024x768, 768x1024, 844x390, 390x844 and 320x640. The smallest gaps are about 16px, between SPACE BACK and the load at short laptop sizes. A last change for 1026x700 was calculated and not re-measured by me.

Logo against the heading under a scripted flick: 0 frames of overlap at 420, 1,020, 2,520 and 4,200 px/s, on both pages at 390x844, 320x640, 1440x900, 1240x700 and 1024x768. It counts only logo hanging below the bar over visible words. Each frame was measured after the scroll event ran, so a frame painted a step late wouldn't show in this test. A real phone scrolls on another thread and could paint the logo a frame late; I couldn't test one.

Reduced motion, emulated in Chromium on both pages at 1440: nothing left hidden or offset, truck visible, logo 108px at the top and 84px at 40px of scroll.

Also checked at the end, in the browser: the menu at 390 on Services opens, closes on Escape and returns focus; the jump row swipes without widening the page and #mattresses lands 16px under the bar; focus shows on the card links, which are 44px tall; the slider drags to 4% and holds; the picker gives all four prices.

Pages: Home 7 bands, Services 8 (both counting the estimate band). Home is 7,380px tall at 1440, 7,882px at 390. Services is 6,793px at 1440, 9,107px at 390. No sideways overflow, broken images or console messages at either width.

## 12. What I could not check, and what I guessed
- **The Critic did not see the last round of fixes.** Section 10 lists them. 8.1 was scored before them. Only a third Critic round, or Varun, can say whether they raised or lowered it.
- **No real phone, no Safari, no Firefox.** Chromium only. No physical 2x screen: the logo's sharpness rests on the pixel numbers. The shared rows on the cards use subgrid, which I didn't test outside Chromium.
- **The back-in motion and the load change have not been judged in real time by me or the Critic.** Positions and settled frames only.
- **No screen reader run. No slow-network test.** "Book this load" sends ?load= to the old Book page; I didn't check that the old page reads it.
- **Tablet widths** were checked by me only, at 1024 and 768, after the last fixes: Services' banner, clean outs and can't-take at both, its cards at 768, Home's towns at 1024. The Critic looked only at 1440 and 390. Other widths have the banner's measurements and nothing by eye.
- **Inner page lists and word targets other than Services are untested.** They're my judgment from the built pages' structure and critic logs, not from a build at this level. So are the short banner and the per-page truck loads in section 5.
- **Reading of Varun's note 2** (section 3) is an interpretation. Decision 1.
- **The before and after is still two different rooms.** I searched for a free matched pair (two searches, standard depth) and found only copyrighted or paid ones. Decision 3.
- **Home's hero scrim on phones** wasn't lightened or re-sampled. The Critic flagged it more mildly than the banner's.
- **Machine memory:** my one attempt to read free memory was refused, so I never had a number. I kept to one browser and closed it before each Critic round. Neither Critic round was killed.
- **The appliance photo is still the soft fridge,** now with its badge painted out and a whole-fridge crop. Varun allowed a better one. I looked (old fridge, old washing machine, washer and dryer, fridge in garage) and previewed three: two clean new machines and one dark courtyard abroad, all worse. Others were rusted in fields, which the Critic rejected earlier as dereliction. Only Shawn's own photo really fixes this.
- **The rejected downloads** are still in prototype/revision/stock-new/ (washer-small-room, washer-basket, washers-courtyard). My one attempt to delete them was refused, so I left them. Nothing uses them; safe to delete.
- **The street photo's licence** was read from the page by a fetch tool, not by me in a browser. Worth one look before anything goes live. It is must-replace either way.
- **Truck proportions** come from general knowledge of medium-duty cab-forward trucks, not a measured drawing.
- **The word count** counts every token as a word, including town names and "1/8".

## 13. Decisions for Varun
1. **Hero position.** Words on the middle of the hero's height, set in 120px from the left at 1440, truck bottom right. If you meant the true centre line of the page, the truck has to shrink by about 30%. Which do you want?
2. **Demo shares a band with Yard waste** on Services, keeping its own heading, anchor and booking link. The brief says "its own section". Fine, or give it a band alone?
3. **Before and after.** The Critic's worst band both rounds, because a stock pair can't be one room. Keep the warm garage pair until Shawn sends a real one (my default), draw a matched pair in the truck's style, or hold the band back? A drawing would need your call under your "sketch among photos" ruling.
4. **Drawn items on two bands.** The sofa and chair on the review card and the paint can, propane tank and battery on "can't take" are the same solid hand as the truck, and both Critic notes asked for something like them. They do bend your "sketch among photos" ruling. Keep them?
5. **Inner banners with no pills.** Heading and one line, with Book now and the number in the header, and the call bar on phones. Town pages and Contact keep one pill. It's what makes a banner stop reading as a second hero, but it's less of a sell on the first screen. Fine?

## 14. After this round
Copywriter rewrites content/copy.md to section 2 and section 4 and lists what changed. Developer rebuilds the homepage first and stops for Varun to see it once, so text-amount notes are applied once, then rebuilds the rest in batches from this file, removes the grade from tools/images.py, updates tokens.css, moves the trucks across and logs the stock above. Then the final whole-site Critic pass, README and handover, checkpoint 3. None of that has started.

## Progress, revision round 2 (for a restart)
Run started 2026-11-04 from choices.md "Checkpoint R1 result". Steps: homepage notes, services.html, this file, Critic, log. New stock in prototype/revision/stock-new/. Files starting with an underscore in shots/ are scratch and safe to delete.
- [x] Homepage notes applied (more text, hero lower and nearer the centre, priced-by-load full width)
- [x] services.html built, contrast and geometry measured
- [x] revision.md updated (text level, page list, inner pattern, shared parts)
- [x] Critic rounds (2, the skill's limit), fixes, final shots, review-log.md line

Stopped for Varun. Restart 1 of round 2 (low-memory kill at the first Critic round): checked the three files against the brief in the browser before going on. Homepage notes, services.html and this file held up, so nothing was rebuilt. The killed Critic round left 4 partial captures in shots/critic-r2-1/ and no scores, so it counts as not run. Critic round 1 then scored 7.9, round 2 scored 8.1. Sections above describe the final state. Final shots: shots/r2-*.png.

## Progress (round 1)
Done and stopped at checkpoint R1: looked at the references for feel, trucks redrawn, revised homepage, 2 critic rounds (7.8, 7.9), fixes after round 2. Restart 1 after a low-memory kill left only scratch crops.
