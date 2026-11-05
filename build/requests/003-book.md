# Request 003: Book, the form parts, its load step and states
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs request 002. Page source: site/src/pages-v2/book.body.html.

## What is needed
1. Reset additions, because the new reset leaves out h3, ol, dl, dd and legend.
2. The shared form parts lifted out of OLD INNER PAGES and restyled to the new look (`.m-field`, `.m-check`, `.m-upload`). Contact and Commercial use them too (requests 010 and 011).
3. A chip for light grounds (`.a-choice.-light`), a light load picker (`.m-loadPicker.-light`) and small facts in a row (`.m-factRow`).
4. Book's own sheet lifted out of OLD INNER PAGES, and `.t-book`.
5. A `load-radios` block, shared with Home's picker.
6. Script changes: copy.md's three no-price states, the new prefill, Try again, the default town note, a second email error, and Remove beside each file.

Values are carried over from the old rules or from the prototype's matching parts. None is measured. P2 checks them at 1440 and 390.

## Why
- copy.md's Book has words the old page never had: "Pick a size to see the price.", the "Not sure" and Demo lines, "Add your email", "Remove", "Try again", the town note before typing (copy-changes.md, For the Developer, point 4).
- revision.md: "The ruling and mono labels can stay here, and only here." Square bullets are on the retired list and not on the kept list, so `.a-label` keeps its mono caps and loses the bullet. Square frames retire too, so the sheet and the fields get round corners; the hairlines inside stay.
- Roboto Mono as body text is retired (revision.md section 1), so fields and helpers go to Bio Sans here as well. Phone numbers stay mono.

## Exact change

### site/assets/global.css: Reset. Replace these two lines and the input line
```css
h1, h2, h3, p, ul, ol, dl, dd, figure, blockquote, fieldset, legend { margin: 0; padding: 0; border: 0; }
ul, ol { list-style: none; }
button, input, textarea { font: inherit; color: inherit; }
```
Also add `fieldset { min-width: 0; }` beside them, so a long chip row can't widen its fieldset.

### site/assets/global.css: "Atoms", right after the `.a-choice` block
```css
/* A chip on cream: steel outline and ink text, like a link chip. The picked one fills with slate. The same real radio underneath */
.a-choice.-light .a-choice__face { box-shadow: inset 0 0 0 1px var(--c-steel); color: var(--c-ink); }
.a-choice.-light .a-choice__input:checked + .a-choice__face { background: var(--c-slate); box-shadow: none; color: var(--c-cream); }
@media (hover: hover) and (any-pointer: fine) { .a-choice.-light:hover .a-choice__input:not(:checked) + .a-choice__face { box-shadow: inset 0 0 0 2px var(--c-slate); } }
```

### site/assets/global.css: right after the `.m-loadPicker` rules
```css
/* Book's picker, on cream: the same pill and the same sliding ring, in slate. Level 0 is nothing picked, or "Not sure", which sits outside the pill */
.m-loadPicker.-light { box-shadow: inset 0 0 0 1px var(--c-steel); }
.m-loadPicker.-light .a-choice__face { color: var(--c-ink); }
.m-loadPicker.-light .a-choice__input:checked + .a-choice__face { background: rgba(52, 61, 78, .1); box-shadow: inset 0 0 0 2px var(--c-slate); }
.js .m-loadPicker.-light .a-choice__input:checked + .a-choice__face { background: none; box-shadow: none; }
.js .m-loadPicker.-light .m-loadPicker__thumb { background: rgba(52, 61, 78, .1); box-shadow: inset 0 0 0 2px var(--c-slate); }
.m-loadPicker[data-level="0"] .m-loadPicker__thumb { opacity: 0; }
@media (hover: hover) and (any-pointer: fine) { .m-loadPicker.-light .a-choice:hover .a-choice__input:not(:checked) + .a-choice__face { box-shadow: inset 0 0 0 1px var(--c-slate); } }
```

