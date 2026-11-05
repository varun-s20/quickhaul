# Quick Haul: site copy, v4 for batch d (staged, not built)
Copywriter, 2026-11-05. The expansion pass from Varun's notes in design/choices.md, "Varun's additions to batch d". This file is staging: content/copy.md stays v3 until batch d promotes this file, so the running batch c is not disturbed. Older versions: content/copy.md (v3 for now), content/copy-v2.md and content/copy-v1.md. Written from those, the built site/*.html, design/revision.md, brief.md, prd/client-chat.txt and content/placeholders.md. What changed, page by page, with word counts, the Developer's list and the sources for the general facts: content/copy-v4-changes.md.

## How to read this file
- Organized by page, then by band, using the band names in design/revision.md section 4. They replace the section list in design-spec.md. A band marked (new) isn't in v3.
- Text level: revision.md section 2 still holds band by band. One short heading, one or two supporting lines, at most one short list, a few steps or three small facts. One picture, one action. The pages grow by adding bands of that kind, not by making bands longer, so one idea per section stands. Varun's target for this pass: every inner page up about 40 to 70 percent in useful content, Home a bit, About a lot more, and a new Pricing page.
- The recipe named after a new band (seated card, promo, cards) is a suggestion from revision.md section 5. The Developer may swap it, but never the same recipe twice in a row.
- Headlines are two rows, in reading order. The row in bold here is the heavy weight; the other is the light weight. Most headlines put the heavy row second; service names put it first, so the bold lands on the word a visitor scans for. Written in sentence case; the CSS sets them in capitals. No full stops, no italics, no color change.
- Body copy is final wording, in US English.
- Every value marked with a dagger (†) is a placeholder: a realistic stand-in for a fact Shawn has not confirmed. Each one is in content/placeholders.md with what is needed to replace it. The dagger is for this file only; do not print it on the site.
- A line with no dagger is either from Shawn's own material or general information about how junk removal works. State and federal rules quoted as general information are sourced in copy-v4-changes.md.
- Lines marked HOLD are written but must not be built until the fact behind them is confirmed. They are collected under "Held lines" near the end.
- Phone everywhere: (603) 555-0142†, tel:+16035550142. Hours everywhere: Mon to Sat, 7am to 7pm†. Email: quickhaul@example.com†.
- Prices everywhere: 1/8 truck $149†, 1/4 truck $249†, 1/2 truck $399†, full truck $649†. New in v4: a fridge, freezer or AC unit adds $30†. Load sizes everywhere: about one, two, four and eight pickup beds†.
- Image slots hold stock for now (choices.md, 2b decision 3 and stage 6). Every alt describes the photo actually shown and never claims it is a Quick Haul job or a real place on the list (checkpoint 2c). If a different photo is placed, the alt changes with it. Rewrite every alt when Shawn's own photos arrive. Every photo named for a new band is already logged stock. No new downloads are needed for this copy.

---

## Global (every page)

### Preview label (off for now, required before any deploy-preview)
Varun took this line off the page. The brief still requires it, or a gate, before Shawn sees a preview.
- Text: Design preview. Phone, hours, towns, prices, reviews and photos are sample content until Quick Haul confirms them.

### Skip link
- Skip to content

### Header
- Nav, in this order: Services (services.html); About (about.html); Pricing (pricing.html); Reviews (reviews.html); Donate (donate.html)
- Logo alt: Quick Haul home
- Call link: Questions? Give us a call (603) 555-0142†
- Button: Book now
- Phone: Menu (button label)
- FAQ, Contact, Service area, Commercial and Privacy are not in the header. They live in the footer and in in-page links.

### Menu
- Accessible name: Menu
- Close button accessible name: Close menu
- Main links, the same five as the header: Services; About; Pricing; Reviews; Donate
- Second, smaller group (accessible name: More pages): Service area; FAQ; Contact
- Buttons: Book now; (603) 555-0142†
- Commercial and Privacy stay in the footer only.

### Call bar (phones, call-only)
- Button: Give us a call (603) 555-0142†
- Region accessible name: Call Quick Haul

