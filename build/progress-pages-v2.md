# Pages session, rebuild in the revised design: notes
Owner: pages session (build/COORDINATION.md). Started 2026-11-05. A fresh session resumes from here.

## How to resume
- Read build/COORDINATION.md first. Phase P1 only writes staged sources: no build, no browser, no QA, no Critic, nothing outside this session's own files.
- Staged pages: site/src/pages-v2/<slug>.body.html. The town template: site/src/pages-v2/_templates/town.body.html (it goes to src/templates/, never src/pages/, or build.py would make a town.html). Staged data: site/src/pages-v2/_data/.
- Words: content/copy.md, word for word. Structure: design/revision.md section 4 and 5, prototype/revision/.
- Shared needs go in build/requests/NNN-<page>.md.

## Phase P1 checklist, in the agreed order
- [x] Services
- [x] Book
- [x] Service area hub
- [x] Town template
- [x] Reviews
- [x] About
- [x] Donate
- [x] FAQ
- [x] Contact
- [x] Commercial
- [x] 404
- [x] Privacy

## Page notes

### Services
- Source: site/src/pages-v2/services.body.html. Request 001.
- Structure is the prototype's, every word is copy.md's. The four spots copy-changes.md lists as differing from the prototype are in: junk removal line, yard waste line and link, pricing line, can't-take line.
- Changes from the prototype, and why:
  - Book links name their job: `book.html?job=junk-removal` and so on (copy-changes.md, For the Developer, point 1). The form's values are junk-removal, clean-out, furniture, appliances, mattresses, yard-waste, demo.
  - Dropped `-last` on the two-card band and `m-promo__lede` on the promo line: neither class has a rule in the prototype or the site.
  - The row of four loads is a generated block, `price-row`, not typed markup, so it can't drift from data/prices.json.
  - og:image is assets/images/home/og-home.jpg, not the old square crop, since the old crops go with the old pages.
- Class check against global.css's new part: only `t-services` is missing (request 001).

### Book
- Source: site/src/pages-v2/book.body.html. Requests 002 (short and no-truck banner), 003 (everything else).
- Three small facts sit at the top of the form's band, so the page stays two bands (revision.md's table).
- My calls, all easy to reverse:
  - **Short banner.** revision.md names FAQ, Contact and Commercial for it, not Book. Book is a utility page and the form is what the visitor came for; at 520px the first field falls under the fold at 1440x900 (worked out, not measured).
  - **"Not sure" sits beside the long pill, not in it.** copy.md lists it as a fifth stop. The pill reads as one scale from a little to a lot, and "Not sure" isn't on that scale. It's still the same radio group, and it means no fifth stop squeezing the pill at 390.
  - **The square bullet on `.a-label` goes.** revision.md keeps "the ruling and mono labels" here; square bullets are on its retired list and not on its kept list.
  - **Inputs get round corners and Bio Sans,** even on this page. Square frames and mono body text retire site-wide; only the hairlines and mono labels were kept.
  - **Empty truck is decorative** while nothing is picked or "Not sure" is on (aria-hidden). copy.md has no label for that state, and it treats the 404's empty truck as decorative.
- Facts in the markup that changed from the old page: progress line is Day, Load, Address, Your details. "Next: your address" replaces "Next: address and details". Nothing is preselected on the load step. Email has two errors.
- Without JS every step shows with a native date field, as before. The truck then shows a 1/8 load beside "Pick a size to see the price", since only the script can empty it. Acceptable for the no-JS case; noted so nobody reads it as a bug.
- Removed `data-book-sheet` and `data-book-daycell`: nothing reads them.

### Service area hub
- Source: site/src/pages-v2/service-area.body.html. Requests 002 and 004.
- Recipe: Home's towns promo with the map in the photo's place. copy.md's words only.
- copy.md's Truck labels has no line for the hub. I used the town pages' quarter load and label, since the hub leads to them. Flagged to Varun.

### Town template
- Source: site/src/pages-v2/_templates/town.body.html. Requests 001, 002, 005.
- Town tile links go to Services' anchors, as Home's do.
- My call: a slim light strip after the price row, holding "See other towns", so the trucks have a fold and the two slate bands don't run together (request 005 explains it and how to undo it).

