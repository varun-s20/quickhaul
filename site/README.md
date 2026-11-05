# Quick Haul website

A custom static site: 25 HTML pages, one stylesheet, one script. No framework and no build step for visitors. Python only assembles the pages.

**State:** design preview. Phone, hours, towns, prices, reviews, photos and much of the wording are placeholders until Shawn confirms them. See "Before launch" below, content/placeholders.md and build/handover.md.

## Quick start
From this folder (`site/`):

```
python -m http.server 8841 --bind 127.0.0.1
```

Then open http://127.0.0.1:8841/index.html. Open pages through a server, not from `file://`.

## Rebuild order
1. `python tools/images.py` only if a photo or `data/images.json` changed. It needs Pillow.
2. `python tools/build.py` rebuilds every page from `src/` and `data/`, plus the sitemap and robots.txt.
3. `python tools/check.py` is the site check. It must end in PASS.
4. `python tools/build.py --check` fails if a built page is stale.

`python tools/build_trucks.py` redraws the truck set, and only needs running if the trucks change.

Browser QA for one page needs Playwright and a server on the port you name:

```
python tools/qa.py pricing.html <output folder> --section "<newline>## Pricing (new page, pricing.html)" --port 8841 --no-shots
```

`--no-shots` measures only, with no screenshots or contact sheets. `--no-tab` skips the tab-through. `--section` also compares the page's words with that section of content/copy.md, and it needs the leading newline, or `## Reviews` also matches Home's `### Reviews`.

## To change X, edit Y
| To change | Edit | Then |
|---|---|---|
| Words on a page | `src/pages/<slug>.body.html` | build |
| Town pages, all 12 | `src/templates/town.body.html` | build |
| Town list, nearby towns, map positions | `data/towns.json` | build |
| Header, phone menu, call bar | `src/partials/header.html` | build |
| Footer | `src/partials/footer.html` | build |
| Page title and description | the meta comment at the top of the page's body file | build |
| Prices and what each load holds | `data/prices.json` | build. Then also the hand-typed prices its `_note` lists |
| FAQ questions, and their FAQPage JSON-LD | `data/faq.json` | build |
| Review cards | `data/reviews.json` | build |
| Colours, fonts, sizes | `:root` in `assets/global.css`, and `design/tokens.css` to match | |
| Behaviour | `assets/global.js` | |
| Structured data | `src/schema/<slug>.json` | build |
| Domain | `SITE_URL` in `tools/build.py` | build |
| Phone, email, hours | see "Where contact details live" | build |
| A photo | see "Replacing media" | images, build |

Never edit a built `.html` file. Each one opens with a note naming its source.

## Folders
```
site/
  *.html                  built pages (published)
  service-area/*.html     12 built town pages (published)
  sitemap.xml robots.txt  written by tools/build.py (published)
  assets/
    global.css global.js  loaded by every page
    fonts/ images/<topic>/ icons/ trucks/ fx/
  src/                    never published
    pages/                one body file per page
    templates/            the town page
    partials/             head, header, footer, truck set
    schema/               JSON-LD per page
    stock/                untouched photo downloads
    pages-v2/             old staging folder, stale, do not copy from it
  data/                   prices, towns, FAQ, reviews, image jobs and manifest (never published)
  tools/                  build.py, build_trucks.py, images.py, check.py, qa.py (never published)
```

## Pages
Home `index.html`, `services.html`, `pricing.html`, `book.html`, `reviews.html`, `about.html`, `donate.html`, `faq.html`, `contact.html`, `service-area.html`, `commercial.html`, `privacy.html`, `404.html`, and 12 pages in `service-area/`. Nav: Services, About, Pricing, Reviews, Donate, plus Book now and the call line. FAQ, Contact, Service area, Commercial and Privacy are in the footer and in-page links. The phone menu adds Service area, FAQ and Contact as a smaller second group.

## CSS and JS conventions
- Class levels: `a-` atom, `m-` module, `o-` section, `t-` page wrapper, `b-` reusable block. Block in camelCase, element after `__`, variant as a single-dash class: `o-svcBand__img`, `a-button -cream`.
- `is-` classes are runtime states set by JS. JS hooks are data attributes (`data-menu`). A `js` class on `<html>` gates every hidden start state, so nothing is hidden without JS.
- 1rem is 10px. The base is the phone, with steps at `min-width: 641px` and `1025px`. Hover rules live in `@media (hover: hover) and (any-pointer: fine)`, and each has a matching `:focus-visible`.
- Page-only rules hang off the page wrapper, `.t-pricing .o-x`. Page bodies hold no `<style>`, `<script>` or inline styles.
- `global.js` is one IIFE in plain ES5. Each feature is a block that starts with a presence check.
- Internal links are written `slug.html`, with an optional `#hash`. The 404 page's local paths are written from the site root by `tools/build.py`, because it can be served at any depth.

