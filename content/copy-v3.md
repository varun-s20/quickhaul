# Quick Haul: site copy, v3 for the revised design
Copywriter, 2026-11-05. A targeted update of v2 for Varun's notes in design/choices.md, "Homepage approval and instruction to finish". Only Home, Reviews, Donate, About and Book's picker labels changed. Older versions: content/copy-v2.md and content/copy-v1.md. Written from those, the built site/index.html, design/revision.md, brief.md, prd/client-chat.txt and content/placeholders.md. What changed, page by page: content/copy-changes.md.

## How to read this file
- Organized by page, then by band, using the band names in design/revision.md section 4. They replace the section list in design-spec.md.
- Text level: revision.md section 2, set by Varun at checkpoint R1. One short heading, one or two supporting lines, at most one short list or three small facts. It replaces the write-copy skill's 40 to 80 words a section. Since Varun's homepage approval, Home's main content sits at about 450 to 500 words, and Reviews, Donate and About rise about 10 to 15 percent.
- Headlines are two rows, in reading order. The row in bold here is the heavy weight; the other is the light weight. Most headlines put the heavy row second; service names put it first, so the bold lands on the word a visitor scans for. Written in sentence case; the CSS sets them in capitals. No full stops, no italics, no color change.
- Body copy is final wording, in US English.
- Every value marked with a dagger (†) is a placeholder: a realistic stand-in for a fact Shawn has not confirmed. Each one is in content/placeholders.md with what is needed to replace it. The dagger is for this file only; do not print it on the site.
- Lines marked HOLD are written but must not be built until the fact behind them is confirmed. They are collected under "Held lines" near the end.
- Phone everywhere: (603) 555-0142†, tel:+16035550142. Hours everywhere: Mon to Sat, 7am to 7pm†. Email: quickhaul@example.com†.
- Prices everywhere: 1/8 truck $149†, 1/4 truck $249†, 1/2 truck $399†, full truck $649†.
- Image slots hold stock for now (choices.md, 2b decision 3 and stage 6). Every alt describes the photo actually shown and never claims it is a Quick Haul job or a real place on the list (checkpoint 2c). If a different photo is placed, the alt changes with it. Rewrite every alt when Shawn's own photos arrive.

---

## Global (every page)

### Preview label (off for now, required before any deploy-preview)
Varun took this line off the page. The brief still requires it, or a gate, before Shawn sees a preview.
- Text: Design preview. Phone, hours, towns, prices, reviews and photos are sample content until Quick Haul confirms them.

### Skip link
- Skip to content

### Header
- Nav: Services; Pricing; Towns; Reviews; Donate
- Logo alt: Quick Haul home
- Call link: Questions? Give us a call (603) 555-0142†
- Button: Book now
- Phone: Menu (button label)

### Menu
- Accessible name: Menu
- Close button accessible name: Close menu
- Links: Services; Pricing; Towns; Reviews; Donate; About; FAQ; Contact
- Buttons: Book now; (603) 555-0142†

### Call bar (phones, call-only)
- Button: Give us a call (603) 555-0142†
- Region accessible name: Call Quick Haul

### Estimate band
On every page except Book, Commercial, 404 and Privacy (Varun, 5 Nov: the lighter option, design/revision.md conflict 21). Donate has its own words (see Donate).
- Headline: Got a garage / **full of junk?**
- Line: Pick a day online in a couple of minutes†, or call and tell us what you've got.
- Button: Book now
- Home only, three small facts between the line and the button:
  - You book. Pick a day and your load.
  - We confirm. Shawn checks the job, the time and the price.†
  - We haul. We load it and leave the space clear.†

### Footer
- Phone (big, underlined): (603) 555-0142†
- Hours under the phone: Mon to Sat, 7am to 7pm†
- Email: quickhaul@example.com†
- Column: Services. Junk removal; Clean outs; Yard waste; Demo projects; Commercial
- Column: Booking. Book now; Pricing; Service area; FAQ
- Column: Quick Haul. About; Reviews; Donate; Contact; Privacy
- Social pills: Facebook; Instagram; TikTok (each adds "opens in a new tab" for screen readers; profile links wait for Shawn†)
- Fact line: Junk removal and demo across Massachusetts and New Hampshire
- Back to top
- Created with love by Digital Heroes

