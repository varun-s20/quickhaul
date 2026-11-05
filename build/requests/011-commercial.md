# Request 011: Commercial, the regular-pickups fields
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs requests 002 (`truck-banner-full`, `.-short`, `.a-hero.-long`), 003 and 010. Page source: site/src/pages-v2/commercial.body.html.

## What is needed
1. Two small rules for "How often", which shows only for regular pickups.
2. `.t-commercial` in the page scope rule.
3. A decision to note: revision.md disagrees with itself on this page's truck.

## Why
- The script's "Commercial: How often shows only for regular pickups" block reads `[data-rhythm-often]` and works as it is. It takes the height from `often.parentNode`'s row gap, so the wrapper needs to be a flex column with a gap. The show and hide rules were `.o-enquiry__rhythm` and `.o-enquiry__often`, which retire.
- revision.md section 5 says "Only Home's truck is piled high" and section 6's truck table says "Piled high is Home's alone" for inner banners, but the same table's Commercial row says "truck-full parked on a photo", and copy.md gives a label for it: "The Quick Haul truck with a full load, parked on the street". I followed the two that name this page, so it is the one inner banner with a pile. To change it, swap the block in the page for `{{> truck-banner}}` (half a load) and take the `truck-banner-full` lines out of request 002. copy.md's label would need to change with it.

## Exact change

### site/assets/global.css: after the request-form rules from request 010
```css
/* One job or regular, and How often under it. A flex column with a gap: the script takes the gap back as How often closes (global.js, "How often shows only for regular pickups") */
.m-form__rhythm { display: flex; flex-direction: column; gap: var(--s-5); grid-column: 1 / -1; }
.js .m-form__often { display: none; }
.js .m-form__often.is-open { display: block; }
```

### site/assets/global.css: the page scope rule
Add `.t-commercial`.

### When Commercial moves in
Take `commercial` off LEGACY_PAGES. With Contact also moved, delete the `.t-legacy` copies of `.m-field*`, `.m-check*`, `.m-upload*`, and the old `.o-contactForm*` and `.o-enquiry*` rules. Delete the `commercial-art` partial and the `banner-art-commercial` block (request 014).

## Checks P2 has to run
- Pick Regular pickups, then One job, then Regular pickups again: How often eases in and out, its choice comes back, and it stays out of the send while hidden.
- `.m-form__help`: "Phone or email is enough." has to read as belonging to both fields above it, and error messages under them push it down rather than overlap it.
- The field names in site/README.md (when it's written): name, company, role, phone, email, property, job_type, frequency, job, photos.

## Other pages this touches
None.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written (CSS lifted from this file by script). Taking Commercial off LEGACY_PAGES and deleting the old rules stay with the move-in and request 014. The truck decision in this request stands: `truck-banner-full` is built, so this is the one inner banner with a pile.
- Real site: check.py PASS on 24 pages, build.py --check up to date. Home, old Commercial and old Contact 0.0% changed in full-page shots at 1440 and 390. Old Commercial's computed styles identical with and without the new rules (build/tmp/v3/leak.py, 0 differences).
- Staged Commercial in a scratch copy: build and check.py PASS. tools/qa.py without the tab pass: no overflow, console or reveal problems, 79 words until Regular pickups is picked (target about 80).
- build/tmp/v3/flow_trial_commercial.py at 1440 and 390, 0 failures: How often is hidden and disabled at rest, eases in and out, Weekly comes back when Regular pickups is picked again, and `frequency` stays out of the send while hidden. Empty send: three messages, and the help line sits under the error (12px at 1440). A stubbed send shows the thanks with the form gone (uses request 010's `.m-form[hidden]`). No endpoint keeps the fields and shows the failed state.
- Note for anyone writing a browser test here: the radio lies over its face, and the face's press scale puts it on top mid-press, so Playwright's own click refuses both. A real mouse at the chip's centre works, and the test does that.
- Read fine by eye at 1440: "Phone or email is enough." reads as belonging to both fields, with or without errors.
- At 390x844 the sentence is 3.9:1 and at 320x640 3.73:1, under the 4.5 target. Handled in the banners pass after request 013.
- Not run here, for P2: the page's tab pass and Critic round. site/README.md's field names wait for that file.