## Forms and how to connect them
No form has a backend yet. Set the endpoint once, before `global.js` loads:

```html
<script>window.SITE_FORM_ENDPOINT = 'https://your-endpoint.example/submit';</script>
```

Forms POST `FormData` to that URL. A form reports success only if the endpoint answers OK. Any other answer, or no endpoint, shows the failed state with the phone number. Every send in this preview shows that failed state. Photo fields stay hidden until an endpoint is set, because there is no file input without a backend.

| Form | Field names |
|---|---|
| Book (`book.html`, `data-book`) | `day`, `time`, `load`, `price`, `job`, `street`, `town`, `zip`, `where`, `going`, `photos`, `notes`, `name`, `phone`, `email`, `sms` |
| Contact (`contact.html`, `data-request`) | `name`, `phone`, `email`, `town`, `job`, `photos`, `reply` |
| Commercial (`commercial.html`, `data-request`) | `name`, `company`, `role`, `phone`, `email`, `property`, `job_type`, `frequency`, `job`, `photos` |

`job` means different things: on Book it is the kind of job (a chip), on Contact and Commercial it is the free-text description. Book's description is `going`. Photos accept JPG and PNG only. Contact and Commercial need a phone or an email, either one.

## Preview gate
Two switches near the top of `tools/build.py`:

| Switch | Now | What it does |
|---|---|---|
| `PREVIEW` | `True` | Adds `noindex`, prefixes every description with "Design preview with placeholder content." and writes a robots.txt that disallows everything. Set `False` at launch. |
| `PREVIEW_LABEL` | `False` | Prints the visible line in the header: "Design preview. Phone, hours, towns, prices, reviews and photos are sample content until Quick Haul confirms them." It only prints while `PREVIEW` is also `True`. |

**The line is off by Varun's call, and it stays off for his own review. Set `PREVIEW_LABEL = True` and rebuild, or put the preview behind a password, before anyone outside the studio sees a deployed preview.** The brief requires one or the other before Shawn sees it. With the label on, the layout has not been rechecked.

## Replacing media
1. Put the original in `src/stock/`.
2. Add or edit its job in `data/images.json`: name, folder, ratio, focus and widths. Widths never upscale.
3. Run `python tools/images.py`, then `python tools/build.py`. Width, height and srcset come from the manifest, so never type them.
4. Rewrite the alt text wherever the photo appears, and update its row in `content/placeholders.md`.

Every file name under `assets/` must stay unique, because WordPress flattens them into one Media Library.

The logo is a crop of a phone screenshot, about 233px across, so about 108px wide is its sharp ceiling on 2x screens. A bigger logo needs the original file or a vector.

## Where contact details live
- Phone and email: `src/partials/header.html`, `src/partials/footer.html`, and the page bodies and `data/faq.json`. Search for `555-0142` and `quickhaul@example.com`, including `assets/global.js`.
- Hours: `src/partials/footer.html`, the page bodies and `data/faq.json`. Search for `7am to 7pm`.
- Social links: `src/partials/footer.html` and `src/pages/contact.body.html`. The Facebook links on Home and Reviews come from `facebook_url` in `data/reviews.json`. All of them point at the bare network addresses for now.

## What to publish
Publish the root `.html` files, `service-area/`, `assets/`, `sitemap.xml` and `robots.txt`. Never publish `src/`, `data/`, `tools/` or this README. Long cache on `assets/`, short on HTML, compression on, and `404.html` as the error page. Add a 301 map from Shawn's old URLs if he has a live site.

## Before launch
- Set `PREVIEW = False`, set `SITE_URL` to the real domain, then rebuild.
- Replace every placeholder in `content/placeholders.md`: phone, hours, email, towns, prices, load sizes, the $30 fridge fee, practices and About's story.
- Replace the six sample review cards with Shawn's real Facebook reviews, each with its post link. Held wording is in `content/copy.md`, "Held lines".
- Replace all stock photos with Shawn's own, including real before and after pairs from one spot, and rewrite their alts.
- Licensed, insured and guarantee stay unbuilt until Shawn confirms them.
- Connect the forms (`window.SITE_FORM_ENDPOINT`), and confirm the SMS wording.
- Have someone qualified review the Privacy draft against the services really used, and add its "Last updated" date.
- Check the general facts (state disposal rules and the rest) listed in `content/copy-v4-changes.md`.
- Bio Sans ships as `.otf` with no licence file on hand. Confirm the web licence. Converting to woff2 needs fontTools, which isn't installed.
- Strip working notes from HTML comments (they name Varun and decisions) before the site goes to the client.