### Reviews
- Sources: site/src/pages-v2/reviews.body.html, site/src/pages-v2/_data/reviews.json. Requests 002 and 006.
- copy.md doesn't name the grid's photos. I picked three already on the site, with copy.md's alts: orange truck, white pickup, man with a mattress. Each is placed away from the sample card about the same job. Flagged to Varun.
- Grid cards carry Home's initials avatar ("SR", decorative), for the same slots as Home's card. copy.md's Reviews section doesn't list one, but Home's says real reviews "fill the same slots".
- The garage pair reuses Home's compare-before and compare-after: copy.md gives them the same alts, and those crops are the tuned ones. The other pairs use the old square crops.
- Pair alts are copy.md's, minus the sentence-ending stop, matching Home's.
- "Book now" sits under the band's line, not after the pairs (the old page's critic note, kept in the comment).
- `o-svcBand` is reused for "a cream band after a cream band" (padding-top 0). Same on About.

### About
- Source: site/src/pages-v2/about.body.html. Requests 002, 003, 007.
- Story is copy.md's, 60 words, in one `.a-lede`. One action in the band: the call. Book now is left to the estimate band.
- The call pill carries `data-call-here`, as copy-changes.md asks. Existing script handles it on a mid-page pill, but check on the page.
- og:image is the shared og-home, not the driveway photo, because of the badges below.
- **Open for Varun:** the driveway photo shows Chevrolet badges that can't be cropped out (request 007, placeholders-add-pages.md). Used as copy.md names it; not re-cut.

### Donate
- Source: site/src/pages-v2/donate.body.html. Requests 002 and 008.
- Heading "What we can donate" at the full-band size (88px), since the band spans the width.
- Band line: copy.md's sentence is two sentences and they're both in. "Not these" is `.m-fact__title` over the marked list.
- Own estimate band in the page body, with `estimate: no`. Reasoning in request 008. Means the band sits inside `<main>` on this one page; only word counts care.
- Photo is the square crop that already exists, so no new crop is needed.

### FAQ
- Sources: site/src/pages-v2/faq.body.html, site/src/pages-v2/_data/faq.json. Requests 002 and 009.
- My call: built with the seated cards rather than waiting to see it flat, since this phase has no browser. Request 009 says how to drop them. Flagged to Varun, since his "drawn items" answer named only two bands.
- Questions and answers are copy.md's, unchanged. Copy.md marks "give us a call" in the banner line with no link note; I linked it to the phone as on every other line, with the same words.
- The FAQ's `id`s stay on the groups, though the jump strip is cut, so a deep link can still land on a group.

### Contact
- Source: site/src/pages-v2/contact.body.html. Requests 002, 003, 004, 010.
- Pill is `-glass`, as revision.md section 7 says for Contact. `data-call-here` is on its wrapper, as Home's is.
- Map and hours has no heading in copy.md, so the section takes `aria-label="Map and hours"` and the two facts carry a bigger size. It may read thin at 1440; judge it in P2.
- Form states: "Got / it" and "Something / went wrong" use `.a-section -card` as h3s under the band's h2. The failed state is inside the form so it sits right under the send.
- Commercial's line is copy.md's. The old page's "Send a commercial enquiry" pill is now the link "Ask about commercial work".

### Commercial
- Source: site/src/pages-v2/commercial.body.html. Requests 002, 003, 010, 011.
- Field ids changed from enquiry-* to commercial-*, because copy.md now says "request". Field names are unchanged, so nothing downstream moves.
- "Phone or email is enough." is one helper under both fields, tied to both by aria-describedby. The JS change in request 003 lets a field name its error first and a helper second.
- Full-load truck on the banner: revision.md contradicts itself; request 011 says why I followed the table and copy.md.

### 404
- Source: site/src/pages-v2/404.body.html. Requests 002 and 012.
- Three links go in a slim rising band of chips, the Services index's own markup. That band also gives the truck its fold, so nothing new is built.
- "drop-off" is held with `.a-nowrap`, as the old page held it.
- No description in the meta, on purpose: copy.md gives it none and it's noindex.

### Privacy
- Source: site/src/pages-v2/privacy.body.html. Request 013.
- Heading is an h1 in `.a-section -small`, since this page has no banner.
- Copy.md's three small fixes are in (the checkbox wording and analytics in who we share with). "Last updated" stays off as a CLIENT COPY REQUIRED comment.
- `estimate: no`; see request 013.

