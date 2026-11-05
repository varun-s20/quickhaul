# Revision rebuild plan (2026-11-05)
Direction: design/revision.md, copy: content/copy.md v2, approved at checkpoint R1 (design/choices.md). The rest of this file is the old build's plan, for reference.

**This run: shared parts and the homepage, then stop for Varun.** Then the other pages in batches from revision.md sections 4 and 5, then the final pass.

**Shared parts, done means:** tokens in design/tokens.css and the first :root block; Bio Sans Regular body; header with the 108px logo settling to 84px, no top bar, no preview line, five links; menu; call-only bar; footer in V10's order; estimate band with Home's steps behind a slot; pills per V9 and revision.md; truck set from one tool; photos full colour with no grade. Old inner pages keep working under .t-legacy, their content untouched, their look expected to be mixed.

**Home, sections in order:** hero; what we haul (7 photos, one line each); priced by the load (spanning the width); before and after; reviews (one sample in a seated card); do you come to my town; estimate band (three steps).

**Home, done means:** words from copy.md, not the prototype; 300 to 400 words in main; one idea per band; hero headline at least 3:1 and sentence at least 4.5:1 over the photo at every window, sampled; words clear of the truck at every window; picker, slider and menu work by mouse, touch and keyboard; number shows once per screen; "Book this load" and "Book a clean out" arrive with the pick made; no tells from anti-slop; QA clean; Critic at most 2 rounds.

