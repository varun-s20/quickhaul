"""Quick Haul: mechanical browser QA for one page. Needs Playwright (already installed). One headless Chromium at a time;
it closes when the page is done, so memory stays low.

At 1440x900 and 390x844 (desktop Chromium at 390, not a real phone: hover rules still run):
console and network errors, horizontal overflow, clipped headline rows, images shown above their native width or
under half their slot, targets under 44px (links inside a sentence, .a-textLink and .a-inlineLink, are exempt), tall empty stretches, reveals still hidden after scrolling, a tab-through
checking the skip link and a visible focus on every stop. Then reduced motion. Then copy: every text node in <main>
must appear in content/copy.md, and every copy line of the page's section must appear on the page.

Writes screen stops and one contact sheet per width into the output folder.

Usage: python tools/qa.py <url path> <output folder> [--section "## Services"] [--no-tab] [--no-shots] [--init file.js] [--port 8850]
--no-shots: measures only. No stops, no contact sheets, and the output folder is not created.
"""
import json
import os
import re
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPY = os.path.join(os.path.dirname(ROOT), 'content', 'copy.md')
BASE = 'http://127.0.0.1:8820/'
SIZES = [(1440, 900), (390, 844)]
HIDE_BARS = 'html{scrollbar-width:none;scroll-behavior:auto !important} ::-webkit-scrollbar{display:none}'

MEASURE = r"""
() => {
  const out = {};
  const W = innerWidth;
  out.overflow = document.documentElement.scrollWidth - W;
  out.height = document.documentElement.scrollHeight;
  const vis = el => { const s = getComputedStyle(el), r = el.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0; };
  out.hiddenReveals = [...document.querySelectorAll('.a-inview,.a-reveal')].filter(e => vis(e) && +getComputedStyle(e).opacity < 1).map(e => e.className).slice(0, 8);
  out.clippedRows = [...document.querySelectorAll('.a-hero__row,.a-section__row')].filter(vis).filter(e => e.scrollWidth > e.clientWidth + 1).map(e => e.textContent.trim());
  out.images = [...document.images].filter(vis).map(i => { const r = i.getBoundingClientRect(); const s = i.parentElement.closest('.b-photo') || i.parentElement; const p = s.getBoundingClientRect(); return { src: (i.currentSrc || i.src).split('/').pop(), natural: i.naturalWidth, shown: Math.round(r.width), slot: Math.round(p.width), ratio: +(r.width / r.height).toFixed(2), complete: i.complete }; });
  out.upscaled = out.images.filter(i => { const m = i.src.match(/-(\d+)\.webp$/); const file = m ? +m[1] : i.natural; return file && i.shown > file && !/logo/.test(i.src); });   /* naturalWidth is density-corrected by sizes, so read the file's real width from its name */
  out.broken = out.images.filter(i => !i.natural);
  out.small = out.images.filter(i => i.shown < i.slot / 2 && !/logo|item-/.test(i.src));
  out.targets = [...document.querySelectorAll('main a, main button, main input:not([type=radio]):not([type=checkbox]):not([type=range]), main textarea, main summary, main select')].filter(vis).filter(e => getComputedStyle(e).pointerEvents !== 'none' && !e.matches('.a-textLink, .a-inlineLink')).map(e => ({ t: (e.textContent || e.name || e.tagName).trim().slice(0, 40), h: Math.round(e.getBoundingClientRect().height) })).filter(e => e.h < 44);
  out.textOverflow = [...document.querySelectorAll('main *')].filter(vis).filter(e => { const s = getComputedStyle(e); return s.overflowX === 'hidden' && e.scrollWidth > e.clientWidth + 1 && !e.closest('.sr-only, .a-choice__unit') && !e.matches('.m-banner'); }).map(e => e.className).slice(0, 8);
  const blocks = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) { const n = walker.currentNode; if (!n.textContent.trim()) continue; const p = n.parentElement; if (!p || p.closest('script,style,.sr-only,svg,[hidden]') || !vis(p)) continue; const rg = document.createRange(); rg.selectNodeContents(n); const r = rg.getBoundingClientRect(); blocks.push([r.top + scrollY, r.bottom + scrollY]); }
  document.querySelectorAll('img, main svg, .m-compare, input, textarea').forEach(e => { if (vis(e)) { const r = e.getBoundingClientRect(); blocks.push([r.top + scrollY, r.bottom + scrollY]); } });
  blocks.sort((a, b) => a[0] - b[0]);
  let end = 0, gap = 0, at = 0;
  blocks.forEach(b => { if (b[0] - end > gap) { gap = b[0] - end; at = end; } end = Math.max(end, b[1]); });
  out.biggestGap = { px: Math.round(gap), atY: Math.round(at) };
  out.h1 = document.querySelectorAll('h1').length;
  const words = []; const tw = document.createTreeWalker(document.querySelector('main'), NodeFilter.SHOW_TEXT);
  while (tw.nextNode()) { const n = tw.currentNode, p = n.parentElement; if (!n.textContent.trim() || p.closest('script,style,.sr-only,svg,[hidden]') || !vis(p)) continue; words.push(n.textContent); }
  out.wordsInMain = words.join(' ').split(/\s+/).filter(Boolean).length;   /* revision.md's rule: words a visitor can see in main, sr-only text left out */
  out.headings = [...document.querySelectorAll('main h1, main h2, main h3')].map(h => h.tagName[1]).join('');
  return out;
}
"""