## Phase P1 result (2026-11-05): stopped after the last page
All 12 sources are staged. **Nothing has been built or seen in a browser.** No build.py, images.py, QA or Critic ran, as gate 1 requires.

What I did check, read-only, against my own files, with inline scripts that wrote nothing:
- Every visible string, alt, label and error, against copy.md, both directions. No invented or missing copy left. The FAQ section's made-up accessible name was removed. "More pages" comes from conventions. The calendar's Sun to Sat labels are carried over from the old page (aria-hidden).
- Every class, against global.css's new part plus the CSS in the requests. Found and fixed two with no rule: `.m-fact` (Home has this gap too) and `.o-reviewPairs__pair`.
- Every block is in BLOCKS or a request. Every picture name is in image-manifest.json. One h1 per page, no duplicate ids, no dangling aria references, no em dashes, no inline styles.

These text checks don't prove the pages render. The Python in the requests has never been run, and every CSS value in them is unmeasured.

### Staged files
- site/src/pages-v2/: services, book, service-area, reviews, about, donate, faq, contact, commercial, 404, privacy (.body.html)
- site/src/pages-v2/_templates/town.body.html
- site/src/pages-v2/_data/: reviews.json, faq.json (replace site/data/'s when their page moves in)
- No schema file changed: services.json, faq.json, contact.json, town.json and page.json still fit, so none is staged. prices.json and towns.json aren't staged either; request 014 trims them at the end, because old pages read `fill` until then.

### Invented blocks and classes
Every one is in a request. Blocks: price-row, truck-banner and its five variants (eighth, quarter, full, empty, donate), load-radios, facebook-url. New markup for existing blocks: town-list, review-grid, faq-groups. Classes: request files 001 to 013, in fenced CSS.

## What phase P2 needs
1. **The go-ahead:** the homepage session finished, shared parts declared frozen (gate 2). Only one session builds at a time. This session's port is 8841.
2. **Requests applied in number order,** each with its checks rerun on the pages it names. 002 and 003 are the big ones: 003 touches Home (reset, load_radios, gauge script) and 006 touches Home (slider script).
3. **Suggested batches.** Each moves its staged page, takes it off LEGACY_PAGES, then build, check, QA and Critic per page:
   - Services (001)
   - Book (002, 003)
   - Service area hub and town template (004, 005). The template goes to src/templates/.
   - Reviews, with _data/reviews.json (006)
   - About (007), Donate (008)
   - FAQ, with _data/faq.json (009)
   - Contact (010), Commercial (011)
   - 404 (012), Privacy (013)
   - Then cleanup (014)
4. **`tools/build_trucks.py` has to run** after request 002, before any banner that uses a new truck. It needs Pillow, which is already in use for the door decal.
5. **Measurements only a browser can give:** scrim sampled on each banner, the words against the truck (Donate and Londonderry, NH first), word counts against revision.md, the short banner's real height, the crops in new slots (town tiles, Reviews' pairs at 4/3).
6. **Merges by the shared-parts owner:** content/placeholders-add-pages.md into content/placeholders.md, logs/review-pages-v2.md into review-log.md, these notes into build/progress.md. Also the "must log" table in revision.md section 7, if the homepage session hasn't.
7. **site/README.md** needs the new form field names (requests 010 and 011 list them).

### Calls for Varun, none blocking
1. **About's photo** shows Chevrolet badges that can't be cropped out: replace, paint out or wait for Shawn's?
2. **Same street photo on every banner,** as copy.md says, including 12 town pages that aren't that street. More photos would mean more downloads and scrims.
3. **FAQ uses drawn items on seated cards,** ahead of seeing it flat. His answer on drawn items named only the review and can't-take bands.
4. **A slim strip on town pages** that holds "See other towns" and gives the trucks a fold. Otherwise the trucks stand on slate with no fold.
5. **Commercial's banner truck is a full load.** revision.md says both ways, and copy.md says full.
6. **Book's banner is short and "Not sure" sits beside the long pill,** my reading of what the page needs.
7. **Hub banner's truck has no line in copy.md.** I used the town pages' quarter load and label. The Copywriter may want to add it.
