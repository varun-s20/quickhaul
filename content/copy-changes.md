# Quick Haul copy: what changed
Copywriter, 2026-11-05. Current copy: content/copy.md (v3). Older versions: content/copy-v2.md and content/copy-v1.md. New placeholder values: the last section of content/placeholders.md.

# v2 to v3: apply this
From Varun's notes in design/choices.md, "Homepage approval and instruction to finish". Home, Reviews, Donate, About and Book's picker labels changed. Every other page is word for word v2. Daggers in copy.md mark what is a placeholder; don't print them.

## Home (src/pages/index.body.html, tools/build.py)
- **Hero:** no change. The words already sit about 16px from the truck at short laptop sizes (revision.md section 11).
- **What we haul:** four tile lines change.
  - Mattresses: Twin to king, plus the box spring and bed frame.
  - Furniture: Couches, dressers, desks and dining sets, even from upstairs.
  - Appliances: Fridges, washers, dryers and stoves, working or not.
  - Yard waste: Brush, branches, bagged leaves and whatever the last storm brought down.
- **Priced by the load:**
  - Line: add "Not sure how much that is?" after the first sentence.
  - Load control: visible label "How full?", chips "1/8", "1/4", "1/2", "Full". Hide "truck" at every width, don't remove it: `.a-choice__unit` already hides it under 379px, so screen readers keep "1/8 truck". prices.json doesn't change. Book's picker prints from the same radios, so it follows.
  - Group's accessible name: "How full is the truck", replacing the legend "How much of the truck".
  - "Just one item?" fact: It's priced as a 1/8 load, so that's $149. This is one more place a price is typed by hand, so add it to the list in prices.json's `_note`, or fill it from the data.
- **Before and after:** new plain line (`.m-takes`) under the slider, above the pill and link: **We clear** boxes and bins, shelving, old furniture, tools nobody uses, carpet and rugs. What stays is up to you.
- **Reviews:**
  - Line: "We've got plenty..." is gone. Now: These cards are samples for now. Real reviews from our Facebook page take their place, word for word.
  - One card becomes five, wording in copy.md. Who line "Sample review" and avatar "SR" on each. No source line.
  - "Read them on Facebook" is gone, because "them" would now point at the samples. Now "Read the real ones on Facebook", once for the band, outside the cards.
  - The heading stays. The drawn sofa and chair sit on one card's edge.
  - The cards run 9 to 19 words, so the layout meets uneven cards. Real reviews will run longer, so don't fix a card height to these.
- **Do you come to my town:**
  - Line: add "Pick yours to see what we haul there."
  - Under the chips: Can't see your town? It may just not be on the list yet. Give us a call. The phone link stays on the last four words.
- **Estimate band:** no change. It sits outside main.

## Reviews (src/pages-v2/reviews.body.html, _data/reviews.json)
- **Banner line:** "plenty" is gone. Now: Real reviews from our Facebook page land here, just as their writers left them. Until then, the cards below are samples.
- **Grid:** all six cards reworded, in copy.md. `who` becomes "Sample review" on all six. The photos stay where they are in the data's order: the cards keep v2's order of jobs, so request 006's check on photos and jobs still holds.
- **End of the grid:** line gains "A line or two about the job is all it takes." "Read them all on Facebook" is now "Read the real ones on Facebook".
- **Before and after:** new line under the pairs, no button with it: Got a spot like one of the befores? Add a photo when you book and we'll price it from there.
- **Meta:** no change.

## Donate (src/pages-v2/donate.body.html)
- **Third small fact** in `.o-donateBand__facts`: **If it can't be donated** It goes with the rest of your load, so you're not stuck with it.

## About (src/pages-v2/about.body.html)
- **How we work:** new line (`.a-lede`) under the heading: We're coming onto your property and into your garage or basement, so here's what you can expect.
- **No sales pitch:** text gains "Say no and that's fine."

## Book (src/pages-v2/book.body.html)
- **Picker:** the short labels from Home, plus "Not sure". The label "How much junk", the price line and the notes stay.

## Data and requests
- **reviews.json, both copies** (site/data/ and src/pages-v2/_data/): `home` becomes a list of five, the same words as cards 1 to 5 of `reviews_page`. `source` comes off the samples. Reword `_note`, which still says one card.
- **tools/build.py:** `block_review_home` prints five cards and moves the Facebook link out of the card. Real reviews still need the name, "Facebook", date and post link slots.
- **Request 006 is out of date here:** it says the `home` entry is unchanged.
- **For the Critic:** visible sample wording on these cards is Varun's own instruction (choices.md, 5 Nov, note 3), so it isn't a placeholder-label tell. The critic note in review-log.md (homepage round 2) came before it.

## Word counts
Counted by hand with the same rule as below: words a visitor can see in main, with hidden states, field hints, alt text, screen-reader text and the estimate band left out. The Developer's browser count is the real one, and it will also count the decorative SR avatars.