### site/assets/global.css: right after `.m-fact__text`
```css
/* .m-fact has no rule of its own in the new part of the file, only its title and text do. Home prints it too, and check.py fails on it once OLD INNER PAGES goes */
.m-fact { min-width: 0; }
/* Small facts in a row, on the page's one axis. The same two or three facts Home keeps in its estimate band */
.m-factRow { display: grid; gap: var(--s-4); max-width: 112rem; margin: 0 auto; text-align: center; }
@media (min-width: 641px) {
  .m-factRow.-three { grid-template-columns: repeat(3, 1fr); gap: var(--s-6); }
  .m-factRow.-two { grid-template-columns: repeat(2, 1fr); gap: var(--s-6); }
}
```

### site/assets/global.css: in "Inner pages", a new section after the page banner rules
`.a-button.-block` is new in this part of the file. Everything named here replaces its `.t-legacy` version: delete those from OLD INNER PAGES when Book moves in, except the rules Contact and Commercial still use while they wait (`.m-field*`, `.m-check*`, `.m-upload*` stay under `.t-legacy` until request 011 is done).
```css
/* ---- form parts: every form on the site. Bio Sans, round corners, 56px fields. "Optional" is written into the label (copy.md) ---- */
.a-button.-block { width: 100%; }
.m-field { min-width: 0; }
.m-field__input { display: block; width: 100%; min-height: var(--h-buttonLarge); padding: 0 var(--s-4); border: 0; border-radius: 1.2rem; background: transparent; box-shadow: inset 0 0 0 1px var(--c-steel); color: var(--c-ink); font: var(--w-body) 1.7rem/1.4 var(--f-body); transition: box-shadow var(--d-ui) var(--e-ui); }
.m-field__input::placeholder { color: var(--c-steel); font-size: 1.5rem; opacity: 1; }
.m-field__input:focus-visible { outline-offset: 2px; }
.m-field__input.-area { min-height: 11.2rem; padding: var(--s-3) var(--s-4); resize: vertical; }
.m-field__input[aria-invalid="true"], .m-field__input.is-also { box-shadow: inset 0 0 0 2px var(--c-ink); }
.m-field.-wide { grid-column: 1 / -1; }
.m-field__note { margin-top: var(--s-2); color: var(--c-steel); font: var(--w-body) 1.5rem/1.4 var(--f-body); text-wrap: pretty; }
.m-field__note.is-error { color: var(--c-ink); font-weight: var(--w-semi); }
.m-field__error { margin-top: var(--s-2); color: var(--c-ink); font: var(--w-semi) 1.5rem/1.4 var(--f-body); }
.m-field__small { color: var(--c-steel); font: var(--w-body) 1.4rem/1.45 var(--f-body); }
.m-check { position: relative; display: flex; gap: var(--s-3); min-height: 4.4rem; cursor: pointer; }
.m-check__input { position: absolute; top: 0; left: 0; width: 1px; height: 1px; opacity: 0; }
.m-check__box { position: relative; flex: none; width: 2.4rem; height: 2.4rem; border-radius: .6rem; box-shadow: inset 0 0 0 1px var(--c-slate); }
.m-check__input:checked + .m-check__box { background: var(--c-slate); }
.m-check__input:checked + .m-check__box::after { content: ""; position: absolute; top: .4rem; left: .75rem; width: .7rem; height: 1.2rem; border: solid var(--c-cream); border-width: 0 2px 2px 0; transform: rotate(45deg); }
.m-check__input:focus-visible + .m-check__box { outline: 2px solid var(--c-focus); outline-offset: 3px; }
.m-check__text { color: var(--c-steel); font: var(--w-body) 1.4rem/1.45 var(--f-body); text-wrap: pretty; }
.m-upload { position: relative; display: inline-block; cursor: pointer; }
.m-upload__input { position: absolute; top: 0; left: 0; width: 1px; height: 1px; opacity: 0; }
.m-upload__face { display: inline-flex; align-items: center; min-height: var(--h-button); padding: 0 2.4rem; border-radius: var(--r-pill); box-shadow: inset 0 0 0 1px var(--c-slate); color: var(--c-slate); font: var(--w-semi) var(--t-button)/1 var(--f-body); transition: background-color var(--d-ui) var(--e-ui); }
.m-upload__input:focus-visible + .m-upload__face { outline: 2px solid var(--c-focus); outline-offset: 3px; }
.m-upload__files { margin-top: var(--s-2); color: var(--c-ink); font: var(--w-body) 1.5rem/1.4 var(--f-body); overflow-wrap: anywhere; }
.m-upload__file { display: flex; align-items: center; justify-content: space-between; gap: var(--s-3); }
/* Beside its file name, 44px tall so a thumb can hit it */
.m-upload__remove { flex: none; min-height: var(--h-button); padding: 0 var(--s-2); font-weight: var(--w-semi); text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: .3rem; }
.m-upload__remove:active { transform: scale(.97); }
@media (hover: hover) and (any-pointer: fine) {
  .m-upload:hover .m-upload__face { background: rgba(52, 61, 78, .06); }
  .m-upload__remove:hover { text-decoration-color: transparent; }
}

/* ---- Book: the work order's one home (revision.md section 1). The hairlines and mono labels stay here, and only here, inside one round frame ---- */
.t-book { --c-line: rgba(15, 20, 28, .16); --cell: 1.6rem; }
.t-book .a-label { display: block; color: var(--c-steel); font: 500 1.2rem/1.4 var(--f-mono); letter-spacing: .08em; text-transform: uppercase; }
.t-book .m-field .a-label { margin-bottom: var(--s-2); }
.t-book .a-label.-legend { float: left; width: 100%; margin-bottom: var(--s-3); }
.o-bookBand { padding-top: var(--s-8); }
/* overflow clip, not hidden: hidden would make this box the sticky call line's scroller */
.o-book { display: grid; grid-template-columns: minmax(0, 1fr); max-width: 134.4rem; margin: var(--s-7) auto 0; overflow: clip; border-radius: var(--r-image); box-shadow: inset 0 0 0 1px var(--c-line); }
.o-book__main { display: flex; flex-direction: column; min-width: 0; }
.o-book__form:not([hidden]) { display: flex; flex: 1; flex-direction: column; }
.o-book__step:not([hidden]) { display: flex; flex: 1; flex-direction: column; }
.o-book__progress { position: relative; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-bottom: 1px solid var(--c-line); --done: .25; }
.o-book__progress::before { content: ""; position: absolute; right: 0; bottom: -1px; left: 0; height: 3px; background: var(--c-slate); transform: scaleX(var(--done)); transform-origin: 0 0; transition: transform var(--d-nudge) var(--e-out); }
.o-book__progressItem { display: flex; border-left: 1px solid var(--c-line); }
.o-book__progressItem:first-child { border-left: 0; }
.o-book__progressBtn { display: flex; align-items: center; width: 100%; min-height: 6.4rem; padding: var(--s-2); color: var(--c-steel); font: var(--w-semi) 1.2rem/1.2 var(--f-display); letter-spacing: var(--tr-nav); text-align: left; text-transform: uppercase; transition: background-color var(--d-ui) var(--e-ui); }
.o-book__progressBtn[aria-current="step"] { color: var(--c-ink); font-weight: var(--w-heavy); }
.o-book__progressBtn:disabled { font-weight: var(--w-light); cursor: default; }
.o-book__progressBtn:focus-visible { outline-offset: -4px; }
.o-book__step [data-book-heading]:focus { outline: 0; }
.o-book__cells { display: grid; flex: 1; grid-template-columns: minmax(0, 1fr); }
.o-book__cell { min-width: 0; padding: var(--s-5) var(--cell) var(--s-6); border-top: 1px solid var(--c-line); }
.o-book__cells .o-book__cell:first-child { border-top: 0; }
.o-book__cell.-column { display: flex; flex-direction: column; gap: var(--s-5); }
.o-book__cell.-fields { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--s-5); align-content: start; }
.o-book__group { min-width: 0; }
.o-book__group .m-loadPicker { clear: both; }
.o-book__chips { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .6rem; clear: both; }
.o-book__chips.-stack { grid-template-columns: minmax(0, 1fr); }
.o-book__chips.-five .a-choice:last-child { grid-column: 1 / -1; }
.o-book__chips.-seven .a-choice:first-child { grid-column: 1 / -1; }
@media (max-width: 640px) {
  .o-book__chips.-lead .a-choice:first-child { grid-column: 1 / -1; }
  .o-book__chips.-lead .a-choice:last-child { grid-column: auto; }
}
.o-book__chips .a-choice__face { min-width: 0; padding: 0 var(--s-2); font-size: 1.5rem; line-height: 1.2; text-align: center; white-space: normal; }
/* "Not sure" sits outside the pill: the pill is one scale, and this isn't on it */
.o-book__unsure { width: fit-content; margin-top: var(--s-2); clear: both; }
.o-book__unsure .a-choice__face { min-height: var(--h-button); font-size: 1.5rem; }
/* The drawing carries its own margin, so it overhangs its cell a little. It stands on its own contact shadow here, with no fold to park on */
.o-book__truck { margin-top: var(--s-4); }
.o-book__price { margin-top: var(--s-3); font: var(--w-heavy) 2.8rem/1.1 var(--f-display); text-wrap: balance; }
.o-book__price[hidden] { display: none; }
.o-book__foot { margin-top: auto; padding-top: var(--s-3); }
.o-book__foot .m-field__error { margin: 0 0 var(--s-3); }
.m-calendar__native { display: block; clear: both; width: 100%; min-height: var(--h-buttonLarge); padding: 0 var(--s-4); border: 0; border-radius: 1.2rem; background: transparent; box-shadow: inset 0 0 0 1px var(--c-steel); font: var(--w-body) 1.7rem/1 var(--f-body); }
.js .m-calendar__native { display: none; }
.m-calendar { display: none; clear: both; }
.js .m-calendar { display: block; }
.m-calendar__head { display: flex; align-items: center; justify-content: space-between; gap: var(--s-3); margin-bottom: var(--s-3); }
.m-calendar__title { font: var(--w-heavy) 2.2rem/1 var(--f-display); letter-spacing: .01em; text-transform: uppercase; }
.m-calendar__arrows { display: flex; gap: var(--s-1); }
/* Was .a-square. Round now: square frames retire (revision.md section 1) */
.m-calendar__arrow { display: grid; place-items: center; width: 4.4rem; height: 4.4rem; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--c-slate); transition: background-color var(--d-ui) var(--e-ui), color var(--d-ui) var(--e-ui), transform 160ms var(--e-out); }
.m-calendar__arrow.-prev .a-svg { transform: scaleX(-1); }
.m-calendar__arrow:disabled { opacity: .3; cursor: default; }
.m-calendar__arrow:active:not(:disabled) { transform: scale(.97); }
@media (hover: hover) and (any-pointer: fine) { .m-calendar__arrow:hover:not(:disabled) { background: var(--c-slate); color: var(--c-cream); } }
.m-calendar__dows { display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: .4rem; margin-bottom: var(--s-1); color: var(--c-steel); font: 500 1.1rem/1.4 var(--f-mono); letter-spacing: .08em; text-align: center; text-transform: uppercase; }
.m-calendar__grid { display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: .4rem; }
.a-choice.-cal .a-choice__face { min-width: 0; min-height: 4.4rem; padding: 0; font: var(--w-semi) 1.6rem/1 var(--f-body); }
.a-choice.-light.-off { cursor: default; }
.a-choice.-light.-off .a-choice__face { box-shadow: none; color: var(--c-steel); opacity: .45; }
.a-choice.-off:active .a-choice__face { transform: none; }
@media (hover: hover) and (any-pointer: fine) { .a-choice.-light.-off:hover .a-choice__input:not(:checked) + .a-choice__face { box-shadow: none; } }
.m-calendar__empty { margin-top: var(--s-3); }
.o-book__state { padding: var(--s-7) var(--cell) var(--s-8); }
.o-book__state:focus { outline: 0; }
.o-book__summary { border-top: 1px solid var(--c-line); }
.o-book__summaryRow { display: grid; grid-template-columns: 11rem minmax(0, 1fr); gap: var(--s-3); padding: var(--s-3) 0; border-bottom: 1px solid var(--c-line); }
.o-book__stateFoot { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--s-3) var(--s-5); margin-top: var(--s-5); }
.o-book__aside { border-top: 1px solid var(--c-line); }
.o-book__call { padding: var(--s-5) var(--cell) var(--s-6); }
.o-book__callLine { max-width: 28ch; color: var(--c-steel); font: var(--w-body) 1.6rem/1.4 var(--f-body); text-wrap: balance; }
.o-book__callNumber { display: inline-flex; align-items: center; min-height: 4.4rem; margin: var(--s-2) 0; color: var(--c-ink); font: 600 2.4rem/1 var(--f-mono); letter-spacing: -.01em; text-underline-offset: .4rem; text-decoration-thickness: 1px; white-space: nowrap; }
@media (hover: hover) and (any-pointer: fine) {
  .o-book__progressBtn:not(:disabled):hover { background: rgba(52, 61, 78, .06); }
  .o-book__callNumber:hover { text-decoration-color: transparent; }
}
@media (min-width: 641px) {
  .o-book__progressBtn { padding: var(--s-3) var(--cell); font-size: 1.3rem; }
  .o-book__chips { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .o-book__chips.-five { grid-template-columns: repeat(6, minmax(0, 1fr)); }
  .o-book__chips.-five .a-choice { grid-column: span 2; }
  .o-book__chips.-five .a-choice:nth-child(n + 4) { grid-column: span 3; }
  .o-book__cell.-fields { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .t-book { --cell: 2rem; }
}
@media (min-width: 1025px) {
  .t-book { --cell: 2.4rem; }
  .o-book { grid-template-columns: minmax(0, 9fr) minmax(0, 3fr); min-height: 56rem; }
  .o-book__main { border-right: 1px solid var(--c-line); }
  .o-book__cells { grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); }
  .o-book__cell { padding: var(--s-6) var(--cell); border-top: 0; }
  .o-book__cell + .o-book__cell { border-left: 1px solid var(--c-line); }
  .o-book__aside { border-top: 0; }
  .o-book__call { position: sticky; top: calc(var(--h-header) + 1.6rem); padding: var(--s-6) var(--cell); }
  .o-book__callNumber { font-size: clamp(1.9rem, 1.7vw, 2.4rem); }
  .o-book__state { padding: var(--s-8) var(--cell); }
}
```
Add `.t-book` to the page scope rule (request 001's rule). `.t-book { --c-line ... }` alone would pass check.py, but keep one scope rule for every page.

In the closing reduced-motion block, add these to the transition list: `.o-book__progress::before`, `.m-calendar__arrow`, `.m-field__input`, `.m-upload__face`.

### site/tools/build.py: load radios
Pull the radios out of block_load_picker, so Home and Book print the same ones:
```python
def load_radios(first_checked):
    """The four loads as real radios, from data/prices.json, so prices can't drift. Home starts on 1/8; Book starts with nothing picked (copy.md)."""
    cards = json.loads(read(DATA, 'prices.json'))['cards']
    rows = []
    for i, c in enumerate(cards):
        first, unit = c['label'].split(' ', 1)
        rows.append(
            '      <label class="a-choice"><input class="a-choice__input" type="radio" name="load" value="%s"%s data-level="%d" data-price="$%d" data-unit="%s" data-note="%s" data-label="%s"><span class="a-choice__face">%s<span class="a-choice__unit"> %s</span></span></label>'
            % (esc(c['value']), ' checked' if first_checked and i == 0 else '', c['level'], c['price'], esc(c['unit']), esc(c['fits']), esc(c['load_label']), esc(first), esc(unit)))
    return '\n'.join(rows)
```
In block_load_picker, replace the `rows` loop and `'\n'.join(rows)` with `load_radios(True)`. Add to BLOCKS: `'load-radios': lambda: load_radios(False),`. Home's output must come out byte for byte the same.

### site/assets/global.js: the "priced by the load" block
Replace everything from `var shown = 1;` through the end of the block, keeping setLevel as it is:
```js
    /* Book only: the line that holds the price, hidden when there's no set price. Home has neither this line nor job chips, and always has a pick */
    var line = $('[data-gauge-line]', section);
    var shown = 1;

    function setLevel(level) { /* unchanged */ }

    /* What the current pick costs. On Book there can be no pick, "Not sure" or a demo job, and then a line takes the price's place (copy.md, Book: load step). Book's prefill sends a change event, so ?load= and ?job= land here too */
    function readout() {
      var input = $('input[name="load"]:checked', section);
      var job = $('input[name="job"]:checked', section);
      var isDemo = !!job && job.value === 'demo';
      var level = input ? Number(input.getAttribute('data-level')) : 0;
      var hasPrice = !!input && !!input.getAttribute('data-price') && !isDemo;
      setLevel(level);
      if (line) { line.hidden = !hasPrice; }
      if (hasPrice) {
        price.textContent = input.getAttribute('data-price');
        unit.textContent = input.getAttribute('data-unit');
      }
      if (isDemo) { note.textContent = note.getAttribute('data-demo'); }
      else { note.textContent = input ? input.getAttribute('data-note') : note.getAttribute('data-empty'); }
      /* an empty truck is decorative (copy.md, Truck labels) */
      if (level) {
        svg.removeAttribute('aria-hidden');
        svg.setAttribute('aria-label', 'The Quick Haul truck carrying ' + input.getAttribute('data-label'));
      } else {
        svg.setAttribute('aria-hidden', 'true');
      }
    }
    $$('input[name="load"], input[name="job"]', section).forEach(function (input) {
      input.addEventListener('change', readout);
    });
    /* also covers a browser restoring the form on Back */
    readout();
    if (shown) { svg.setAttribute('data-level', shown); }
  }());
```
The old Home code only re-applied when the pick wasn't 1/8. `readout()` at load gives the same result on Home, since its first radio is checked, but check Home's truck doesn't re-run its drop on load: level-1 items are already on, so `entering` stays 0.

### site/assets/global.js: the Book block
1. Delete the "load: the price line follows the chip" part (`priceLine`, `setPrice`, its listeners and the `setPrice();` call after prefill). The gauge block does it now.
2. pickRadio tells the gauge:
```js
    function pickRadio(name, value) {
      var r = $$('input[name="' + name + '"]', form).filter(function (x) { return x.value === value; })[0];
      if (!r) return;
      r.checked = true;
      r.dispatchEvent(new Event('change'));
    }
```
3. In the submit handler, replace the `setSummary('price', ...)` line:
```js
      var job = $('input[name="job"]:checked', form);
      var hasPrice = load && load.getAttribute('data-price') && !(job && job.value === 'demo');
      var priceCell = $('[data-book-sum="price"]');
      setSummary('price', hasPrice ? load.getAttribute('data-price') : priceCell.getAttribute('data-none'));
```
4. Town note, in checkBookTown. Replace `townNote.hidden = !name;` and `if (!name) return;`:
```js
        if (!name) { townNote.textContent = townNote.getAttribute('data-default'); return; }
```
and change `callLink.className = 'm-field__smallLink';` to `callLink.className = 'a-inlineLink';`.
5. Calendar chips: `label.className = 'a-choice -light -cal' + (ok ? '' : ' -off');`
6. Try again, after the failed state is set up:
```js
    /* copy.md: "Your details are still here, so try again": hiding the form never cleared it */
    var retry = $('[data-book-retry]');
    if (retry) {
      retry.addEventListener('click', function () {
        failedState.hidden = true;
        form.hidden = false;
        show(current, true);
      });
    }
```

### site/assets/global.js: shared form helpers
1. fieldError, the email line, so a missing email and a mistyped one say different things (copy.md: "Add your email"; "That email doesn't look right"):
```js
    if (input.hasAttribute('data-email') && v && !EMAIL_RE.test(v)) return input.getAttribute('data-error-format') || input.getAttribute('data-error');
```
2. showFieldError reads the first id only, so a field can also point at a helper line:
```js
    var note = document.getElementById((input.getAttribute('aria-describedby') || '').split(' ')[0]);
```
3. setupUploads, the part that lists file names. "Remove" comes from `data-remove` on the list, so the word stays in the HTML. Choosing again still replaces the set:
```js
        if (list) {
          while (list.firstChild) list.removeChild(list.firstChild);
          Array.prototype.forEach.call(input.files, function (f, index) {
            var li = document.createElement('li');
            li.className = 'm-upload__file';
            li.appendChild(document.createTextNode(f.name));
            var remove = document.createElement('button');
            remove.type = 'button';
            remove.className = 'm-upload__remove';
            remove.textContent = list.getAttribute('data-remove');
            remove.setAttribute('aria-label', list.getAttribute('data-remove') + ' ' + f.name);
            remove.addEventListener('click', function () {
              var keep = new DataTransfer();
              Array.prototype.forEach.call(input.files, function (g, i) { if (i !== index) { keep.items.add(g); } });
              input.files = keep.files;
              input.dispatchEvent(new Event('change'));
            });
            li.appendChild(remove);
            list.appendChild(li);
          });
          list.hidden = !input.files.length;
        }
```

### When Book moves in
Take `book` off LEGACY_PAGES in tools/build.py. The Book block in global.js already runs on any page with `[data-book]`, so it can move out of the OLD INNER PAGES banner into the new part of the file.

## Checks P2 has to run
- Load step at 1440 and 390: picker fits, truck fits the cell, every stop works by keyboard, focus rings show. `?load=half`, `?job=demo` and both at once open the right state.
- Each no-price state: nothing picked, Not sure, Demo picked with a load already chosen, then Demo unpicked by choosing another job.
- `.a-choice__input` is inset 0 in the new CSS, and the old one was 1px. Check the calendar's tap targets and that the disabled days ignore clicks.
- With `window.SITE_FORM_ENDPOINT` set by hand, the photo field, Remove and the upload error.
- A failed send, then Try again: the form comes back filled, on the last step.

## Other pages this touches
- Home: the reset additions, load_radios and the gauge block. Rerun QA on Home after this one. It should not change.
- Contact and Commercial: `.m-field*`, `.m-check*`, `.m-upload*`, the `fieldError` and `showFieldError` changes, and Remove. Their old pages still run under `.t-legacy` until they move, so keep the `.t-legacy` copies until then, and rerun QA on both after this one.
- Every page: `.a-button.-block` and the reset are global, though only forms use them.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written (CSS lifted from this file by script), except where the old pages or Varun's picker note needed otherwise. The staged page is not moved in.

Changed from the request, and why:
- **`.m-loadPicker.-light` follows the small picker** (Varun, 5 Nov). Picked text is ink, the rest steel, because the small picker's picked rule sets cream and outranks the rule here. "Not sure" sits beside the pill at the same 36px with a 44px target, and drops under it at 400 and narrower.
- **The old Book still runs, so four things stay until it moves.** The price-line code (`priceLine`, `setPrice`) stays and does nothing on the new page. Calendar chips take `-light` only outside `.t-legacy`. The town note hides when it has no `data-default`. "Remove" prints only when the list has `data-remove`. Request 014 now lists these for deletion.
- **`.t-legacy` copies kept, plus an undo.** The new rules share class names with the old pages at lower specificity, so properties the old rules never set leaked through (rings on fields, a frame on the old sheet, smaller calendar chips). A short block at the end of OLD INNER PAGES undoes exactly those, and goes with that block.

Checks:
- Old Book, Contact and Commercial: every element's computed style at 1440 and 390, with Book's hidden steps opened, is identical with and without the new rules (build/tmp/v3/leak.py, 0 differences). Full-page shots 0.0% changed. flow_contact.py 0 problems. flow_book.py and flow_book_r2.py ran to the end with no script errors. flow_commercial.py has 1 problem, the known one: at 390 the success panel lands 2px under the bar (progress.md, open since the old build), and it goes with that page's rebuild.
- Home: tools/qa.py clean, flow_home.py no problems, full-page shots 0.0% changed, truck doesn't re-run its drop on load.
- Staged Book in a scratch copy with the page moved in: build and check.py PASS. build/tmp/v3/flow_trial_book.py, 21 lines, no failures: nothing picked, Not sure, Demo with a load, Demo unpicked, arrows, radio names, `?load=half`, `?job=demo`, both, `?load=notsure`, town prefill and all three town notes, both email errors, a failed send, Try again back on the last step with the fields filled. Day and load steps read fine by eye at 1440 and 390.
- Not run here, for P2: the calendar's tap targets, `window.SITE_FORM_ENDPOINT` with photos and Remove, the page's own QA and Critic round.
