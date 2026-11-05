# Request 004: Service area hub, town chips and the drawn map
Filed by the pages session, phase P1, 2026-11-05. Status: open. Needs request 002. Page source: site/src/pages-v2/service-area.body.html.

## What is needed
1. `town-list` prints chips under state labels, not ruled rows.
2. The drawn map restyled for a promo card's picture slot (`.m-promo__media.-map`).
3. A lit state for a chip (`.a-chip.is-lit`) and state labels in a promo (`.m-promo__group`, `.m-promo__label`).
4. `.t-area` in the page scope rule.

CSS values are carried over from the old map rules and are not measured. P2 checks them.

## Why
- revision.md, Service area hub: "Map beside town chips by state." Home's towns band is already a slate promo of chips, so the hub repeats its recipe with the map where the photo goes.
- The halftone is on the retired list (revision.md section 1), and the 1px square frame goes with square frames. The north becomes slate at 8%, the seated card's ground.
- The map's own markup stays. Its `fill` attribute keeps the old pages' halftone while they wait, and the new `fill` rule beats it through CSS. All the new map rules hang off `.m-promo__media.-map`, so old Contact and old town pages don't change until they move. Request 014 removes the pattern at the end.

## Exact change

### site/tools/build.py: replace block_town_list
```python
def block_town_list():
    """Service area hub: the towns as link chips under their state labels, alphabetical. data-place lights the same town on the map."""
    data = json.loads(read(DATA, 'towns.json'))
    groups = []
    for state in ('Massachusetts', 'New Hampshire'):
        links = '\n'.join(
            '          <li><a class="a-chip" href="service-area/%s.html" data-place="%s">%s</a></li>' % (esc(t['slug']), esc(t['slug']), esc(t['name']))
            for t in sorted((t for t in data['towns'] if t['state'] == state), key=lambda t: t['name']))
        groups.append(
            '      <div class="m-promo__group">\n'
            '        <h3 class="m-promo__label">%s</h3>\n'
            '        <ul class="m-promo__chips">\n%s\n        </ul>\n'
            '      </div>' % (esc(state), links))
    return '\n'.join(groups)
```
Only the hub uses this block, so it changes when the hub moves in.

### site/assets/global.css: right after the `.a-chip` hover rule
```css
/* A town chip and its spot on the map light together (the hub only) */
.a-chip.is-lit { background: var(--c-cream); box-shadow: none; color: var(--c-ink); }
```

### site/assets/global.css: right after the `.m-promo` rules
```css
/* State labels over the town chips (the hub) */
.m-promo__group { margin-top: var(--s-5); }
.m-promo__label { color: var(--c-chrome); font: var(--w-semi) 1.6rem/1.2 var(--f-body); }
.m-promo__group .m-promo__chips { margin-top: var(--s-2); }

/* The drawn map in the picture's slot (hub and Contact). Our own drawing, placeholder towns at public map positions. Cream under it, so the labels read as they did. It fills the slot from 1025 up and letterboxes itself. Hangs off .-map so the old pages keep their own map until they move */
.m-promo__media.-map { aspect-ratio: 1; background: var(--c-cream); }
.m-promo__media.-map .m-map { position: absolute; inset: var(--s-2); display: block; width: calc(100% - var(--s-2) * 2); height: calc(100% - var(--s-2) * 2); }
.m-promo__media.-map .m-map__north { fill: rgba(52, 61, 78, .08); stroke: none; }
.m-promo__media.-map .m-map__river { fill: none; stroke: var(--c-chromeMid); stroke-width: 2.5; vector-effect: non-scaling-stroke; stroke-linecap: round; opacity: .55; }
.m-promo__media.-map .m-map__border { fill: none; stroke: var(--c-slate); stroke-width: 1.25; vector-effect: non-scaling-stroke; stroke-linejoin: round; }
.m-promo__media.-map .m-map__dot { fill: var(--c-ink); transform: scale(1.5); transform-box: fill-box; transform-origin: center; transition: transform var(--d-ui) var(--e-ui); }
.m-promo__media.-map .m-map__town { fill: var(--c-ink); font: var(--w-semi) 3rem/1 var(--f-display); letter-spacing: .01em; text-transform: uppercase; stroke: var(--c-cream); stroke-width: 6px; paint-order: stroke; }
.m-promo__media.-map .m-map__state { fill: var(--c-steel); font: var(--w-semi) 2.6rem/1 var(--f-body); letter-spacing: .04em; text-transform: uppercase; stroke: var(--c-cream); stroke-width: 6px; paint-order: stroke; }
.m-promo__media.-map .m-map__link { pointer-events: none; }
.m-promo__media.-map .m-map__hit { fill: transparent; }
.m-promo__media.-map .m-map__place.is-lit .m-map__dot { transform: scale(1.8); }
.m-promo__media.-map .m-map__place.is-lit .m-map__town { font-weight: var(--w-heavy); }
@media (max-width: 640px) { .m-promo__media.-map .m-map__town.-drop { transform: translateY(9px); } }
@media (min-width: 641px) and (max-width: 1024px) { .m-promo__media.-map { aspect-ratio: 16 / 10; } }
@media (min-width: 1025px) {
  .m-promo__media.-map { aspect-ratio: auto; }
  .m-promo__media.-map .m-map__dot { transform: none; }
  .m-promo__media.-map .m-map__town { font-size: 2.2rem; }
  .m-promo__media.-map .m-map__state { font-size: 1.6rem; }
}
@media (min-width: 1025px) and (hover: hover) and (any-pointer: fine) { .m-promo__media.-map .m-map__link { cursor: pointer; pointer-events: auto; } }
```
The old `.m-map` label sizes were tuned to a 658px map at 1440 and a full-width map at 390. Here the map is about 540px at 1440, and letterboxed at tablet widths, so P2 should read the labels at 1440, 1024, 768 and 390 and check no name touches another.

### site/assets/global.css: the page scope rule
Add `.t-area`.

### site/assets/global.js
No change. "Service area map" reads `[data-place]` on anything. It sits under OLD INNER PAGES; move it out of that banner when the hub moves in.

### When the hub moves in
Take `service-area` off LEGACY_PAGES.

## Other pages this touches
- Contact uses `.m-promo__media.-map` later (request 010).
- Old town pages and old Contact keep their map and its old rules until they move.
- Home's `.a-chip` only gains a state it never gets, since Home's chips have no `data-place`.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written (CSS lifted from this file by script), with these changes. Taking the hub off LEGACY_PAGES stays with the move-in.
- **The old hub keeps its rows until it moves.** The old hub still calls `town-list`, so tools/build.py has `CURRENT_LEGACY` and `block_town_list_old`. Off LEGACY_PAGES, the page gets the new block with no further edit. Request 014 deletes both.
- **Fixed after seeing it:** at tablet widths the map letterboxed into a floating shape with a slanted left edge and a notch on the right, because the state's polygon ended at the square. `block_town_map` now runs the state, its line and the river on past the square. A square slot clips them, so the old pages look the same. `.m-map` fills the slot instead of sitting 8px inside it. The card's slate moved onto the words through `:has()`, because under the map's cream it showed as a dark fringe on the round corners.

Checks:
- Real site: check.py PASS, build.py --check up to date. Home, old hub, old Lowell and old Contact unchanged in full-page shots at 1440 and 390 (0.0%). build/tmp/map_check.py on the old maps: 0 problems.
- Staged hub in a scratch copy: build and check.py PASS. Read by eye at 1440, 820 and 390: no name touches another, chips and state labels fine.
- Not run here, for P2: 1024 and 768 label reads beyond the 820 one, the map's mouse links, and chip and map lighting together.
