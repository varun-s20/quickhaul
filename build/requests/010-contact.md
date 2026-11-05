# Request 010: Contact, the request form
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs requests 002, 003 and 004. Page source: site/src/pages-v2/contact.body.html.

## What is needed
1. Request-form CSS, shared with Commercial (`.m-field__label`, `.m-form`, `.m-form__chips`, `.m-form__foot`, `.m-formState`).
2. Contact's small page rules (`.o-contactFacts`, `.o-contactMore`).
3. One line in the request-form script, so the keep-the-label-clear scroll finds the new label.
4. `.t-contact` in the page scope rule.

CSS values are not measured. P2 checks them.

## Why
- revision.md, Contact: "Short banner with the call pill. Map with hours beside it. Short form. Merge: Commercial cell into one line and a link. Cut: Contact cells that repeat the footer. Line art."
- "The ruling and mono labels can stay here [Book], and only here." So this form gets plain Bio Sans labels and no hairlines. The old `.o-contactForm*` and `.o-enquiry*` were both built on ruled cells, so both retire. `.a-label` stays Book's.
- The map and hours use the hub's promo-with-a-map recipe (request 004). Two small facts look small on a 520px card, so they step up a size here.

## Exact change

### site/assets/global.css: in "Inner pages", after the form parts from request 003
```css
/* ---- request forms (Contact and Commercial): the same field parts as Book, with no ruling. Plain labels, two columns from tablets, one axis with the heading ---- */
.m-field__label { display: block; margin-bottom: var(--s-2); font: var(--w-semi) 1.6rem/1.3 var(--f-body); }
.m-form { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--s-5); max-width: 96rem; margin: 0 auto; }
.m-form__chips { display: flex; flex-wrap: wrap; gap: var(--s-2); }
.m-form__chips .a-choice__face { min-height: var(--h-button); padding: 0 var(--s-4); font-size: 1.5rem; }
.m-form__help { grid-column: 1 / -1; margin-top: calc(var(--s-3) * -1); }
.m-form__foot { display: flex; flex-direction: column; gap: var(--s-4); grid-column: 1 / -1; }
.m-form__foot .a-button { width: 100%; }
/* What follows a send, on the same axis. In the form on failure, so what was typed stays above it; under it on success, when the form has gone */
.m-formState { grid-column: 1 / -1; max-width: 96rem; margin: 0 auto; text-align: center; }
.m-formState:focus { outline: 0; }
@media (min-width: 641px) {
  .m-form { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .m-form__foot { flex-direction: row; align-items: center; justify-content: space-between; gap: var(--s-5); }
  .m-form__foot .a-button { flex: none; width: auto; }
}

/* ---- Contact ---- */
.o-contactFacts { display: grid; gap: var(--s-6); }
.o-contactFacts .m-fact__title { font-size: 2.4rem; }
.o-contactFacts .m-fact__text { margin-top: var(--s-1); font-size: 1.8rem; }
.o-contactFacts .a-link { margin-top: var(--s-2); }
.o-contactMore { max-width: 72rem; margin: var(--s-7) auto 0; text-align: center; text-wrap: balance; }
```

### site/assets/global.css: the page scope rule
Add `.t-contact`.

### site/assets/global.js: Request forms block, in the focusin handler
```js
      var label = field && $('.a-label, .m-field__label', field);
```

### When Contact moves in
Take `contact` off LEGACY_PAGES. `contact.json` is unchanged.

## Checks P2 has to run
- Send with nothing filled in, then with an empty phone and email: both fields marked, one message. Send with a mistyped email.
- With no endpoint, a send shows the failed state and keeps the fields filled.
- The number once per screen: the banner's pill in view, then scrolled away.
- The pill beside the truck on a short banner at 1025 to 1240 and on phones.

## Other pages this touches
Commercial reuses all of the form CSS (request 011). Book doesn't use it, except the shared parts from request 003.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written (CSS lifted from this file by script), with two rules added after trying it. Taking Contact off LEGACY_PAGES stays with the move-in.
- **Bug found and fixed: `.m-form[hidden] { display: none; }`.** The grid on `.m-form` outranks the browser's own `[hidden]`, so after a successful send the whole form stayed on screen under "Got it". The stubbed endpoint test caught it. Commercial gets the fix too.
- **`.m-formState` gets `scroll-margin-top: var(--s-6)`.** "Got it" is scrolled to the top on success and landed 2px under the logo. Now y 118 at 1440 and y 94 at 390, about 30px under the bar.

Checks:
- Real site: check.py PASS on 24 pages, build.py --check up to date. Home, old Contact, old Commercial and old Book 0.0% changed in full-page shots at 1440 and 390. Computed styles on the three old form pages identical with and without the block, with Book's hidden steps opened (build/tmp/v3/leak.py, 0 differences). No page on the real site prints the two added rules' classes yet.
- Staged Contact in a scratch copy: build and check.py PASS. tools/qa.py without the tab pass: no overflow, console or reveal problems, 120 words at both widths (target about 110). Its one list of short targets is the map's mouse links, 36px, which stay mouse-only by the old Service area decision.
- build/tmp/v3/flow_trial_contact.py at 1440 and 390, 0 failures: empty send gives three messages with phone and email both marked and one message between them; a mistyped email; no endpoint keeps the fields filled, shows the failed state, focuses it, and shows no success; reply chips move by arrows; the header number and the phone's call bar hide while the banner's pill is in view and come back past it; with a stubbed endpoint the photo field shows, then "Got it", with the form gone.
- States read fine by eye at 1440 and 390. Banner at 1240 and 1025: the pill shows icon and number only, as Home's does in landscape, with no collision with the truck. banner_check.py flags "logo" at 1025 to 1240 because the headline's line box starts level with the logo's foot. The painted letters clear it by about 15px or more in the shots, so nothing is touching.
- At 320x640 the sentence is 3.78:1, under 4.5. Handled in the banners pass after request 013.
- Not run here, for P2: the page's tab pass and Critic round.
