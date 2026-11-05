# Varun's choices (checkpoint 2a, 2026-11-03)

- Concept: 1, The work order (the site is a job ticket: Town, Load, Day, "from" price, then Book now plus the call line).
- Type pairing: A, Bio Sans with Roboto Mono (the reference's own approach). Bio Sans is commercial; its web licence has not been checked or bought. See open items.
- Palette: 1, Slate wall (the logo as Shawn shows it: chrome on slate, dark-led, monochrome).

## Defaults that stand unless Varun says otherwise
- Donor sections: FREITAG header and Donate block, Muval selector and per-town price cards, Piece of Cake quote-plus-call hero (as measured in phase A). Varun did not answer.
- Conflicts resolved the art-direct way: pills for buttons and chips only, square corners on frames, tiles and images; quieter palette than Truewerk (no lime); type-led hero (no client footage yet); slimmed sticky header near 90px with the call line in the top bar; no em-dash headings, full-stop headlines or two-colour headlines.

## Open items before phase B
- Bio Sans licence: needs a web licence (Dharma Type, from $29.99 a style) or a free substitute (pairing B, Barlow, is the closest). Varun to decide.
- Logo: only assets/logo.png (736 by 1600 phone screenshot, mark about 220 by 233 px). The original PNG from Fiverr or a vector is needed for a sharp logo.

## Font check (2026-11-03)
- assets/fonts/biosans/: 12 OpenType (CFF) files, Bio Sans by Ryoichi Tsunekawa, vendor Dharma Type: ExtraLight, Light, Regular, SemiBold, Bold, ExtraBold, each with an italic.
- Read-only structural check: every file has a valid font header, normal tables only, no scripts, no executables, no hidden data (2 padding bytes each). Only URL inside is the vendor link (dharmatype.com).
- No licence file in the folder. File names start with "Flat-it - ", so the source of this copy is unclear. Varun says he has the font available; web licence (woff2 on the client's site) still to be confirmed.
- Needs conversion to woff2 for the web. Conversion needs fontTools (a package install, to be approved by Varun).
- Licence: Varun decided to use Bio Sans without a licence file on hand (2026-11-03). No fontTools install approved, so phase B uses the .otf files directly; woff2 conversion is a later decision.

## Decisions at checkpoint 2b (2026-11-03)
Varun approved phase B (Critic's last weighted score 7.6, fail on craft; accepted by Varun) and answered the five handover decisions:
1. Palette: keep the grey slate as picked. No extra accent.
2. Fonts: fine as they are. Bio Sans ships as the .otf files; no fontTools install approved (woff2 conversion stays an open, optional later step).
3. Images: use stock photos for now, from Unsplash, Pexels or similar. No line drawings, no empty cells. This overrides the 1a rule of no stock, for the design stage only. The proposal (term 06) promises Shawn's own job photos and no stock unless he agrees in writing, so every stock image must be logged in content/placeholders.md as must-replace, with its source and licence, and nothing goes to the client as final with stock in it.
4. Phone: Book now is NOT in both places. Keep Book now in the header; the bottom bar is call-only.
5. Logo: fine as it is. Use assets/logo.png (clipped to a circle, small sizes only, max about 56px tall) and do not wait for the original.

## Decisions at stage 6, copy (2026-11-04)
- Questions for the client: not forwarded. They stay placeholder values (content/placeholders.md). Nothing is going live right now.
- Stock photos are fine everywhere, including a person photo for Shawn on the About page. Every one is logged in content/placeholders.md as must-replace (source, licence, where used). Do not caption a stock person as Shawn by name until his real photo exists.
- Defaults stand: sample review cards as written in copy.md; booking written as a request Shawn confirms; trust claims (licensed, insured, guarantee) stay HOLD and unbuilt.
- Developer applies the copy.md note: before a town is typed, the strip reads "Start typing to check we come to you".

## Decisions at checkpoint 2c (2026-11-04)
Varun delegated the five homepage decisions to the Studio Lead ("do as you will"). Chosen, as notes for homepage rerun 1 of 2:
1. Before/after: keep the section with the two stock garages for now (nothing is live), marked must-replace in content/placeholders.md as "needs Shawn's real before/after pair from one spot".
2. Alt text: rewrite every alt to describe the stock photo actually shown, so screen readers are not misled. Rewrite again when Shawn's photos arrive.
3. Replace the junk removal photo (reads as firewood delivery) and the clean-outs photo (busy workshop) with better-fitting stock. Log the swaps.
4. Photo grade: make it stronger so the red pickup and orange truck sit inside the slate palette.
5. Section openings: vary the opening of the towns section (or reviews, whichever reads better) so services, towns and reviews do not all open statement-left, right-half-empty. Keep the spec's rules otherwise.

## Checkpoint 2c result (2026-11-04)
Varun approved the homepage as it stands (Critic 7.9 vs 8.0 pass mark, no tells; rerun 2 not used). The three open questions (reviews lines, town-card price, hero lede) were not decided: leave the homepage as built, and carry them into the final whole-site pass as open items.

## Varun's feedback on the built pages (2026-11-04), a revision round after the last page
Applies to every built page. Queued to run after the Commercial, 404 and Privacy batch, so no two agents edit site/ at once.
1. Images: full colour, not monochrome. Replaces checkpoint 2c decision 4 (the strong mono grade). The site was too bland. Remove the grade in tools/images.py; keep a light unifying treatment only if it does not drain colour. Rebuild the derivatives for every page and the og image.
2. Too wordy: sections that follow each other, or sit apart, say too much, and the pages lose focus. Cut copy and sections on every page: one idea per section, fewer sections per page, shorter lead text, drop repeats of the same point (for example the call line, the trust row and the price said again and again). Copywriter trims content/copy.md first and lists what was cut or merged; the developer then restructures the pages. Keep the open copy questions (reviews lines, town-card price, hero lede, About intro and call line) in scope: resolve them while trimming.
3. Logo: make it larger in the navbar, as the main thing in the header. Limit: assets/logo.png is a small phone screenshot (mark about 233 px), so about 100 to 110 px wide is the sharp ceiling on 2x screens, and the spec caps the header near 90 px tall. Use the largest size that stays sharp and fits the header cap, and note the ceiling in the handover. A bigger logo needs the original file or a vector.
4. Remove the "design preview" line from the top bar. Varun's call; nothing is live. The brief says the site must be labelled as a design preview with placeholder content before Shawn sees it, so put the label back, or gate it, before any deploy-preview.

## More feedback from Varun (2026-11-04): a direction change, not only polish
Joins the revision round above (colour images, trim the words, bigger logo, no design-preview line).
5. Trucks: the hand-drawn truck illustrations (hero, gauge, sections, wherever they appear) must be more realistic, more detailed and more refined, everywhere they are used.
6. Feel: next to the client's own references (easyscrapofficial.com and junkteens.com), our site reads as word-heavy, sharp and professional. They are casual and image-led and easy on the eye. Ours is information-centric: every section holds many things (your town, your junk, pick a day, price), too much to take in at once. Aim for casual, image-led, easy to look at, with one clear thing per section.
   - This pulls against approved concept 1 (the work order ticket with Town, Load, Day and price in the hero) and against the dense ruled-grid system. The Art Director must decide how far to simplify (for example a single booking prompt plus the call line in the hero, with the rest moved to the Book page).
   - Reference rule stands: take the feel and the density, never their layout, images, text or code. They are same-market competitors, so no primary-reference use.
   - Skills may be used where they help (for example impeccable, frontend-design, emil-design-eng for polish and restraint).

## Plan agreed in the Studio Lead's reply (pending Varun's checkpoint)
1. Finish batch 7: Commercial, 404, Privacy.
2. Art Director: revision direction (design/revision.md) plus a revised homepage hero prototype with redrawn trucks, colour photos, a bigger logo and a calmer ticket. Checkpoint R1 for Varun before any rebuild.
3. Copywriter trims copy.md to the new direction.
4. Developer rebuilds all pages in batches.
5. Final whole-site Critic pass, README and handover, checkpoint 3.

## Checkpoint R1 result (2026-11-04)
Varun approved the revision direction: the prototype in prototype/revision/ is better than the built site, and the whole site moves to it (trucks, photos, layout, logo, calmer look). The five open questions were not answered one by one; Varun liked everything in the prototype, so the Art Director's defaults stand (distance from the work order, truck over photos, header with the top bar cut, Bio Sans Regular body with cream buttons, better appliance and New England street photos may be downloaded).
Notes on the prototype to apply:
1. Too little text. The prototype has almost none; Varun wants a mix of both: a tad more text all around, across the whole website, not a return to the wordy build. Rough target: each band gets a short heading plus one or two supporting lines (some get a short list or three small facts); the homepage lands well above 133 words (about 300 to 400) and well below the old 779.
2. Hero text: come down a bit and sit closer to the centre of the hero.
3. Priced-by-load section: the text is cramped at the left end. It must span the full width of the section (truck, load picker, price and supporting text spread across the whole width).
4. Every other page is redesigned to match the new look, with the same text balance.
5. Build the complete new version for all pages. Plan: Art Director applies these notes and adds an inner-page prototype; Copywriter rewrites copy.md to the new text level; Developer rebuilds the homepage first and stops for Varun to see it once (so text-amount notes are applied once, not on 14 pages), then rebuilds the rest in batches; final pass.

## Revision pass 2 result (2026-11-04)
Art Director finished: Critic round 2 scored 8.1 (narrow pass; fixes made after it are unscored). Homepage prototype 354 words; Services inner-page pattern 536 words; design/revision.md holds word targets, the page-by-page list, the inner-page pattern and the Developer's shared-parts list.
Open questions from the Art Director, answered by defaults so the build can go on (Varun can change any of them when he sees the rebuilt homepage):
1. Hero position: middle of the hero's height, set in about 120px from the left (not the true centre line).
2. Demo shares a band with Yard waste, with its own heading, anchor and booking link.
3. Before/after: keep the warm stock garage pair until Shawn sends a real pair.
4. Drawn items stay on the review and "can't take" bands.
5. Inner banners have no buttons; town pages and Contact keep one.

## Homepage approval and instruction to finish (2026-11-05)
Varun approved the new homepage ("this is the design I was wanting") and told the Studio Lead to finish the whole website without asking him anything further, judging for himself, restarting after low-memory kills.
Notes on the homepage (apply once, then pages follow):
1. More text on the homepage ("a bit more"): target about 450 to 500 words in the main content. Inner pages may rise about 10 to 15 percent where thin (Reviews, Donate, About), never back to the wordy v1 build.
2. Priced-by-load section: keep the design, but the load chips/filter (1/8 truck, 1/4 truck, ...) are too big. Make them much smaller and lighter (compact segmented control or small pill row), same function.
3. Reviews: more than one. Show several sample review cards (about 4 to 6) on the homepage and the Reviews page. They are placeholders: clearly marked sample wording, no star rating, no score or count, no real names or real people, each logged in content/placeholders.md as must-replace by Shawn's real Facebook reviews. Remove the "we've got plenty" line that contradicts the sample cards.
4. Everything else on the homepage stays as approved.
Judgment calls delegated to the Studio Lead: the seven staged-page defaults stay; Critic: round 1 on each inner page, round 2 only if round 1 fails; one builder at a time in phase P2; whole-site Critic pass at full strength.

## Varun's additions to batch d (2026-11-05)
1. Navbar items become: Services, About, Pricing, Reviews, Donate (plus the existing Book now button and call line). FAQ, Contact, Service area, Commercial and Privacy move to the footer and in-page links. Studio Lead's call: Pricing becomes its own page (pricing.html), built from the Services pricing section and expanded, since Varun wants more information on the site and the nav needs a real destination.
2. The pages are too small, with too little information (example: About is two sections with nothing in them). Increase the information across the site, in a way that keeps the approved look, one idea per section, and does not return to the wordy v1 build. About gets more sections, including one more about-section (an "About Quick Haul" opening section ahead of the story). Other thin pages grow in the same way.
3. All of this is done together in batch d instead of a new batch. Copy is written first in content/copy-v4.md (staging, so the running batch c is not disturbed); batch d then promotes it and builds.
Rules that still apply: no invented client facts (Shawn-specific details are realistic placeholders logged in content/placeholders.md; general how-it-works and what-affects-price information is fine), no trust claims, sample reviews only, no em dashes.

## Speed-up (2026-11-05, Varun: "it shouldn't take this long")
Studio Lead's changes to the pipeline for the rest of the build: page work runs at high effort, not max; no Critic rounds per page inside batch d; mechanical QA (qa.py, check.py, form flows) stays after every step because it takes minutes; the Critic runs once, on the whole site, in the integration review (all new or heavily changed pages in one pass, with one fix pass after). Whole-site Critic stays at full strength.