### Truck labels (accessible names, one load per page as revision.md section 5 suggests)
- Home hero: The Quick Haul truck, piled high with a sofa, boxes, a mattress, a dresser, a bike and yard waste
- Load picker, Home and Book, changes with the chip: The Quick Haul truck carrying an eighth of a load; a quarter of a load; half a load; a full load, piled high
- Price row, Services and town pages: The Quick Haul truck with an eighth of a load; with a quarter of a load; with half a load; with a full load, piled high
- Services banner: The Quick Haul truck, half loaded, parked on the street
- Reviews and town banners: The Quick Haul truck, a quarter loaded, parked on the street
- FAQ, Contact and About banners: The Quick Haul truck with a small load, parked on the street
- Donate banner: The Quick Haul truck with a dresser and a bike set apart at the curb (Developer, 5 Nov: the load in the body is a quarter now, Studio Lead's ruling. These words still hold.)
- Commercial banner: The Quick Haul truck with a full load, parked on the street (Developer, 5 Nov: drawn as a full body with no heap, because "piled high" is Home's alone. These words still hold.)
- 404 empty truck and the drawn items on seated cards: decorative, no label

---

## Home
- Meta title: Junk Removal and Demo in MA and NH | Quick Haul
- Meta description: Junk removal, clean outs and demo work across Massachusetts and New Hampshire. Loads start at $149†. Book a day online or give us a call.
- Preview builds prefix the description with "Design preview with placeholder content." and stay noindex.

### Hero
- Headline: Junk out / **Space back**
- Line: Junk removal, clean outs and demo work across Massachusetts and New Hampshire. Loads start at $149†. You point, we carry.†
- Button: Book now
- Button: Give us a call (603) 555-0142† (accessible name: Give us a call at (603) 555-0142)
  - Known exception, Developer 5 Nov: in landscape windows from 641 to 1240 wide the pill shows the phone icon and number only, because the words reach the truck's load at short heights (revision round, critic r2). The accessible name keeps the words.
- Photo alt: A sunny back yard with a wide lawn, a wooden fence and a gray house

### What we haul
- Headline: What we / **haul away**
- Line: Most of what's in a house, a garage or a yard can go on the truck. If it's heavy, awkward or just in the way, ask us.
- Photo tiles (name, the line under the photo, then alt), in the prototype's order. Each name links to its band on Services:
  - Junk removal. Anything from one couch to a full truck, loaded by us.† Alt: A white pickup truck piled high with black trash bags
  - Mattresses. Twin to king, plus the box spring and bed frame.† Alt: A man walking down a sidewalk with a striped mattress on his head
  - Furniture. Couches, dressers, desks and dining sets, even from upstairs.† Alt: A cream armchair and a small sofa set out by the door of a brick building
  - Appliances. Fridges, washers, dryers and stoves, working or not.† Alt: A pale green retro fridge freezer against a brick wall
  - Yard waste. Brush, branches, bagged leaves and whatever the last storm brought down.† Alt: The back of an orange work truck loaded with green garden waste
  - Garage and basement clean outs. Clear the floor and get the room back. Alt: An empty basement with white walls, square pillars and a clear wood floor
  - Demo projects. Sheds, decks and tear-outs taken down and hauled off.† Alt: A weathered wooden garden shed with glazed double doors
- Button: Book now
- Text link: See everything we take

### Priced by the load
- Headline: Priced by / **the load**
- Line: You pay for how much of the truck your junk fills. Not sure how much that is? Add a few photos when you book and we confirm the price before we show up.†
- Load control (Varun, 5 Nov: much smaller and lighter, same function):
  - Visible label: How full?
  - Chips: 1/8; 1/4; 1/2; Full
  - Group's accessible name: How full is the truck. Each chip's accessible name keeps the word: 1/8 truck; 1/4 truck; 1/2 truck; Full truck
  - The readout below keeps the long form ("$149 for a 1/8 truck"), so nobody has to guess what 1/8 means.
- Price and note, changing with the picker†:
  - $149 for a 1/8 truck. A couple of big items, like a couch and a chair.
  - $249 for a 1/4 truck. A room's worth, or a pile of boxes and bags.
  - $399 for a 1/2 truck. A small garage or basement clean out.
  - $649 for a full truck. A packed garage, a full basement or a whole move-out.
- Button: Book this load
- Three small facts†:
  - In the price. The loading, the hauling and the drop-off.
  - Just one item? It's priced as a 1/8 load, so that's $149.
  - Heavy stuff or demo? Concrete, dirt and shingles can cost more. Demo is priced per job.

### Before and after
- Headline: Before / **and after**
- Line: Drag the line across to see what a clean out does. The junk goes, the floor comes back and the room is yours again.
- Slider tags: Before; After
- Slider accessible name: Compare before and after. Value text at rest: Half before, half after
- Alt, before: Before: a garage crowded with a ride-on mower, a workbench, shelving and stacked gear
- Alt, after: After: a garage with a clear concrete floor and tools hung tidily on the wall
- Plain line under the slider: **We clear** boxes and bins, shelving, old furniture, tools nobody uses, carpet and rugs.† What stays is up to you.
- Button: Book a clean out
- Text link: See more before and afters

### Reviews
Five sample cards, worded so nobody can mistake them for real reviews (Varun, 5 Nov). No stars, no score, no count, no real names and no customer's voice (proposal term 05). Each one holds the place of one of Shawn's real Facebook reviews and is logged in content/placeholders.md as must-replace. They are cards 1 to 5 of the Reviews page's six, the way the agreed scope features a few reviews on the homepage.
- Headline: Read the / **reviews**
- Line: These cards are samples for now. Real reviews from our Facebook page take their place, word for word.
- Who line on every card: Sample review. Avatar on every card: SR (decorative). The same initials on purpose, so they can't be read as five people. No source line, because these words didn't come from Facebook.
- Sample cards, in this order:
  1. "Sample review. A garage clean out goes here, told by the person whose garage it was."
  2. "Sample review. A quick word about a mattress pickup."
  3. "Sample review. A real customer's words about a furniture pickup belong here."
  4. "Sample review. A longer one fits here, about a yard cleanup, the kind people write after a big job."
  5. "Sample review. Saved for a shed or deck demo, with the writer's name and date."
- Real reviews fill the same slots: initials, the writer's name, "Facebook" and the date. A sample is replaced, never edited into a real-sounding review.
- Text link, one for the band: Read the real ones on Facebook (adds "opens in a new tab" for screen readers; goes to the placeholder link until Shawn sends his page†)
- Drawn sofa and chair: decorative, no alt. They sit on one card's edge, not on all five.

### Do you come to my town
No price on any town name. The price lives in the band above, and this line says once that it doesn't change by town.
- Headline: Do you come / **to my town?**
- Line: Probably. We cover towns on both sides of the Massachusetts and New Hampshire line, and the prices are the same in every one.† Pick yours to see what we haul there.
- Town chips†, each linking to its town page: Andover; Dracut; Haverhill; Lawrence; Lowell; Methuen; Derry; Hudson; Londonderry; Nashua; Pelham; Salem
- Line under the chips: Can't see your town? It may just not be on the list yet.† Give us a call (the last four words are the phone link)
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

---

## Services
- Meta title: Junk Removal Services in MA and NH | Quick Haul
- Meta description: Garage and basement clean outs, furniture, appliance, mattress and yard waste removal, plus demo projects. See what we take, what it costs and book a day online.

### Banner
- Headline: Our / **services**
- Line: Clean outs, single items, yard waste and demo work across Massachusetts and New Hampshire.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Jump chips
- Region accessible name: On this page
- Chips: Junk removal; Clean outs; Furniture; Appliances; Mattresses; Yard waste; Demo; Pricing

### Junk removal (lead band, anchor #junk-removal)
- Headline: **Junk** / removal
- Line: Got a pile and no easy way to get rid of it? Tell us how much of the truck it fills and pick a day. We do the lifting.†
- We take†: **We take** boxes and bags, old furniture and rugs, exercise equipment, bikes and toys, move-out leftovers, scrap wood and metal.
- Button: Book now (screen readers hear: Book now for junk removal)
- Photo alt: A white pickup truck piled high with black trash bags

### Garage and basement clean outs (promo, anchor #clean-outs)
- Headline: Garage and basement / **clean outs**
- Line: Garages and basements fill up slowly, then all at once. Point at what goes and what stays, and we leave you with a floor you can actually use.
- We take†: **We take** boxes and bins, shelving, old furniture, tools nobody uses, carpet and rugs.
- Button: Book a clean out
- Photo alt: A garage crowded with a ride-on mower, a workbench, shelving and gas cans

### Furniture, appliances and mattresses (three cards)
Region accessible name: Furniture, appliance and mattress removal

**Furniture (anchor #furniture)**
- Headline: **Furniture** / removal
- Line: Too big for your car or too heavy to move on your own? We take it, and pieces in good shape can go to donation.†
- We take†: **We take** couches and sectionals, recliners, dressers, desks and dining sets.
- Link: Book a furniture pickup
- Photo alt: A cream armchair and a small sofa set out by the door of a brick building

**Appliances (anchor #appliances)**
- Headline: **Appliance** / removal
- Line: Old fridge in the garage? Washer that finally quit? Heavy and awkward is the part we handle.
- We take†: **We take** fridges and freezers, washers and dryers, stoves, dishwashers and water heaters.
- Link: Book an appliance pickup
- Photo alt: A pale green retro fridge freezer against a brick wall

**Mattresses (anchor #mattresses)**
- Headline: **Mattress** / removal
- Line: The one thing nobody wants to wrestle into a car. Book one pickup on its own, or add it to a bigger load.
- We take†: **We take** mattresses from twin to king, box springs, bed frames and futons.
- Link: Book a mattress pickup
- Photo alt: A man walking down a sidewalk with a striped mattress on his head

### Yard waste and demo (two cards)
Region accessible name: Yard waste removal and demo projects

**Yard waste (anchor #yard-waste)**
- Headline: **Yard waste** / removal
- Line: Spring cleanup, a storm that brought half a tree down or a whole fall's worth of leaves. Bag the small stuff if you can and we'll take care of the rest.†
- We take†: **We take** brush and branches, bagged leaves, old fencing, planters and pots, swing sets.
- Link: Book a yard waste pickup
- Photo alt: The back of an orange work truck loaded with green garden waste

**Demo (anchor #demo)**
- Headline: **Demo** / projects
- Line: We take it apart and haul the debris away, so there's no dumpster sitting in your driveway for a week. Every job is different, so we price it with you.†
- We take down†: **We take down** sheds, decks and porches, fences, playsets, kitchen and bathroom tear-outs.
- Link: Book a demo project
- Photo alt: A weathered wooden garden shed with glazed double doors

### Priced by the load (slate row, anchor #pricing)
- Headline: Priced by / **the load**
- Line: You pay for how much of the truck your junk fills. The price covers the loading, the hauling and the drop-off, and we confirm it before we show up.†
- Fact chips† (accessible name: Good to know): One item: priced as a 1/8 load; Demo: priced per job; Concrete, dirt and shingles can cost more
- Row of four loads (label, figure, note, link)†:
  - 1/8 truck. $149. A couple of big items, like a couch and a chair. Book this load
  - 1/4 truck. $249. A room's worth, or a pile of boxes and bags. Book this load
  - 1/2 truck. $399. A small garage or basement clean out. Book this load
  - Full truck. $649. A packed garage, a full basement or a whole move-out. Book this load
- Screen readers hear each link with its load: Book this load: 1/8 truck

### What we can't take
- Headline: What we / **can't take**
- Line: A few things can't go on the truck. Not sure about something? Send a photo with your booking, or give us a call. (The last four words are the phone link.)
- Marked list† (accessible name: What we can't take): Paint, oil and chemicals; Propane tanks and gas cylinders; Asbestos; Medical waste; Car batteries; Anything still connected to gas
- Drawn paint can, propane tank and battery on the card's edge: decorative, no alt.

---

## Book
- Meta title: Book a Junk Pickup | Quick Haul
- Meta description: Pick a day, tell us what's going and add photos. We confirm your time and price before we come. Junk removal and demo across Massachusetts and New Hampshire.
- No estimate band on this page.

### Banner
- Headline: Book a / **pickup**
- Line: It takes a couple of minutes.†
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Three small facts (under the banner)
The same three as Home's estimate band.
- You book. Pick a day and your load.
- We confirm. Shawn checks the job, the time and the price.†
- We haul. We load it and leave the space clear.†

### Booking form
Written as a request Shawn confirms (choices.md, stage 6). Progress line: Day; Load; Address; Your details. Each step has a hidden heading with the same words.

**Step: Day**
- Label: Pick a day
- Calendar accessible name: Available days. Month arrows: Previous month; Next month
- Label: Pick a time
- Time chips†: 8am to 11am; 11am to 2pm; 2pm to 5pm
- Helper: Arrival windows. We'll confirm yours before we come.†
- Empty state: No open slots that week. Try the next week, or call us and we'll find a time.
- Error: Pick a day and a time to keep going
- Button: Next: your load

**Step: Load** (the filling truck and the load control from Home)
- Label: How much junk
- Picker: 1/8; 1/4; 1/2; Full; Not sure. The same short labels as Home, since Book uses the same control. Screen readers still hear "1/8 truck" and so on. This step's own label, How much junk, does the job of Home's "How full?".
- Price line, changing with the picker†: From $149 for a 1/8 truck; From $249 for a 1/4 truck; From $399 for a 1/2 truck; From $649 for a full truck
- Note, changing with the picker†: the same four notes as Home's Priced by the load
- Before a size is picked (if nothing is preselected): Pick a size to see the price.
- For "Not sure": No problem. We'll price it from your photos or a quick call.
- When the job chip is Demo†: Demo is priced per job. We'll price it with you from your photos or a quick call.
- Label: What kind of job (optional)
- Chips: Junk removal; Clean out; Furniture; Appliances; Mattresses; Yard waste; Demo
- Button: Next: your address

**Step: Address**
- Label: Street address
- Label: Town (filled in when the visitor came from a town page)
  - Note, before typing: Start typing to check we come to you
  - Note, town on the list: Yes, we come to Lowell, MA. (the town fills in)
  - Note, town not on the list: Not on our list yet. Call (603) 555-0142† and ask
- Label: ZIP code (optional)
- Label: Where's the junk (optional)
- Chips: Curb or driveway; Garage; Basement; Inside the house; Yard
- Label: What's going
  - Field hint: For example: old couch, two mattresses, a pile of boxes in the basement
- Label: Add photos (optional). Shows only once a form endpoint exists.
  - Helper: Photos help us confirm your price and bring the right gear.
  - Upload button: Choose photos
  - Beside each chosen file: Remove
  - Upload error: That file didn't upload. Try a JPG or PNG photo.
- Label: Anything we should know (optional)
  - Field hint: Gate code, parking, stairs, items you'd like donated
- Errors: Add the street address for the pickup; Type your town so we can check we cover it; Tell us a little about the job
- Button: Next: your details

**Step: Your details**
- Label: Your name
- Label: Phone
- Label: Email
- Checkbox (SMS consent, for review before launch†): Text me booking updates and a reminder the day before. Message and data rates may apply. Reply STOP to opt out.
- Small print: We only use your details for this booking. Read our privacy policy.
- Errors: Add your name; Add a phone number we can reach you at; Add your email; That email doesn't look right
- Button: Send booking request

### Call line (beside every step, under every step on phones)
Shawn's agreed line, word for word.
- Line: Need help booking or have questions? Give us a call
- Number: (603) 555-0142†
- Hours: Mon to Sat, 7am to 7pm†

### Confirmation state
- Headline: Request / **sent**
- Body: Thanks, your booking request is in. Shawn will look it over and get back to you to confirm your time and price. A copy is on its way to your email.†
- Summary labels: Day; Time; Load; Price from; Address
- Price from, when there is no set price: We'll confirm it with you
- Line: Need to change something? Call (603) 555-0142†
- Button: Back to home

### Error state (booking system down)
- Headline: Something / **went wrong**
- Body: Your booking didn't go through, and that's on our end. Your details are still here, so try again, or give us a call at (603) 555-0142† and we'll book it with you on the phone.
- Button: Try again

---

## Reviews
- Meta title: Customer Reviews | Quick Haul Junk Removal
- Meta description: Read what customers say about Quick Haul on Facebook, and see before and after photos of garage, basement and yard clean outs.

### Banner
- Headline: Customer / **reviews**
- Line: Real reviews from our Facebook page land here, just as their writers left them. Until then, the cards below are samples.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Review grid (quotes mixed with photos)
Six sample cards: Home's five plus one. Obviously samples, replaced and never edited into real-sounding reviews. No stars, score, count, real names or customer's voice. Each one is logged in content/placeholders.md as must-replace. Stock photos in the grid carry an alt and no caption, and never sit inside a quote card, so no photo reads as the job a review is about (revision.md, conflict 19). The cards keep v2's order of jobs, so the photo order already staged still keeps each photo away from its own job.
- Who line on every card: Sample review. Avatar on every card: SR (decorative). No source line, as on Home.
- Sample cards, in this order:
  1. "Sample review. A garage clean out goes here, told by the person whose garage it was."
  2. "Sample review. A quick word about a mattress pickup."
  3. "Sample review. A real customer's words about a furniture pickup belong here."
  4. "Sample review. A longer one fits here, about a yard cleanup, the kind people write after a big job."
  5. "Sample review. Saved for a shed or deck demo, with the writer's name and date."
  6. "Sample review. An old fridge or a dead washer goes here, in the words of whoever had to live with it."

### End of the grid
- Line: Used us already? Tell the next person what it was like. A line or two about the job is all it takes.
- Text link: Leave a review on Facebook
- Text link: Read the real ones on Facebook

### Before and after
- Headline: Before / **and after**
- Line: Drag each line across to see the difference. Garages, basements, yards and demo jobs, cleared and ready to use.
- Line under the pairs: Got a spot like one of the befores? Add a photo when you book and we'll price it from there.†
- Slider tags: Before; After
- Pairs (caption, then alts). Each pair is stock from two different places, so no alt says "the same":
  - Garage clean out. Before: a garage crowded with a ride-on mower, a workbench, shelving and stacked gear. After: a garage with a clear concrete floor and tools hung tidily on the wall.
  - Basement clean out. Before: a low storage room with loaded shelves, a blue barrel, a covered board and a snowblower. After: an empty unfinished basement with exposed joists, steel poles and stairs. (Developer, 5 Nov: the before swapped, because the old one showed shoe brands on every box. The alt follows the photo, as this file's rule says.)
  - Yard cleanup. Before: a heap of cut branches and brush on grass. After: a lawn scattered with a few leaves, in front of a wooden fence and a small deck. (Developer, 5 Nov: another photo, so the two are at one distance.)
  - Shed demo. Before: a weathered wooden garden shed with glazed double doors. After: a fenced back yard with clear lawn, a concrete patio and a large tree. (Developer, 5 Nov: the two afters swapped photos.)
- Slider accessible names: Compare the garage clean out; Compare the basement clean out; Compare the yard cleanup; Compare the shed demo
- Button: Book now (Developer, 5 Nov: not printed. Above the pairs it asked before it showed, and under them it sat right over the estimate band's own. Critic, Reviews r1; revision.md section 5.)

---

## Donate
Whether Quick Haul donates at all, and where, is unconfirmed. This whole page is placeholder wording†.
- Meta title: Donate Your Old Furniture and Household Items | Quick Haul
- Meta description: Some of what we haul still has plenty of life in it. Tell us what's still good when you book and we set it aside for donation instead of the dump.

### Banner
- Headline: Still good? / **Someone wants it**
- Line: A lot of what we pick up still works, so the good stuff goes to local charities and reuse stores instead of the dump.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### What we can donate
- Headline: What we / **can donate**
- Line: The dresser that doesn't fit the new place, the kids' bikes, the spare couch from the basement. If you'd use it, someone else probably will too.
- Plain line: **Yes to** furniture in good shape, working appliances, kitchenware, clothes and shoes, books, toys, bikes, tools and sports gear.
- Marked list (label: Not these. Accessible name: What we can't donate): Anything broken, stained or missing parts; Worn-out mattresses; Car seats; Recalled cribs; Anything that's been in a flood or fire
- Three small facts:
  - Where it goes. Local charities and reuse stores in Massachusetts and New Hampshire. We check what they're taking before each drop-off.
  - How to ask. Add a note when you book saying what's still good, or tell us when we get there. We'll load it separately.
  - If it can't be donated. It goes with the rest of your load, so you're not stuck with it.
- Photo alt: A small wooden dresser set out on an empty street, in front of a wooden fence (Developer, 5 Nov: cropped in, so the French rooftops are gone. The alt follows the photo, as this file's rule says.)

### Estimate band, Donate's own words
- Headline: Ready to / **clear it out?**
- Line: Book a pickup and tell us what's still good. Want to check an item first? Give us a call. (The last four words are the phone link.)
- Button: Book a pickup

---

## About
- Meta title: About Quick Haul | Local Junk Removal in MA and NH
- Meta description: Quick Haul is Shawn and a small local crew†, clearing garages, basements and yards across Massachusetts and New Hampshire. Give him a call.

### Banner
- Headline: About / **Quick Haul**
- Line: Shawn and a small local crew†, clearing garages, basements and yards across Massachusetts and New Hampshire, and taking down the old sheds and decks too.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Pick up the phone (slate promo)
- Headline: Pick up / **the phone**
- Story: Shawn still answers the phone himself, and that's on purpose.† A quick call tells him what's in the garage, how close the truck can get and what to bring. It tells you who's showing up and what it costs. You can book online any time, but if you'd rather talk it through first, call. That's what the number is for.
- Button: Call Shawn (603) 555-0142† (accessible name: Call Shawn at (603) 555-0142)
- One action only in this band. Book now is in the estimate band below it.
- Photo: stock is allowed, a person included, but never captioned or described as Shawn (choices.md, stage 6). The alt describes the photo shown. As built: A gray house with a barn-shaped roof behind a bright red shrub and a big bare tree, with a paved drive in front (Developer, 5 Nov: the old pickup showed Chevrolet badges on an Arizona lot, and a stock truck beside "how close the truck can get" read as Shawn's, critic, About r1. No vehicle or person until his own photo; logged must-replace in content/placeholders.md)
- Alt once Shawn's photo arrives: Shawn, owner of Quick Haul, beside the truck

### How we work (three small facts)
- Headline: How we / **work**
- Line: We're coming onto your property and into your garage or basement, so here's what you can expect.
- Easy to reach. A real number with a real person on the end of it, Mon to Sat, 7am to 7pm.†
- No sales pitch. Tell us what's going and we'll tell you straight what it costs. Say no and that's fine.†
- Less in the dump. Anything still good goes to donation where we can, not straight on the pile.†

---

## FAQ
- Meta title: Junk Removal FAQ: Prices, Booking and What We Take | Quick Haul
- Meta description: How much junk removal costs, what we take and don't take, how booking works and where we go. Straight answers from Quick Haul.

### Short banner
- Headline: Questions / **answered**
- Line: Prices, booking and what we take. Can't find yours? Give us a call.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### The list (one list, four small group labels, 12 questions)
(Developer, 5 Nov: the four labels print as section headings, in three bands, because as small labels they failed the Critic and Varun's rulings on the headline system. Wording unchanged, in this order.)

**Pricing**
- How much does junk removal cost? / You pay for how much of the truck your junk fills, from $149† for a 1/8 truck or one item to $649† for a full truck. Demo is priced per job.†
- What if I'm not sure how much I have? / Pick "Not sure" when you book and add a few photos. We'll price it from those and confirm before we come.†
- Can the price change when you get here? / Only if the job is different from what we agreed, like extra items or heavy material we didn't know about. If it does, we tell you before we load anything.†

**What we take**
- What do you take? / Furniture, appliances, mattresses, household junk, garage and basement clutter, yard waste and demo debris. The full list is on our services page.†
- What don't you take? / Paint, oil and chemicals, propane tanks, asbestos, medical waste and car batteries.† Not sure about something? Ask us.
- Do you donate things? / Yes, where we can. Tell us what's still good when you book and we'll take it to a local charity or reuse store instead of the dump.†
- Do I need to carry anything outside? / No. We carry it out from wherever it is, including basements and upstairs rooms.†

**Booking**
- How does booking work? / Pick a day and your load online, add photos if you can, and send it. Shawn looks it over and gets back to you to confirm the time and the price.†
- Can I just call instead? / Yes. Call (603) 555-0142†, Mon to Sat, 7am to 7pm†, and we'll book it with you on the phone.
- How soon can you come? / Check the calendar for the next open days. If you need it sooner, call us and we'll see what we can do.
- Do you come to my town? / Probably. See the full list on our service area page, and if yours isn't there, give us a call.†

**Paying**
- When and how do I pay? / When the job's done, before we drive off. Card or cash.†

Links inside the answers: "services page" to Services, "calendar" to Book, "service area page" to the hub, the number to the phone.

---

## Contact
- Meta title: Contact Quick Haul | Junk Removal Quotes in MA and NH
- Meta description: Call, email or send us a quick request for a junk removal or demo price. Quick Haul works towns across Massachusetts and New Hampshire, Mon to Sat.

### Short banner
- Headline: Call, book / **or ask**
- Line: The fastest way to a price is a call. Rather write it down? Send us a request.
- Button: Give us a call (603) 555-0142† (accessible name: Give us a call at (603) 555-0142)
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Map and hours
- Map accessible title: Map of the towns Quick Haul covers in Massachusetts and New Hampshire
- Map center: Salem, NH† (base town placeholder, not marked on the map as a base)
- Hours. Mon to Sat, 7am to 7pm†. Closed Sundays.†
- Where we go. Towns across Massachusetts and New Hampshire. Link: See the full list

### Ask for a price (short form)
(Developer, 5 Nov: built before Map and hours, straight under the banner, because "ask" is in the headline and it started two screens down. "Send us a request" in the banner line links here. In the form, How should we get back to you comes before Add photos. Wording unchanged.)
- Headline: Ask for / **a price**
- Line: Phone or email is enough, and we'll get back to you.
- Label: Your name
- Label: Phone
- Label: Email
- Label: Your town (optional)
- Label: What do you need gone
  - Field hint: For example: clearing out a two-car garage, or one old fridge in the basement
- Label: Add photos (optional). Shows only once a form endpoint exists.
  - Helper: Photos help us give you a real price instead of a guess.
  - Upload button, Remove and upload error: as on Book
- Label: How should we get back to you
  - Chips: Call; Text; Email
- Small print: We only use your details to answer your request. Read our privacy policy.
- Button: Send my request
- Errors: Add your name; Add a phone number or email so we can reach you; That email doesn't look right; Tell us a little about the job
- Success, heading: Got / **it**
- Success, line: We'll get back to you with a price soon. Need it faster? Call (603) 555-0142†
- Failed, heading: Something / **went wrong**
- Failed, line: Your request didn't go through, and that's on our end. What you typed is still in the form, so try again, or give us a call at (603) 555-0142†

### Commercial line (one line and a link under the form)
- Line: Landlord, realtor or property manager?† Turnovers, move-outs and regular pickups have their own form.
- Link: Ask about commercial work

---

## Service area (hub)
- Meta title: Junk Removal Service Area: MA and NH Towns | Quick Haul
- Meta description: See every Massachusetts and New Hampshire town Quick Haul covers. Same prices in all of them. Can't see yours? Give us a call.

### Banner
- Headline: Where / **we go**
- Line: Towns on both sides of the Massachusetts and New Hampshire line, all at the same prices.†
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Find your town (map beside the chips)
- Headline: Find / **your town**
- Line: Each town has its own page, with what we haul there and what it costs.
- Label: Massachusetts. Chips†: Andover; Dracut; Haverhill; Lawrence; Lowell; Methuen
- Label: New Hampshire. Chips†: Derry; Hudson; Londonderry; Nashua; Pelham; Salem
- Line under the chips: Can't see your town? Give us a call. If we can get to you, we'll tell you the price on the phone.
- Map accessible title: Map of the towns Quick Haul covers in Massachusetts and New Hampshire

---

## Town pages (one template)
Written here for Lowell, MA. Every other town page uses the same copy with its own town and state. Nothing else changes, and no local claims are added per town until Shawn gives them.
- Meta title: Junk Removal in Lowell, MA | Quick Haul
- Meta description: Junk removal, clean outs, furniture, appliance, mattress and yard waste pickup, plus demo, in Lowell, MA. Loads start at $149†. Book a day online or call.

### Banner
- Headline: Junk removal in / **Lowell, MA**
- Line: Clean outs, single items, yard waste and demo work in Lowell.
- Button: Book in Lowell
- Photo alt: A sunny street of old wooden houses with a brick sidewalk. The photo is not of the town, so the alt never names it.

### What we haul
- Headline: What we haul / **in Lowell**
- Line: We come to Lowell with the truck, load it ourselves and haul it away.†
- Photo tiles (names only, Home's photos and alts): Junk removal; Clean outs; Furniture; Appliances; Mattresses; Yard waste; Demo
- Text link: See everything we take

### Priced by the load (the row of four)
- Headline: Priced by / **the load**
- Line: You pay for how much of the truck your junk fills.
- Row of four loads: the same as Services.
- Text link: See other towns

### Reviews from this town
Built only when real Facebook reviews from this town exist. No sample cards on town pages.

---

## Commercial
Shawn has not said he does commercial or repeat work (brief section 2). The whole page is placeholder wording†, must-confirm, and invites a request without claiming a track record. No estimate band on this page.
- Meta title: Commercial and Repeat Junk Removal | Quick Haul
- Meta description: Landlords, realtors and property managers: tell us about turnovers, move-outs or regular pickups across Massachusetts and New Hampshire.

### Short banner
- Headline: Commercial and / **repeat work**
- Line: Turnovers, move-outs and regular pickups for landlords, realtors and property managers. Tell us about the property and we'll get back to you.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Request form
- Label: Your name
- Label: Company (optional)
- Label: You are (optional)
  - Chips: Landlord; Realtor; Property manager; Contractor; Other
- Label: Phone
- Label: Email
- Helper under Phone and Email: Phone or email is enough.
- Label: Property address or town (optional)
- Label: One job or regular
  - Chips: One job; Regular pickups
- Label: How often (shows for regular pickups)
  - Chips: Weekly; Every two weeks; Monthly; As needed
- Label: Tell us about the job
  - Field hint: For example: unit turnover, tenant left furniture and a full basement
- Label: Add photos (optional). Shows only once a form endpoint exists. Helper, upload button, Remove and upload error: as on Contact
- Small print: We only use your details to answer your request. Read our privacy policy.
- Button: Send request
- Errors: Add your name; Add a phone number or email so we can reach you; That email doesn't look right; Tell us a little about the job
- Success, heading: Thanks, / **we've got it**
- Success, line: We'll get back to you to talk it through. Need it sooner? Call (603) 555-0142†
- Failed, heading: Something / **went wrong**
- Failed, line: Your request didn't go through, and that's on our end. What you typed is still in the form, so try again, or give us a call at (603) 555-0142†

---

## 404
- Meta title: Page Not Found | Quick Haul
- Meta description: (none; noindex)
- Headline: Nothing / **to haul here**
- Line: This page is empty, like the truck after a drop-off. It may have moved.
- Button: Book now
- Links: Home; Services; Contact
- No estimate band on this page.

---

## Privacy policy
Plain-language draft. The length stays. It must be checked against the services actually used (booking plugin, SMS provider, analytics, form spam protection) and reviewed by someone qualified before launch. The site has no analytics or upload yet, so this describes things not connected. Business name and contact details are placeholders.
- Meta title: Privacy Policy | Quick Haul
- Meta description: How Quick Haul collects and uses your details when you book, ask for a price or visit the site.
- No estimate band on this page.
- Headline: Privacy / **policy**
- Sections:
  - What we collect. When you book or ask for a price, we collect your name, phone number, email, the pickup address, details about the job and any photos you upload. When you visit the site, we collect basic analytics like which pages are viewed.
  - Why we collect it. To confirm and carry out your booking, to give you a price, to send booking confirmations and reminders, and to understand how people use the site so we can improve it.
  - Text messages. If you check the text message box on the booking form, we text you booking updates and a reminder. Message and data rates may apply. Reply STOP to opt out at any time.
  - Who we share it with. Only the services that run the site, the booking calendar, email, text messages and analytics. We don't sell your details.
  - How long we keep it. As long as we need it for your booking and our records, then we delete it.
  - Your choices. Ask us to see, correct or delete your details at any time.
  - Contact. Quick Haul, quickhaul@example.com†, (603) 555-0142†.
  - Last updated. The launch date. Left off until that date exists.

---

## Held lines (HOLD: written, not built)
Nothing here goes on the site until the fact behind it is confirmed. Shawn has confirmed none of the three trust claims, though our scope lists them.
- Licensed†. Licensed to haul in Massachusetts and New Hampshire. Ask us for the details.
- Insured†. Insured for the work we do on your property. We'll send proof if you ask.
- Guarantee†. Shawn's guarantee goes here in his own words, once he confirms what it covers.
- The trust row they sat in is cut from Home (revision.md section 4). If Shawn confirms any, they have no slot yet; three small facts on About is the natural place.
- Home's Reviews line, once real reviews are in and each links to its post: Every review here links back to Facebook, so you can see who wrote it and when.
- Reviews banner line, once real reviews are in: Real reviews from our Facebook page, just as their writers left them.
- The Facebook link on Home and at the end of the Reviews grid, once real reviews are in: Read more on Facebook
- Reviews page, on each card, once each review has a post URL: Read on Facebook
- Before and after line, Home and Reviews, once Shawn's own photos replace the stock pairs: Every pair here is one of our own jobs, photographed the day we did it.
- Footer fact line, once Shawn confirms the year: Hauling since 2022†

---

## Questions for the client
Varun's call at stage 6: not forwarded for now, they stay placeholder values. Kept here so they can go to Shawn in one pass. Most important first.
1. Phone, hours, base town and the full town list. Is Sunday a working day? Do prices change for towns further out?
2. Prices. Will they go on the site? What are the real bands, is there a minimum or single-item price, what does each band hold in your truck, and what costs extra (heavy material, appliances with refrigerant, stairs)?
3. Booking. Are you happy with a request you confirm? What time windows do you offer? Can customers be out during the job? What is your change and cancel rule? When and how do customers pay?
4. Licensed, insured, guaranteed. Which are true, and in which states? The lines for these are written but held.
5. Your story. Who is on the crew, do you answer the phone yourself, and are you happy for your first name to be used across the site? We need a photo of you, or of you with the truck.
6. What you take and don't take. Please check both lists. Do you take electronics and TVs? Do you disconnect appliances, or only take ones already unhooked?
7. Demo. What size of job do you take on (sheds, decks, kitchens, anything structural)? How do you price it?
8. Donations. Do you take usable items to charity? Which ones, and what won't they accept?
9. Commercial and repeat work. Do you do it, and for whom? The commercial page is placeholder until you say yes.
10. Your Facebook, Instagram and TikTok links, and which Facebook reviews you want on the site: at least six, five of them for the homepage. No real reviews or ratings go up until then.
11. Photos. Your own job photos, especially before and after pairs from the same spot, to replace the stock images.

## Left out on purpose
- No real review quotes, star ratings or review counts. The proposal (term 05, as quoted in brief.md) rules out any rating that hasn't been earned, and none have been supplied. The sample cards name a kind of job and never speak as a customer.
- No "plenty" on the page any more. It is still Shawn's word for his Facebook reviews (chat, 31 Aug), but it contradicted sample cards, and nobody here has seen his page.
- No license, insurance or guarantee claims in any built copy. Written and held only.
- No story on About beyond the phone. When Shawn started, who is on the crew and why he does this aren't in his material, so About's extra words are a line about coming onto someone's property and one short line under No sales pitch.
- Nothing on Donate about which charities, how much of a load gets donated or whether donating changes the price. None of it is in his material.
- No year in business anywhere that gets built. 2022 now sits only in the held footer line.
- No named charities or partners. Naming a real organization would be a claim about a real business.
- No response-time promises ("within an hour", "same day"), no "no hidden fees" or "no surprises" claim and no eco or recycling percentages. Nothing in the material supports them.
- No reason given for the can't-take list. V1's "the dump won't take them from us" was a claim nobody had made.
- No blog or scrap talk, as Shawn asked.
