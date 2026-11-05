# Request 002: banners, every inner page but Services and Privacy
Filed by the pages session, phase P1, 2026-11-05. Status: open. Used by the staged Book, hub, town, Reviews, About, Donate, FAQ, Contact, Commercial and 404.

## What is needed
1. Five more banner trucks: an eighth, a quarter, a full load, empty, and Donate's.
2. A short banner, a no-truck banner and a wide-drawing banner (`.-short`, `.-noTruck`, `.o-pageBanner__truck.-wide`).
3. A size for long headline rows (`.a-hero.-long`).
4. A class on Contact's call label, so it hides at the same widths as Home's (`.o-pageBanner__callLabel`).

The CSS values below are worked out from the prototype's numbers, not measured. Phase P1 has no browser. P2 sets them for real (see "Checks").

## Why
- revision.md section 5 gives each page its own load. tools/build_trucks.py only writes half a load for banners. Labels are copy.md's, under Truck labels. The 404 truck and the Donate words come from the same list.
- revision.md section 5 calls for a short banner "about 440px" and says it is not built yet.
- Book's banner has no truck (revision.md, Book), but the words keep room for one on phones and portrait tablets through `--truckW`.
- `.a-hero.-banner` is 15.4cqi, which fits about 6.5em. These rows run longer: SOMEONE WANTS IT about 9.2em, JUNK REMOVAL IN and LONDONDERRY, NH about 8.7em, COMMERCIAL AND about 8em, TO HAUL HERE about 6.8em (from SPACE BACK at 5.76em). At 15.4cqi they would wrap to a third row (conventions: size the headline off its column so the row count holds).

## Exact change

### site/tools/build_trucks.py: add after row_svg
```python
# Inner banners: a load that suits the page (revision.md section 5). Words: copy.md, Truck labels. Services' half load is banner_svg above.
BANNER_LOADS = {
    'truck-banner-eighth': (1, 'The Quick Haul truck with a small load, parked on the street'),
    'truck-banner-quarter': (2, 'The Quick Haul truck, a quarter loaded, parked on the street'),
    'truck-banner-full': (4, 'The Quick Haul truck with a full load, parked on the street'),
}


def banner_load_svg(level, label):
    return ('<svg class="m-truck" viewBox="%s" role="img" aria-label="%s"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, label, wheels_markup(), uses(level)))


def banner_empty_svg():
    """The 404: decorative, no label (copy.md, Truck labels)."""
    return ('<svg class="m-truck" viewBox="%s" aria-hidden="true" focusable="false"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/><use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, wheels_markup()))


def banner_donate_svg():
    """Donate: the same drawing as truck-donate.svg, inline, with the dresser and bike at the curb and left off the load."""
    load = uses(4).replace('<use href="#qh-i-dresser"/>', '').replace('<use href="#qh-i-bike"/>', '').replace('<use href="#qh-i-lamp"/>', '')
    return ('<svg class="m-truck" viewBox="-400 62 1464 558" role="img" aria-label="The Quick Haul truck with a dresser and a bike set apart at the curb"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/>'
            '<ellipse cx="-214" cy="602" rx="190" ry="10" fill="url(#qh-contact)"/>%s</svg>'
            % (wheels_markup(), load, curb_items(-392)))
```

### site/tools/build_trucks.py: in inline_parts, after the truck-row line
```python
    parts += [(key, banner_load_svg(level, label)) for key, (level, label) in BANNER_LOADS.items()]
    parts += [('truck-banner-empty', banner_empty_svg()), ('truck-banner-donate', banner_donate_svg())]
```
Then run `python tools/build_trucks.py`.

### site/tools/build.py: add to BLOCKS
```python
    'truck-banner-eighth': lambda: truck_part('truck-banner-eighth'),
    'truck-banner-quarter': lambda: truck_part('truck-banner-quarter'),
    'truck-banner-full': lambda: truck_part('truck-banner-full'),
    'truck-banner-empty': lambda: truck_part('truck-banner-empty'),
    'truck-banner-donate': lambda: truck_part('truck-banner-donate'),
```

### site/assets/global.css: right after the rule `.a-hero.-banner { ... }`, which it has to follow
```css
/* The long rows: SOMEONE WANTS IT runs about 9.2em, the longest of them. It fits at 10.4cqi and keeps the title to two rows (conventions) */
.a-hero.-long { font-size: min(8.4rem, 10.4cqi, 12vh); }
```

