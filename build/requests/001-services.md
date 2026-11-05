# Request 001: Services, the truck blocks and the price row
Filed by the pages session, phase P1, 2026-11-05. Status: open. Page source: site/src/pages-v2/services.body.html.

## What is needed
1. Two new `{{> }}` blocks in tools/build.py: `truck-banner` and `price-row`.
2. A page scope rule for `.t-services` in global.css. It now only appears in the OLD INNER PAGES block, so check.py fails on it once that block goes.

Every other class on the page already has a rule in the new part of global.css (compared against global.css on 2026-11-05).

## Why
- `src/partials/trucks/truck-banner.html` and `truck-row-1` to `truck-row-4` exist, but BLOCKS only registers truck-sprite, truck-hero and truck-gauge.
- The row of four loads is repeated on Services and on every town page, and its prices must not drift from data/prices.json (the reason `load-picker` is generated). The prototype typed them by hand; `price-cards` prints the old card and bed glyph, so it can't be reused.
- On a town page each "Book this load" should carry the town as well (copy.md, Book: Town is "filled in when the visitor came from a town page"), so the block reads CURRENT_TOWN.

## Exact change

### site/tools/build.py: add after block_price_cards
```python
def block_price_row():
    """Services #pricing and the town pages: the row of four loads, one truck each, from data/prices.json, so prices can't drift. On a town page each link carries the town too, so Book opens with both filled in."""
    cards = json.loads(read(DATA, 'prices.json'))['cards']
    town = '&amp;town=' + quote_plus('%s, %s' % (CURRENT_TOWN['name'], CURRENT_TOWN['abbr'])) if CURRENT_TOWN else ''
    rows = []
    for c in cards:
        rows.append(
            '    <li class="m-load">\n'
            '      <div class="m-load__copy a-inview">\n'
            '        <p class="m-load__label">%s</p>\n'
            '        <p class="m-load__figure">$%d</p>\n'
            '        <p class="m-load__note">%s</p>\n'
            '        <a class="a-link m-load__link" href="book.html?load=%s%s"><span class="a-link__text">Book this load</span><span class="sr-only">: %s</span><svg class="a-link__arrow" aria-hidden="true"><use href="#i-arrow"/></svg></a>\n'
            '      </div>\n'
            '      <div class="m-load__truck">%s</div>\n'
            '    </li>' % (esc(c['label']), c['price'], esc(c['fits']), esc(c['value']), town, esc(c['label'].lower()), truck_part('truck-row-%d' % c['level'])))
    return '\n'.join(rows)
```

### site/tools/build.py: add to BLOCKS
```python
    'truck-banner': lambda: truck_part('truck-banner'),
    'price-row': block_price_row,
```

### site/assets/global.css: the "Page scope" section
```css
/* ===== Page scope ===== */
.t-home, .t-services { display: block; }
```
Later requests add their page's class to this same rule.

### When Services moves in
Take `services` off LEGACY_PAGES in tools/build.py and delete its rules from OLD INNER PAGES.

## Other pages this touches
- None when applied. Town pages use `price-row` later (request 005).
- `price-cards` and `price_glyph` stay until the old town template and the old FAQ are gone (request 014).

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written: `block_price_row`, the blocks `truck-banner` and `price-row`, `.t-services` in the page scope rule. Moving the page in stays with the move-in step.
- Real site: build.py, check.py PASS on 24 pages, build.py --check up to date. Home and old Services unchanged in full-page shots at 1440 and 390 (0.0%; one Services shot differs 0.03% in the header pill, the same timing noise as in the baseline run).
- Staged Services, in a scratch copy with the page moved in (build/tmp/v3/trial.py; site/ untouched): builds, check.py PASS. tools/qa.py without the tab pass: no overflow, console, network or reveal problems, no upscaled images, 513 words at 1440 and 390. Row of four and all bands read fine by eye at 1440. qa.py's copy check lists the screen-reader tails ": 1/4 truck" and so on, which are this request's own and aren't copy.
- Not run: the page's Critic round, which belongs to P2.