| Page | Asked for | v2 | v3 | Note |
|---|---|---|---|---|
| Home | about 450 to 500 | 359 | 481 | 486 with the five avatars |
| Reviews | up 10 to 15 percent | 200 | 222 | Up 11 percent. Without the sample cards, 82 to 118. 228 with the six avatars |
| Donate | up 10 to 15 percent | 145 | 164 | Up 13 percent |
| About | up 10 to 15 percent | 153 | 175 | Up 14 percent |
| Book | no change asked | 204 | 200 | Only the hidden "truck" on four chips |

Home by band, v2 to v3: Hero 32 to 32. What we haul 104 to 117. Priced by the load 93 to 100. Before and after 38 to 58. Reviews 43 to 108. Towns 49 to 66.

v2's table below gave Reviews as "about 195". An exact recount of v2 gives 200, so the percentage uses 200.

## My calls, for Varun to overrule
1. **One set of six sample cards.** Home shows cards 1 to 5 and Reviews shows all six, the way the scope features a few reviews on the homepage. It also means one list to replace.
2. **No source line on a sample.** "Sample review, Facebook" said the words came from Facebook, and they didn't. Real reviews get the source back.
3. **The lines say "samples" out loud.** That is right for a preview and wrong for launch. The launch wording waits under Held lines in copy.md.
4. **"Read the reviews" stays as the heading,** since Varun approved it. The line right under it says what the cards are.
5. **Small new claims, all placeholders, all logged:** "even from upstairs", "working or not", "whatever the last storm brought down", "What stays is up to you", "It may just not be on the list yet", "If it can't be donated", "Say no and that's fine". Most are short forms of lines already on Services, Book or the FAQ. "If it can't be donated" and "Say no and that's fine" are new.
6. **Most of Home's rise is sample wording:** 65 of the 122 new words are in the Reviews band. They are placeholders, so a real set of reviews will change the count.

---

# v1 to v2, for the record

## The open copy points
- **Reviews lines.** "Tap any review to read it where it was posted", "Every review on this site links back to Facebook", "Every review here is copied from our Facebook page" and the heading "Straight from Facebook" all claimed things a sample card can't do. The new lines stay true now and later: the reviews are on Shawn's Facebook page, in his word "plenty", and any we bring over stay word for word. Home is "Read the reviews"; the Reviews page is "Customer reviews". Sample cards lose their job tags and "Read on Facebook" links. The old claims wait as HOLD lines for real reviews.
- **Town-card price.** No town name carries a price anywhere now. Home and the hub list names only. The price sits in Priced by the load, and one line says it's the same in every town.
- **Hero lede.** "Pick your town, your load and a day below" pointed at a ticket that's gone, and the prototype's line priced demo work at $149 when demo is per job. Now: "Junk removal, clean outs and demo work across Massachusetts and New Hampshire. Loads start at $149. You point, we carry."
- **About intro and call line.** The banner line now does the statement's job and the statement is gone, so nothing is said twice. In "Pick up the phone" the one action is the call, "Call Shawn (603) 555-0142". "Or call Shawn on" is gone, and Book now is left to the estimate band.
- **Card links.** Confirmed: Book a furniture pickup; Book an appliance pickup; Book a mattress pickup; Book a demo project; Book a clean out; Book this load. Fixed: "Book a yard clean-up" is now "Book a yard waste pickup". It uses Shawn's own term and matches the other pickups, and "clean-up" promised a yard tidy he never offered. Demo stays "Book" because the brief asks for a booking link on every service, so Book gets a new line saying demo is priced per job.

