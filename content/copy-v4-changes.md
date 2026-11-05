# Quick Haul copy: v3 to v4, what changed
Copywriter, 2026-11-05. New copy: content/copy-v4.md (staged). Current copy until batch d promotes it: content/copy.md (v3), not edited in this pass. Earlier change lists: content/copy-changes.md. New placeholder values: the last section of content/placeholders.md. Daggers in copy-v4.md mark what is a placeholder; don't print them.

## When batch d promotes this file
1. Copy content/copy-v4.md over content/copy.md, keeping v3 as content/copy-v3.md, the way v1 and v2 were kept.
2. copy-v4.md was written from copy.md as it stood during this pass. If batch c adds a Developer note to copy.md for FAQ, Contact or Commercial after that, carry it across.
3. Batch c builds FAQ, Contact and Commercial from v3, so all three change again in batch d.

## Global (header partial, footer partial, tools/build.py)
- **Header nav:** Services; About; Pricing; Reviews; Donate. Towns is gone. Book now and the call line stay as they are.
- **Pricing link:** every `services.html#pricing` becomes `pricing.html`: header, menu, footer, 404. Keep the `#pricing` anchor on Services, and on the town pages, for anything still pointing at it.
- **Menu:** the same five, then a smaller second group, Service area; FAQ; Contact (accessible name: More pages). Commercial and Privacy are footer only. My call, see below.
- **Footer:** labels and columns don't change, because all five footer pages were already there. Only Pricing's target changes.
- **Estimate band:** the words stay. Pricing and About now carry their own, the way Donate does, so the same partial switch applies.
- **Truck labels:** Pricing's banner shares Services' label.
- **Towns leaving the header:** in-page links to the hub are added on Home, About, Pricing and the town pages.

## Home (src/pages/index.body.html)
Everything Varun approved stays. Four small additions:
- **What we haul:** new plain line (`.m-takes`) under the tiles: **We can't take** paint, oil and chemicals, propane tanks or asbestos.
- **Priced by the load:** new text link beside Book this load: See how pricing works.
- **Who's showing up (new slim band), between Reviews and Do you come to my town:** heading, one line, one link to About.
- **Do you come to my town:** new text link under the chips: See the full service area.

