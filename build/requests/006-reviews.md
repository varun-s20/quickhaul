# Request 006: Reviews, the loose grid and four sliders
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs request 002. Sources: site/src/pages-v2/reviews.body.html, site/src/pages-v2/_data/reviews.json.

## What is needed
1. `review-grid` rewritten to print cards and photos from the new data.
2. A `facebook-url` block, so the page's two links read the one value in data/reviews.json.
3. CSS for the grid and the pairs (`.o-reviewGrid*`, `.m-quote.-card`, `.o-reviewPairs*`).
4. Home's before-and-after script running on every slider on a page, not just Home's one.
5. `.t-reviews` in the page scope rule.
6. data/reviews.json replaced by the staged file. The `home` entry and `facebook_url` are unchanged; `filter` goes.

CSS values are not measured. P2 checks them.

## Why
- revision.md, Reviews: "Quotes mixed with photos in a loose grid." "Cut: Filter column."
- Conventions: repeated content the owner edits comes from data/*.json as identical item markup. That now includes the photos, so an owner can move or drop one without touching the page.
- The card is Home's card with no drawn items: `.m-quote__*` already exists in the new CSS. Grid cards are smaller, since six big 32px quotes would be a wall.
- Home's slider has the new behaviour (a vertical swipe scrolls the page, it eases in once). The old `.t-legacy` slider has none of that.
- The pairs share one `.m-compare`. Its frames are 16/9 and wider because Home shows one at full width. In a row of two they'd be thin, so the pairs go to 4/3 here.

## Exact change

### site/tools/build.py: replace block_review_grid
```python
def block_review_grid():
    """Reviews: quotes mixed with photos, in reading order, from data/reviews.json. A photo is never inside a card, so none reads as the job a review is about (copy.md). Photos come out as picture tags, which expand() fills in next."""
    data = json.loads(read(DATA, 'reviews.json'))
    rows = []
    for item in data['reviews_page']:
        if 'photo' in item:
            rows.append('    <div class="o-reviewGrid__photo a-inview">{{picture name="%s" class="o-reviewGrid__img" alt="%s" sizes="(min-width: 1025px) 31vw, (min-width: 641px) 47vw, 100vw"}}</div>' % (item['photo'], item['alt']))
        else:
            rows.append(
                '    <figure class="m-quote -card a-inview">\n'
                '      <blockquote class="m-quote__text"><p>&ldquo;%s&rdquo;</p></blockquote>\n'
                '      <figcaption class="m-quote__foot"><span class="m-quote__who"><span class="m-quote__avatar" aria-hidden="true">%s</span><span class="m-quote__name">%s</span></span></figcaption>\n'
                '    </figure>' % (esc(item['quote']), esc(item['initials']), esc(item['who'])))
    return '\n'.join(rows)
```

### site/tools/build.py: add to BLOCKS
```python
    'facebook-url': lambda: esc(json.loads(read(DATA, 'reviews.json'))['facebook_url']),
```

### site/assets/global.css: in "Inner pages", a new section
```css
/* ---- Reviews: quotes and photos in loose columns. Columns, not a grid: cards of different lengths and photos of different shapes settle with no row of gaps, and real reviews of any length will too. Reading order is the data's, down each column ---- */
.o-reviewGrid { padding-top: var(--s-8); }
.o-reviewGrid__cols { max-width: 134.4rem; margin: 0 auto; column-gap: var(--s-4); }
.m-quote.-card, .o-reviewGrid__photo { margin-bottom: var(--s-4); break-inside: avoid; }
/* Slate at 8%, the seated card's ground, with nothing set on its edge: six seated cards in a row would be a shelf of furniture */
.m-quote.-card { padding: var(--s-5); border-radius: var(--r-image); background: rgba(52, 61, 78, .08); }
.m-quote.-card .m-quote__text { font-size: 2.2rem; }
.m-quote.-card .m-quote__foot { margin-top: var(--s-4); }
.o-reviewGrid__photo { overflow: hidden; border-radius: var(--r-image); background: var(--c-slate); }
.o-reviewGrid__img { display: block; width: 100%; height: auto; }
.o-reviewGrid__end { margin-top: var(--s-6); text-align: center; }
.o-reviewGrid__end .a-lede { margin-top: 0; }
.o-reviewGrid__end .m-rowActions { margin-top: var(--s-2); }
@media (min-width: 641px) { .o-reviewGrid__cols { columns: 2; } }
@media (min-width: 1025px) {
  .o-reviewGrid__cols { columns: 3; }
  .m-quote.-card { padding: var(--s-6); }
}

