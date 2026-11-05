# Quick Haul: site copy
Copywriter, 2026-11-03. Written from prd/client-chat.txt, prd/Proposal-shawndowling-DH-SHAWNDOWLING-20260831-R1.pdf, brief.md (including Varun's answers at checkpoint 1a), design/design-spec.md and design/choices.md (checkpoint 2b).

## How to read this file
- Organised by page, then by section, using the spec's section names.
- Headlines are two rows. Row 1 is the light weight, row 2 (in bold here) is the heavy weight. Written in sentence case; the CSS sets them in capitals. No full stops, no italics, no colour change.
- Body copy is final wording. Labels are the mono field and fact labels from the spec; they are never used as section eyebrows.
- Every value marked with a dagger (†) is a placeholder: a realistic stand-in for a fact Shawn has not confirmed. Each one is in content/placeholders.md with what is needed to replace it. The dagger is for this file only; do not print it on the site.
- Lines marked HOLD are written and approved in wording, but must not be built until Shawn confirms the fact behind them.
- Phone everywhere: (603) 555-0142†, tel:+16035550142. Hours everywhere: Mon to Sat, 7am to 7pm†. Email: quickhaul@example.com†.
- Prices everywhere: 1/8 truck $149†, 1/4 truck $249†, 1/2 truck $399†, full truck $649†.
- Image slots: per choices.md decision 3, slots use stock photos for now, each logged as must-replace. Alt text below describes what the slot shows and never claims a stock photo is a Quick Haul job. When Shawn's own photos replace them, the developer rewrites each alt to match the real photo.

---

## Global (every page)

### Preview label (required by the brief until launch)
A slim line above the top bar, on the preview only. Remove at launch.
- Text: Design preview. Phone, hours, towns, prices, reviews and photos are sample content until Quick Haul confirms them.

### Top bar
- Desktop, left: Need help booking or have questions? Give us a call (603) 555-0142†
- Desktop, right: Mon to Sat, 7am to 7pm†
- Phone (one line): Questions? Give us a call (603) 555-0142†
- Shawn's own suggested line was "need help, booking? or have questions, give us a call". The wording above is the tidy version we agreed with him in the chat.

### Header
- Nav: Services, Pricing, Reviews, Donate, About
- Logo alt: Quick Haul home
- Call circle accessible name: Call Quick Haul on (603) 555-0142†
- Button: Book now
- Phone: Menu (button label)

### Menu (phones and tablets)
- Accessible name: Menu
- Close button accessible name: Close menu
- Links: Services, Pricing, Service area, Reviews, Donate, About, FAQ, Contact
- Buttons: Call us; Book now
- Line under the buttons: (603) 555-0142†, Mon to Sat, 7am to 7pm†

### Phone action bar (call-only, per choices.md decision 4)
- Button: Call (603) 555-0142†
- Region accessible name: Call Quick Haul

### Estimate band (before the footer on every page except Book)
- Headline: Got a garage / **full of junk?**
- Supporting: Pick a day online in a couple of minutes, or call and tell us what you've got. Either way you know the price before we show up.
- Button: Book now
- Call line: Need help booking or have questions? Give us a call (603) 555-0142†

### Footer
- Phone (big, underlined): (603) 555-0142†
- Email: quickhaul@example.com†
- Hours line under the phone: Mon to Sat, 7am to 7pm†
- Tagline (two heavy rows): Junk out / Space back
- Column: Services. Junk removal; Garage and basement clean outs; Furniture removal; Appliance removal; Mattress removal; Yard waste removal; Demo projects
- Column: Booking. Book now; Pricing; Service area; Commercial enquiries
- Column: Quick Haul. About; Reviews; Donate; FAQ; Contact
- Column: Help. Privacy policy; Need help booking? Call (603) 555-0142†
- Social pills: Facebook; Instagram; TikTok (handles not given; links stay unset until Shawn sends them)
- Fact line: Junk removal and demo across Massachusetts and New Hampshire
- Fact line, HOLD until Shawn confirms the year: Hauling since 2022†
- Back to top
- Created with love by Digital Heroes

---

## Home
- Meta title: Junk Removal and Demo in MA and NH | Quick Haul
- Meta description: Junk removal, garage and basement clean outs, furniture, appliance, mattress and yard waste pickup, plus demo work across Massachusetts and New Hampshire. See your price and book a day online.
- Preview builds prefix the description with "Design preview with placeholder content." and stay noindex.

### Hero
- Headline: Junk out / **Space back**
- Lede: Junk removal, clean outs and demo work across Massachusetts and New Hampshire. Pick your town, your load and a day below to see your price, or give us a call.
- Truck drawing: decorative, no alt (aria-hidden, as built).

### Ticket (the work order)
- Hidden heading (screen readers): Start a booking
- Label: Your town
  - Field hint: Type your town
  - Note, before typing: Start typing to check we come to you
  - Note, town on the list: Yes, we come to Lowell, MA. (the town fills in)
  - Note, town not on the list: Not on our list yet. Call (603) 555-0142† and ask
  - Listbox accessible name: Towns we cover
  - Towns†: Andover, MA; Dracut, MA; Haverhill, MA; Lawrence, MA; Lowell, MA; Methuen, MA; Derry, NH; Hudson, NH; Londonderry, NH; Nashua, NH; Pelham, NH; Salem, NH
- Label: How much junk
  - Chips: 1/8; 1/4; 1/2; Full (screen readers hear "1/8 truck" and so on)
  - Helper under the chips†: 1/8 is a couple of big items. Full is a packed garage.
- Label: Pick a day
  - Day chips: the next open days from the calendar (weekday short name over the date)
  - Empty state: No open days showing. Call us and we'll find one.
- Label: Price from
  - Figure and unit: $149† for a 1/8 truck (updates with the chip: $249† for a 1/4 truck, $399† for a 1/2 truck, $649† for a full truck)
- Button: Book now
- Call link: Or call (603) 555-0142†
- Error, no town: Type your town so we can check we cover it
- Error, no day: Pick a day, or call us to find one

### Services overview
- Headline: What we / **haul away**
- Supporting: One crew, one truck, and a list that covers most of what ends up in a garage, a basement or a back yard. Pick the job below to see what we take, or book now and tell us what's going. If it's heavy, awkward or just in the way, ask us.
- Cells (label, then one line under it):
  - Junk removal. Anything from one couch to a full truck, loaded by us.
  - Garage and basement clean outs. Clear the floor and get the room back.
  - Demo projects. Sheds, decks and tear-outs taken down and hauled off.†
  - Furniture. Couches, dressers, desks and dining sets.
  - Appliances. Fridges, washers, dryers and stoves.
  - Mattresses. Mattresses, box springs and bed frames, any size.
  - Yard waste. Brush, branches, leaves and clean-up piles.
- Button: Book now
- Text link: See everything we take
- Image alt text:
  - Junk removal: A pickup load of old furniture and boxes ready to be hauled away
  - Clean outs: A garage cleared down to bare concrete
  - Demo: An old wooden shed partly taken down
  - Furniture: A worn couch being carried out through a front door
  - Appliances: An old refrigerator on a hand truck
  - Mattresses: A mattress and box spring leaning against a wall
  - Yard waste: A pile of cut branches and bagged leaves at the edge of a lawn

### Price and service area
- Headline: Do you come / **to my town?**
- Supporting: Probably. We cover towns on both sides of the Massachusetts and New Hampshire line†, and every one of them starts at the same price. You pay for how much of the truck your junk fills. Add photos when you book and we confirm the price before the day, so nothing changes in your driveway.
- Cards (town, state label, figure, unit)†: Lowell, Massachusetts, from $149, 1/8 truck. The same for Andover, Dracut, Haverhill, Lawrence, Methuen (Massachusetts) and Derry, Hudson, Londonderry, Nashua, Pelham, Salem (New Hampshire). Each card links to its town page.
- Closing card: Can't see your town? / Call us. If we can get to you, we'll tell you the price on the phone. / Call (603) 555-0142†
- Arrow buttons, accessible names: Previous towns; Next towns
- Text link: See all prices

### Featured reviews
Spec: the section waits for real reviews. For the design preview it uses sample cards worded so nobody can mistake them for real ones (brief, checkpoint 1a rule). No star rating and no score row until a real Facebook rating exists (proposal term 05).
- Headline: Straight from / **Facebook**
- Supporting: These are our customers' own words, copied from our Facebook page exactly as they wrote them, with their name and the date. Tap any review to read it where it was posted.
- Sample cards (quote, then name line):
  - "Sample review. A real review from Quick Haul's Facebook page goes here, word for word, once Shawn picks which ones to use." / Sample review, Facebook
  - "Sample review. This card is sized for a two or three line review about a garage or basement clean out." / Sample review, Facebook
  - "Sample review. This card is sized for a short review about a single item pickup, like a couch or a mattress." / Sample review, Facebook
  - "Sample review. This card is sized for a longer review about a yard clean-up or a demo job, the kind that runs to four or five lines on a phone." / Sample review, Facebook
- Text link: Read all our reviews on Facebook
- Arrow buttons, accessible names: Previous reviews; Next reviews
- Final build: the sample cards are replaced, never edited into real-sounding reviews.

### Trust indicators (one ruled row inside the reviews section)
These three describe how the site and the booking work, which the scope already commits to. They make no claim about licences, insurance or guarantees.
- Label: Price first. Body: Pick your load and the starting price is right there. Send photos with your booking and we confirm it before the day.
- Label: A real person. Body: Every booking goes straight to Shawn. Rather talk it through first? Call and ask before you book.
- Label: Reviews you can check. Body: Every review on this site links back to Facebook, so you can see who wrote it and when.
- HOLD, build only once Shawn confirms each one (neutral wording, flagged must-confirm in placeholders.md):
  - Label: Licensed†. Body: Licensed to haul in Massachusetts and New Hampshire. Ask us for the details.
  - Label: Insured†. Body: Insured for the work we do on your property. We'll send proof if you ask.
  - Label: Guarantee†. Body: Shawn's guarantee goes here in his own words, once he confirms what it covers.

### How it works
FREITAG 3 + 6 + 3. Three stacked ticket lines: a mono label, one Bio Sans 600 line, one mono sentence. No numbers.
- Headline: From booking / **to bare floor**
- Line 1. Label: You book. Line: Pick your town, your load and a day. Sentence: It takes a couple of minutes online, and you can add photos of the junk so we know exactly what's coming.
- Line 2. Label: We confirm. Line: We check the job and lock in your time. Sentence: Shawn looks over every booking and gets back to you to confirm the time and the price, so there are no surprises on the day.†
- Line 3. Label: We haul. Line: We load it, take it and leave the space clear. Sentence: You point, we carry, and anything still in good shape goes to donation instead of the dump.†
- Button: Book now
- Call line: Need help booking or have questions? Give us a call (603) 555-0142†

### Before and after
- Headline: Before / **and after**
- Supporting: Drag the line across to see the difference a clean out makes. Garages, basements and yards that hadn't seen daylight in years, cleared down to the floor and ready to use again. Book the same job for your place below.
- Final-only line, HOLD until Shawn's own photos replace the stock pair: Every pair here is one of our own jobs, photographed on the day.
- Slider accessible name: Drag to compare before and after
- Slider labels: Before; After
- Caption: Garage clean out
- Image alt text: Before: a garage packed with boxes, old furniture and clutter. After: the same garage cleared to bare concrete.
- Button: Book a clean out
- Text link: See more before and afters

---

## Services
- Meta title: Junk Removal Services in MA and NH | Quick Haul
- Meta description: Garage and basement clean outs, furniture, appliance, mattress and yard waste removal, plus demo projects. See what we take, what it costs and book a day online.

### Inner banner
- Headline: Our / **services**
- Lede: Clean outs, single items, yard waste and demo work across Massachusetts and New Hampshire. Every section lists what we take, and you can book any of them right from there.

### Junk removal (split band)
- Headline: Junk / **removal**
- Body: Got a pile and no easy way to get rid of it? Tell us roughly how much of the truck it fills, pick a day, and we come and load it. We do the lifting and carrying, from the curb, the driveway or a back room, so you don't need to drag anything outside first.† Add a few photos when you book and we can confirm the price before we arrive.
- What we take†: Boxes, bags and loose household junk; Old furniture and rugs; Exercise equipment; Bikes, toys and sports gear; Moving and move-out leftovers; Scrap wood and metal
- Button: Book now
- Call link: Or call (603) 555-0142†
- Image alt: A truck bed loaded with old furniture, boxes and bags

### Garage and basement clean outs (split band)
- Headline: Garage and basement / **clean outs**
- Body: Garages and basements fill up slowly, then all at once. We clear them out: old boxes, broken shelving, furniture nobody sits on and the leftovers of every past project. Point at what goes and what stays, and we carry it out, load it and leave you with a floor you can actually use. Moving out or getting a house ready to sell? Same job, same crew.
- What we take†: Boxes and storage bins; Shelving and workbenches; Old furniture; Tools and hardware nobody uses; Holiday decorations; Bikes, toys and sports gear; Carpet and rugs; Anything else you point at, inside our list
- Button: Book a clean out
- Call link: Or call (603) 555-0142†
- Image alt: A basement with the floor cleared and shelving emptied

### Furniture removal (split band)
- Headline: Furniture / **removal**
- Body: Couches, sectionals, recliners, dressers, desks and dining sets. If it's too big for your car or too heavy to move on your own, we take it. We carry it out of whatever room it's in, down the stairs and onto the truck.† Pieces that are still in good shape can go to donation instead of the dump, so tell us which ones when you book.
- What we take†: Couches, sofas and sectionals; Recliners and armchairs; Dressers and wardrobes; Desks and office chairs; Dining tables and chairs; Bookcases and entertainment centres; Patio furniture
- Button: Book now
- Call link: Or call (603) 555-0142†
- Image alt: Two people carrying a worn sofa out of a house

### Appliance removal (split band)
- Headline: Appliance / **removal**
- Body: Old fridge in the garage? Washer that finally quit? We haul out fridges, freezers, washers, dryers, stoves and more, from the kitchen, the basement or wherever they ended up. Appliances are heavy and awkward to move, and that's the part we handle. Let us know when you book if anything is still hooked up, so we know what we're walking into.
- What we take†: Refrigerators and freezers; Washers and dryers; Stoves and ovens; Dishwashers; Microwaves; Window air conditioners; Water heaters; Dehumidifiers
- Button: Book now
- Call link: Or call (603) 555-0142†
- Image alt: An old white refrigerator and washing machine standing in a garage

### Mattress removal (split band)
- Headline: Mattress / **removal**
- Body: A mattress is the one thing nobody wants to wrestle into a car. We take mattresses and box springs of every size, plus the frames, headboards and futons that go with them. Book one pickup on its own or add it to a bigger load. Replacing a bed? Book us for the day the new one arrives and the old one leaves with us.
- What we take†: Mattresses, twin to king; Box springs; Bed frames and headboards; Futons and sofa beds; Cribs and toddler beds; Memory foam toppers
- Button: Book now
- Call link: Or call (603) 555-0142†
- Image alt: A mattress and box spring leaning against a bedroom wall

### Yard waste removal (split band)
- Headline: Yard waste / **removal**
- Body: Spring clean-up, a storm that brought half a tree down or a whole fall's worth of leaves. We load and haul brush, branches, bagged leaves and clippings, plus the old fencing, planters and patio furniture that pile up behind the shed. Bag the small stuff if you can and we'll take care of the rest.†
- What we take†: Brush and branches; Bagged leaves and grass clippings; Small logs and limbs; Old fencing and lattice; Planters and pots; Broken patio furniture; Swing sets and trampolines
- Button: Book now
- Call link: Or call (603) 555-0142†
- Image alt: A pile of cut branches and full leaf bags on a lawn

### Demo projects (split band on slate)
- Headline: Demo / **projects**
- Body: We do demo projects as well. Old sheds, rotting decks, fences, playsets, and interior tear-outs like a kitchen or a bathroom.† We take it apart and haul the debris away, so there's no dumpster sitting in your driveway for a week. Every demo job is different, so send photos with your booking or give us a call and we'll price it with you.
- What we take down†: Sheds; Decks and porches; Fences; Playsets and swing sets; Above-ground pools and hot tubs; Kitchen and bathroom tear-outs
- Button: Book now
- Call link: Or call (603) 555-0142† to talk it through
- Image alt: A backyard shed with its roof and one wall removed
- The first sentence is Shawn's own line from the chat.

### What we take and what we don't
- Headline: What we take / **and what we don't**
- Supporting: Most of what's in a house, a garage or a yard can go on the truck. A few things can't, for safety and because the dump won't take them from us. Not sure about something? Send a photo with your booking or call us and ask.†
- Column label: We take. Items: Furniture of every size; Appliances; Mattresses and box springs; Boxes, bags and household junk; Yard waste; Demo debris; Electronics and TVs†; Scrap wood and metal
- Column label: We don't take†. Items: Paint, oil and chemicals; Propane tanks and gas cylinders; Asbestos; Medical waste; Car batteries; Anything still connected to gas
- Button: Book now
- Call line: Need help booking or have questions? Give us a call (603) 555-0142†

### Pricing (anchor: #pricing)
- Headline: Priced by / **the load**
- Supporting: You pay for how much of the truck your junk fills, and the price covers the loading, the hauling and the drop-off.† Pick a size when you book and add photos, and we confirm the price before the day. Heavy loads like concrete, dirt or roofing shingles can cost more, so tell us about them up front.†
- Cards (label, figure, what fits)†:
  - 1/8 truck. $149. A couple of big items, like a couch and a chair, or one mattress set.
  - 1/4 truck. $249. A room's worth: a bedroom set, or a pile of boxes and bags.
  - 1/2 truck. $399. A small garage or basement clean out.
  - Full truck. $649. A packed garage, a full basement or a whole move-out.
- Note line†: Just one item? It's priced as a 1/8 load. Demo work is priced per job.
- Button: Book now
- Call link: Or call (603) 555-0142† for a price on the phone

---

## Book
- Meta title: Book a Junk Pickup | Quick Haul
- Meta description: Pick a day, tell us what's going and add photos. We confirm your time and price before we come. Junk removal and demo across Massachusetts and New Hampshire.

### Inner banner
- Headline: Book a / **pickup**
- Lede: Pick a day, tell us what's going and add a few photos. We'll confirm your time and price before the day.

### Booking ticket
Progress line labels: Day; Load; Address and details; Your details.
Booking model is not decided (brief, open question 3). The wording below is request-then-confirm, which fits Shawn's worry that self-booked slots are "less solid". If Varun picks instant confirmation, swap the lines marked "Request" for the alternates marked "Instant".

**Step: Day**
- Label: Pick a day
- Calendar accessible name: Available days
- Label: Pick a time
- Time chips†: 8am to 11am; 11am to 2pm; 2pm to 5pm
- Helper: These are arrival windows. We'll confirm yours before the day.
- Empty state: No open slots that week. Try the next week, or call us and we'll find a time.
- Error: Pick a day and a time to keep going
- Button: Next: your load

**Step: Load**
- Label: How much junk
- Chips: 1/8 truck; 1/4 truck; 1/2 truck; Full truck; Not sure
- Helper†: 1/8 is a couple of big items. Full is a packed garage. Not sure? Pick the closest and add photos.
- Price line: From $149† for a 1/8 truck (updates with the chip). For "Not sure": We'll price it from your photos.
- Label: What kind of job
- Chips: Junk removal; Clean out; Furniture; Appliances; Mattresses; Yard waste; Demo
- Button: Next: address and details

**Step: Address and details**
- Label: Street address
- Label: Town (filled from the home ticket when the visitor came from there)
- Label: ZIP code
- Label: Where's the junk
- Chips: Curb or driveway; Garage; Basement; Inside the house; Yard
- Label: What's going
  - Field hint: For example: old couch, two mattresses, a pile of boxes in the basement
- Label: Add photos (optional)
  - Helper: Photos help us confirm your price and bring the right gear. A few from different angles is plenty.
  - Upload button: Choose photos
  - Upload error: That file didn't upload. Try a JPG or PNG photo.
- Label: Anything we should know (optional)
  - Field hint: Gate code, parking, stairs, items you'd like donated
- Button: Next: your details

**Step: Your details**
- Label: Your name
- Label: Phone
- Label: Email
- Checkbox (SMS consent, for review before launch): Text me booking updates and a reminder the day before. Message and data rates may apply. Reply STOP to opt out.
- Small print: We only use your details for this booking. Read our privacy policy.
- Request button: Send booking request
- Instant button: Book now
- Errors: Add your name; Add a phone number we can reach you on; That email doesn't look right; Add the street address for the pickup

### Call cell (fixed right cell at desktop, under every step on phones)
- Line: Need help booking or have questions? Give us a call
- Number: (603) 555-0142†
- Hours: Mon to Sat, 7am to 7pm†

### Confirmation state
- Request headline: Request / **sent**
- Request body: Thanks, your booking request is in. Shawn will look it over and get back to you to confirm your time and price. A copy is on its way to your email.
- Instant headline: You're / **booked**
- Instant body: Thanks, you're on the calendar. A confirmation is on its way to your email, and we'll send a reminder the day before.
- Summary labels: Day; Time; Load; Price from; Address
- Line: Need to change something? Call (603) 555-0142†
- Button: Back to home

### Error state (booking system down)
- Headline: Something / **went wrong**
- Body: Your booking didn't go through, and that's on our end. Give us a call on (603) 555-0142† and we'll book it with you on the phone.

---

## Reviews
- Meta title: Customer Reviews | Quick Haul Junk Removal
- Meta description: Read what customers say about Quick Haul, straight from our Facebook page, and see before and after photos of garage, basement and yard clean outs.

### Inner banner
- Headline: Straight from / **our customers**
- Lede: Every review here is copied from our Facebook page, word for word, with a link back so you can check it.

### Filter column
- Label: Filter by job
- Options: All; Clean outs; Furniture; Appliances; Mattresses; Yard waste; Demo
- No star filter until real ratings are on the page.
- Empty filter state: No reviews for that job yet. Book one and you could be the first.

### Review grid
- Sample cards (same rule as the homepage: obviously samples, replaced and never edited into real-sounding reviews):
  - "Sample review. A real review from Quick Haul's Facebook page goes here, word for word." / Sample review, Facebook / Job: Clean outs
  - "Sample review. This card is sized for a short review about a mattress pickup." / Sample review, Facebook / Job: Mattresses
  - "Sample review. This card is sized for a medium review about a furniture or appliance pickup, around three lines." / Sample review, Facebook / Job: Furniture
  - "Sample review. This card is sized for a longer review about a yard clean-up, the kind a customer writes after a big job." / Sample review, Facebook / Job: Yard waste
  - "Sample review. This card is sized for a review about a shed or deck demo." / Sample review, Facebook / Job: Demo
  - "Sample review. This card is sized for a short review about an appliance pickup." / Sample review, Facebook / Job: Appliances
- Link on each card: Read on Facebook

### Leave a review
- Headline: Used us / **already?**
- Body: Tell the next person what it was like. Reviews go on our Facebook page, and the best ones make it onto this site exactly as you wrote them.
- Button: Leave a review on Facebook
- Text link: See all our reviews on Facebook

### Before and after gallery
- Headline: Before / **and after**
- Supporting: Drag each line across to see the job from start to finish. Garages, basements, yards and demo jobs, cleared and ready to use.
- HOLD, final only: Every pair here is one of our own jobs, photographed on the day.
- Pairs (caption, then alt):
  - Garage clean out. Before: a garage stacked with boxes and old furniture. After: the same garage with a clear concrete floor.
  - Basement clean out. Before: a basement crowded with storage bins and broken shelving. After: the same basement with the floor and walls clear.
  - Yard clean-up. Before: a back yard with piles of branches and debris. After: the same yard with the lawn clear.
  - Shed demo. Before: an old wooden shed in a back yard. After: the same spot with the shed gone and the ground clear.
- Slider accessible names: Drag to compare the garage clean out; Drag to compare the basement clean out; Drag to compare the yard clean-up; Drag to compare the shed demo
- Button: Book now

---

## Donate
- Meta title: Donate Your Old Furniture and Household Items | Quick Haul
- Meta description: Some of what we haul still has plenty of life in it. Tell us what's still good when you book and we set it aside for donation instead of the dump.

### Title cell
- Headline: Still good? / **Someone wants it**

### Statement cell
- Body: A lot of what we pick up still works. The dresser that doesn't fit the new place, the kids' bikes, the spare couch from the basement. Throwing that in the dump makes no sense when someone nearby could use it. So when we haul your junk, we sort out the good stuff and take it to local charities and reuse stores instead.† You get the space back and the stuff gets a second life.

### Labelled cells (6 + 6, left column)
- Label: What we can donate†. Body: Furniture in good shape, working appliances, kitchenware, clothes and shoes, books, toys, bikes, tools and sports gear. If you'd use it, someone else probably will too.
- Label: What we can't†. Body: Anything broken, stained or missing parts, mattresses that have been slept on for years, car seats, recalled cribs and anything that's been in a flood or a fire.
- Label: Where it goes†. Body: Local charities and reuse stores in Massachusetts and New Hampshire that take household goods. What they accept changes, so we check before every drop-off.
- Label: How to ask. Body: When you book, add a note saying which items are still good, or tell us on the day. We'll load them separately so they don't end up on the pile.†
- Photo tile alt: A sturdy wooden dresser and a kitchen chair set aside in good condition
- Button: Book a pickup
- Call line: Want to check an item first? Call (603) 555-0142†

---

## About
- Meta title: About Quick Haul | Local Junk Removal in MA and NH
- Meta description: Quick Haul is a local junk removal and demo crew working across Massachusetts and New Hampshire. Meet Shawn and see how we work.

### Inner banner
- Headline: About / **Quick Haul**
- Lede: A local junk removal and demo crew, working towns across Massachusetts and New Hampshire.

### Statement block
- Statement (light, full measure): Quick Haul is Shawn and a small crew† who clear out garages, basements and yards across Massachusetts and New Hampshire, and take down the sheds and decks that need taking down.

### Split band
- Headline: Pick up / **the phone**
- Body: Shawn started Quick Haul in 2022† and still answers the phone himself. That's on purpose. A two-minute call tells him what's in the garage, how to get the truck close and what to bring, and it tells you who's showing up and what it costs. You can book online any time, but if you'd rather talk it through first, call. That's what the number is for.
- Second paragraph: Every job is the same idea: show up when we said, carry out what you point at, leave the space clear and take the good stuff to donation where we can.† No sales pitch, no guessing on the price.
- Button: Book now
- Call link: Or call Shawn on (603) 555-0142†
- Image slot: Shawn's own photo is needed here. Do not use a stock photo of a person in this slot, because it would read as Shawn. Until his photo arrives, use a stock photo of a work truck or a cleared garage.
  - Alt (stock, until then): A work truck parked in a residential driveway
  - Alt (once Shawn's photo arrives): Shawn, owner of Quick Haul, beside the truck

### How we work (ruled cells)
- Label: Local. Body: We work towns on both sides of the Massachusetts and New Hampshire line†, so we're never far away.
- Label: Upfront. Body: You see the starting price before you book, and we confirm it before the day.
- Label: Reachable. Body: A real number with a real person on the end of it, Mon to Sat, 7am to 7pm†.
- Label: Less in the dump. Body: Anything still good goes to donation where we can, not straight on the pile.†

---

## FAQ
- Meta title: Junk Removal FAQ: Prices, Booking and What We Take | Quick Haul
- Meta description: How much junk removal costs, what we take and don't take, how booking works and where we go. Straight answers from Quick Haul.

### Inner banner
- Headline: Questions / **answered**
- Lede: Prices, booking and what we take. Can't find yours? Give us a call on (603) 555-0142†.

### Accordion: pricing
- How much does junk removal cost? / You pay for how much of the truck your junk fills. A 1/8 truck is $149†, a 1/4 truck $249†, a 1/2 truck $399† and a full truck $649†. Loading, hauling and drop-off are included.†
- What if I'm not sure how much I have? / Pick the closest size when you book and add a few photos. We'll confirm the price before the day.
- Can the price change on the day? / Only if the job is different from what we agreed, like extra items or heavy material we didn't know about. If it does, we tell you before we load anything.†
- How much for just one item? / A single item is priced as a 1/8 load, $149†.
- How is demo priced? / Every demo job is different, so we price it per job. Send photos with your booking or call us and we'll talk it through.†

### Accordion: what we take
- What do you take? / Furniture, appliances, mattresses, household junk, garage and basement clutter, yard waste and demo debris. The full list is on our services page.
- What don't you take? / Paint, oil and chemicals, propane tanks, asbestos, medical waste and car batteries.† Not sure about something? Ask us.
- Do you donate things? / Yes, where we can. Tell us what's still good when you book and we'll take it to a local charity or reuse store instead of the dump.†
- Do I need to carry anything outside? / No. We carry it out from wherever it is, including basements and upstairs rooms.†

### Accordion: booking
- How does booking work? / Pick your town, your load and a day online, add photos if you can, and send it. Shawn looks over every booking and gets back to you to confirm the time and the price.†
- Can I just call instead? / Yes, any time. Call (603) 555-0142†, Mon to Sat, 7am to 7pm†, and we'll book it with you on the phone.
- How soon can you come? / Check the calendar for the next open days. If you need it sooner, call us and we'll see what we can do.
- Do I need to be home? / Not always. If the junk is outside and the price is agreed, we can do the job while you're out. Tell us when you book.†
- Can I change or cancel my booking? / Yes. Call us at least a day ahead and we'll move it or cancel it.†
- Do you come to my town? / We cover towns across Massachusetts and New Hampshire. Type yours into the booking form to check, or see the full list on our service area page.

### Accordion: paying
- When do I pay? / When the job's done, before we drive off.† 
- How can I pay? / Card or cash.†

### Close
- Line: Still have a question? Give us a call (603) 555-0142†
- Button: Book now

---

## Contact
- Meta title: Contact Quick Haul | Junk Removal Quotes in MA and NH
- Meta description: Call, email or send us a quick request for a junk removal or demo price. Quick Haul works towns across Massachusetts and New Hampshire, Mon to Sat.

### Inner banner
- Headline: Call, book / **or ask**
- Lede: The fastest way to a price is a call. If you'd rather write it down, send us a request and we'll get back to you.

### Contact cells
- Label: Phone. Value: (603) 555-0142†. Line: Need help booking or have questions? Give us a call.
- Label: Email. Value: quickhaul@example.com†
- Label: Hours. Value: Mon to Sat, 7am to 7pm†. Line: Closed Sundays.†
- Label: Where we go. Value: Towns across Massachusetts and New Hampshire. Link: See the full list

### Map
- Accessible title: Map of the towns Quick Haul covers in Massachusetts and New Hampshire
- Map centre: Salem, NH† (base town placeholder)

### Quote request form
- Form heading: Ask for a price
- Label: Your name
- Label: Phone
- Label: Email
- Label: Your town
- Label: What do you need gone
  - Field hint: For example: clearing out a two-car garage, or one old fridge in the basement
- Label: Add photos (optional)
  - Helper: Photos help us give you a real price instead of a guess.
- Label: How should we get back to you
  - Chips: Call; Text; Email
- Button: Send my request
- Success: Got it. We'll get back to you with a price soon. Need it faster? Call (603) 555-0142†.
- Errors: Add your name; Add a phone number or email so we can reach you; Tell us a little about the job
- Small print: We only use your details to answer your request. Read our privacy policy.

### Commercial link (a ruled cell under the form)
- Label: Landlords, realtors and property managers†
- Body: Turnovers, move-outs and regular pickups have their own form.
- Link: Send a commercial enquiry

---

## Service area (hub)
- Meta title: Junk Removal Service Area: MA and NH Towns | Quick Haul
- Meta description: See every Massachusetts and New Hampshire town Quick Haul covers, with prices from $149. Can't see yours? Call us.

### Inner banner
- Headline: Where / **we go**
- Lede: Towns on both sides of the Massachusetts and New Hampshire line†, all at the same prices.

### Town list
- Label: Massachusetts. Towns†: Andover; Dracut; Haverhill; Lawrence; Lowell; Methuen
- Label: New Hampshire. Towns†: Derry; Hudson; Londonderry; Nashua; Pelham; Salem
- Each town links to its town page.
- Closing cell: Can't see your town? Call us. If we can get to you, we'll tell you the price on the phone. / Call (603) 555-0142†

### Map
- Accessible title: Map of the towns Quick Haul covers in Massachusetts and New Hampshire

---

## Service-area page (one template per town)
Written here for Lowell, MA. Every other town page uses the same copy with its own town and state. Fields that change: town, state, state abbreviation. Nothing else changes, and no local claims are added per town until Shawn gives them.
- Meta title: Junk Removal in Lowell, MA | Quick Haul
- Meta description: Junk removal, clean outs, furniture, appliance, mattress and yard waste pickup, plus demo, in Lowell, MA. Prices from $149. Book a day online or call.

### Inner banner
- Headline: Junk removal in / **Lowell, MA**
- Lede: Clean outs, single items, yard waste and demo work in Lowell. Pick your load and a day below, or give us a call.

### Ticket (town pre-filled)
- Same copy as the homepage ticket, with the town field filled and the note: Yes, we come to Lowell, MA.

### Services in town
- Headline: What we haul / **in Lowell**
- Body: Garage and basement clean outs, furniture, appliances, mattresses, yard waste and demo projects. We come to Lowell with the truck, load everything ourselves and haul it away, with the good stuff going to donation where we can.† Prices start at $149† for a 1/8 truck, and you'll know your price before the day.
- Text link: See everything we take
- Button: Book in Lowell

### Price cards
- Same four cards as the Services pricing section.

### Reviews from this town
- Built only when real Facebook reviews from this town exist. No sample cards on town pages.

---

## Commercial enquiry
Shawn has not said he does commercial or repeat work (brief section 2). The whole page is placeholder wording, must-confirm, and invites an enquiry without claiming a track record.
- Meta title: Commercial and Repeat Junk Removal | Quick Haul
- Meta description: Landlords, realtors and property managers: tell us about turnovers, move-outs or regular pickups across Massachusetts and New Hampshire.

### Inner banner
- Headline: Landlords, realtors / **and property managers**
- Lede: Turnovers, move-outs and regular pickups. Tell us about the property and we'll get back to you with a plan and a price.†

### Enquiry form
- Label: Your name
- Label: Company (optional)
- Label: You are
  - Chips: Landlord; Realtor; Property manager; Contractor; Other
- Label: Phone
- Label: Email
- Label: Property address or town
- Label: One job or regular
  - Chips: One job; Regular pickups
- Label: How often (shows for regular pickups)
  - Chips: Weekly; Every two weeks; Monthly; As needed
- Label: Tell us about the job
  - Field hint: For example: unit turnover, tenant left furniture and a full basement
- Label: Add photos (optional)
- Button: Send enquiry
- Success: Thanks, we've got it. We'll get back to you to talk it through. Need it sooner? Call (603) 555-0142†.
- Small print: We only use your details to answer your enquiry. Read our privacy policy.

---

## 404
- Meta title: Page Not Found | Quick Haul
- Meta description: (none; noindex)
- Headline: Nothing / **to haul here**
- Body: This page is empty, like the truck after a drop-off. It may have moved, or the link was typed wrong.
- Button: Book now
- Links: Home; Services; Pricing; Contact
- Drawing (empty truck bed): decorative, no alt.

---

## Privacy policy
Plain-language draft for structure. It must be checked against the plugins and services actually used (booking plugin, SMS provider, analytics, form spam protection) and reviewed by someone qualified before launch. Business name and contact details are placeholders.
- Meta title: Privacy Policy | Quick Haul
- Meta description: How Quick Haul collects and uses your details when you book, ask for a price or visit the site.
- Headline: Privacy / **policy**
- Sections:
  - What we collect. When you book or ask for a price, we collect your name, phone number, email, the pickup address, details about the job and any photos you upload. When you visit the site, we collect basic analytics like which pages are viewed.
  - Why we collect it. To confirm and carry out your booking, to give you a price, to send booking confirmations and reminders, and to understand how people use the site so we can improve it.
  - Text messages. If you tick the box, we text you booking updates and a reminder. Message and data rates may apply. Reply STOP to opt out at any time.
  - Who we share it with. Only the services that run the site, the booking calendar, email and text messages. We don't sell your details.
  - How long we keep it. As long as we need it for your booking and our records, then we delete it.
  - Your choices. Ask us to see, correct or delete your details at any time.
  - Contact. Quick Haul, quickhaul@example.com†, (603) 555-0142†.
  - Last updated. The launch date.

---

## Questions for the client
Everything here is either a placeholder in this file (and in content/placeholders.md) or something the copy deliberately leaves out. Most important first.
1. Phone, hours, base town and the full town list. Is Sunday a working day? Do prices change for towns further out?
2. Prices. Will they go on the site? What are the real bands, is there a minimum or single-item price, what does each band hold in your truck, and what costs extra (heavy material, appliances with refrigerant, stairs)?
3. Booking. Should a booked slot be a request you confirm, or confirmed straight away? What time windows do you offer? Can customers be out during the job? What is your change and cancel rule? When and how do customers pay?
4. Licensed, insured, guaranteed. Which are true, and in which states? The trust cells for these are written but held.
5. Your story. When did you start, who is on the crew, and are you happy for your first name to be used on the About page? We need a photo of you, or of you with the truck.
6. What you take and don't take. Please check both lists, and the electronics and TV line in particular. Do you disconnect appliances, or only take ones already unhooked?
7. Demo. What size of job do you take on (sheds, decks, kitchens, anything structural)? How do you price it?
8. Donations. Do you take usable items to charity? Which ones, and what won't they accept?
9. Commercial and repeat work. Do you do it, and for whom? The commercial page is placeholder until you say yes.
10. Facebook, Instagram and TikTok links, and which Facebook reviews you want on the site. No real reviews or ratings go up until then.
11. Photos. Your own job photos, especially before and after pairs from the same spot, to replace the stock images.

## Left out on purpose
- No review quotes, star ratings or review counts. The proposal (term 05) rules out any rating that hasn't been earned, and none have been supplied.
- No licence, insurance or guarantee claims in any built copy. Written and held only.
- No years-in-business or crew-size claims outside the About page and the held footer fact line, both marked.
- No named charities or partners. Naming a real organisation would be a claim about a real business.
- No response-time promises ("within an hour", "same day"), no "no hidden fees" claim and no eco or recycling percentages. Nothing in the material supports them.
- No blog or scrap talk, as Shawn asked.