## Services
- **Banner:** the line grows from 14 to 23 words. Recheck it against the truck at 320 and 844x390.
- **Jump chips:** adds Can't take and Getting ready.
- **Not sure what to book? (new):** three small facts that sort a visitor into a pickup, a clean out or demo.
- **Junk removal, Furniture, Appliances, Mattresses, Yard waste, Demo:** each gains one **Good to know** line after its "We take" line. The card rows share a subgrid, so this is one new shared row.
- **How a clean out goes (new), under the clean outs promo:** Walk it, Load it, Sweep up.
- **Priced by the load:** the three fact chips come off, because the Pricing page says all of it in full. New link: See how pricing works. The row of four stays word for word.
- **What we can't take:** new anchor #cant-take. New plain line, **Where those go**, under the list.
- **Getting ready (new, anchor #getting-ready), last band before the estimate band:** Clear a path, Check inside, Mark what stays.
- **Meta description:** now ends "what it costs and how to get ready".

## Pricing (new page: site/src/pages-v2/pricing.body.html, pricing.html)
Built from Services' pricing band. Bands in order, with words:
| Band | Words | Holds |
|---|---|---|
| Banner | 27 | Heading "What it costs", one line, half-loaded truck |
| Jump chips | 14 | Seven links down the page |
| Four loads | 112 | Slate row of four trucks: price, pickup beds, what each holds, Book this load |
| Which load is mine? | 73 | Seated card, three small facts |
| What changes the price | 75 | Lead band: one photo, three small facts, one link to the hub |
| What's in the price | 53 | Slate promo: one photo, four-line list |
| What can cost more | 98 | Seated card, four-line list with no crosses |
| Two jobs, added up | 66 | Two cards with the sums laid out |
| Not quite a load? | 72 | Three small facts: one item, demo, regular pickups |
| From estimate to booked | 83 | Three small facts: You pick, Shawn confirms, We haul, you pay |
| Estimate band (outside main) | 26 | Its own words, with Shawn's agreed call line |

The sum in card two is $399 + $30 = $429. If either number changes, the total changes with it.

## Book (src/pages-v2/book.body.html)
Not in Varun's list, and a form doesn't get better with more words, so it is word for word v3 with one addition: on the load step, a text link, See what each load holds, to pricing.html#load-sizes. It opens in a new tab so the form isn't lost mid-booking.

## Reviews (src/pages-v2/reviews.body.html)
- **Six sample cards and the banner:** no change. `reviews.json` doesn't change.
- **End of the grid:** down to one link, Read the real ones on Facebook. Its line and the other link move to the new band below.
- **Word for word (new), after the grid:** Nothing edited, A name and a date, A link back. It keeps to the future tense while samples are up, and the launch line is under Held lines.
- **Before and after:** each pair gains one line under its caption: what a job like that usually takes.
- **Used us already? (new band), after the pairs:** What it was, How it went, Which town, and Leave a review on Facebook. New promise: "we'll send you the link after the job", from the offer's automated review requests.

## Donate (src/pages-v2/donate.body.html)
- **What we can donate:** the three facts leave this band. New plain line: **Good to know** Massachusetts bans clothes and other textiles from the regular trash.
- **How it works (new):** v3's "How to ask" text becomes the line. Where it goes and If it can't be donated are word for word. Need a receipt? is new.
- **Getting it ready (new):** Empty it, Keep it together, Wipe it down.
- **Run a charity nearby? (new, slim):** one line and a link to Contact. It invites and claims no partner.
- **Estimate band:** no change.

## About (src/pages-v2/about.body.html)
From 3 bands to 8, as Varun asked. In order, with words:
| Band | Words | Holds |
|---|---|---|
| Banner | 29 | **New heading: Hi, we're / Quick Haul.** The line is word for word v3 |
| About Quick Haul (new) | 74 | Lead band: one line, one photo, Owner-run, Who calls us, How to reach us |
| Pick up the phone (the story) | 81 | v3's slate promo, with one new opening line. "still answers the phone" becomes "still answers that phone" |
| What we do (new) | 77 | Three cards linking to Services: Clean outs, Junk pickups, Demo projects |
| How a job works (new) | 75 | Seated card, four steps, no numbers |
| The crew (new) | 67 | Three small facts, no person photo |
| Where we work (new) | 50 | Drawn map, the towns by state, can't-see line, link to the hub |
| What we stand for | 77 | v3's How we work, renamed. Same line. Talk first and Less in the dump are reworded so they state a stand and no unconfirmed fact. No sales pitch is now Straight prices, with the same text |
| Estimate band (outside main) | 22 | The closing call, in its own words, with Shawn's agreed line |

Keep `data-call-here` on the story's call pill.

## FAQ (data/faq.json, src/pages-v2/faq.body.html)
17 questions, up from 12. Group labels are now Pricing and paying; What we take; Booking; On the day. The Paying group's id changes to `on-the-day`. Regenerate the FAQPage JSON-LD.
- **New:** What kind of demo do you do? Can I change or cancel? Do I need to be home? How should I get ready? How long does a job take?
- **Moved:** When and how do I pay? goes into Pricing and paying. Do I need to carry anything outside? goes into On the day.
- **Longer answers:** How much does junk removal cost? (what's included, and a link to Pricing), What don't you take? (hazardous waste days), Do you donate things? (receipt).
- **Banner line:** now also says "what to expect on the day".
- Do I need to be home? and Can I change or cancel? were cut at v2 because their answers were invented policy. Both are back with no rule in them: they point to Shawn or a call, and state no fee, notice period or condition.

## Contact (src/pages-v2/contact.body.html)
- **Which way is best? (new), under the banner:** Call, Book, Ask, one line each.
- **Map and hours:** adds Email and Find us (the three social links).
- **Ask for a price:** new plain line above the fields: **It helps to tell us** what's going, where it is and whether the truck can get close.
- Everything else is word for word.

## Service area hub (src/pages-v2/service-area.body.html)
- **One price list, every town (new, slim):** one line, one link to Pricing.
- **When the curb won't take it (new):** one line, one photo. It speaks of "many towns", because Lowell runs its own bulky pickup and some towns differ, so this line stays off the town pages.

## Town pages (src/pages-v2/_templates/town.body.html, data/towns.json)
- **Banner:** the line adds "Loads start at $149."
- **What we haul:** the line adds "You don't need to drag anything to the curb."
- **How it works in Lowell (new):** one line, plus Home's three small facts.
- **Priced by the load:** the line adds "The prices are the same in Lowell as everywhere else we go." New link: See how pricing works.
- **Also near Lowell (new):** three chips in the slim strip, beside See other towns. The table is in copy-v4.md. I worked it out by hand as the three nearest by lat and lon in towns.json, so the build can compute it instead. Recheck when the real town list arrives.

## Commercial (src/pages-v2/commercial.body.html)
- **Who this is for (new):** Landlords, Realtors, Property managers and contractors, one line each, none claiming a past job.
- **Request form:** new plain line above the first field: **It helps to tell us** how many units or rooms, how close the truck can get and how soon you need it. It is the one thing v2's "form intro" cut that now comes back, as a list of what to tell us and no promise.

## 404 (src/pages-v2/404.body.html)
- **Line:** adds "Try one of these, or give us a call."
- **Links:** Home; Services; Pricing; Contact. Pricing goes to pricing.html from the site root.

## Privacy (src/pages-v2/privacy.body.html)
- **What we collect:** adds one sentence on cookies.
- **Photos you send (new):** we use them to price and plan the job, and they go on the site or social media only if the customer agrees.
- Still a draft. It needs review by someone qualified before launch, and the photo line needs Shawn's yes.

## Data files
- **prices.json:** add to each card the long fields: size ("About one pickup bed") and holds ("A couch and a chair, a mattress set and a dresser, or one big item."). Keep `fits` for Home, Services, Book and the town pages. Add a fridge fee, 30, and let the example sum read from the data if it's easy. Add to `_note`'s hand-typed list: the town banner line, Pricing's Just one item and the examples.
- **faq.json:** as above.
- **towns.json:** `near`, or compute it.
- **reviews.json:** no change.

## For the Developer
1. **Banner lines:** Services' line is 23 words, Pricing's 24, a town's 15. The longest built so far is About's at 25 and it clears the truck, but Services' scrim was sampled for a 14-word line, so re-sample.
2. **New recipes per page:** a suggestion for each band is in copy-v4.md. Never the same recipe twice in a row (revision.md section 5). Pricing has the most bands with facts, so vary those most.
3. **Stock:** no new downloads. New slots reuse logged photos: About opening (backyard-lawn-fence), About cards (basement-cleared, sofa-by-door, shed-weathered), Pricing (garage-clutter-before, basement-cleared, sofa-by-door, fridge-in-room), hub (sofa-by-door). Log each one where it lands.
4. **Drawn items:** Pricing uses item-sofa, item-boxes and item-fridge on its seated cards. All are already in assets/trucks/.
5. **The worked examples are the only place on the site with a sum.** Set them as label and figure rows, with the total stronger. The figures use the mono face's one job, price units, if that reads well.
6. **A preview label or gate is still needed before any deploy-preview.** This pass doesn't change that.

## Word counts
Counted by hand with the same rule as earlier passes: words a visitor can see in main, with hidden states, field hints, alt text, screen-reader text and the estimate band left out. All of a form's steps count. The Developer's browser count is the real one.

| Page | Asked for | v3 | v4 | Change |
|---|---|---|---|---|
| Home | a bit | 481 | 533 | +11%. 501 without the slim band |
| Services | +40 to 70% | 512 | 873 | +71% |
| Pricing | new page | 113, as a band on Services | 673 | New |
| Book | not listed | 200 | 205 | One link |
| Reviews | +40 to 70% | 222 | 367 | +65%. Without the sample cards, 118 to 263 |
| Donate | +40 to 70% | 164 | 275 | +68% |
| About | many more sections | 175 | 530 | +203%, from 3 bands to 8 |
| FAQ | back to about 16 questions | 354 | 557 | +57%, 17 questions |
| Contact | +40 to 70% | 120 | 196 | +63% |
| Service area hub | +40 to 70% | 74 | 127 | +72% |
| Town pages | +40 to 70% | 132 | 217 | +64% |
| Commercial | +40 to 70% | 88 | 144 | +64%. 135 until Regular pickups is picked |
| 404 | as needed | 23 | 33 | |
| Privacy | as needed | about 185 | about 230 | Legal copy, two additions |

Services' new bands, in words: Not sure what to book? 67, How a clean out goes 70, Getting ready 69. The Good to know lines add 126 across six services. Fact chips removed: 18.

## General facts and where they come from
These carry no dagger, because they aren't facts about Quick Haul. I read them through search results, not each source page in full, so they are worth one check before launch. Rules change.
- **Massachusetts bans mattresses and textiles from disposal, since Nov 1, 2022.** [MassDEP](https://www.mass.gov/news/new-waste-disposal-ban-regulations-take-effect-today), [Somerville](https://somervillema.gov/news/massachusetts-expands-waste-disposal-ban-include-mattresses-textiles). Used on the Mattresses card and on Donate. Some towns do collect mattresses for recycling, so the line says "can't just leave one out". The ban doesn't cover contaminated textiles, and the line doesn't go into that.
- **Both states keep yard waste out of landfills.** [NH RSA 149-M:27](https://gc.nh.gov/rsa/html/X/149-M/149-M-27.htm), [NHDES](https://des.nh.gov/blog/september-2021-leave-your-leaves-and-let-them-feed-your-soil), [MassDEP waste bans](https://mass.gov/eea/agencies/massdep/recycle/solid/massachusetts-waste-disposal-bans.html). Used on the Yard waste card. The search summary couldn't confirm NH's current subsection, and a recent NH bill touched this section, so check this one first.
- **Refrigerant has to be recovered before an appliance is scrapped.** [EPA, appliance disposal](https://www.epa.gov/section608/appliance-disposal). Used on Pricing. The $30 is ours, a placeholder. I found no sourced figure for what haulers charge.
- **Household hazardous waste days; old car batteries and propane tanks go back to the seller.** [Somersworth NH](https://www.somersworthnh.gov/node/86791), [Dunstable MA](https://www.dunstable-ma.gov/home/events/50141), [Dedham MA](https://www.dedhamma.gov/town-departments/health/household-hazardous-waste). Hence "many towns" and "usually". Used on Services and in the FAQ.
- **Bulky item limits and stickers vary by town.** [Danvers](https://www.danversma.gov/379/Bulky-Item-Pickup), [Wakefield](https://www.wakefieldma.gov/428/Bulky-Items-TVs-White-Goods), [Merrimac](https://townofmerrimac.com/273/Bulk-Items), [Lowell's own bulk pickup](https://lowellma.gov/1358/Curbside-Collection). I found nothing for most of the 12 placeholder towns, so the line says "many towns" and stays on the hub. "Transfer stations have their own rules" is general knowledge; the search found no local source for our towns.
- **Demo can need a permit, and older buildings can hide asbestos.** [MassDEP asbestos survey guide](https://www.mass.gov/doc/asbestos-survey-requirements-prior-to-demolition-or-renovation-information-guide/download), [Westford MA](https://westfordma.gov/216/Building-Demolition-Permit-Requirements). The guide says Massachusetts wants a survey before demolition or renovation whatever the building's age. Our line is softer and points to the building department. I found nothing on New Hampshire, so no line says anything state-specific about demo.
- **Pickup beds.** Fractions of a truck are the industry's norm ([1-800-GOT-JUNK](https://www.1800gotjunk.com/us_en/pricing), [LawnStarter](https://www.lawnstarter.com/blog/cost/junk-removal-price/)). Sources disagree on how many pickup loads make a full truck, from about 4 to 9. I used eight because it lines up with the fractions (1/8 is one). This one is a placeholder and carries a dagger.

## My calls, for Varun to overrule
1. **About's banner now reads "Hi, we're Quick Haul".** You asked for an "About Quick Haul" section ahead of the story, and with the banner's old heading the page would have said it twice in a row. It also suits the casual feel you asked for. To undo: banner back to "About / Quick Haul", band renamed "Who / we are".
2. **Home gets one new slim band, Who's showing up.** "Everything else stays as approved" was your earlier note, so this is the one thing on Home that adds a section. It is droppable, and Home would still be at 501.
3. **The phone menu keeps Service area, FAQ and Contact in a smaller second group.** With Towns gone from the header, a phone visitor would otherwise have to scroll to the footer to learn whether you come to their town. To follow the header exactly, cut the group.
4. **Services keeps a short price row.** A visitor reading about a job should still see what it costs without leaving, and the town pages have the same row. Only the chips came off. Services is at +71%, a hair over the band, and the hub at +72%. Neither felt worth trimming useful lines for.
5. **FAQ is 17, not 16.** How long does a job take? is the first to go if you want 16.
6. **About is 530 words, well past +70%,** because the eight sections you listed need words. No band tops 81. Most of it is placeholder, because Shawn has told us so little. This page will change the most when he answers.
7. **The origin line is an invention, flagged as one.** "It started with a truck, a phone and people who needed something gone" has no year, place or name in it, so it can't be caught out, but it is still a guess at his story. Same for "small on purpose", "not a franchise" (the brief infers this) and "works them too". All are logged as must-confirm.
8. **New practice claims, all placeholders, all logged:** sweeping up, a walk-through, taking furniture apart, a keep pile, "you'll hear it before we load anything", a link sent after the job, asking the charity for a receipt, and a customer's photos going online only with their OK.
9. **$30 for a fridge is made up,** because a worked example needs one extra with a number. Home's "Just one item? It's priced as a 1/8 load, so that's $149" doesn't mention it, and I left that as you approved it. Pricing does mention it. If Shawn confirms a fee, Home should follow.
10. **"Good to know" repeats six times on Services,** on purpose, so the eye learns where to look. If it reads as a template, keep it on the cards and drop it from the junk removal band.

## What I couldn't do
- The proposal PDF is still unreadable here: no poppler, and the viewer refused the local file (not in its allowed list). I didn't work around it, so its terms come from brief.md's quotes. Term 05 on reviews is the one this pass leans on.
- Nothing was seen in a browser. Fit against trucks and rows at real widths is the Developer's to check.
- Word counts are by hand.