/* ---- Reviews: the pairs. A row of two needs a taller frame than Home's one wide slider ---- */
.o-reviewPairs { display: grid; gap: var(--s-6) var(--s-4); max-width: 134.4rem; margin: 0 auto; }
.o-reviewPairs__pair { min-width: 0; }
.o-reviewPairs .m-compare { aspect-ratio: 4 / 3; }
.o-reviewPairs__caption { margin-top: var(--s-3); font: var(--w-semi) 1.8rem/1.25 var(--f-body); text-align: center; }
@media (min-width: 641px) { .o-reviewPairs { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
```

### site/assets/global.css: the page scope rule
Add `.t-reviews`.

### site/assets/global.js: the "before and after" block
Change the opening so it runs once per slider, and leave the body alone. Its early `return`s then return from the callback:
```js
  $$('[data-compare]').filter(function (box) { return !box.closest('.t-legacy'); }).forEach(function (box) {
    var range = $('[data-compare-range]', box);
    /* ...the rest of the block, unchanged... */
  });
```
Remove the old `(function () { var box = $('.t-home [data-compare]'); if (!box) { return; }` and its closing `}());`.

### When Reviews moves in
Take `reviews` off LEGACY_PAGES. Delete the old Reviews filter block and the `$$('.t-legacy [data-compare]')` block from global.js. Nothing else uses them.

## Checks P2 has to run
- Look at each pair at 1440 and 390: the three non-garage pairs use the old square crops at 4/3, so the subject may need an `object-position`. Don't re-cut without logging it.
- At 390, a tag must not sit under the divider at rest (rulings, R0 A13), and the knob must not clip at 0% or 100% (R0 B3).
- `.a-inview` inside CSS columns: confirm nothing is left hidden after scrolling to the end and back.
- A photo must not land beside a card about its own job (the order in the data is set so it shouldn't, but columns move things as widths change). Yard photo versus the yard card is the one to watch.
- The same photos also appear on Services and Home, so check it doesn't read as repetition.

## Other pages this touches
- Home: the slider script changes shape. Rerun Home's QA, including drag, keyboard and the first-view ease.
- Home's `block_review_home` still reads the `home` entry, unchanged.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied, with these changes. Taking Reviews off LEGACY_PAGES and deleting its old filter and slider blocks stay with the move-in.
- **Don't copy the staged `_data/reviews.json` over at move-in.** It still has copy v2's words and one Home card, and it would undo copy v3 on Home. site/data/reviews.json is the file now: v3's words, `home` as a list of five, plus this request's photo items. `filter` stays on the cards until the old Reviews page moves; request 014 drops it.
- **The old page keeps its grid** through `block_review_grid_old` and `CURRENT_LEGACY`, the same way as request 004. It skips the photo items.
- **Photo order changed from the staged file's, because that order failed this request's own check.** In the browser the yard photo sat right beside the yard card at 1440, and the mattress photo beside the mattress card on tablets. build/tmp/v3/photo_order.py tried all 336 placings at 9 widths from 641 to 1920, card order fixed by copy.md. Now: card 1, card 2, pickup photo, cards 3, 4, 5, yard photo, card 6, mattress photo. No photo sits beside its own job at any of those widths, or on the phone's single column. copy.md's sentence that "the photo order already staged" keeps them apart is out of date (Copywriter's file; flagged in build/progress.md).
- **The card's CSS is shared with Home.** Home needed `.m-quote.-card` first, so this request's copy of it is left out, and its column rules hang off `.o-reviewGrid__cols`. Home's card type is 2.6rem from 1025, so grid cards are 2.6rem too, not 2.2rem. They read fine in three columns.
- `facebook-url` was already added for Home's link.
- The slider script runs per slider as written.

Checks:
- Home: flow_home.py no problems, including drag, keys and value text. Full-page shots 0.0% changed.
- Old Reviews: full-page shots 0.0% changed. Its filter and sliders are untouched.
- Staged Reviews in a scratch copy: build and check.py PASS. tools/qa.py without the tab pass: no overflow, console or reveal problems, nothing left hidden in the columns, 192 words. Grid and pairs read fine by eye at 1440 and 390: tags clear of the divider, knob not clipped at rest.
- **The staged page body still has copy v2's lines** ("Our Facebook page has plenty of them", "Read them all on Facebook"). copy-changes.md lists them. Applying them is the pages step's, because this run doesn't touch pages-v2.
- Not run here, for P2: the three non-garage pairs' subjects at 4/3 on a close read, knob at 0% and 100% on these frames, the page's QA with tab and its Critic round.

## P2 batch b (2026-11-05)
Moved in. The checks above were run: build/qa-report.md, "P2 batch b: Reviews". Differs from this request: real columns from 1025 and groups of two cards and a photo at 641 to 1024, not CSS columns, because photos fill what the cards leave and no column ends short; order and photos in data/reviews.json changed for it; the old filter and `.t-legacy [data-compare]` blocks stay until request 014, whose script removes them by exact match.