## What changed, page by page
- **Global:** top bar, footer tagline, Help column and the repeated call line cut. Nav is now Services, Pricing, Towns, Reviews, Donate. Estimate band loses its second sentence and call line; Home alone keeps three steps. US English throughout ("at" not "on", no "enquiry", "cleanup", "gray"). Preview label kept, off until a deploy-preview.
- **Home:** ticket, trust row, town cards and every multi-sentence section paragraph cut. How it works merged into the estimate band. New: Priced by the load. Reviews is one sample card. Before and after line no longer says yards have floors.
- **Services:** seven long bands become two big bands, three cards and two cards, each with one line and one "We take" line. "What we take and what we don't" becomes "What we can't take". Call links and "Anything else you point at, inside our list" cut. Pricing keeps its four loads with three fact chips.
- **Book:** the work order's home. Three small facts added under a shorter banner line. Step notes down to one helper each. Instant-booking alternates retired. New lines: demo and "Not sure" prices, ZIP and other fields marked optional, "Add your email", "Remove", "Try again" on the error state. Town notes moved here from the ticket. Shawn's call line unchanged, word for word.
- **Reviews:** filter column cut. "Used us already?" is now a line and two links at the end of the grid. Before and after line no longer says "the job from start to finish", because the pairs are two different places.
- **Donate:** the 74-word statement becomes one banner line plus one band line. Can is a plain line, Can't a marked list, Where it goes and How to ask two small facts. Own estimate band, which replaces the Book and call stack. "On the day" gone.
- **About:** statement, second paragraph and second action cut. Story is 60 words. Four values become three small facts: Upfront cut (Home says it), Local cut (the banner says it), No sales pitch added from v1's second paragraph. No year stated.
- **FAQ:** 17 questions down to 12. One-item and demo prices merged into the first answer, which no longer lists all four prices. "How can I pay" merged into "When". "Do I need to be home?" and "Can I change or cancel?" cut, along with their invented policies. Close row cut. "Yes, any time" against Mon to Sat fixed.
- **Contact:** contact cells cut except hours and where we go. Call pill added to the banner. "Phone or email is enough" now shows at rest, town marked optional. Real failed state written. Commercial is one line and a link.
- **Service area hub:** $149 cut from the meta, and "same prices" is said once on the page. New short heading and line for the chips, which the page lacked.
- **Town pages:** ticket, map and paragraph cut. One line and Book in Lowell on the banner, photo tile names, the row of four loads, a link to other towns.
- **Commercial:** headline now "Commercial and repeat work", since the form also offers Contractor and Other. Plan-and-price promise cut. Optional fields marked. Real failed state written, which no longer says "booking". "Enquiry" is now "request".
- **404:** down to one line. "The link was typed wrong" cut. Three links, not four.
- **Privacy:** length kept, three small fixes: "If you tick the box" now names the box and says "check", and analytics is added to who we share with. "Last updated" stays off until launch.

## Word counts
Counted by hand with revision.md's rule (words a visitor can see in main; hidden states, field hints, alt text, screen-reader text and the estimate band left out). The Developer's browser count is the real one.

| Page | Target | v2 | Note |
|---|---|---|---|
| Home | 300 to 400 | 359 | Home's estimate band adds 53 |
| Services | about 500 | 512 | |
| Book | about 170 | 204 | Over. All four steps counted, and a visitor sees one at a time. See below |
| Reviews | about 120 plus the reviews | 82 plus the samples | Under, not padded. About 195 with the six samples |
| Donate | about 170 | 145 | Under, not padded |
| About | about 180 | 153 | Under. The list in revision.md tops out about here |
| FAQ | about 350 | 354 | |
| Contact | about 110 | 120 | |
| Service area hub | about 80 | 74 | |
| Town pages | about 130 | 132 | |
| Commercial | about 80 | 88 | 79 until Regular pickups is picked |
| 404 | about 25 | 23 | |
| Privacy | legal copy stays | about 185 | |

## Home and Services words that now differ from the prototype
Build from copy.md, not the prototype's text.
- **Home:** meta description; hero line; hero pill's accessible name ("at"); hero alt ("gray"); yard tile ("cleanup piles"); price line ("before we show up"); before and after line; Reviews heading, line and link; towns line; town chip order (alphabetical within each state); the We confirm and We haul steps.
- **Services:** junk removal line; yard waste line ("Spring cleanup") and link; pricing line; can't-take line.

## For the Developer
1. **Links that name a job should open Book with that job picked** (?job=furniture and so on, the form's values: junk-removal, clean-out, furniture, appliances, mattresses, yard-waste, demo). The prototype's links all go to a bare book.html. Revision.md already flags that nobody has checked ?load= either.
2. **The hero line is about 10 characters longer than the prototype's.** Recheck the words against the truck at short laptop sizes, where the gap was already about 16px.
3. **About's call pill shows the number mid-page,** so the header's number would show too. Mark it data-call-here, or the number shows twice on one screen.
4. **Book needs three new states:** no size picked, Not sure, and Demo.
5. **Data files must follow:** site/data/prices.json (shorter fits), faq.json (12 questions), reviews.json (Home's one card, no job tags).
6. **Revision.md disagrees with itself on Privacy:** its table says one band, its section 7 says the estimate band runs everywhere but Book, Commercial and 404. No words depend on it. I would leave it off: the Privacy critic called it a loud close after a legal page. *Resolved by Varun, 5 Nov: off. revision.md and copy.md now agree.*

## My calls, for Varun to overrule
1. **"Plenty" of reviews** rests only on Shawn's chat line. Nobody here has seen his Facebook page.
2. **Book is over target.** Going lower means dropping a form field, which isn't a copy call. Cutting "Where's the junk" would save 13 words.
3. **Reviews, Donate and About are under target.** More words would have been repeats. They can take one more line each if the rebuilt pages read thin.
4. **FAQ cuts.** "Do I need to be home?" and "Can I change or cancel?" are real questions customers ask. I cut them because the answers were invented policy. They should come back once Shawn gives his rules.
5. **No year on About.** 2022 was a placeholder doing little work. It stays only in the held footer line.