# Build plan: Quick Haul
Developer, 2026-11-04. Scope of this run: foundation plus the homepage only (Varun's prompt). Inner pages follow in later runs.
Sources: design/design-spec.md, design/tokens.css, design/choices.md (decisions at 2b and stage 6 override the spec where they differ), prototype/, content/copy.md, taste/signature.md, taste/anti-slop.md, taste/critic-rulings.md, .claude/skills/build-site/conventions.md.

## Overrides from design/choices.md that change the spec
- Images: stock photos (Unsplash, Pexels or similar) fill every image slot for now, logged in content/placeholders.md as must-replace with source, licence and where used. No line drawings, no empty cells. This replaces spec 2c's item drawings and puts the before-and-after section back into the homepage with a stock pair.
- Phone action bar: call-only ("Call (603) 555-0142"). Book now stays in the header only.
- Bio Sans ships as the .otf files. No package installs. Roboto Mono is self-hosted as woff2 files downloaded from Google Fonts (Apache 2.0); no conversion needed.
- Logo: assets/logo.png unchanged, clipped to a circle, small sizes only (max about 56px tall).
- Reviews: the sample cards in copy.md are built (obvious samples, no stars, no score row). Trust row: the three non-HOLD cells only; licensed, insured and guarantee stay unbuilt.
- Ticket default note: "Start typing to check we come to you".

## Pages, in build order
1. Home (index.html): this run.
2. Services (with #pricing), 3. Book, 4. Service area hub and town template, 5. Reviews, 6. About, 7. Donate, 8. FAQ, 9. Contact, 10. Commercial enquiry, 11. 404, 12. Privacy. Later runs.

## Remaining pages (run started 2026-11-04, after Varun approved the homepage at checkpoint 2c)
Homepage output must stay byte-identical (build/tmp/home-baseline.sha); its three open questions go to the final pass as open items.

Shared for all of them: inner banner (slate, stripe, slats, registration marks, grain, frame lines, no breadcrumbs, about 440px at 1440), one h1, estimate band everywhere but Book, every word from copy.md, HOLD lines unbuilt, stock logged in placeholders.md with alts describing the stock shown, no stock person captioned as Shawn, no em dashes, no upscaled media, 44px targets, visible focus, reduced motion. Each page: QA, then the critic at high effort (2 rounds at most), one at a time.

Decisions taken for this run, from the conventions and choices:
- No file input without a backend (conventions): the photo fields are in the markup, hidden, and shown only when window.SITE_FORM_ENDPOINT is set. Flagged in the handover, because the copy mentions adding photos.
- A form never reports success without an endpoint answering OK. In the preview, Book shows copy.md's error state (it says so and offers the phone). Contact and Commercial have no failure copy, so they reuse the approved "Something went wrong" headline and the call line.
- Service area map: our own drawing from data/towns.json, no third-party embed. The brief's Google Map waits for the real base town. Flagged in the handover.
- About photo: a stock person is allowed (choices, stage 6), never captioned or described as Shawn.
- Calendar day cells 44px, not the spec's 39px (conventions: 44px targets).
- Commercial reuses Contact's three error lines (copy.md gives Commercial none).

Contracts:
1. Services: banner; seven split bands (photo cell with 12px inner padding, ruled, sides alternating, demo on slate) with #junk-removal, #clean-outs, #furniture, #appliances, #mattresses, #yard-waste, #demo; each with its heading, body, checklist, button and call link. What we take and don't. Pricing (#pricing) four cards, note, button, call. Done: every homepage anchor lands correctly under the sticky header; photos at least as sharp as their frame.
2. Book: banner; ruled ticket, progress line (Day, Load, Address and details, Your details), calendar, time chips, load and job chips, price line, address fields, contact fields, SMS box, call cell (right at 1025 and up, under the step on phones). Prefills town, load, day and job from the query string. Confirmation and error states. Done: can't move on without what the step needs, errors inline, focus managed, no estimate band.
3. Service area: hub (map, town lists, closing cell) and town template (banner with the town, ticket pre-filled, services in town, price cards), 12 pages.
4. Reviews: filter column, 3-column ruled grid with Read on Facebook, leave a review, four-pair gallery at #before-after. No stars.
5. About: statement, split band, four ruled cells. Stock, not captioned as Shawn.
6. Donate: title, statement cell, 6 + 6 labelled cells and one photo tile, button and call line.
7. FAQ: four groups of details rows, close line, FAQPage JSON-LD.
8. Contact: map, contact cells, quote form, commercial cell.
9. Commercial: enquiry form with the conditional How often chips.
10. 404: empty truck bed, button, four links, noindex.
11. Privacy: plain ruled sections; "Last updated" left out until the launch date exists.
Then: critic once on the whole site at xhigh, site/README.md, build/handover.md (the three open homepage questions carried as open items, unchanged).

## Shared parts (foundation)
Preview label (until launch), sprite, skip link, top bar, header (nav, logo cell, call circle, Book now), menu dialog, call-only action bar, estimate band, halftone band, footer (phone, email, hours, tagline, four link columns, social pills, fact line, Back to top, credit). Focus ring, reduced-motion block, `js` gate.

## Home: sections in order
1. Hero (slate): "Junk out / Space back", lede, truck drawing with load gauge. Stripe, grain, registration marks, slats.
2. Ticket (cream): Town (combobox), How much junk (chips plus helper), Pick a day (chips plus error and empty slot), Price from, Book now plus call link. Inline errors on submit.
3. Halftone band.
4. Services overview (cream): statement "What we / haul away", supporting line, ruled tile grid (junk removal 2x2, clean outs and demo stacked, then furniture, appliances, mattresses, yard waste), Book now plus "See everything we take".
5. Price and service area (slate): "Do you come / to my town?", supporting, row of square ruled town cards (12 towns plus "Can't see your town?"), square arrows with a progress hairline, "See all prices".
6. Featured reviews (cream): "Straight from / Facebook", supporting, row of sample quote cells, arrows, "Read all our reviews on Facebook"; trust row of three ruled cells.
7. How it works (slate): "From booking / to bare floor", FREITAG 3 + 6 + 3 with three stacked ticket lines, Book now plus call line.
8. Before and after (cream): split band, square frame with a native range slider over a stock pair, text column, "Book a clean out", "See more before and afters".
9. Estimate band (slate): "Got a garage / full of junk?", supporting, Book now, call line, faint arrow-ring glyph.
10. Halftone band, footer (ink).

## Contract: what "done" means for the homepage
- Copy: every word from content/copy.md Home and Global, word for word. No invented copy; HOLD lines unbuilt. No em dashes anywhere in shipped files.
- Composition (spec 2b): 48px margins and frame lines at 1440, 20px at 390; ruled cells with shared hairlines, no gutters, square frames, pills for buttons and chips only. Hero 484px banner at 1440 with the headline the largest thing on screen; ticket one row of five cells at every desktop width with price and Book now on the first screen at 1366x768 and 1100x800.
- Headlines: light row plus heavy row, caps, no full stops, no colour change, no italics, sized off their column, balanced.
- No AI eyebrows (labels are field and fact labels only), no numbered steps, no three icon cards, no breadcrumbs, no glow.
- Media: every image fills its slot (aspect and focal point), never shown larger than its native pixels at 1440 or 390 (2x density checked against the srcset), WebP derivatives with matching sizes, lazy below the fold. One grade for every photo. Logo never above 56px tall.
- Interaction: the town combobox, load chips (price and truck fill), day chips, form validation with inline errors, carousels with arrows and progress, before-and-after slider by drag and keyboard, footer accordions at 390, menu dialog (inert page, focus trap, Escape, focus return), call-only action bar after the ticket.
- Accessibility: skip link first, visible focus everywhere, 44px targets, 4.5:1 body contrast, text over photos readable on every tile, landmarks and aria-labelledby, one h1, heading order.
- Motion: load sequence once (rows from masks, lede and cells rise, truck fills); in-view rises for later sections; tile push-in on hover; nothing endless; reduced motion shows everything at once.
- Network: no 404s for shipped assets (links to inner pages not yet built are listed as pending), no console errors, no unused preloads.
- Critic: at most 2 rounds at high effort; target PASS, originality 8 or more, no tells.