### Estimate band
On every page except Book, Commercial, 404 and Privacy (Varun, 5 Nov: the lighter option, design/revision.md conflict 21). Donate, Pricing and About have their own words (see those pages).
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
- Column: Services. Junk removal; Clean outs; Yard waste; Demo projects; Commercial (commercial.html)
- Column: Booking. Book now; Pricing (pricing.html, was services.html#pricing); Service area (service-area.html); FAQ (faq.html)
- Column: Quick Haul. About; Reviews; Donate; Contact (contact.html); Privacy (privacy.html)
- Social pills: Facebook; Instagram; TikTok (each adds "opens in a new tab" for screen readers; profile links wait for Shawn†)
- Fact line: Junk removal and demo across Massachusetts and New Hampshire
- Created with love by Digital Heroes (links to https://digitalheroesco.com/)

### Truck labels (accessible names, one load per page as revision.md section 5 suggests)
- Home hero: The Quick Haul truck, piled high with a sofa, boxes, a mattress, a dresser, a bike and yard waste
- Load picker, Home and Book, changes with the chip: The Quick Haul truck carrying an eighth of a load; a quarter of a load; half a load; a full load, piled high
- Price row, Services, Pricing and town pages: The Quick Haul truck with an eighth of a load; with a quarter of a load; with half a load; with a full load, piled high
- Drawn items on seated cards: decorative, no label

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
- Plain line under the tiles (new): **We can't take** paint, oil and chemicals, propane tanks or asbestos.†
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
- Text link (new): See how pricing works (pricing.html)
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

### Who's showing up (new, a slim band)
Home says nothing about who comes to the house, and About is now in the header, so this is one heading, one line and one link. If the page feels long, this is the band to drop.
- Headline: Who's / **showing up**
- Line: Shawn and a small local crew.† He still answers the phone himself, so the person you talk to knows your job before the truck rolls.†
- Text link: More about Quick Haul (about.html)

### Do you come to my town
No price on any town name. The price lives in the band above, and this line says once that it doesn't change by town.
- Headline: Do you come / **to my town?**
- Line: Probably. We cover towns on both sides of the Massachusetts and New Hampshire line, and the prices are the same in every one.† Pick yours to see what we haul there.
- Town chips†, each linking to its town page: Andover; Dracut; Haverhill; Lawrence; Lowell; Methuen; Derry; Hudson; Londonderry; Nashua; Pelham; Salem
- Line under the chips: Can't see your town? It may just not be on the list yet.† Give us a call (the last four words are the phone link)
- Text link (new, Towns has left the header): See the full service area (service-area.html)
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

---

## Services
- Meta title: Junk Removal Services in MA and NH | Quick Haul
- Meta description: Garage and basement clean outs, furniture, appliance, mattress and yard waste removal, plus demo projects. See what we take, what it costs and how to get ready.

### Banner
- Headline: Our / **services**
- Line: Clean outs, single items, yard waste and demo work across Massachusetts and New Hampshire. What each one covers, and how to book it.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Jump chips
- Region accessible name: On this page
- Chips: Junk removal; Clean outs; Furniture; Appliances; Mattresses; Yard waste; Demo; Pricing; Can't take; Getting ready

### Not sure what to book (new, seated card with three small facts)
- Headline: Not sure / **what to book?**
- Line: Most jobs look like one of these three.
- A few things. A couch, an old fridge, a mattress. Book a pickup for just those.
- A whole room. A garage, a basement or a storage space. Book a clean out and point at what goes.
- Something built. A shed, a deck, a fence or a tear-out. That's a demo project, priced per job.†

### Junk removal (lead band, anchor #junk-removal)
- Headline: **Junk** / removal
- Line: Got a pile and no easy way to get rid of it? Tell us how much of the truck it fills and pick a day. We do the lifting.†
- We take†: **We take** boxes and bags, old furniture and rugs, exercise equipment, bikes and toys, move-out leftovers, scrap wood and metal.
- Good to know†: **Good to know** You don't have to sort it first. Just bag loose small stuff if you can.
- Button: Book now (screen readers hear: Book now for junk removal)
- Photo alt: A white pickup truck piled high with black trash bags

### Garage and basement clean outs (promo, anchor #clean-outs)
- Headline: Garage and basement / **clean outs**
- Line: Garages and basements fill up slowly, then all at once. Point at what goes and what stays, and we leave you with a floor you can actually use.
- We take†: **We take** boxes and bins, shelving, old furniture, tools nobody uses, carpet and rugs.
- Button: Book a clean out
- Photo alt: A garage crowded with a ride-on mower, a workbench, shelving and gas cans

### How a clean out goes (new, three small facts on cream)
- Headline: How a clean out / **goes**
- Line: Most start with a quick walk-through and end with a swept floor.†
- Walk it. Show us what goes and what stays. Still deciding on something? We can work around a keep pile.†
- Load it. We carry it out to the truck, so you don't have to drag anything out first.†
- Sweep up. We sweep the spot when we're done, so you get the floor back.†

### Furniture, appliances and mattresses (three cards)
Region accessible name: Furniture, appliance and mattress removal

**Furniture (anchor #furniture)**
- Headline: **Furniture** / removal
- Line: Too big for your car or too heavy to move on your own? We take it, and pieces in good shape can go to donation.†
- We take†: **We take** couches and sectionals, recliners, dressers, desks and dining sets.
- Good to know†: **Good to know** If it came in through the door, it can usually go out that way. If not, we can take it apart.
- Link: Book a furniture pickup
- Photo alt: A cream armchair and a small sofa set out by the door of a brick building

**Appliances (anchor #appliances)**
- Headline: **Appliance** / removal
- Line: Old fridge in the garage? Washer that finally quit? Heavy and awkward is the part we handle.
- We take†: **We take** fridges and freezers, washers and dryers, stoves, dishwashers and water heaters.
- Good to know†: **Good to know** Empty the fridge before we come, and tell us if anything's still plumbed or wired in.
- Link: Book an appliance pickup
- Photo alt: A pale green retro fridge freezer against a brick wall

**Mattresses (anchor #mattresses)**
- Headline: **Mattress** / removal
- Line: The one thing nobody wants to wrestle into a car. Book one pickup on its own, or add it to a bigger load.
- We take†: **We take** mattresses from twin to king, box springs, bed frames and futons.
- Good to know (general): **Good to know** Massachusetts bans mattresses from the regular trash, so you can't just leave one out at the curb.
- Link: Book a mattress pickup
- Photo alt: A man walking down a sidewalk with a striped mattress on his head

### Yard waste and demo (two cards)
Region accessible name: Yard waste removal and demo projects

**Yard waste (anchor #yard-waste)**
- Headline: **Yard waste** / removal
- Line: Spring cleanup, a storm that brought half a tree down or a whole fall's worth of leaves. Bag the small stuff if you can and we'll take care of the rest.†
- We take†: **We take** brush and branches, bagged leaves, old fencing, planters and pots, swing sets.
- Good to know (general): **Good to know** Massachusetts and New Hampshire both keep yard waste out of their landfills, so it can't go with the trash.
- Link: Book a yard waste pickup
- Photo alt: The back of an orange work truck loaded with green garden waste

**Demo (anchor #demo)**
- Headline: **Demo** / projects
- Line: We take it apart and haul the debris away, so there's no dumpster sitting in your driveway for a week. Every job is different, so we price it with you.†
- We take down†: **We take down** sheds, decks and porches, fences, playsets, kitchen and bathroom tear-outs.
- Good to know (general): **Good to know** Demo can need a town permit, and older buildings can hide asbestos. Your building department can tell you what applies.
- Link: Book a demo project
- Photo alt: A weathered wooden garden shed with glazed double doors

### Priced by the load (slate row, anchor #pricing)
The short form. The full story moved to the Pricing page, so the fact chips came off this band.
- Headline: Priced by / **the load**
- Line: You pay for how much of the truck your junk fills. The price covers the loading, the hauling and the drop-off, and we confirm it before we show up.†
- Row of four loads (label, figure, note, link)†:
  - 1/8 truck. $149. A couple of big items, like a couch and a chair. Book this load
  - 1/4 truck. $249. A room's worth, or a pile of boxes and bags. Book this load
  - 1/2 truck. $399. A small garage or basement clean out. Book this load
  - Full truck. $649. A packed garage, a full basement or a whole move-out. Book this load
- Screen readers hear each link with its load: Book this load: 1/8 truck
- Text link (new): See how pricing works (pricing.html)

### What we can't take (seated card, anchor #cant-take)
- Headline: What we / **can't take**
- Line: A few things can't go on the truck. Not sure about something? Send a photo with your booking, or give us a call. (The last four words are the phone link.)
- Marked list† (accessible name: What we can't take): Paint, oil and chemicals; Propane tanks and gas cylinders; Asbestos; Medical waste; Car batteries; Anything still connected to gas
- Plain line under the list (new, general): **Where those go** Many towns run a household hazardous waste day for paint and chemicals. Places that sell car batteries or fill propane tanks usually take the old ones back.
- Drawn paint can, propane tank and battery on the card's edge: decorative, no alt.

### Getting ready (new, three small facts, anchor #getting-ready)
General advice, so no daggers.
- Headline: Getting / **ready**
- Line: A few minutes now makes the job go faster.
- Clear a path. Move the car and anything blocking the way, and tell us about gates, stairs or tight spots.
- Check inside. Take a last look through drawers, closets and boxes. It's hard to get something back once it's gone.
- Mark what stays. Put a note on anything that isn't going, or show us when we get there.

---

## Pricing (new page, pricing.html)
Built from Services' pricing band and expanded. Every price, load size and rule here is a placeholder†, logged in content/placeholders.md. General lines on how volume and weight work carry no dagger.
- Meta title: Junk Removal Pricing: What Each Load Costs | Quick Haul
- Meta description: What each truck load holds and costs, from $149† to $649†, what's in the price, what can cost more and how booking works. Junk removal in MA and NH.

### Banner
- Headline: What it / **costs**
- Line: You pay for how much of the truck your junk fills. What each load holds, what's in the price and what can change it.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk
- Truck: half a load, parked on the fold.

### Jump chips
- Region accessible name: On this page
- Chips: Load sizes; Which load; What changes it; What's included; What costs more; Examples; Booking

### Four loads (slate row, anchor #load-sizes)
- Headline: Four loads, / **four prices**
- Line: Every price covers the loading, the hauling and the drop-off. Find the one closest to your pile.†
- Row of four loads (label, figure, size, what it holds, link)†:
  - 1/8 truck. $149. About one pickup bed. A couch and a chair, a mattress set and a dresser, or one big item. Book this load
  - 1/4 truck. $249. About two pickup beds. A room's worth, a bedroom set, or a pile of boxes and bags. Book this load
  - 1/2 truck. $399. About four pickup beds. A small garage or basement clean out, or what's left after a move. Book this load
  - Full truck. $649. About eight pickup beds. A packed garage, a full basement or a whole move-out. Book this load
- Screen readers hear each link with its load: Book this load: 1/8 truck

### Which load is mine (seated card with three small facts, anchor #which-load)
- Headline: Which load / **is mine?**
- Line: You don't need to measure anything. A rough guess is fine, because we confirm it before we come.†
- Picture a pickup. Stand in front of your pile and count how many pickup beds it would fill.
- Count the big stuff. Couches, fridges and mattresses take up the most room.
- Still not sure? Pick "Not sure" when you book and add a few photos. We'll tell you which load fits.†
- Drawn sofa and boxes on the card's edge: decorative, no alt.

### What changes the price (lead band, anchor #what-changes)
- Headline: What changes / **the price**
- Line: Mostly it's how much room your junk takes up. Your town doesn't change it: the prices are the same everywhere we go.† ("everywhere we go" links to service-area.html)
- How much. More room on the truck means a bigger load. That's most of the price.
- How heavy. A truck can only carry so much, and heavy loads cost more to drop off.
- How hard to reach. Stairs, tight turns and long walks to the truck take more time.†
- Photo alt: A garage crowded with a ride-on mower, a workbench, shelving and gas cans

### What's in the price (slate promo, anchor #included)
- Headline: What's in / **the price**
- Line: On an everyday load, the price covers the whole job, start to finish.†
- Short list†:
  - Loading. We do the lifting and carrying, from wherever it is.
  - Hauling. The truck, the gas and the trip.
  - The drop-off. The dump fees on everyday junk.
  - Sweeping up. We sweep the spot when we're done.
- Photo alt: An empty basement with white walls, square pillars and a clear wood floor

### What can cost more (seated card, anchor #cost-more)
- Headline: What can / **cost more**
- Line: Most everyday loads don't run into any of this.† If yours does, you'll hear it before we load anything.†
- Short list, not marked with crosses, because these aren't refusals:
  - Heavy material. Concrete, dirt, brick and shingles weigh more and cost more to drop off.†
  - Fridges, freezers and AC units. Federal rules say the refrigerant has to come out before they're scrapped. That adds $30† each.
  - Hard carries. Several flights of stairs or a long walk to the truck. Tell us when you book.†
  - More than we agreed. Extra items on the day can move you up a load. You'll see the new price first.†
- Drawn fridge and boxes on the card's edge: decorative, no alt.

### Two jobs, added up (new worked examples, two cards, anchor #examples)
Sample jobs with placeholder prices. The photos are stock, carry an alt and no caption, and nothing says they are real jobs.
- Headline: Two jobs, / **added up**
- Line: Two everyday jobs with the numbers filled in. They're examples, not quotes.†
- Card one: A couch and a chair
  - 1/8 truck: $149†
  - Extras: None
  - Total: $149†
  - Note: Ground floor, nothing heavy. Everything's in the load price.†
  - Photo alt: A cream armchair and a small sofa set out by the door of a brick building
- Card two: A basement and an old fridge
  - 1/2 truck: $399†
  - One fridge: $30†
  - Total: $429†
  - Note: A small basement clean out, with one fridge that needs its refrigerant taken care of.†
  - Photo alt: A pale green retro fridge freezer against a brick wall

### Not quite a load (three small facts on cream)
- Headline: Not quite / **a load?**
- Line: Some jobs don't fit the four sizes, so they're priced a little differently.†
- Just one item. It's priced as a 1/8 load, so that's $149.† A fridge or freezer adds its $30.†
- Demo. Every job is different, so it's priced per job. Send photos or call and we'll price it with you.†
- Regular pickups. Landlord, realtor or property manager? Tell us what you need on our commercial page.† ("commercial page" links to commercial.html)

### From estimate to booked (promo or seated card, anchor #booking)
- Headline: From estimate / **to booked**
- Line: Picking a load gets you an estimate. The price is set once Shawn has looked it over and confirmed it with you.†
- You pick. Choose a load and a day online, and add photos if you can. Or call and do it by phone.
- Shawn confirms. He checks the job and gets back to you with the time and the price.†
- We haul, you pay. We load it and leave the space clear. You pay when the job's done.†

### Estimate band, Pricing's own words
Shawn's agreed line, word for word, with the phone link on the last four words.
- Headline: Know your load? / **Book it**
- Line: Pick a day online in a couple of minutes.† Need help booking or have questions? Give us a call
- Button: Book now

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
- Text link (new), opens in a new tab so the form isn't lost: See what each load holds (pricing.html#load-sizes; screen readers hear "opens in a new tab")
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
- Text link at the end of the grid: Read the real ones on Facebook (adds "opens in a new tab" for screen readers)

### Word for word (new, seated card with three small facts)
From proposal term 05, as quoted in brief.md. The line stays in the future tense while the samples are up; its launch wording is under Held lines.
- Headline: Word / **for word**
- Line: When our real reviews go up, they go up the way people wrote them.
- Nothing edited. No trimming and no tidying, typos and all.
- A name and a date. Each one shows who wrote it and when.
- A link back. Each one links to its Facebook post, so you can read it there too.

### Before and after
- Headline: Before / **and after**
- Line: Drag each line across to see the difference. Garages, basements, yards and demo jobs, cleared and ready to use.
- Line under the pairs: Got a spot like one of the befores? Add a photo when you book and we'll price it from there.†
- Slider tags: Before; After
- Pairs (caption, new line under the caption†, then alts). Each pair is stock from two different places, so no alt says "the same". The new lines talk about a job like this one and never say this was the load:
  - Garage clean out. A garage like this is usually a 1/2 to a full truck. Before: a garage crowded with a ride-on mower, a workbench, shelving and stacked gear. After: a garage with a clear concrete floor and tools hung tidily on the wall.
  - Basement clean out. Usually around a 1/2 truck, depending on what's on the shelves. Before: a low storage room with loaded shelves, a blue barrel, a covered board and a snowblower. After: an empty unfinished basement with exposed joists, steel poles and stairs. (Developer, 5 Nov: the before swapped, because the old one showed shoe brands on every box. The alt follows the photo, as this file's rule says.)
  - Yard cleanup. A pile like this is usually a 1/4 to a 1/2 truck. Before: a heap of cut branches and brush on grass. After: a lawn scattered with a few leaves, in front of a wooden fence and a small deck. (Developer, 5 Nov: another photo, so the two are at one distance.)
  - Shed demo. Demo is priced per job, so send a photo and we'll price it with you. Before: a weathered wooden garden shed with glazed double doors. After: a fenced back yard with clear lawn, a concrete patio and a large tree. (Developer, 5 Nov: the two afters swapped photos.)
- Slider accessible names: Compare the garage clean out; Compare the basement clean out; Compare the yard cleanup; Compare the shed demo
- Button: Book now (Developer, 5 Nov: not printed. Above the pairs it asked before it showed, and under them it sat right over the estimate band's own. Critic, Reviews r1; revision.md section 5.)

### Used us already (new band, grown from the end of the grid's line)
- Headline: Used us / **already?**
- Line: Tell the next person what it was like. A line or two is all it takes, and we'll send you the link after the job.†
- What it was. A garage, a couch, a pile of brush.
- How it went. Did it go the way you were told it would?
- Which town. So your neighbors know we come to them.
- Text link: Leave a review on Facebook (adds "opens in a new tab" for screen readers)

---

## Donate
Whether Quick Haul donates at all, and where, is unconfirmed. This whole page is placeholder wording†, except "Getting it ready" and the Massachusetts line, which are general.
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
- Plain line (new, general): **Good to know** Massachusetts bans clothes and other textiles from the regular trash.
- Photo alt: A small wooden dresser set out on an empty street, in front of a wooden fence (Developer, 5 Nov: cropped in, so the French rooftops are gone. The alt follows the photo, as this file's rule says.)

### How it works (new band, seated card with three small facts)
v3's three facts lived in the band above. How to ask is now the line, and the receipt is new.
- Headline: How it / **works**
- Line: Add a note when you book saying what's still good, or tell us when we get there. We'll load it separately.
- Where it goes. Local charities and reuse stores in Massachusetts and New Hampshire. We check what they're taking before each drop-off.
- If it can't be donated. It goes with the rest of your load, so you're not stuck with it.
- Need a receipt? Say so when you book and we'll ask the charity for one.

### Getting it ready (new, three small facts on cream)
General advice.
- Headline: Getting it / **ready**
- Line: Charities are more likely to say yes to things that are clean and complete.
- Empty it. Check drawers, pockets and boxes, and take out anything personal.
- Keep it together. Tape screws, shelves and cords to the piece they belong to.
- Wipe it down. A quick clean goes a long way.

### Run a charity nearby (new, a slim band)
An invitation, in line with the agreed scope's "encouraging community engagement". It claims no partner and names none.
- Headline: Run a charity / **nearby?**
- Line: If you run a shelter, a thrift store or a reuse store in Massachusetts or New Hampshire, tell us what you can use.
- Text link: Get in touch (contact.html)

### Estimate band, Donate's own words
- Headline: Ready to / **clear it out?**
- Line: Book a pickup and tell us what's still good. Want to check an item first? Give us a call. (The last four words are the phone link.)
- Button: Book a pickup

---

## About
- Meta title: About Quick Haul | Local Junk Removal in MA and NH
- Meta description: Quick Haul is Shawn and a small local crew†, clearing garages, basements and yards across Massachusetts and New Hampshire. See how a job works and who shows up.

### Banner
The heading changes so "About Quick Haul" isn't said twice in a row: the band under it now carries those words, as Varun asked. If the banner should keep "About / **Quick Haul**", the band below becomes "Who / **we are**" and nothing else moves.
- Headline: Hi, we're / **Quick Haul**
- Line: Shawn and a small local crew†, clearing garages, basements and yards across Massachusetts and New Hampshire, and taking down the old sheds and decks too.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### About Quick Haul (new, lead band with three small facts)
"Who calls us" is Shawn's own description of his customers, from the requirements form.
- Headline: About / **Quick Haul**
- Line: We're a junk removal and demolition business. If it's in the way and you want it gone, that's the job.
- Owner-run. Quick Haul is Shawn's business, not a franchise. You deal with the owner.†
- Who calls us. People freeing up space, moving out, fixing up the house or getting rid of things they don't use.
- How to reach us. Book online any time, or call Mon to Sat, 7am to 7pm.†
- Photo: logged stock, no vehicle and no person (critic, About r1). As suggested: A fenced back yard with clear lawn, a concrete patio and a large tree

### Pick up the phone (the story, slate promo, anchor #story)
- Headline: Pick up / **the phone**
- Story: It started with a truck, a phone and people who needed something gone.† Shawn still answers that phone himself, and that's on purpose.† A quick call tells him what's in the garage, how close the truck can get and what to bring. It tells you who's showing up and what it costs. You can book online any time, but if you'd rather talk it through first, call. That's what the number is for.
- Button: Call Shawn (603) 555-0142† (accessible name: Call Shawn at (603) 555-0142)
- One action only in this band. Book now is in the estimate band at the end of the page.
- Photo: stock is allowed, a person included, but never captioned or described as Shawn (choices.md, stage 6). The alt describes the photo shown. As built: A gray house with a barn-shaped roof behind a bright red shrub and a big bare tree, with a paved drive in front (Developer, 5 Nov: the old pickup showed Chevrolet badges on an Arizona lot, and a stock truck beside "how close the truck can get" read as Shawn's, critic, About r1. No vehicle or person until his own photo; logged must-replace in content/placeholders.md)
- Alt once Shawn's photo arrives: Shawn, owner of Quick Haul, beside the truck

### What we do (new, three cards, anchor #what-we-do)
- Headline: What we / **do**
- Line: It comes down to three kinds of job, from a single couch to a shed that's seen better days.
- Clean outs (heading: **Clean** / outs). Garages and basements, from a few shelves to the whole room. Link: See clean outs (services.html#clean-outs). Photo alt: An empty basement with white walls, square pillars and a clear wood floor
- Junk pickups (heading: **Junk** / pickups). Furniture, appliances, mattresses, yard waste and anything else in the way, from one item to a full truck. Link: See what we take (services.html#junk-removal). Photo alt: A cream armchair and a small sofa set out by the door of a brick building
- Demo projects (heading: **Demo** / projects). Sheds, decks, fences and tear-outs, taken down and hauled off.† Link: See demo projects (services.html#demo). Photo alt: A weathered wooden garden shed with glazed double doors

### How a job works (new, seated card with four steps, anchor #how-it-works)
No numbers on the steps (anti-slop: no numbered labels).
- Headline: How a job / **works**
- Line: From the first call to the swept floor, it goes like this.†
- You tell us. Book online or call, and say what's going. Photos help.
- We confirm. Shawn checks the job and gets back to you with the time and the price.†
- We show up. You walk us through what goes and what stays.†
- We clear it. We load it, sweep up and take it away. You pay when it's done.†

### The crew (new, three small facts on cream, anchor #crew)
No stock person here, and no name but Shawn's. This slot wants Shawn's own photo of the crew; alt then: Shawn and the Quick Haul crew beside the truck.
- Headline: The / **crew**
- Line: Quick Haul is small on purpose. The people you talk to are the people who show up.†
- Shawn. The owner. He answers the phone, looks over the jobs and works them too.†
- The crew. A small local team, with enough hands for the job in front of them.†
- On your property. They'll check with you first, then do the lifting. You don't need to help.†

### Where we work (new, promo with the street map, anchor #where)
- Headline: Where / **we work**
- Line: Both sides of the Massachusetts and New Hampshire line, at the same prices in every town.†
- Plain line†: **In Massachusetts** Andover, Dracut, Haverhill, Lawrence, Lowell and Methuen.
- Plain line†: **In New Hampshire** Derry, Hudson, Londonderry, Nashua, Pelham and Salem.
- Line: Can't see your town? Give us a call. (The last four words are the phone link.)
- Text link: See the service area (service-area.html)
- Map accessible title: Map of the towns Quick Haul covers in Massachusetts and New Hampshire

### What we stand for (seated card with three small facts, v3's How we work, anchor #stand-for)
Nothing here claims a license, insurance, a guarantee or a recycling figure. If Shawn confirms any of the held lines, this is their slot.
- Headline: What we / **stand for**
- Line: We're coming onto your property and into your garage or basement, so here's what you can expect.
- Talk first. You can talk to a person before you commit to anything. That's why the number is on every page.
- Straight prices. Tell us what's going and we'll tell you straight what it costs. Say no and that's fine.†
- Less in the dump. If something's still good, we'd rather see it used again than buried.†

### Estimate band, About's own words (the closing call)
Shawn's agreed line, word for word, with the phone link on the last four words.
- Headline: Got something / **in the way?**
- Line: Need help booking or have questions? Give us a call. Or pick a day online.
- Button: Book now

---

## FAQ
- Meta title: Junk Removal FAQ: Prices, Booking and What We Take | Quick Haul
- Meta description: How much junk removal costs, what we take and don't take, how booking works and what to expect on the day. Straight answers from Quick Haul.

### Short banner
- Headline: Questions / **answered**
- Line: Prices, booking, what we take and what to expect on the day. Can't find yours? Give us a call.
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### The list (one list, four small group labels, 17 questions)
Answers are general, or a placeholder that sets no rule. Where a real policy is unknown (changing or canceling, not being home), the answer points to a call or to Shawn and states no fee, notice period or condition.

**Pricing and paying**
- How much does junk removal cost? / You pay for how much of the truck your junk fills, from $149† for a 1/8 truck or one item to $649† for a full truck, loading, hauling and drop-off included.† Demo is priced per job.† See the pricing page.
- What if I'm not sure how much I have? / Pick "Not sure" when you book and add a few photos. We'll price it from those and confirm before we come.†
- Can the price change when you get here? / Only if the job is different from what we agreed, like extra items or heavy material we didn't know about. If it does, we tell you before we load anything.†
- When and how do I pay? / When the job's done, before we drive off. Card or cash.†

**What we take**
- What do you take? / Furniture, appliances, mattresses, household junk, garage and basement clutter, yard waste and demo debris. The full list is on our services page.†
- What don't you take? / Paint, oil and chemicals, propane tanks, asbestos, medical waste and car batteries.† Many towns run a household hazardous waste day for paint and chemicals. Not sure about something? Ask us.
- Do you donate things? / Yes, where we can. Tell us what's still good when you book and we'll take it to a local charity or reuse store instead of the dump.† Need a receipt? Say so and we'll ask for one.†
- What kind of demo do you do? / Sheds, decks and porches, fences, playsets, and kitchen and bathroom tear-outs.† Demo can need a town permit, and older buildings can hide asbestos, so check with your building department first.

**Booking**
- How does booking work? / Pick a day and your load online, add photos if you can, and send it. Shawn looks it over and gets back to you to confirm the time and the price.†
- Can I just call instead? / Yes. Call (603) 555-0142†, Mon to Sat, 7am to 7pm†, and we'll book it with you on the phone.
- How soon can you come? / Check the calendar for the next open days. If you need it sooner, call us and we'll see what we can do.
- Do you come to my town? / Probably. See the full list on our service area page, and if yours isn't there, give us a call.†
- Can I change or cancel? / Call us as soon as you know and we'll work it out with you.†

**On the day**
- Do I need to carry anything outside? / No. We carry it out from wherever it is, including basements and upstairs rooms.†
- Do I need to be home? / It helps to have someone there at the start to show us what goes and what stays. If you can't be there, tell Shawn when he confirms and you can work it out.†
- How should I get ready? / Clear a path to the junk, move the car and check drawers and boxes for anything you want to keep. If something's staying, put a note on it.
- How long does a job take? / It depends on how much there is and how far it has to go. One item can be minutes, and a full basement can take a few hours.†

Links inside the answers: "pricing page" to Pricing, "services page" to Services, "calendar" to Book, "service area page" to the hub, the number to the phone.

---

## Contact
- Meta title: Contact Quick Haul | Junk Removal Quotes in MA and NH
- Meta description: Call, email or send us a quick request for a junk removal or demo price. Quick Haul works towns across Massachusetts and New Hampshire, Mon to Sat.

### Short banner
- Headline: Call, book / **or ask**
- Line: The fastest way to a price is a call. Rather write it down? Send us a request.
- Button: Give us a call (603) 555-0142† (accessible name: Give us a call at (603) 555-0142)
- Photo alt: A sunny street of old wooden houses with a brick sidewalk

### Which way is best (new, three small facts)
The three words are the banner's own, in the same order. Book links to book.html; Ask jumps to the form below.
- Headline: Which way / **is best?**
- Line: Use whichever suits you. Each one's good for something different.
- Call. Best for a quick price, an odd job or a question.
- Book. Best when you know your load and want to pick a day.
- Ask. Best when you'd rather write it down or send photos first.

### Map and hours
- Map accessible title: Map of the towns Quick Haul covers in Massachusetts and New Hampshire
- Map center: Salem, NH† (base town placeholder, not marked on the map as a base)
- Hours. Mon to Sat, 7am to 7pm†. Closed Sundays.†
- Where we go. Towns across Massachusetts and New Hampshire. Link: See the full list
- Email (new). quickhaul@example.com†
- Find us (new). Facebook, Instagram and TikTok. (Each name links to its profile†, opens in a new tab.)

### Ask for a price (short form)
- Headline: Ask for / **a price**
- Line: Phone or email is enough, and we'll get back to you.
- Plain line (new): **It helps to tell us** what's going, where it is and whether the truck can get close.
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

### One price list (new, a slim band)
- Headline: One price list, / **every town**
- Line: A load costs the same in Lowell as it does in Londonderry.†
- Text link: See the prices (pricing.html)

### When the curb won't take it (new, promo with one photo)
General information, so no dagger. It speaks about many towns and names none.
- Headline: When the curb / **won't take it**
- Line: Many towns limit big items at the curb or charge for a sticker, and transfer stations have their own rules. Skip the trip and book a pickup.
- Photo alt: A cream armchair and a small sofa set out by the door of a brick building

---

## Town pages (one template)
Written here for Lowell, MA. Every other town page uses the same copy with its own town and state. Nothing else changes, and no local claims are added per town until Shawn gives them.
- Meta title: Junk Removal in Lowell, MA | Quick Haul
- Meta description: Junk removal, clean outs, furniture, appliance, mattress and yard waste pickup, plus demo, in Lowell, MA. Loads start at $149†. Book a day online or call.

### Banner
- Headline: Junk removal in / **Lowell, MA**
- Line: Clean outs, single items, yard waste and demo work in Lowell. Loads start at $149.†
- Button: Book in Lowell
- Photo alt: A sunny street of old wooden houses with a brick sidewalk. The photo is not of the town, so the alt never names it.

### What we haul
- Headline: What we haul / **in Lowell**
- Line: We come to Lowell with the truck, load it ourselves and haul it away. You don't need to drag anything to the curb.†
- Photo tiles (names only, Home's photos and alts): Junk removal; Clean outs; Furniture; Appliances; Mattresses; Yard waste; Demo
- Text link: See everything we take

### How it works (new, three small facts)
The same three facts as Home's estimate band and Book.
- Headline: How it works / **in Lowell**
- Line: Book online or call. Either way, you hear the time and the price before we come.†
- You book. Pick a day and your load.
- We confirm. Shawn checks the job, the time and the price.†
- We haul. We load it and leave the space clear.†

### Priced by the load (the row of four)
- Headline: Priced by / **the load**
- Line: You pay for how much of the truck your junk fills. The prices are the same in Lowell as everywhere else we go.†
- Row of four loads: the same as Services.
- Text link (new): See how pricing works (pricing.html)

### Also nearby (the slim light strip the trucks park on)
- Label: Also near Lowell
- Chips, each linking to its town page: the three nearest towns on the list, from the table below
- Text link: See other towns

| Town page | Also near it |
|---|---|
| Andover, MA | Lawrence; Methuen; Dracut |
| Dracut, MA | Lowell; Pelham; Methuen |
| Haverhill, MA | Salem; Lawrence; Methuen |
| Lawrence, MA | Methuen; Andover; Salem |
| Lowell, MA | Dracut; Pelham; Methuen |
| Methuen, MA | Lawrence; Salem; Andover |
| Derry, NH | Londonderry; Salem; Hudson |
| Hudson, NH | Nashua; Pelham; Londonderry |
| Londonderry, NH | Derry; Hudson; Nashua |
| Nashua, NH | Hudson; Pelham; Londonderry |
| Pelham, NH | Dracut; Hudson; Methuen |
| Salem, NH | Methuen; Lawrence; Haverhill |

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

### Who this is for (new, three small facts)
The kinds of job each one might ask about. Nothing says we have done them.
- Headline: Who this / **is for**
- Landlords. Unit turnovers, what tenants leave behind, shared basements and storage.
- Realtors. Clearing a listing before photos or showings.
- Property managers and contractors. Regular pickups, and debris after a job.

### Request form
- Plain line above the first field (new): **It helps to tell us** how many units or rooms, how close the truck can get and how soon you need it.
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
- Line: This page is empty, like the truck after a drop-off. It may have moved. Try one of these, or give us a call. (The last four words are the phone link.)
- Button: Book now
- Links: Home; Services; Pricing; Contact
- No estimate band on this page.

---

## Privacy policy
Plain-language draft. The length stays, plus the two additions marked new. It must be checked against the services actually used (booking plugin, SMS provider, analytics, form spam protection) and reviewed by someone qualified before launch. The site has no analytics or upload yet, so this describes things not connected. Business name and contact details are placeholders.
- Meta title: Privacy Policy | Quick Haul
- Meta description: How Quick Haul collects and uses your details when you book, ask for a price or visit the site.
- No estimate band on this page.
- Headline: Privacy / **policy**
- Sections:
  - What we collect. When you book or ask for a price, we collect your name, phone number, email, the pickup address, details about the job and any photos you upload. When you visit the site, we collect basic analytics like which pages are viewed. Analytics tools can use cookies to do this, and you can block cookies in your browser settings. (Last sentence new.)
  - Why we collect it. To confirm and carry out your booking, to give you a price, to send booking confirmations and reminders, and to understand how people use the site so we can improve it.
  - Photos you send (new). We use them to price and plan your job. We don't put them on the site or on social media unless you say it's OK.†
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
- The trust row they sat in is cut from Home (revision.md section 4). If Shawn confirms any, About's What we stand for is their slot.
- Home's Reviews line, once real reviews are in and each links to its post: Every review here links back to Facebook, so you can see who wrote it and when.
- Reviews banner line, once real reviews are in: Real reviews from our Facebook page, just as their writers left them.
- Reviews, Word for word line, once real reviews are in: Every review here is just the way its writer left it.
- The Facebook link on Home and at the end of the Reviews grid, once real reviews are in: Read more on Facebook
- Reviews page, on each card, once each review has a post URL: Read on Facebook
- Before and after line, Home and Reviews, once Shawn's own photos replace the stock pairs: Every pair here is one of our own jobs, photographed the day we did it.
- Reviews pair captions, once Shawn's own pairs are in: each load line says what that job actually took, in his numbers.
- Footer fact line, once Shawn confirms the year: Hauling since 2022†

---

## Questions for the client
Varun's call at stage 6: not forwarded for now, they stay placeholder values. Kept here so they can go to Shawn in one pass. Most important first.
1. Phone, hours, base town and the full town list. Is Sunday a working day? Do prices change for towns further out?
2. Prices. Will they go on the site? What are the real bands, is there a minimum or single-item price, how big is your truck, and how much does each band really hold? We wrote one, two, four and eight pickup beds. What costs extra: heavy material, fridges and AC units (we made up $30), stairs and long carries? Do mattresses cost extra in Massachusetts, now they can't go in the trash there?
3. Booking. Are you happy with a request you confirm? What time windows do you offer? Can customers be out during the job? What is your change and cancel rule? When and how do customers pay?
4. Licensed, insured, guaranteed. Which are true, and in which states? The lines for these are written but held.
5. Your story. How did Quick Haul start, and when? Who is on the crew, do you answer the phone yourself, and are you happy for your first name to be used across the site? Is "small on purpose" and "not a franchise" fair? We need a photo of you, or of you with the truck and crew.
6. What you take and don't take. Please check both lists. Do you take electronics and TVs? Do you disconnect appliances, or only take ones already unhooked? Do you take furniture apart? Do you sweep up after? Do customers need to bag small stuff?
7. Demo. What size of job do you take on (sheds, decks, kitchens, anything structural)? How do you price it? Who handles the permit and, in Massachusetts, the asbestos survey?
8. Donations. Do you take usable items to charity? Which ones, what won't they accept, and can a customer get a receipt?
9. Where does the rest go? We only say "the drop-off". If you use a transfer station or a recycler, it could be a good line.
10. Commercial and repeat work. Do you do it, and for whom? The commercial page is placeholder until you say yes.
11. Your Facebook, Instagram and TikTok links, and which Facebook reviews you want on the site: at least six, five of them for the homepage. No real reviews or ratings go up until then. Should the automated review request send the Facebook link after each job?
12. Photos. Your own job photos, especially before and after pairs from the same spot, to replace the stock images. May customers' photos ever go on the site? The privacy draft says only if they agree.

## Left out on purpose
- No real review quotes, star ratings or review counts. The proposal (term 05, as quoted in brief.md) rules out any rating that hasn't been earned, and none have been supplied. The sample cards name a kind of job and never speak as a customer.
- No "plenty" on the page any more. It is still Shawn's word for his Facebook reviews (chat, 31 Aug), but it contradicted sample cards, and nobody here has seen his page.
- No license, insurance or guarantee claims in any built copy, including What we stand for. Written and held only.
- About's story stops at one placeholder line about how it started. When Shawn started, where, what he did before and why he does this aren't in his material, so there is no year, no town, no former job and no family detail.
- The crew has no names, no headcount and no claim about background checks or uniforms. Only Shawn's first name is used.
- Nothing on Donate about which charities, how much of a load gets donated or whether donating changes the price. None of it is in his material.
- No year in business anywhere that gets built. 2022 now sits only in the held footer line.
- No named charities or partners. Naming a real organization would be a claim about a real business.
- No response-time promises ("within an hour", "same day"), no "no hidden fees" or "no surprises" claim and no eco or recycling percentages. Nothing in the material supports them.
- No reason given for the can't-take list. V1's "the dump won't take them from us" was a claim nobody had made.
- No change or cancel fee, notice period or rule about being home. The answers point to a call and state no policy.
- No truck dimensions or cubic yards. His truck is unknown, and pickup beds are easier to picture.
- No dollar figure for heavy material or hard carries. Only the fridge fee has one, because a worked example needs one extra with a number.
- Nothing about who pulls demo permits or handles asbestos surveys, and nothing on where junk goes after the drop-off.
- No local detail on town pages: no neighborhoods, landmarks or local rules. "Also near" comes from public map positions only.
- No blog or scrap talk, as Shawn asked.
