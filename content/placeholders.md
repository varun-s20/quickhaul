# Quick Haul: placeholder register
Every unconfirmed fact used anywhere in the project, so all of them can be replaced in one pass before launch (brief, checkpoint 1a rules). Nothing here may reach Shawn as if confirmed.

| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Phone number | (603) 555-0142, tel:+16035550142 | prototype/audition.html (every specimen), design/concepts.md (call line) | Shawn's business number | yes |
| Smallest load price | "1/8 truck from $149" | prototype/audition.html (fact chips) | Shawn's price bands, eighth to full truck | yes |
| Towns served | Haverhill, Salem, Nashua, Lowell (real towns in the MA and NH region from the brief, used only as examples) | prototype/audition.html (band tag) | Shawn's base town and full town list | yes |
| Demo work | "Demo projects too" | prototype/audition.html (fact chip) | What size of demolition he takes on | yes |
| Hero and section lines | "Junk out / Space back", the lede, the clean-outs paragraph | prototype/audition.html | Working lines only. The Copywriter writes the real copy | no (copy, not fact) |

Added by the Art Director, phase A, 2026-11-03. Later stages append here.

## Added in phase B (Art Director, 2026-11-03, hero prototype)
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Phone number | (603) 555-0142, tel:+16035550142 | prototype/index.html (top bar, header call circle, ticket call link, menu, action bar), prototype/assets/global.js (PHONE_HREF, PHONE_TEXT) | Shawn's business number | yes |
| Business hours | "Mon to Sat, 7am to 7pm" | prototype/index.html (top bar, menu hours line) | Shawn's real hours, and whether he works Sundays | yes |
| Price per load | 1/8 truck $149, 1/4 truck $249, 1/2 truck $399, full truck $649 (plausible round figures, inside the brief's market sense check for a full truck) | prototype/index.html (ticket load chips, data-price; "Price from" figure) | Shawn's price bands, and whether prices go on the site at all | yes |
| Towns served | Andover, Dracut, Haverhill, Lawrence, Lowell, Methuen (MA); Derry, Hudson, Londonderry, Nashua, Pelham, Salem (NH). Real towns in the region, used only as examples | prototype/index.html (town suggestion list, o-homeTicket__options), prototype/assets/global.js (TOWNS) | Shawn's base town and full town list | yes |
| Open days | The next three days after today, Sundays skipped (markup fallback: Wed 4, Thu 5, Fri 6 November 2026) | prototype/index.html (day chips), prototype/assets/global.js | Real availability from the booking calendar | yes |
| Hero lede | "Junk removal, clean outs and demo across Massachusetts and New Hampshire. Pick your town, your load and a day below, or give us a call." | prototype/index.html | Working line only. The Copywriter writes the real copy | no (copy, not fact) |
| Ticket notes | "We cover Massachusetts and New Hampshire", "Yes, we come to [town].", "Not on our list? Call (603) 555-0142" | prototype/index.html, prototype/assets/global.js | Working lines; the coverage claim depends on the town list | partly (coverage) |

## Added by the Copywriter (2026-11-03, content/copy.md)
Every value marked † in content/copy.md is listed here. The copy reuses the phone, hours, towns and load prices above unchanged. Note for the developer: the ticket's default note in copy.md is now "Start typing to check we come to you", replacing the prototype's "We cover Massachusetts and New Hampshire", so the strip makes no coverage claim before a town is typed.

### Trust claims and reviews (must confirm; never shown as confirmed)
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Licensed | HOLD cell: "Licensed to haul in Massachusetts and New Hampshire. Ask us for the details." | copy.md Home, trust indicators (held, not built) | Whether Quick Haul holds any licence, and in which state | yes, do not build until confirmed |
| Insured | HOLD cell: "Insured for the work we do on your property. We'll send proof if you ask." | copy.md Home, trust indicators (held, not built) | Whether he has liability insurance, and the cover | yes, do not build until confirmed |
| Guarantee | HOLD cell: "Shawn's guarantee goes here in his own words, once he confirms what it covers." | copy.md Home, trust indicators (held, not built) | Whether there is a guarantee, and its terms | yes, do not build until confirmed |
| Reviews | Sample cards worded as obvious samples ("Sample review. A real review from Quick Haul's Facebook page goes here..."), attributed "Sample review, Facebook". No stars, no score, no count | copy.md Home featured reviews (4 cards), Reviews page grid (6 cards) | Shawn's chosen Facebook reviews, exact text, name and date, plus the page URL | yes, replace, never edit into real-sounding reviews |
| Before and after "own jobs" line | HOLD line: "Every pair here is one of our own jobs, photographed on the day." | copy.md Home before and after, Reviews gallery | Shawn's own before and after pairs | yes, add only with his photos |

### Contact and business facts
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Email | quickhaul@example.com | copy.md footer, Contact, Privacy | Shawn's business email | yes |
| Base town | Salem, NH (map centre only) | copy.md Contact map | Where Quick Haul is based | yes |
| Sunday closed | "Closed Sundays." | copy.md Contact hours | Whether he works Sundays | yes |
| Coverage line | "Towns on both sides of the Massachusetts and New Hampshire line" | copy.md Home price section, About, Service area hub | True only if the real town list spans the border | yes |
| Same price in every town | Every town card "from $149", "all at the same prices" | copy.md Home price cards, Service area hub, town pages | Whether price varies by distance | yes |
| Year started | 2022 ("Shawn started Quick Haul in 2022", footer "Hauling since 2022", footer line held) | copy.md About split band, Footer fact line (held) | The real year | yes |
| Crew | "Shawn and a small crew" | copy.md About statement | Team size, and whether Shawn is happy to be named | yes |
| Shawn answers the phone | "still answers the phone himself" | copy.md About | Whether that is true | yes |
| Social handles | Facebook, Instagram, TikTok pills with no link | copy.md Footer | The three URLs | yes |

### Prices and booking rules
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| What fits in each load | 1/8 "a couple of big items, like a couch and a chair, or one mattress set"; 1/4 "a room's worth"; 1/2 "a small garage or basement clean out"; full "a packed garage, a full basement or a whole move-out"; ticket helper "1/8 is a couple of big items. Full is a packed garage." | copy.md Home ticket helper, Book load step, Services pricing cards | His truck size and what each band really holds | yes |
| What the price covers | "covers the loading, the hauling and the drop-off"; FAQ "Loading, hauling and drop-off are included." | copy.md Services pricing, FAQ | What is included and what is extra | yes |
| Heavy material surcharge | "Heavy loads like concrete, dirt or roofing shingles can cost more" | copy.md Services pricing | Whether heavy loads cost more | yes |
| Single item price | "A single item is priced as a 1/8 load, $149" | copy.md Services pricing note, FAQ | Single item or minimum price | yes |
| Demo pricing | "Demo work is priced per job" | copy.md Services pricing note, Demo band, FAQ | How demo is priced | yes |
| Price change on the day | "Only if the job is different from what we agreed... we tell you before we load anything" | copy.md FAQ | His real policy | yes |
| Booking model | Request-then-confirm ("Shawn looks over every booking and gets back to you to confirm the time and the price"), with instant alternates written | copy.md How it works, Book page, FAQ | Varun's decision (brief open question 3) | yes |
| Arrival windows | 8am to 11am; 11am to 2pm; 2pm to 5pm | copy.md Book, day step | His real time slots | yes |
| Customer not home | "If the junk is outside and the price is agreed, we can do the job while you're out." | copy.md FAQ | His policy | yes |
| Change or cancel | "Call us at least a day ahead" | copy.md FAQ | His policy | yes |
| Payment timing | "When the job's done, before we drive off." | copy.md FAQ | When customers pay; deposit or not (offer lists "Payment Integration - 1") | yes |
| Payment methods | "Card or cash." | copy.md FAQ | Accepted methods | yes |
| Carry-out service | "We carry it out from wherever it is, including basements and upstairs rooms"; "so you don't need to drag anything outside first"; furniture "down the stairs and onto the truck" | copy.md Services (junk removal, furniture), FAQ | Whether he does full-service carry-out | yes |
| SMS consent wording | "Text me booking updates and a reminder the day before. Message and data rates may apply. Reply STOP to opt out." | copy.md Book, Privacy | Check against the SMS provider and A2P 10DLC registration | yes (legal and technical) |
| Privacy policy | Plain-language draft | copy.md Privacy | Review against the real plugins and by someone qualified | yes |

### Services, items and donations
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| "What we take" lists | Per-service checklists (junk removal, clean outs, furniture, appliances, mattresses, yard waste) | copy.md Services bands | Shawn only named the categories; he needs to check every item | yes |
| Electronics and TVs | Listed under "We take" | copy.md Services, what we take | Whether he takes them (often regulated or charged extra in MA) | yes |
| "What we don't take" list | Paint, oil and chemicals; propane tanks and gas cylinders; asbestos; medical waste; car batteries; anything still connected to gas | copy.md Services, FAQ | His real exclusions | yes |
| Demo scope | Sheds, decks and porches, fences, playsets, above-ground pools and hot tubs, kitchen and bathroom tear-outs; "haul the debris away, so there's no dumpster sitting in your driveway" | copy.md Home services cell, Demo band | What size and kind of demo he takes on | yes |
| Yard waste detail | "Bag the small stuff if you can" | copy.md Yard waste band | Whether he needs leaves bagged | yes |
| Donation practice | "we sort out the good stuff and take it to local charities and reuse stores"; "anything still in good shape goes to donation"; "We'll load them separately" | copy.md Donate, How it works, About, FAQ, town pages | Whether Quick Haul donates at all, and how | yes |
| Donation destinations | "Local charities and reuse stores in Massachusetts and New Hampshire" (no names, on purpose: naming a real charity would be a claim about a real organisation) | copy.md Donate | Which charities, if any | yes |
| Can and can't donate lists | Donate page lists | copy.md Donate | What his donation partners accept | yes |
| Commercial and repeat work | Whole commercial enquiry page, Contact page commercial cell | copy.md Commercial enquiry, Contact | Whether he does commercial or recurring work | yes |

### Images (stock, per choices.md decision 3)
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Image alt text | Alt text written for the intended subject, never claiming a stock photo is a Quick Haul job | copy.md every image slot | Rewrite each alt when Shawn's own photo replaces the stock one. Source and licence of each stock image are logged by whoever places it | yes, must-replace |
| About photo | No stock person in Shawn's slot; stock truck or cleared garage until his photo arrives | copy.md About split band | A photo of Shawn, or Shawn with the truck | yes |

## Stock photos placed by the Developer (2026-11-04, homepage build)
Every image below is a stock placeholder under choices.md decision 3 and must be replaced with Shawn's own job photos before anything goes to him as final (proposal term 06). None is captioned or described as a Quick Haul job. Licence for all: Unsplash License (free for commercial and non-commercial use, no permission or attribution needed; the photos may not be sold unaltered or used to build a competing image service). Each one was listed as free (not Unsplash+) on its Unsplash page and downloaded from the images.unsplash.com CDN, not plus.unsplash.com. Originals: site/src/stock/. Crops, grade and sizes: site/data/images.json, site/tools/images.py.

| File (site/assets/images/) | What it shows | Photographer, Unsplash photo id | Source URL | Where used | Must replace |
|---|---|---|---|---|---|
| services/pickup-trash-bags | A white pickup truck piled high with black trash bags. Cropped tight so the number plate, the make badge and the street stay out of frame | iridial, photo-1781425009053-2baffa997d8c | https://unsplash.com/photos/a-white-pickup-truck-overloaded-with-black-trash-bags-F0b_VsXo3ls | Home, services overview, junk removal cell; Home og:image (replaced the red pickup of firewood, homepage rerun 1) | yes |
| services/basement-cleared | An empty finished basement with white walls, square pillars and a wood floor | Point3D Commercial Imaging Ltd., photo-1646592474103-cfd22d1d9e34 | https://unsplash.com/photos/TcnHgP7Nf5I | Home, services overview, garage and basement clean outs cell (replaced the busy workshop garage, homepage rerun 1) | yes |
| services/renovation-tearout | A house extension mid tear-out: OSB wall, a work table of tools, broken slab and old window frames | Annie Spratt (inferred: the id sits in her upload batch of renovation photos, 1785484267xxx, all hers and free; the photo's own page was not found, confirm before reuse), photo-1785484267511-77d63142023f | https://images.unsplash.com/photo-1785484267511-77d63142023f (photo- prefix, so a free Unsplash License photo, not Unsplash+) | Home, services overview, demo projects cell (replaced the collapsed shed, build round 1) | yes |
| services/sofa-by-door | A cream armchair and sofa set out beside a front door on a brick building | Vlad Ionita, photo-1772057593098-edb9b9429059 | https://images.unsplash.com/photo-1772057593098-edb9b9429059 | Home, services overview, furniture cell | yes |
| services/fridge-in-room | A pale retro fridge freezer against a brick wall on a wooden floor | Raymond Petrik, photo-1721563927724-74b1a0ddef33 | https://unsplash.com/photos/a-white-refrigerator-freezer-sitting-on-top-of-a-wooden-floor-5CJlOhMCOMY | Home, services overview, appliances cell (replaced the rusted fridge in grass, build round 1) | yes |
| services/mattress-at-curb | A discarded mattress on a concrete sidewalk, black and white | Sarah Louise Kinsella, photo-1788365621525-c161ddb0b2be | https://unsplash.com/photos/discarded-mattress-on-concrete-sidewalk-WaV1idsQlR0 | Home, services overview, mattresses cell (replaced the mattresses in a derelict room, build round 1) | yes |
| services/yard-waste-truck | The back of an orange utility truck loaded with green garden waste | Ries Bosch, photo-1781517028333-85014c59c9a4 | https://images.unsplash.com/photo-1781517028333-85014c59c9a4 | Home, services overview, yard waste cell | yes |
| before-after/garage-clutter-before | A white-walled garage crowded with ride-on mowers, chairs, a workbench and shelving | Clay Banks, photo-1726929219819-b90904f9d329 | https://unsplash.com/photos/a-garage-filled-with-lots-of-different-types-of-items-BrPQWVn5Xmo | Home, before and after slider (before side; replaced Richard Bell's brick-wall garage in build round 1 so both sides show white walls over a concrete floor at about the same horizon) | yes: needs Shawn's real before/after pair from one spot |
| before-after/garage-after | A tidy garage wall with tools hung up and a clear floor | Liz Crosswell, photo-1727823065187-7b11ee08c1d8 | https://images.unsplash.com/photo-1727823065187-7b11ee08c1d8 | Home, before and after slider (after side) | yes: needs Shawn's real before/after pair from one spot |

Notes for the swap:
- The before and after pair is still two different garages from two photographers (no free stock pair of one room before and after exists on Unsplash: searched "garage before and after" and "cluttered garage", 2026-11-04). Since build round 1 both are white-walled and cropped to about the same floor line, so the slider reads closer, but it is not one job. Kept for now (checkpoint 2c, decision 1): must-replace, needs Shawn's real before/after pair from one spot.
- Alt text (checkpoint 2c, decision 2): every homepage alt now describes the stock photo actually shown, listed below. They replace copy.md's alts on the page for as long as the stock stands. copy.md's alts describe the intended real photos and stay there as the starting point. Rewrite every alt again when Shawn's photos arrive.
- The photos are graded by tools/images.py so they read as one set inside the slate palette (values under "Homepage rerun 1").

### Other placeholders added by the Developer (2026-11-04)
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Facebook reviews link | https://www.facebook.com/ (bare platform address) | Home featured reviews text link | Quick Haul's Facebook page URL (reviews tab) | yes |
| Social pills | https://www.facebook.com/, https://www.instagram.com/, https://www.tiktok.com/ (bare platform addresses, allowed by critic-rulings.md) | Footer social pills | The three profile URLs | yes |
| Sample review cards | Not linked (copy.md says tap a review to read it on Facebook; samples have no post to link to) | Home featured reviews | Each real review's post URL | yes |

### Removed in build round 1 (2026-11-04)
Shed (Mandell Smock), rusted fridge (Ella Wimer), mattresses in a worn room (X F) and the brick-wall garage (Richard Bell) are no longer used anywhere. The critic read them as dereliction, not homes being cleared. Their files were removed from site/; the raw downloads stay in build/stock-raw/full/ for the record.
Social pill icons: Facebook, Instagram and TikTok marks from Simple Icons (CC0 1.0, simple-icons v13 via jsdelivr), in the header sprite. Trademarks of their owners, used only to link to the profiles.

### Homepage rerun 1 (2026-11-04, checkpoint 2c decisions)
Stock changes:
| Change | Old | New | Why | Licence |
|---|---|---|---|---|
| Swapped, junk removal cell and og:image | services/junk-pickup-load (Justin Meckes, photo-1574462233115-1a4a05e33433) | services/pickup-trash-bags (iridial, photo-1781425009053-2baffa997d8c) | Decision 3: the old one read as firewood delivery | Unsplash License, confirmed free on the photo's page 2026-11-04 |
| Swapped, clean outs cell | services/garage-clear-floor (Point3D, photo-1635108198854-26645ffe6714) | services/basement-cleared (Point3D, photo-1646592474103-cfd22d1d9e34) | Decision 3: the old one was a busy workshop, not a cleared room. No free, empty home garage turned up (the two found are Unsplash+ Getty images), so this cell shows the basement half of "garage and basement" | Unsplash License, confirmed free on the photo's page 2026-11-04 |
| Kept, marked | before-after/garage-clutter-before, before-after/garage-after | same files | Decision 1: needs Shawn's real before/after pair from one spot | Unsplash License |
| Regraded, every photo | Spec 2c grade: saturation .85, contrast 1.10, small cool gain | Saturation .42 (greens through teals .24, reds and oranges .06), contrast 1.03, then 34% of a tone map from ink through slate to a cool near-white. The speck grain over photos drops from .14 to .08 | Decision 4: keep the trucks and brick inside the slate palette. Set after critic rerun round 1 found pink casts, vivid greens and crunchy contrast in the first attempt. The files are altered from the downloads (grade and crop only); the Unsplash License allows that | Unsplash License |
| Recropped, junk removal | Focus x .425 | Focus x .40 | Critic rerun round 1: the title ran into the tail lamp | Unsplash License |
| Recropped, appliances | Focus y .50 | Focus y .58 | Critic rerun round 1: takes the SMEG badge out of frame | Unsplash License |
| Recropped, demo | Focus .50, .55, full width | Focus .43, .60, zoom 1.12 | Critic rerun round 1: takes the "Elliot" machine name out of frame. Sterling OSB's board stamps partly remain; they run down the middle of the shot | Unsplash License |

The old files were removed from site/; the raw downloads stay in build/stock-raw/full/. New downloads: build/stock-raw/round2/. The pickup's original shows an Italian number plate and an Isuzu badge, so keep it cropped as set in data/images.json (zoom 1.37) if it is ever recut.

Homepage alt text now on the page (rewrite again when Shawn's photos arrive):
| Slot | Alt |
|---|---|
| Junk removal, and og:image alt | A white pickup truck piled high with black trash bags |
| Clean outs | An empty basement with white walls, square pillars and a clear wood floor |
| Demo | A building site with bare OSB walls, tools on a work table and a broken concrete floor |
| Furniture | A pale armchair and a small sofa set out by the door of a brick building |
| Appliances | A pale retro fridge freezer beside a brick wall, with a small white bin at its foot |
| Mattresses | A discarded mattress lying on a concrete sidewalk |
| Yard waste | The back of a work truck loaded with green garden waste |
| Before | Before: a white-walled garage crowded with two ride-on mowers, a workbench, shelving and stacked gear. |
| After | After: a tidy garage wall with tools hung on racks above a clear concrete floor. |

## Stock photos, round 3 (Developer, 2026-11-04, inner pages)
Same rules: must-replace, under choices.md decision 3 and stage 6. Licence for all nine: Unsplash License; each photo's own page reads "Free to use under the Unsplash License" (checked 2026-11-04).

How the source was established: the run that downloaded these was killed before logging them, so nothing on disk named their source and the files carry no metadata. On 2026-11-04 each file was traced back: a small copy of the candidate photo from the Unsplash CDN was compared with our file (mean grey difference at 64 by 64; a mismatch scores 50 to 87). All nine match. Three scored higher (yard branches 10.64, lawn with deck 5.42, lawn with fence 4.14), so those were also compared by eye, side by side, and are the same photos. Results: build/tmp/match_stock.json, build/tmp/match-sheet.jpg.

| File (site/src/stock/) | What it shows | Photographer, Unsplash photo id | Source URL | Match score | Where used | Must replace |
|---|---|---|---|---|---|---|
| man-carrying-mattress | A man carrying a striped mattress on his head along a sidewalk | Rosa Jakobi, photo-1769972557854-7eae6f95585b | https://unsplash.com/photos/man-carrying-a-mattress-down-a-sidewalk-8QttzdTGGV4 | 2.82 | Services, mattress removal | yes |
| room-stacked-boxes | A small room stacked to the ceiling with cardboard boxes | Declan Sun, photo-1757837593538-b4a8654132f1 | https://unsplash.com/photos/a-room-filled-with-many-stacked-cardboard-boxes-6N6EXN0x_E4 | 2.08 | Reviews gallery, basement pair, before side | yes: needs Shawn's real pair from one spot |
| basement-unfinished | An unfinished basement with exposed joists, steel poles and stairs | Josh Lemmon, photo-1782353921981-bb73a53a7482 | https://unsplash.com/photos/spacious-unfinished-basement-with-exposed-joists-support-poles-and-stairs-hV-fLWrDF3I | 1.57 | Reviews gallery, basement pair, after side | yes: needs Shawn's real pair from one spot |
| yard-branches | A heap of cut branches and brush on grass | Iryna Muller, photo-1667755582571-d7b98b88d326 | https://unsplash.com/photos/a-pile-of-branches-and-leaves-AFzUMcg3AZI | 10.64, same by eye | Reviews gallery, yard pair, before side | yes: needs Shawn's real pair from one spot |
| backyard-lawn-fence | A fenced back yard with lawn, concrete patio and a large tree | Josh Lemmon, photo-1792628953895-5d46f431b402 | https://unsplash.com/photos/backyard-with-wooden-fence-and-patio-x1rFTWcXoOc | 4.14, same by eye | Reviews gallery, yard pair, after side | yes: needs Shawn's real pair from one spot |
| shed-weathered | A weathered wooden garden shed with glazed double doors | Ries Bosch, photo-1764786405596-75baf8e9c879 | https://unsplash.com/photos/a-weathered-wooden-shed-with-glass-windows-RcDC4eXm5Xw | 3.45 | Reviews gallery, shed pair, before side | yes: needs Shawn's real pair from one spot |
| backyard-lawn-deck | A grassy back yard with a wooden fence and a grey house with a small deck | Josh Lemmon, photo-1792630862784-562c292fbe46 | https://unsplash.com/photos/backyard-with-wooden-fence-and-house-GFAm_bzlU48 | 5.42, same by eye | Reviews gallery, shed pair, after side | yes: needs Shawn's real pair from one spot |
| dresser-and-chair | A wooden dresser with a mirror and lamp, and a wooden chair by a window | Clay Banks, photo-1603112089080-3ef8f7bb9dcf | https://unsplash.com/photos/brown-wooden-chair-beside-brown-wooden-drawer-Fr62lAJFnII | 1.23 | No longer used: replaced on Donate, see round 5 below. The original stays in site/src/stock/; nothing ships from it | yes |
| man-boxes-van | A man wheeling a tall stack of boxes on a hand truck beside a white van | Richard Stachmann, photo-1694715669993-ea0022b470f7 | https://unsplash.com/photos/a-man-is-unloading-boxes-from-a-van-GgmZ23grWNY | 2.36 | No longer used: replaced on About, see below. Never captioned or described as Shawn (choices.md, stage 6) | yes: needs Shawn's own photo |

Services page, recuts of photos already logged above (band- files in site/assets/images/services-page/, square crops at quality 88): band-basement (basement-cleared, Point3D), band-sofa (sofa-by-door, Vlad Ionita), band-fridge (fridge-in-room, Raymond Petrik), band-yard-truck (yard-waste-truck, Ries Bosch), band-tearout (renovation-tearout, Annie Spratt inferred). Services also reuses pickup-trash-bags (iridial). All must-replace.

Town pages (12, one template): pickup-trash-bags (iridial) is their og:image only, alt "A white pickup truck piled high with black trash bags". It is not of the town. Must replace. The what-we-haul band no longer shows it: that band now shows the map with the page's town marked (critic, Service area r1). The service area map is a real street map (OpenStreetMap data, OpenFreeMap tiles) with a pin for each placeholder town at its public map position. Pins follow data/towns.json, so they update with the real list.

Each pair in the Reviews gallery is two different places from two photographers: no free stock shows one spot before and after. Same must-replace note as the homepage pair.

Services alt text now on the page (rewrite when Shawn's photos arrive):
| Slot | Alt |
|---|---|
| Junk removal | A white pickup truck piled high with black trash bags |
| Clean outs | An empty basement with white walls, square pillars and a clear wood floor |
| Furniture | A pale armchair and a small sofa set out by the door of a brick building |
| Appliances | A pale retro fridge freezer beside a brick wall, with a small white bin at its foot |
| Mattresses | A man carrying a striped mattress on his head along a sidewalk |
| Yard waste | The back of a work truck loaded with green garden waste |
| Demo | A building site with bare OSB walls, tools on a work table and a broken concrete floor |

Reviews gallery: the garage pair reuses garage-clutter-before and garage-after (Clay Banks, Liz Crosswell, logged above). Derivatives in site/assets/images/before-after/ are named by slot: basement-boxes-before (room-stacked-boxes), basement-empty-after (basement-unfinished), yard-branches-before (yard-branches), yard-lawn-after (backyard-lawn-fence), shed-old-before (shed-weathered), shed-gone-after (backyard-lawn-deck). All must-replace.

Reviews placeholders: every card's Read on Facebook link, Leave a review on Facebook and See all our reviews on Facebook go to the bare https://www.facebook.com/ until Shawn sends his page and each review's post URL. Must replace.

Reviews alt text now on the page (rewrite when Shawn's photos arrive; copy.md's pair alts describe real pairs, so they wait for those):
| Slot | Alt |
|---|---|
| Garage, before | Before: a white-walled garage crowded with two ride-on mowers, a workbench, shelving and stacked gear. |
| Garage, after | After: a tidy garage wall with tools hung on racks above a clear concrete floor. |
| Basement, before | Before: a small room stacked to the ceiling with cardboard boxes. |
| Basement, after | After: an empty unfinished basement with exposed joists, steel poles and stairs. |
| Yard, before | Before: a heap of cut branches and brush on grass. |
| Yard, after | After: a fenced back yard with clear lawn, a concrete patio and a large tree. |
| Shed, before | Before: a weathered wooden garden shed with glazed double doors. |
| Shed, after | After: a grassy back yard with a wooden fence and a grey house with a small deck. |

## Stock photos, round 4 (Developer, 2026-11-04, About)
| File (site/src/stock/) | What it shows | Photographer, Unsplash photo id | Source URL | Licence | Where used | Must replace |
|---|---|---|---|---|---|---|
| old-pickup-driveway | An old Chevrolet pickup parked on a gravel driveway beside a stucco house. Shot in Prescott, Arizona, so not New England | Joseph Lee, photo-1633060774899-5a5b7aeb738d | https://unsplash.com/photos/a-blue-pick-up-truck-parked-in-front-of-a-house-e5wPdn2-HKE | Unsplash License; the photo's page reads "Free to use under the Unsplash License" (checked 2026-11-04) | About, split band and og:image | yes: needs Shawn's own photo |

Swapped on About: man-boxes-van (Richard Stachmann) came out after critic r1. Its readable Turkish plate and Istanbul street contradicted "local", and as the only person on the page he read as Shawn. Choices.md (stage 6) allows a stock person, but copy.md's own fallback for this slot is a work truck, so this follows that. The original stays in site/src/stock/; its cuts are deleted, so nothing ships.

About alt text now on the page (rewrite when Shawn's photo arrives): "A work truck parked in a residential driveway" (copy.md's stock alt for this slot, word for word).

## Stock photos, round 5 (Developer, 2026-11-04, Donate)
| File (site/src/stock/) | What it shows | Photographer, Unsplash photo id | Source URL | Licence | Where used | Must replace |
|---|---|---|---|---|---|---|
| dresser-on-street | A small wooden dresser set out on an empty street, in front of a wooden fence and rooftops. Shot in Le Havre, France, so not New England | eduard (@eduardmilitaru), photo-1498378520120-901cc2e4547e | https://unsplash.com/photos/brown-wooden-dresser-near-brown-fence-during-daytime-1a4UIXzapLw | Unsplash License; the photo's page reads "Free to use under the Unsplash License" (checked 2026-11-04) | Donate, photo tile and og:image | yes: needs Shawn's own photo of an item set aside for donation |

The run that downloaded this was killed before logging it, so the source was traced the way round 3's was: a small copy from the Unsplash CDN scored 1.87 mean grey difference at 64 by 64 against our file, a match (a mismatch scores 50 to 87). Copy: build/stock-raw/verify/dresser-on-street/.

Swapped on Donate: dresser-and-chair (Clay Banks) came out after critic r1, which read the antique room as off-story. It stays in site/src/stock/; its cuts are deleted, so nothing ships.

Donate alt text now on the page, and the og:image alt (rewrite when Shawn's photo arrives; copy.md's alt describes a dresser and a chair this photo doesn't show): "A small wooden dresser set out on an empty street, in front of a wooden fence and rooftops".

## FAQ (Developer, 2026-11-04)
No new stock. og:image is pickup-trash-bags (iridial, logged above), alt "A white pickup truck piled high with black trash bags", not of any job. Must replace. Every price, policy and hour on the page is a placeholder logged above; prices now also sit in site/data/faq.json's answers as well as site/data/prices.json and src/partials/ticket.html. The page's four line drawings are our own (no licence question).

## Contact (Developer, 2026-11-04)
No new stock. og:image is pickup-trash-bags (iridial, logged above), alt "A white pickup truck piled high with black trash bags", not of any job. Must replace. The phone, email, hours, "Closed Sundays", towns and the commercial cell are placeholders logged above. The map is a real street map with pins at the placeholder towns' public map positions. It isn't a Google Map: see site/README.md, Before launch. Copy.md's map centre (Salem, NH, placeholder) isn't marked on it. The form has no backend: photos stay hidden and a send shows the failure state with the phone until window.SITE_FORM_ENDPOINT is set. The drawing above the form is our own.

## Commercial enquiry (Developer, 2026-11-04)
No new stock. og:image is pickup-trash-bags (iridial, logged above), alt "A white pickup truck piled high with black trash bags", not of any job. Must replace. The whole page is placeholder wording until Shawn says he does commercial or repeat work (row above); the phone is the placeholder logged above. The form has no backend: photos stay hidden and a send shows the failure state with the phone until window.SITE_FORM_ENDPOINT is set. The banner's drawing is our own, of no real building.

## 404 (Developer, 2026-11-04)
No new stock. og:image is pickup-trash-bags (iridial, logged above), alt "A white pickup truck piled high with black trash bags", not of any job. Must replace. The drawing is the banner truck, our own. No facts on the page beyond the shared phone, email and hours logged above.

## Privacy (Developer, 2026-11-04)
No new stock. og:image is pickup-trash-bags (iridial, logged above), alt "A white pickup truck piled high with black trash bags", not of any job. Must replace. The whole policy is a plain-language draft (row above): it describes analytics, photo uploads, a booking calendar and text messages that aren't connected yet, so it must be checked against the real services and reviewed by someone qualified before launch. Business name, email and phone are the placeholders logged above. "Last updated" waits for the launch date.

## Copywriter, rewrite for the revised design (2026-11-05, content/copy.md v2)
Earlier rows name v1's sections as "where used"; v1 is now content/copy-v1.md. This section is what v2 prints. Unchanged and still placeholders: phone, hours, email, the four load prices, the town list, base town, "Closed Sundays", arrival windows, social and Facebook links, SMS wording, the privacy draft, the "we take" and "can't take" lists (shortened to one line each on Services), demo scope. Licensed, insured and guarantee stay HOLD and unbuilt, wording unchanged: the trust row is cut, so they now sit under "Held lines" in copy.md. Stock photos for the rebuild are the Developer's to log (design/revision.md section 7).

### New or reworded in v2
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Smallest load | "Loads start at $149" | copy.md Home hero, Home meta, town page meta | Shawn's smallest price | yes |
| Carry-out, short forms | "You point, we carry"; "loaded by us"; "We do the lifting"; "We load it and leave the space clear"; "load it ourselves" | copy.md Home hero and tile, estimate band, Book facts, Services junk removal, town pages | Whether he does full-service carry-out | yes |
| Price confirmed first | "we confirm the price before we show up"; "we confirm it before we show up"; "We'll confirm yours before we come"; "Shawn checks the job, the time and the price" | copy.md Home and Services price bands, estimate band, Book | Booking model, and whether he confirms every price | yes |
| Jobs with no set figure | "No problem. We'll price it from your photos or a quick call."; "Demo is priced per job. We'll price it with you from your photos or a quick call."; "We'll confirm it with you" | copy.md Book load step and confirmation | How he prices unsure loads and demo | yes |
| Time to book | "in a couple of minutes"; "It takes a couple of minutes." | copy.md estimate band, Book banner | Time the real booking form once the plugin is in | yes |
| Confirmation email | "A copy is on its way to your email." | copy.md Book confirmation | Depends on the booking plugin | yes |
| What fits, shorter | 1/8 "A couple of big items, like a couch and a chair."; 1/4 "A room's worth, or a pile of boxes and bags." (1/2 and full unchanged) | copy.md Home picker, Services and town price rows, Book | His truck size and what each band really holds | yes |
| Same prices in every town | "the prices are the same in every one"; "all at the same prices"; "Same prices in all of them". No town name or card carries a price now | copy.md Home towns, hub, hub meta | Whether price varies by distance | yes |
| Crew | "Shawn and a small local crew" ("local" is new here) | copy.md About banner and meta | Team size, where they are based, and whether Shawn is happy to be named | yes |
| About story | "Shawn still answers the phone himself"; "A quick call tells him what's in the garage, how close the truck can get and what to bring" | copy.md About promo | Whether that is how he works | yes |
| About facts | "A real number with a real person on the end of it"; "Tell us what's going and we'll tell you straight what it costs." | copy.md About, How we work | Whether that is how he works | yes |
| Donate, reworded | "the good stuff goes to local charities and reuse stores instead of the dump"; "Worn-out mattresses" (was "mattresses that have been slept on for years"); "We check what they're taking before each drop-off"; "tell us when we get there. We'll load it separately." | copy.md Donate | Whether Quick Haul donates at all, where, and what they accept | yes |
| Commercial, reworded | Heading "Commercial and repeat work"; "Landlord, realtor or property manager?"; "Ask about commercial work" | copy.md Commercial, Contact | Whether he does commercial or repeat work | yes |
| Review sample cards | Home now holds 1 card, "Sample review. A real one from Quick Haul's Facebook page goes here, word for word."; Reviews holds 6, with no job tags and no links | copy.md Home, Reviews | Shawn's chosen reviews, exact text, name, date and post URL | yes, replace, never edit into real-sounding reviews |

### Not a placeholder, but check it
| What | Wording | Where used | Source | To do |
|---|---|---|---|---|
| Reviews on Facebook | "We've got plenty on our Facebook page, in our customers' own words and with their names on them"; "Our Facebook page has plenty of them" | copy.md Home Reviews, Reviews banner | Shawn's own words in the chat, 31 Aug: "on my Facebook page I have plenty of reviews". Not a count or a rating. Nobody in the studio has seen the page | Read the page when the URL arrives |

### No longer printed in v2
- Year started: "Shawn started Quick Haul in 2022" is cut from About. 2022 is now only in the held footer line.
- Customer not home and change or cancel: both FAQ questions are cut, so "while you're out" and "at least a day ahead" are no longer on the site. The real policies are still unknown and stay in copy.md's client questions.
- "because the dump won't take them from us": cut from the can't-take line. Nobody had said it.
- Electronics and TVs: in no v2 list. The full-truck drawing does show a TV, so look at the drawing again if Shawn says he doesn't take them.
- Trust cells "Price first", "A real person" and "Reviews you can check": cut with the trust row. The last one's line is now HOLD.
- "so there are no surprises on the day", "so nothing changes in your driveway", "so we're never far away", "A two-minute call" and "show up when we said": cut.
- Instant-booking alternates: retired, since booking is written as a request Shawn confirms (choices.md, stage 6).
- About photo: the earlier row's "no stock person in Shawn's slot" is out of date. Stage 6 allows a stock person, never captioned or described as Shawn.

## Developer, revision rebuild, homepage (2026-11-05)
Every photo is still stock under choices.md decision 3 and must be replaced with Shawn's own before anything goes to him as final (proposal term 06). Licence for all: Unsplash License, as logged in the sections above. Originals: site/src/stock/. Crops: site/data/images.json. Treatment: site/tools/images.py is crop, resize and a small unsharp only, full colour, no grade and no grain (choices.md item 1, replaces checkpoint 2c decision 4), plus the paint-outs noted below, so the "photos are graded" notes above no longer apply. Every old inner page's derivatives were recut in colour too. Alts are copy.md v2's.

### New stock
| File (site/assets/images/) | What it shows | Photographer, Unsplash photo id | Source URL | Licence | Where used | Alt on the page | Must replace |
|---|---|---|---|---|---|---|---|
| home/towns-street, and banners/page-street and page-street-phone (cut, used when inner banners are rebuilt). Original: site/src/stock/portsmouth-street.jpg | A sunny street of old wooden houses with a brick sidewalk, Portsmouth, NH | Emi Mo, photo-1781819117983-1828a116f34f | https://unsplash.com/photos/historic-wooden-houses-line-a-sunny-street-with-shadows-j5TewHOqdpw | Page reads "Free to use under the Unsplash License", read 2026-11-04 by the Art Director through a fetch tool, not by eye in a browser. Worth one look before anything goes live | Home, Do you come to my town | A sunny street of old wooden houses with a brick sidewalk | yes |

### Stock already logged, new crops
| File | Original, photographer | Where used now | Alt on the page | Notes |
|---|---|---|---|---|
| home/hero-yard, home/hero-yard-phone | backyard-lawn-deck, Josh Lemmon | Home hero | A sunny back yard with a wide lawn, a wooden fence and a gray house | The slot wants Shawn's own photo of the truck at a job. **Too small for the very widest screens:** the original is 2400 wide, so on a window wider than that (2560, say) this full-bleed photo is stretched a little, 7% at 2560. Nothing else on the page is. Only a larger photo from Shawn fixes it |
| home/tile-junk, home/og-home | pickup-trash-bags, iridial | Home junk removal tile; Home og:image (1200 by 630) | A white pickup truck piled high with black trash bags | Crops keep the plate out. **The tailgate's ISUZU D-MAX badge is painted out** (RETOUCH): it sat inside this crop and showed beside the pill on hover (critic, home r2). A small label on the cab door, in the og:image crop only, stays; it is barely legible |
| home/tile-mattress | man-carrying-mattress, Rosa Jakobi | Home mattresses tile. Replaces the black and white curb mattress (revision.md section 6) | A man walking down a sidewalk with a striped mattress on his head | **A graffitied German "private property" sign and its number plates are painted out** of the hedge (RETOUCH), the bare post stays. The brick flats still don't read as New England |
| home/tile-sofa | sofa-by-door, Vlad Ionita | Home furniture tile | A cream armchair and a small sofa set out by the door of a brick building | |
| home/tile-fridge | fridge-in-room, Raymond Petrik | Home appliances tile | A pale green retro fridge freezer against a brick wall | **Maker badge painted out** in tools/images.py (RETOUCH), the one retouch, under the no-brands rule. The source is soft: extra sharpening only helps. Only Shawn's own photo fixes it |
| home/tile-yard | yard-waste-truck, Ries Bosch | Home yard waste tile | The back of an orange work truck loaded with green garden waste | |
| home/tile-garage | basement-cleared, Point3D Commercial Imaging Ltd. | Home clean-outs tile | An empty basement with white walls, square pillars and a clear wood floor | |
| home/tile-demo | shed-weathered, Ries Bosch | Home demo tile (was Reviews only) | A weathered wooden garden shed with glazed double doors | |
| home/compare-before | garage-clutter-before, Clay Banks | Home before and after, before side | Before: a garage crowded with a ride-on mower, a workbench, shelving and stacked gear | **"ARIENS", its gear emblem, the engine's Kawasaki label, "Cub Cadet" and the Benjamin Moore bucket painted out** in tools/images.py (RETOUCH), under the no-brands rule: they read once the slider is dragged, and "ARIENS" read large. Small labels on bottles and boxes in the clutter stay. Must replace: needs Shawn's real pair from one spot |
| home/compare-after | garage-after, Liz Crosswell | Home before and after, after side | After: a garage with a clear concrete floor and tools hung tidily on the wall | **"Rain Bird" painted out** on the wall box (RETOUCH); the Yakima mark is cropped out. Its crop is only 1500 wide and soft, so the slider now shows at 1120 wide at 1440, not 1344, and never wider than 1500 on a big screen. It still has flaking paint on the floor beside the line "the floor comes back". Must replace: needs Shawn's real pair |
| assets/fx/footer-joists | basement-unfinished, Josh Lemmon | Footer, every page, a faint plain photo at 14% | Decorative, CSS only, no alt | Texture, not a picture of a job |
| services-page/svc-junk, svc-garage, svc-sofa, svc-fridge, svc-mattress, svc-yard, svc-shed | As their originals above | Cut, not on any page until Services is rebuilt | As copy.md Services | Fridge retouch applies; plate rule applies to svc-junk |

### Other things added or changed
| What | Value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Logo | The mark cut from the phone screenshot at its native 234px (assets/images/brand/quickhaul-mark.png), shown 108px at the top of the page and 84px once scrolled. 108 to 117px is its sharp ceiling on a 2x screen. Also the door decal on every truck, at 132px inside the SVG | Header, every page; trucks | Shawn's original file or a vector. A bigger logo needs it. A logo swap means rerunning tools/images.py and tools/build_trucks.py | yes |
| Bio Sans Regular | assets/fonts/biosans-regular.otf, from the same supplied set as the other three | Body text, every page | Web licence still unconfirmed, as for the rest of Bio Sans (choices.md) | yes |
| Preview line | Off, Varun's call (choices.md item 4), behind PREVIEW_LABEL in tools/build.py; wording kept in the header partial and copy.md | Nowhere now | Set PREVIEW_LABEL True, or gate the preview, before any deploy-preview (brief) | yes, before any deploy |
| Town chips on Home | The 12 placeholder towns, names only, from site/data/towns.json | Home | Shawn's real list. If it isn't 12, the chips just wrap | yes |
| Facebook link on the review card | https://www.facebook.com/ (bare platform address) | Home, Read them on Facebook | Shawn's page URL | yes |
| Drawn truck and items | Our own drawing (tools/build_trucks.py). Not stock. The full load shows a TV: see the Copywriter's note above | Home hero, price band, review card | Nothing, unless Shawn says he doesn't take something drawn | no |

### No longer used
Removed from site/assets/ with their jobs: the old derivatives named basement-cleared, renovation-tearout, sofa-by-door, fridge-in-room, mattress-at-curb and yard-waste-truck (their originals stay in site/src/stock/; mattress-at-curb.jpg and renovation-tearout.jpg now have no job and are safe to delete). backyard-lawn-fence and basement-unfinished as an after side are still in use on the old Reviews page until it is rebuilt. assets/images/brand/quickhaul-logo.png is left in place but no page uses it any more. The Art Director's rejected downloads (washer-small-room, washer-basket, washers-courtyard in prototype/revision/stock-new/) were never brought across. Three stale files left from the old grade, band-tearout-1200, -793 and -800 in services-page/, had no job and no page using them, so they were removed too; the backup keeps a copy.

### Paint-outs, all together
tools/images.py (RETOUCH), on the original before any crop, so no hover, width or crop can bring them back. revision.md allowed one, the fridge's badge; the rest were added in the homepage rebuild under the same no-brands rule, and are Varun's to veto. Each changes a stock photo under the Unsplash License, and every one is must-replace regardless. Fridge badge; ISUZU D-MAX on the pickup; ARIENS, gear emblem, Kawasaki, Cub Cadet and Benjamin Moore in the before garage; Rain Bird in the after garage; the German sign on the mattress photo.

## Copywriter, v3 update (2026-11-05, content/copy.md v3)
From Varun's notes in design/choices.md, "Homepage approval and instruction to finish". The last version before this is content/copy-v2.md. Phone, hours, email, prices, towns, stock photos and every other value above are unchanged. Licensed, insured and guarantee stay HOLD and unbuilt. These cards replace the earlier "Reviews" row and the v2 "Review sample cards" row.

### Sample review cards: every one must be replaced by Shawn's real Facebook reviews
Six cards. Home shows cards 1 to 5; the Reviews page shows all six. On every card the who line is "Sample review" and the avatar is "SR" (decorative). No real names, no stars, no score, no count, no source line, no link. A sample is replaced, never edited into a real-sounding review (proposal term 05, as quoted in brief.md).
| Card | Sample wording | Where used | Real value needed | Must replace |
|---|---|---|---|---|
| 1 | "Sample review. A garage clean out goes here, told by the person whose garage it was." | Home Reviews band; Reviews grid; data/reviews.json | A real Facebook review of a garage or basement clean out: exact text, writer's name and initials, date, post URL | yes, by Shawn's real review |
| 2 | "Sample review. A quick word about a mattress pickup." | Home Reviews band; Reviews grid; data/reviews.json | A real Facebook review of a mattress pickup, same details | yes, by Shawn's real review |
| 3 | "Sample review. A real customer's words about a furniture pickup belong here." | Home Reviews band; Reviews grid; data/reviews.json | A real Facebook review of a furniture pickup, same details | yes, by Shawn's real review |
| 4 | "Sample review. A longer one fits here, about a yard cleanup, the kind people write after a big job." | Home Reviews band; Reviews grid; data/reviews.json | A real Facebook review of a yard cleanup, same details | yes, by Shawn's real review |
| 5 | "Sample review. Saved for a shed or deck demo, with the writer's name and date." | Home Reviews band; Reviews grid; data/reviews.json | A real Facebook review of a demo job, same details | yes, by Shawn's real review |
| 6 | "Sample review. An old fridge or a dead washer goes here, in the words of whoever had to live with it." | Reviews grid; data/reviews.json | A real Facebook review of an appliance pickup, same details | yes, by Shawn's real review |

The job on each card is only a guide to the mix. If Shawn's reviews cover other jobs, use his and drop the guide.

### Lines that go with the sample cards
These are true only while the samples are up. Their launch wording is under "Held lines" in copy.md.
| What | Wording now | Where used | When it changes | Must replace |
|---|---|---|---|---|
| Home's Reviews line | "These cards are samples for now. Real reviews from our Facebook page take their place, word for word." | copy.md Home, Reviews | When real reviews go in | yes |
| Reviews banner line | "Real reviews from our Facebook page land here, just as their writers left them. Until then, the cards below are samples." | copy.md Reviews, Banner | When real reviews go in | yes |
| Facebook link label | "Read the real ones on Facebook", linked to the bare https://www.facebook.com/ | copy.md Home, Reviews; Reviews, End of the grid | Shawn's page URL for the link. The label changes when real reviews go in | yes |

### New or reworded in v3
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Single item price, longer | "It's priced as a 1/8 load, so that's $149." | copy.md Home, Priced by the load | Single item or minimum price | yes |
| Mattresses, short form | "Twin to king, plus the box spring and bed frame." | copy.md Home tile | Shawn's real "we take" list | yes |
| Carry-out, short form | "even from upstairs" | copy.md Home furniture tile | Whether he does full-service carry-out, stairs included | yes |
| Appliances that don't work | "working or not" | copy.md Home appliances tile | Whether he takes dead appliances, and any extra cost | yes |
| Yard waste, short form | "bagged leaves and whatever the last storm brought down" | copy.md Home yard waste tile | Whether he needs leaves bagged and takes storm debris | yes |
| Clean outs list and choice | "We clear boxes and bins, shelving, old furniture, tools nobody uses, carpet and rugs."; "What stays is up to you." | copy.md Home, Before and after | What a clean out covers, and whether the customer picks what stays | yes |
| Towns not listed | "It may just not be on the list yet." | copy.md Home, Do you come to my town | The real town list, and whether he goes beyond it | yes |
| Pricing from a photo | "Not sure how much that is? Add a few photos when you book"; "Add a photo when you book and we'll price it from there." | copy.md Home, Priced by the load; Reviews, Before and after | How he prices from photos | yes |
| Donate, item that can't be donated | "It goes with the rest of your load, so you're not stuck with it." | copy.md Donate | Whether Quick Haul donates at all, and what happens to refused items | yes |
| About, no pressure | "Say no and that's fine." | copy.md About, How we work | Whether that is how he works | yes |

Book's picker and Home's load control now print short labels (1/8, 1/4, 1/2, Full). They name the same four placeholder loads, so nothing new to confirm.

### Not a placeholder, but check it
Every "real reviews from our Facebook page" line rests on Shawn's chat line of 31 Aug: "on my Facebook page I have plenty of reviews". Nobody in the studio has seen the page. Read it when the URL arrives.

### No longer printed in v3
- "We've got plenty on our Facebook page, in our customers' own words and with their names on them" and "Our Facebook page has plenty of them. The ones we bring over here stay word for word." Both contradicted the sample cards. The note above replaces the v2 section's "Not a placeholder, but check it" row.
- "Read them on Facebook" and "Read them all on Facebook".
- "Sample review, Facebook" and the "Facebook" source on the samples.
- Home's single sample card, and every "This card is sized for..." sample.
- The tile lines "Mattresses, box springs and bed frames, any size.", "Couches, dressers, desks and dining sets.", "Fridges, washers, dryers and stoves." and "Brush, branches, leaves and cleanup piles."

## Developer, P2 batch a: inner pages moved in (2026-11-05)
Merged from content/placeholders-add-pages.md as each page moves in. No new download in this batch unless a row says so. Every photo is stock and must be replaced before anything goes to Shawn as final. Licence and source: the rows above.

### Services
| File (site/assets/images/) | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk | **Too small for the very widest screens:** the original is 2400 wide, so on a window wider than that this full-bleed photo is stretched a little, 7% at 2560, the same as Home's hero. Only a larger photo fixes it. From 1025 up the crop sits at its foot, so the truck has brick walk and road under it. The real photo needs ground at the lower right too |
| services-page/svc-junk | pickup-trash-bags, iridial | Junk removal, wide photo, 472px tall at 1440 | A white pickup truck piled high with black trash bags | 2380 file added, all the crop has |
| services-page/svc-garage | garage-clutter-before, Clay Banks | Clean outs promo | A garage crowded with a ride-on mower, a workbench, shelving and gas cans | Paint-outs below. Small labels on bottles and boxes stay, including GTX on one bottle: legible only at 2560 |
| services-page/svc-sofa | sofa-by-door, Vlad Ionita | Furniture card | A cream armchair and a small sofa set out by the door of a brick building | |
| services-page/svc-fridge | fridge-in-room, Raymond Petrik | Appliances card | A pale green retro fridge freezer against a brick wall | Badge painted out. **Visibly the softest photo on the page, worst at 2560** (critic, Services r2). Replace it first |
| services-page/svc-mattress | man-carrying-mattress, Rosa Jakobi | Mattresses card | A man walking down a sidewalk with a striped mattress on his head | |
| services-page/svc-yard | yard-waste-truck, Ries Bosch | Yard waste card | The back of an orange work truck loaded with green garden waste | 1600 file added |
| services-page/svc-shed | shed-weathered, Ries Bosch | Demo card, 2:1 from 1025 up | A weathered wooden garden shed with glazed double doors | 1600 file added |

No new facts on Services: the "we take" lists, can't-take list, prices and fact chips are all logged above.

**Two more paint-outs** (tools/images.py, RETOUCH; critic, Services r2: both read at 2560). Same terms as the list above, and Varun's to veto: SATELLITE and the small badge on the pickup's door, which also comes out of the og:image crop; HEDGE SWEEP and its mark on the trimmer's blade cover in the before garage, which also comes out of Home's before photo. The blade cover reads as plain orange if you look close.

### Book
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Short banner | A sunny street of old wooden houses with a brick sidewalk | No truck on this banner, by revision.md |

No new facts. Every line with a dagger in copy.md's Book is already logged: time to book, arrival windows, "Shawn checks the job, the time and the price", jobs with no set figure, confirmation email, SMS wording. The calendar's open days (every day from tomorrow but Sundays, three months ahead) stay a placeholder until a booking system exists. The done state's truck is our own drawing, no licence question.

### Service area hub
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk | |

The map is a real street map, not stock, with pins at the placeholder towns' public map positions. It isn't a Google Map: see site/README.md, Before launch. If the real town list isn't these 12, check the pin labels at phone widths (the side each name sits on is MAP_SIDE in tools/build.py). No new facts.

### Town pages (12, one template)
| File | Original, photographer | Slot | Alt on the page |
|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo. It's Portsmouth, NH, and it appears on every town's page. The alt never names a place | Banner | A sunny street of old wooden houses with a brick sidewalk |
| home/tile-junk | pickup-trash-bags, iridial | Junk removal tile | A white pickup truck piled high with black trash bags |
| home/tile-garage | basement-cleared, Point3D Commercial Imaging Ltd. | Clean outs tile | An empty basement with white walls, square pillars and a clear wood floor |
| home/tile-sofa | sofa-by-door, Vlad Ionita | Furniture tile | A cream armchair and a small sofa set out by the door of a brick building |
| home/tile-fridge | fridge-in-room, Raymond Petrik, badge painted out | Appliances tile | A pale green retro fridge freezer against a brick wall |
| home/tile-mattress | man-carrying-mattress, Rosa Jakobi | Mattresses tile | A man walking down a sidewalk with a striped mattress on his head |
| home/tile-yard | yard-waste-truck, Ries Bosch. 1200 file added | Yard waste tile | The back of an orange work truck loaded with green garden waste |
| home/tile-demo | shed-weathered, Ries Bosch | Demo tile | A weathered wooden garden shed with glazed double doors |

| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Coming to each town | "We come to Lowell with the truck, load it ourselves and haul it away." on all 12 pages, each with its own town | Town template | Shawn's real town list, and whether he does full-service carry-out | yes |

### Also from the pages session's notes, for all inner pages
- og:image on Services, Book, hub and town pages: assets/images/home/og-home.jpg, from pickup-trash-bags, iridial, alt "A white pickup truck piled high with black trash bags". The later pages use it too.
- Every inner banner uses one street photo, as copy.md names it, including 12 town pages that aren't that street. Listed so it's a decision, not an accident: more banner photos would mean a download, a crop and a new scrim sample each. The other pages' rows stay in content/placeholders-add-pages.md until they move in.

## Developer, P2 batch b: Reviews, About, Donate moved in (2026-11-05)
Merged from content/placeholders-add-pages.md as each page moves in. Every photo is stock and must be replaced before anything goes to Shawn as final. Licence and source: the rows above, or round 6 just below.

### Stock photos, round 6 (Unsplash, read through the photo pages on 2026-11-05)
| File (site/src/stock/) | What it shows | Photographer, Unsplash photo id | Source URL | Licence | Where used | Must replace |
|---|---|---|---|---|---|---|
| cellar-shelves | Dark wooden shelves crammed with jars, saws, hardware and bags. No location given | Stephen Pontes (@s_apshot), photo-1784064857689-5f17c9e1539c | https://unsplash.com/photos/messy-cluttered-storage-room-filled-with-various-household-items-NGXcTod3yNI | Unsplash License; the photo's page reads "Free to use under the Unsplash License" | Reviews, grid photo | yes: needs Shawn's own photos |
| storage-room-clutter | A low storage room with loaded shelves, a blue barrel and a snowblower. No location given; the photographer is based in Ottawa | Point3D Commercial Imaging Ltd. (@3dottawa), photo-1635108198322-18c814f9b70f | https://unsplash.com/photos/a-garage-filled-with-lots-of-clutter-and-tools-RL1kwBnUiaA | Unsplash License; the photo's page reads "Free to use under the Unsplash License" | Reviews, basement pair, before side | yes: needs Shawn's own pair from one spot |
| fall-house-drive | A gray gambrel-roofed house behind a burning bush and a big bare tree, with a paved drive in front. Shot in Wisconsin, per its page, so not New England | Mandie Barber (@barbermandie), photo-1636330038781-5dd07e2ecd32 | https://unsplash.com/photos/a-house-with-a-tree-in-front-of-it-y-x76kQ8g9o | Unsplash License; the photo's page reads "Free to use under the Unsplash License" | About, Pick up the phone promo | yes: needs Shawn's own photo. Not his job and not local, and the page doesn't say it is |

Raw copies: build/stock-raw/round6/, one folder per photo.

### Reviews
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk | |
| reviews/cellar-shelves | cellar-shelves, Stephen Pontes | Grid photo, no caption | Dark wooden shelves crammed with jars, saws, hardware and bags | New |
| services/pickup-trash-bags | pickup-trash-bags, iridial | Grid photo, no caption | A white pickup truck piled high with black trash bags | Square crop, because from 1025 the photo fills what its column's cards leave |
| services-page/svc-mattress | man-carrying-mattress, Rosa Jakobi | Grid photo, no caption | A man walking down a sidewalk with a striped mattress on his head | |
| before-after/garage-clutter-before | garage-clutter-before, Clay Banks | Garage pair, before | Before: a garage crowded with a ride-on mower, a workbench, shelving and stacked gear | Paint-outs listed above. Recut at 4:3 |
| before-after/garage-after | garage-after, Liz Crosswell | Garage pair, after | After: a garage with a clear concrete floor and tools hung tidily on the wall | Recut at 4:3, so the whole wall shows and less floor. Paint-outs below |
| before-after/storage-room-before | storage-room-clutter, Point3D | Basement pair, before | Before: a low storage room with loaded shelves, a blue barrel, a covered board and a snowblower | New. It has a garage door's track on the ceiling, so it is a garage more than a basement. The caption says Basement because that's the job shown, and the alt doesn't |
| before-after/basement-empty-after | basement-unfinished, Josh Lemmon | Basement pair, after | After: an empty unfinished basement with exposed joists, steel poles and stairs | Recut at 4:3. Reads almost as black and white beside the warm photos, and it stays, because a finished basement promised a renovation (critic, Reviews r1 faulted this one, r2 the other). Only Shawn's pair settles it |
| before-after/yard-branches-before | yard-branches, Iryna Muller | Yard pair, before | Before: a heap of cut branches and brush on grass | Recut at 4:3 |
| before-after/yard-lawn-after | backyard-lawn-deck, Josh Lemmon | Yard pair, after | After: a lawn scattered with a few leaves, in front of a wooden fence and a small deck | 1200 wide, so the two sit at one distance and share the fallen leaves. A heap of sticks painted out |
| before-after/shed-old-before | shed-weathered, Ries Bosch | Shed pair, before | Before: a weathered wooden garden shed with glazed double doors | Recut at 4:3, so the whole shed shows |
| before-after/shed-gone-after | backyard-lawn-fence, Josh Lemmon | Shed pair, after | After: a fenced back yard with clear lawn, a concrete patio and a large tree | 4:3 crop |

Each pair is two different places, must-replace with Shawn's own pairs from one spot. Grid photos carry an alt and no caption, and stay away from cards about their own job at every width (build/tmp/p2/flow_reviews.py). The drawn boxes and bags on two cards' edges are our own, from the truck set, so there's no licence question.

| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Facebook links, Reviews | "Leave a review on Facebook" and "Read the real ones on Facebook" go to https://www.facebook.com/ | Reviews, end of the grid | Shawn's page URL, and the page's review link | yes |

**Swapped: the basement pair.** room-stacked-boxes (Declan Sun) was a sneaker warehouse: Nike, adidas, Yeezy, Fila and Chinese lettering on every stack, readable at 1440, and too many to paint out. room-stacked-boxes has no job and its original is safe to delete; its cuts are gone, so nothing ships.

**More paint-outs** (tools/images.py, RETOUCH), same terms as the list above, and Varun's to veto. On cellar-shelves: the WD-40 can is now a plain blue can, the Kjeldsens tin's name and oval, Berol Dexter on the sharpener, and the Shelby, Piedmont and Ironman packaging. Its crop leaves a Safety 1st blister out. On storage-room-clutter: John Deere on the snowblower's hood, the Crock-Pot box, the old oven's two plates, Silverwood on a crate, the script on a white box; its crop leaves a CIL box and the engine's labels out. On garage-after: five Spikeball tags, Clicgear and Yakima, because this wider crop shows them; Home's tighter crop never did and is unchanged. On backyard-lawn-deck: a ring of bricks heaped with sticks on the lawn, which also comes out of Home's hero the next time every photo is recut (Home's file isn't recut now, and it isn't in that hero's crop as far as anyone can see at that size). On fall-house-drive: the house's number. Small hardware labels stay, like the ones in the before garage: legible only at 2560 if at all.

### About
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk | |
| about/fall-house-drive | fall-house-drive, Mandie Barber | Pick up the phone promo | A gray house with a barn-shaped roof behind a bright red shrub and a big bare tree, with a paved drive in front | **MUST REPLACE with Shawn's own photo.** It isn't one of his jobs and it isn't local: it was shot in Wisconsin, per its page. The page doesn't say otherwise: no caption, and the alt names no place. The house's number is painted out. Alt once Shawn's photo arrives: "Shawn, owner of Quick Haul, beside the truck" |

**Swapped: the old pickup.** old-pickup-driveway (Joseph Lee) showed a Chevrolet bowtie on the grille and the plate frame and a Custom Deluxe badge on the fender, on a gravel yard and a stucco wall, shot in Prescott, Arizona, on a page that says "local". A paint-out would have left the Arizona. Its original stays in site/src/stock/ with no job and is safe to delete; its cuts are gone, so nothing ships. Tried for one round and dropped: a red and yellow service truck (Steven Cordes, Unsplash, photo-1779397144441-63857e244892). Its plate painted out, nothing was readable, but on an About page it read as Shawn's truck beside "how close the truck can get" (critic, About r1). So this slot has no vehicle or person until he sends his own. man-boxes-van stays retired. The raw copy is in build/stock-raw/round6/; nothing of it ships.

No new facts on About. "Shawn still answers the phone himself", "a small local crew", the hours and "Less in the dump" are placeholder wording, logged above; "Say no and that's fine" is in the v3 list.

### Donate
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk | |
| donate/dresser-on-street | dresser-on-street, eduard | Big photo, and og:image | A small wooden dresser set out on an empty street, in front of a wooden fence | **Must replace with Shawn's own photo of an item set aside for donation.** Shot in Le Havre, France. Cropped in during this batch, so the skyline, chimney, aerial and roofs are gone, with only tile seen through the fence's slats. Heavy grain, its own grade. The blue tag on its side has nothing readable, so it stays. 1156 wide, all the crop has, and shown at most 1138 wide |

The whole page is placeholder wording, logged above ("Donate, reworded", the rows on donation practice, destinations and lists, and "If it can't be donated" in the v3 list). No named charities, on purpose. The truck with the dresser and bike is our own drawing, so there's no licence question.

## Developer, P2 batch c
Merged from content/placeholders-add-pages.md as each page moved in. Same rules as above: nothing here may reach Shawn as if confirmed, and every stock photo is must-replace.

### FAQ
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Short banner | A sunny street of old wooden houses with a brick sidewalk | |

The four drawn items (boxes, fridge, dresser, bags) are our own, from the truck set, so there's no licence question. No new facts: prices, policies and hours in the answers are logged above, and data/faq.json carries the prices as well as data/prices.json. og:image is the shared crop, assets/images/home/og-home.jpg, from pickup-trash-bags (iridial).

## Copywriter, v4 expansion (2026-11-05, content/copy-v4.md, staged)
This section lists what copy-v4.md prints. None of it is on the site until batch d builds it, and content/copy.md stays v3 until then. Unchanged and still placeholders: phone, hours, email, the four load prices, the town list, base town, "Closed Sundays", arrival windows, social and Facebook links, SMS wording, the privacy draft, the "we take" and "can't take" lists, demo scope and the six sample review cards. Licensed, insured and guarantee stay HOLD and unbuilt. No new stock: new bands reuse photos logged above, and the Developer logs each new slot where it lands.

### Prices and what each load holds
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Load sizes | "About one pickup bed"; "About two pickup beds"; "About four pickup beds"; "About eight pickup beds"; "count how many pickup beds it would fill" | copy-v4.md Pricing, Four loads and Which load is mine | His truck's size and what each band really holds. Eight was chosen because it lines up with the fractions; outside sources range from about 4 to 9 pickup loads in a full truck | yes |
| What each load holds, long form | 1/8 "A couch and a chair, a mattress set and a dresser, or one big item."; 1/4 "A room's worth, a bedroom set, or a pile of boxes and bags."; 1/2 "A small garage or basement clean out, or what's left after a move."; full as logged above | copy-v4.md Pricing, Four loads | What each band really holds in his truck | yes |
| Fridge, freezer and AC fee | "That adds $30 each."; "A fridge or freezer adds its $30."; "One fridge: $30" | copy-v4.md Pricing, What can cost more, Not quite a load, Two jobs | Whether he charges this, and how much. The figure is ours, with no source behind it | yes |
| Worked examples | Couch and chair: 1/8 truck $149, extras none, total $149. Basement and fridge: 1/2 truck $399, one fridge $30, total $429. "Ground floor, nothing heavy. Everything's in the load price."; "They're examples, not quotes." | copy-v4.md Pricing, Two jobs | His real prices. Redo both sums when they arrive | yes |
| What's in the price, long form | "On an everyday load, the price covers the whole job, start to finish."; "We do the lifting and carrying, from wherever it is."; "The truck, the gas and the trip."; "The dump fees on everyday junk."; "We sweep the spot when we're done." | copy-v4.md Pricing | What is really included, and whether he sweeps up | yes |
| What can cost more | "Most everyday loads don't run into any of this. If yours does, you'll hear it before we load anything."; "Concrete, dirt, brick and shingles weigh more and cost more to drop off." (brick is new); "Several flights of stairs or a long walk to the truck. Tell us when you book."; "Stairs, tight turns and long walks to the truck take more time."; "Extra items on the day can move you up a load. You'll see the new price first." | copy-v4.md Pricing | His real extras, and whether stairs cost more | yes |
| Estimate wording | "A rough guess is fine, because we confirm it before we come."; "We'll tell you which load fits."; "Some jobs don't fit the four sizes, so they're priced a little differently."; "The price is set once Shawn has looked it over and confirmed it with you."; "You pay when the job's done." | copy-v4.md Pricing | Booking model, and when customers pay | yes |
| Load lines on the pairs | "A garage like this is usually a 1/2 to a full truck."; "Usually around a 1/2 truck, depending on what's on the shelves."; "A pile like this is usually a 1/4 to a 1/2 truck." | copy-v4.md Reviews, Before and after | What such jobs really take in his truck. Replace with each real job's load when his own pairs arrive | yes |
| Smallest load on town pages | "Loads start at $149." | copy-v4.md Town pages, banner | Shawn's smallest price | yes |
| Same prices, new wording | "the prices are the same everywhere we go"; "at the same prices in every town"; "A load costs the same in Lowell as it does in Londonderry."; "The prices are the same in Lowell as everywhere else we go." | copy-v4.md Pricing, About, Service area hub, Town pages | Whether price varies by distance | yes |

### How a job runs
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| No sorting first | "You don't have to sort it first. Just bag loose small stuff if you can." | copy-v4.md Services, Junk removal | Whether he needs anything sorted or bagged | yes |
| Taking furniture apart | "If not, we can take it apart." | copy-v4.md Services, Furniture | Whether he does | yes |
| Appliance prep | "Empty the fridge before we come, and tell us if anything's still plumbed or wired in." | copy-v4.md Services, Appliances | Whether he disconnects appliances | yes |
| Clean out steps | "Most start with a quick walk-through and end with a swept floor."; "Still deciding on something? We can work around a keep pile."; "We carry it out to the truck, so you don't have to drag anything out first."; "We sweep the spot when we're done, so you get the floor back." | copy-v4.md Services, How a clean out goes | How his clean outs really run | yes |
| A job's steps | "From the first call to the swept floor, it goes like this."; "You walk us through what goes and what stays."; "We load it, sweep up and take it away. You pay when it's done." | copy-v4.md About, How a job works | How his jobs really run | yes |
| Being home | "It helps to have someone there at the start to show us what goes and what stays. If you can't be there, tell Shawn when he confirms and you can work it out." | copy-v4.md FAQ | His policy. This wording sets no rule, unlike the v1 answer logged above | yes |
| Change or cancel | "Call us as soon as you know and we'll work it out with you." | copy-v4.md FAQ | His policy. This wording sets no fee or notice period, unlike the v1 answer logged above | yes |
| How long a job takes | "One item can be minutes, and a full basement can take a few hours." | copy-v4.md FAQ | His real times | yes |
| Carry-out, town pages | "You don't need to drag anything to the curb." | copy-v4.md Town pages | Whether he does full-service carry-out | yes |

### About and Home
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| How it started | "It started with a truck, a phone and people who needed something gone." | copy-v4.md About, Pick up the phone | How Quick Haul really started. A guess at his story, with no year, place or name in it | yes |
| Answers the phone, new wording | "Shawn still answers that phone himself, and that's on purpose."; "He still answers the phone himself, so the person you talk to knows your job before the truck rolls." | copy-v4.md About; Home, Who's showing up | Whether that is true | yes |
| Owner-run | "Quick Haul is Shawn's business, not a franchise. You deal with the owner." | copy-v4.md About, About Quick Haul | "my junk removal business" is his own (chat, 28 Aug). "Not a franchise" is the brief's inference | yes |
| Crew | "Quick Haul is small on purpose. The people you talk to are the people who show up."; "The owner. He answers the phone, looks over the jobs and works them too."; "A small local team, with enough hands for the job in front of them."; "They'll check with you first, then do the lifting. You don't need to help." | copy-v4.md About, The crew | Who is on the crew, and how they work | yes |
| Stands, reworded | "Tell us what's going and we'll tell you straight what it costs. Say no and that's fine."; "If something's still good, we'd rather see it used again than buried." | copy-v4.md About, What we stand for | Whether Shawn agrees, and whether he donates at all | yes |

### Reviews, Donate, Contact, Commercial, Privacy
| What | Placeholder value | Where used | Real value needed | Must confirm |
|---|---|---|---|---|
| Review link after a job | "we'll send you the link after the job" | copy-v4.md Reviews, Used us already | Whether the offer's automated review requests go live, and what they send | yes |
| Donation receipt | "Say so when you book and we'll ask the charity for one."; "Need a receipt? Say so and we'll ask for one." | copy-v4.md Donate, FAQ | Whether he donates, and whether a receipt is possible | yes |
| Invitation to charities | "If you run a shelter, a thrift store or a reuse store in Massachusetts or New Hampshire, tell us what you can use." | copy-v4.md Donate | Whether Shawn wants these messages. It names no partner | yes |
| Social links on Contact | "Find us. Facebook, Instagram and TikTok." on the bare platform addresses | copy-v4.md Contact | The three profile URLs | yes |
| Who commercial is for | "Unit turnovers, what tenants leave behind, shared basements and storage."; "Clearing a listing before photos or showings."; "Regular pickups, and debris after a job." | copy-v4.md Commercial | Whether he does commercial or repeat work at all, and for whom | yes |
| Customer photos | "We use them to price and plan your job. We don't put them on the site or on social media unless you say it's OK." | copy-v4.md Privacy | Whether he wants to use customer photos, and review by someone qualified | yes (legal) |
| Cookies | "Analytics tools can use cookies to do this, and you can block cookies in your browser settings." | copy-v4.md Privacy | Check against the analytics tool actually used, and review by someone qualified | yes (legal) |

### Not a placeholder, but check it before launch
General information, so these carry no dagger in copy-v4.md. Sources are in content/copy-v4-changes.md. Read through search results, not each source page in full, and rules change.
- "Massachusetts bans mattresses from the regular trash, so you can't just leave one out at the curb." Services, Mattresses.
- "Massachusetts bans clothes and other textiles from the regular trash." Donate.
- "Massachusetts and New Hampshire both keep yard waste out of their landfills, so it can't go with the trash." Services, Yard waste. Check New Hampshire's current wording first.
- "Federal rules say the refrigerant has to come out before they're scrapped." Pricing.
- "Many towns run a household hazardous waste day for paint and chemicals. Places that sell car batteries or fill propane tanks usually take the old ones back." Services, FAQ.
- "Many towns limit big items at the curb or charge for a sticker, and transfer stations have their own rules." Service area hub. Not checked for most of the 12 placeholder towns, and Lowell runs its own bulky pickup, so it stays off the town pages.
- "Demo can need a town permit, and older buildings can hide asbestos." Services, Demo; FAQ. Nothing found on New Hampshire. Massachusetts' own guide asks for a survey whatever the building's age, which is stricter than this line.
- "Also near" on town pages: the three nearest towns on the placeholder list, from the public map positions in site/data/towns.json. Redo with the real list.

### No longer printed in v4
- About: "Easy to reach. A real number with a real person on the end of it, Mon to Sat, 7am to 7pm." and "Anything still good goes to donation where we can, not straight on the pile." Reworded under What we stand for and About Quick Haul.
- Services: the three fact chips, which the Pricing page now covers. Home's facts still carry the same rules.
- Header and menu: "Towns", replaced by Service area in the footer and the phone menu's second group.

FAQ's line-up on the fold (branches, mattress, fridge, sofa, armchair, dresser and TV, boxes, bike) is our own drawing too. It stands for copy.md's list under "What do you take?", already logged as a placeholder; if Shawn's list changes, the drawing follows it.

### Contact
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Short banner | A sunny street of old wooden houses with a brick sidewalk | |

The map is a street map with pins at the placeholder towns' public map positions (see the hub). copy.md's map center, Salem NH, is a placeholder and isn't marked on it. The form has no backend: photos stay hidden and a send shows the failed state with the phone until window.SITE_FORM_ENDPOINT is set. Commercial's line is already logged ("Commercial, reworded"). The fridge and boxes on the form's card are our own drawing. No new facts. og:image is the shared crop, assets/images/home/og-home.jpg.

### Commercial
| File | Original, photographer | Slot | Alt on the page | Notes |
|---|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Short banner | A sunny street of old wooden houses with a brick sidewalk | |

The whole page stays placeholder wording until Shawn says he does commercial or repeat work (already logged). The form has no backend, as on Contact. The truck, sofa, armchair, boxes and bags are our own drawing. No new facts. og:image is the shared crop, assets/images/home/og-home.jpg.

## Developer, P2 batch d (2026-11-05)
Copy v4 is now built on every page, so "Copywriter, v4 expansion" above is live, not staged. No new downloads this batch: every new slot reuses a logged photo. Everything here stays must-replace.

### Pricing
| File | Original, photographer | Slot | Alt on the page |
|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk |
| home/compare-before | garage-clutter-before, Clay Banks | What changes the price | A garage crowded with a ride-on mower, a workbench, shelving and gas cans |
| pricing/pricing-basement | basement-cleared, Point3D | What's in the price | An empty basement with white walls, square pillars and a clear wood floor |
| pricing/pricing-sofa | sofa-by-door, Vlad Ionita | Two jobs, first card | A cream armchair and a small sofa set out by the door of a brick building |
| pricing/pricing-fridge | fridge-in-room, Raymond Petrik, badge painted out | Two jobs, second card | A pale green retro fridge freezer against a brick wall |

### About
| File | Original, photographer | Slot | Alt on the page |
|---|---|---|---|
| about/about-yard | backyard-lawn-fence, Josh Lemmon | About Quick Haul | A fenced back yard with clear lawn, a concrete patio and a large tree |
| pricing/pricing-basement | basement-cleared, Point3D | What we do, Clean outs | An empty basement with white walls, square pillars and a clear wood floor |
| services-page/svc-sofa | sofa-by-door, Vlad Ionita | What we do, Junk pickups | A cream armchair and a small sofa set out by the door of a brick building |
| services-page/svc-shed | shed-weathered, Ries Bosch | What we do, Demo projects | A weathered wooden garden shed with glazed double doors |

The Pick up the phone photo (fall-house-drive) is already logged under "About". The crew slot has no photo on purpose: it waits for Shawn's.

### Service area hub
| File | Original, photographer | Slot | Alt on the page |
|---|---|---|---|
| pricing/pricing-sofa | sofa-by-door, Vlad Ionita | When the curb won't take it | A cream armchair and a small sofa set out by the door of a brick building |

### 404 (merged from placeholders-add-pages.md)
| File | Original, photographer | Slot | Alt on the page |
|---|---|---|---|
| banners/page-street, page-street-phone | portsmouth-street, Emi Mo | Banner | A sunny street of old wooden houses with a brick sidewalk |

No new facts.

### Privacy (merged from placeholders-add-pages.md)
No photos. The draft and its business name, email and phone are already logged. It describes analytics, photo uploads, a booking calendar and text messages that aren't connected, and v4 adds cookies and "Photos you send", so it needs checking against the real services and review by someone qualified before launch. "Last updated" waits for the launch date.

### Also from placeholders-add-pages.md: decisions, not accidents
- Every inner banner uses one street photo, the same Portsmouth street on all pages, including 12 town pages that aren't Portsmouth. The alt never names a place.
- Before and after pairs are two places each, until Shawn's own pairs from one spot arrive.
- Reviews grid photos repeat Services and Home photos, because no other stock is logged for that job.

### Where used, corrected by request 014 (cleanup)
Older rows above still name the old pages. These lines replace their "where used". Licence and source rows stay as logged.
| Photo or crop | Now |
|---|---|
| band-basement, band-tearout, band-sofa, band-fridge, band-man-mattress, band-yard-truck | Deleted from site/assets/images/services-page/, with their image jobs. The originals stay in site/src/stock/ where they have other jobs |
| renovation-tearout | Not on the site. No image job since the revision homepage; the original is still in site/src/stock/ |
| mattress-at-curb, old-pickup-driveway, dresser-and-chair, man-boxes-van, room-stacked-boxes | Not on the site. No image job; the originals are still in site/src/stock/ and can go |
| backyard-lawn-fence | About Quick Haul (about-yard), and the shed pair's after on Reviews |
| garage-clutter-before | Home's compare, Reviews' garage pair, Services' clean outs promo, Pricing's What changes the price |
| garage-after | Home's compare and Reviews' garage pair |
| pickup-trash-bags | Home's tile, Services' band, town tiles, Reviews' grid and the og:image on most pages |
| assets/fx/grain.svg | Deleted, with the old pages' banner rule |

## Page banners and the estimate band, photos (trucks retired from both)
Only Home's hero keeps a truck. All stock, must-replace, Unsplash License, logged with their sources above. Crop only.
- Services: man-boxes-van. Pricing: storage-room-clutter. Reviews: backyard-lawn-fence. Donate: dresser-and-chair. FAQ: shed-weathered. Contact: man-carrying-mattress. Commercial: renovation-tearout. 404: basement-cleared. Service area and the 12 town pages: fall-house-drive, which isn't of any listed town. About and Book keep portsmouth-street.
- Estimate band, every page that has it: cta-after (garage-after) large, compare-before (garage-clutter-before) as the "Before" snapshot. As on Home's slider, these are two different stock garages, not one job. Replace with one real before and after pair from Shawn, or the Before and After tags say something untrue at launch.

## Varun's revision: review photos, crew photos, fact icons (2026-11-07)
All stock, must-replace, Unsplash License, logged with their sources above. Crop only (site/data/images.json), no new downloads. No alt names Shawn or calls a photo a Quick Haul job.

| Crop (site/assets/images/) | From (site/src/stock/) | Where used | Alt now on the page | Must replace with |
|---|---|---|---|---|
| reviews/review-dresser | dresser-and-chair (Clay Banks) | Home, reviews grid, top row | A wooden dresser with a mirror and lamp beside a wooden rocking chair, by a sunny window | Shawn's own job photos, or drop the photos when real reviews arrive |
| reviews/review-house | fall-house-drive (logged above) | Home, reviews grid, second row | A gray house with a barn-shaped roof behind a bright red shrub and a big tree, with a paved drive in front | as above |
| reviews/cellar-shelves (existing crop) | cellar-shelves (logged above) | Home, reviews grid, second row, from 1025 up only; still on Reviews too | Dark wooden shelves crammed with jars, saws, hardware and bags | as above |
| about/crew-owner | man-carrying-mattress (Rosa Jakobi) | About, the crew, "Shawn" | A man walking down a sidewalk with a striped mattress on his head | A photo of Shawn |
| about/crew-team | man-boxes-van (Richard Stachmann) | About, the crew, "The crew" | A man wheeling a tall stack of cardboard boxes on a hand truck along a street | A photo of the crew at work |
| about/crew-property | backyard-lawn-deck (Josh Lemmon) | About, the crew, "On your property" | A sunny back yard with a wide lawn, a wooden fence and a gray house | A customer's yard or drive after a job, with permission |
| pricing/pricing-one-item | dresser-on-street (logged above) | Pricing, not quite a load, "Just one item" | A small wooden dresser set out on an empty street, in front of a wooden fence | Shawn's own photo |
| pricing/pricing-demo | shed-weathered (Ries Bosch) | Pricing, not quite a load, "Demo" | A weathered wooden garden shed with glazed double doors | Shawn's own demo photo |
| pricing/pricing-regular | portsmouth-street (logged above) | Pricing, not quite a load, "Regular pickups" | A row of old shingled houses along a quiet sidewalk | Shawn's own photo |

Notes:
- This undoes two earlier calls, on Varun's instruction. Home's reviews had no stock photos, so that none would read as the job a review is about; the photos now sit between the cards, never inside one and never beside a card about the same job (data/reviews.json, _home_note). About's crew had no stock person; it now has two. As the first photo under "Shawn", the mattress carrier will read as him, so the crop keeps his face hidden behind the mattress. The crew photo keeps the Turkish plate and the "Dikkat köpek var" sign out of frame (crop zoom 1.9), but the street is still Istanbul's.
- Not used, on purpose: room-stacked-boxes (brand lettering on every stack, see above) and renovation-tearout for any new crop (Makita cases, SterlingOSB print and an Elliott dumper in most of the frame).
- The "not on the site" row under request 014 no longer holds for dresser-and-chair and man-boxes-van.
- Fact icons on Pricing (which load, from estimate to booked), Reviews (word for word, used us already), Donate (getting it ready) and Book (the three steps): Lucide line icons, ISC licence, in site/src/partials/icons.html. Not a placeholder; nothing to replace.