FOCUS = r"""
() => {
  const e = document.activeElement;
  if (!e || e === document.body) return null;
  const has = n => { if (!n) return false; const s = getComputedStyle(n), a = getComputedStyle(n, '::after'); return (s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0) || s.boxShadow !== 'none' || a.boxShadow !== 'none'; };   /* a tile's ring is on its ::after, above the photo */
  const face = e.matches('.a-choice__input') ? e.nextElementSibling : e.matches('.m-compare__range') ? e.parentElement.querySelector('.m-compare__knob') : null;
  const r = e.getBoundingClientRect();
  return { tag: e.tagName, label: (e.getAttribute('aria-label') || e.textContent || e.name || '').trim().slice(0, 30), ok: has(e) || has(face), onScreen: r.bottom > 0 && r.top < innerHeight };
}
"""


def norm(s):
    s = s.replace('†', '').replace('**', '').replace('’', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()


def scroll_through(page, step):
    h = page.evaluate('document.documentElement.scrollHeight')
    y = 0
    while y < h:
        page.evaluate('y => scrollTo({top: y, behavior: "instant"})', y)
        page.wait_for_timeout(160)
        y += step
    page.wait_for_timeout(900)
    page.evaluate('scrollTo({top: 0, behavior: "instant"})')
    page.wait_for_timeout(300)


def sheet(paths, out, cols, cell_w):
    if not paths:
        return
    ims = []
    for p in paths:
        im = Image.open(p).convert('RGB')
        im.thumbnail((cell_w, 10000))
        ims.append(im)
    h = max(i.size[1] for i in ims)
    rows = (len(ims) + cols - 1) // cols
    s = Image.new('RGB', (cols * cell_w + (cols - 1) * 6, rows * h + (rows - 1) * 6), 'white')
    for n, im in enumerate(ims):
        s.paste(im, ((n % cols) * (cell_w + 6), (n // cols) * (h + 6)))
    s.save(out, quality=80)


def copy_section(section):
    """Lines of one page's section in copy.md that should be visible. Drops meta, alts, notes and HOLD lines."""
    text = open(COPY, encoding='utf-8').read()
    m = re.search(re.escape(section) + r'\n(.*?)(?=\n---\n|\Z)', text, re.S)
    if not m:
        return []
    chunks = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith('-') or re.search(r'meta |image alt|^- alt|hold|accessible|final-only|^- slider|^- pairs|^- each ', line, re.I):
            continue
        line = re.sub(r'^-\s*(\*\*)?', '', line)
        line = re.sub(r'^(Headline|Body|Lede|Supporting|Button|Call link|Call line|Text link|Label|Statement|Line|Note line|Second paragraph|Value|Link|Form heading|Column label|Number|Hours|Field hint|Success|Helper|Chips|Items|Options)\s*[:.]\s*', '', line)
        for part in re.split(r'(?<=[.?!])\s+|;\s+|\s/\s', line):
            part = re.sub(r'^.*?:\s(?=[A-Z])', '', part) if part.count(':') == 1 and len(part) > 60 else part
            part = part.strip(' .;')
            if len(part) > 2:
                chunks.append(part)
    return chunks


def main():
    args = sys.argv[1:]
    path, outdir = args[0], args[1]
    section = args[args.index('--section') + 1] if '--section' in args else None
    init = open(args[args.index('--init') + 1], encoding='utf-8').read() if '--init' in args else None
    global BASE
    if '--port' in args:   # each session has its own preview port (build/COORDINATION.md)
        BASE = 'http://127.0.0.1:%s/' % args[args.index('--port') + 1]
    if '--no-shots' not in args:
        os.makedirs(outdir, exist_ok=True)
    copy_text = norm(open(COPY, encoding='utf-8').read())
    report = {'page': path}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            for w, h in SIZES:
                ctx = browser.new_context(viewport={'width': w, 'height': h})
                if init:
                    ctx.add_init_script(init)
                page = ctx.new_page()
                logs, bad = [], []
                page.on('console', lambda m: logs.append(m.type + ': ' + m.text) if m.type in ('error', 'warning') else None)
                page.on('pageerror', lambda e: logs.append('pageerror: ' + str(e)))
                page.on('response', lambda r: bad.append('%d %s' % (r.status, r.url)) if r.status >= 400 else None)
                page.on('requestfailed', lambda r: bad.append('failed ' + r.url))
                page.goto(BASE + path, wait_until='load')
                page.add_style_tag(content=HIDE_BARS)
                page.mouse.move(0, 0)
                page.wait_for_timeout(1800)
                scroll_through(page, int(h * .8))
                r = page.evaluate(MEASURE)
                r['console'] = logs
                r['network'] = bad
                # screen stops
                stops = []
                total = page.evaluate('document.documentElement.scrollHeight')
                y, n = 0, 0
                while y < total:
                    page.evaluate('y => scrollTo({top: y, behavior: "instant"})', y)
                    page.wait_for_timeout(120)
                    if '--no-shots' not in args:   # measures only, for when disk space is short (a full disk cut off batch d)
                        p = os.path.join(outdir, '%s-%d-%02d-studio.png' % (re.sub(r'\W+', '-', path.replace('.html', '')), w, n))
                        page.screenshot(path=p)
                        stops.append(p)
                    y += h - 92 if w > 640 else h - 64
                    n += 1
                if stops:
                    sheet(stops, os.path.join(outdir, 'sheet-%d.jpg' % w), 4 if w > 640 else 7, 480 if w > 640 else 220)
                r['stops'] = n
                # tab through
                if '--no-tab' not in args:
                    page.evaluate('scrollTo({top: 0, behavior: "instant"})')
                    page.reload(wait_until='load')
                    page.add_style_tag(content=HIDE_BARS)
                    page.wait_for_timeout(1000)
                    seen, missing, offscreen, first = 0, [], [], None
                    for _ in range(170):
                        page.keyboard.press('Tab')
                        f = page.evaluate(FOCUS)
                        if f is None:
                            break
                        seen += 1
                        first = first or f['label']
                        if not f['ok']:
                            missing.append(f['tag'] + ':' + f['label'])
                        if not f['onScreen']:
                            offscreen.append(f['tag'] + ':' + f['label'])
                    r['tab'] = {'stops': seen, 'first': first, 'noFocusRing': missing[:12], 'offScreen': offscreen[:12]}
                r.pop('images', None)
                report[str(w)] = r
                ctx.close()
            # reduced motion
            ctx = browser.new_context(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
            page = ctx.new_page()
            page.goto(BASE + path, wait_until='load')
            page.wait_for_timeout(500)
            report['reducedMotion'] = page.evaluate(r"""() => ({
              hidden: [...document.querySelectorAll('.a-inview,.a-reveal,.a-hero__line')].filter(e => +getComputedStyle(e).opacity < 1 || getComputedStyle(e).transform !== 'none').length,
              running: document.getAnimations().filter(a => a.playState === 'running').length })""")
            # copy, both ways
            texts = page.evaluate(r"""() => { const out = []; const w = document.createTreeWalker(document.querySelector('main'), NodeFilter.SHOW_TEXT); while (w.nextNode()) { const n = w.currentNode, p = n.parentElement; if (!n.textContent.trim() || p.closest('script,style')) continue; out.push(n.textContent); } return out; }""")
            page_text = norm(' '.join(texts))
            report['textNotInCopy'] = sorted({t.strip() for t in texts if norm(t).strip('"') not in copy_text and not re.match(r'^[\s\d]+$', t)})
            if section:
                chunks = copy_section(section)
                report['copyNotOnPage'] = [c for c in chunks if norm(c).strip('"') not in page_text]
            ctx.close()
        finally:
            browser.close()
    print(json.dumps(report, indent=1))


if __name__ == '__main__':
    main()