### site/assets/global.css: at the end of the banner rules in "Inner pages", after the 1025 block
```css
/* Short banner: utility pages (Book, FAQ, Contact, Commercial), about 440px at 1440x900 (revision.md section 5). Phones let the words and the truck set the height, as the full banner does */
@media (min-width: 1025px) {
  .o-pageBanner.-short { min-height: min(44rem, calc(100svh - var(--h-header) - 8rem)); --truckW: min(38vw, 58vh, 72rem); }
  .o-pageBanner.-short .o-pageBanner__copy { padding-top: var(--s-5); padding-bottom: calc(var(--r-band) + var(--s-4)); }
}
/* Book: no truck (revision.md, Book), so the room the words keep for one goes too. Must follow .-short, which sets the same value */
.o-pageBanner.-noTruck { --truckW: 0rem; }
/* Donate's drawing is 1464 units wide to the truck's 1064, with the dresser and bike at the curb. Its box grows by that ratio, so the truck stays the size it is on other banners. Phones: the whole drawing fits the width and the truck goes smaller */
.o-pageBanner__truck.-wide { width: calc(var(--truckW) * 1.376); }
@media (max-width: 640px) { .o-pageBanner__truck.-wide { width: var(--truckW); } }
```

### site/assets/global.css: the rule that hides Home's call label
```css
@media (min-width: 641px) and (max-width: 1240px) { .o-homeHero__callLabel, .o-pageBanner__callLabel { display: none; } }
```
check.py only looks for the class name, so this one selector is enough. From 1241px up the label simply shows.

## Checks P2 has to run (not optional)
revision.md section 7: "Each new banner needs its scrim sampled the way section 11 does; don't reuse Services' numbers." All these banners use the same photo, but the short ones change the height, and Donate, town, Commercial and 404 change the words.
- Scrim: prototype/revision/tools/sample_contrast.py's method on each banner, headline 3:1, sentence 4.5:1. Add a per-page scrim only where a target fails.
- Geometry: the drawing's box against the words at the windows in revision.md section 11, for Donate (widest drawing, longest row) and town pages on Londonderry, NH first. If the words reach the drawing, narrow `--truckW` under `.t-donate` or `.t-town`, not on the shared rule.
- The Contact pill and the town pill beside the truck at 1024 to 1240.

## Other pages this touches
None: Home and Services use neither the new classes nor the new trucks. build_trucks.py rewrites all its partials, so compare truck-hero, truck-gauge, truck-banner and truck-row-1 to 4 before and after: they must come out unchanged.

## Note from the shared-parts owner, 2026-11-05 (not applied, still open)
Home's rule changed after this request was filed. `.o-homeHero__callLabel` now hides in landscape only, because a portrait window has the room and copy.md has the words (critic, home r1):
`@media (min-width: 641px) and (max-width: 1240px) and (orientation: landscape) { .o-homeHero__callLabel { display: none; } }`
To hide "at the same widths as Home's", add `.o-pageBanner__callLabel` to that rule rather than the one above. Other shared changes since then that reach banners: `.o-pageBanner__actions` now aligns pills at their own width on phones, `.o-pageBanner__line` uses text-wrap balance, and `.a-hero__row`'s mask is off once `is-risen` is set. All in build/progress.md, spec change log.

## Result (shared-parts owner, 2026-11-05): applied, closed
Applied as written, with the call label added to Home's landscape-only rule as the note above says. tools/build_trucks.py run: 13 partials now.
- Unchanged, compared byte for byte before and after: truck-sprite, truck-hero, truck-gauge, truck-banner, truck-row-1 to 4. The 20 SVGs in assets/trucks/ hash the same.
- Real site: check.py PASS, build.py --check up to date. Home and old Services unchanged in full-page shots at 1440 and 390.
- Tried on the staged 404, Donate, About and Commercial in a scratch copy at 1440: all five new trucks build and draw. By eye the 404, About and Commercial banners read fine.
- **Found, for request 008: at 1440x900 Donate's SOMEONE WANTS IT runs into the load's plant.** Request 008's narrower `--truckW` is the fix it names, and it is checked there.
- **Still P2's, not run here, because they need the pages moved in:** the scrim sampling per banner, the geometry sweep at revision.md section 11's windows, and the pills beside the truck at 1024 to 1240.
