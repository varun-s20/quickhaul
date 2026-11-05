"""Quick Haul: image derivatives.

Reads data/images.json, crops each original in src/stock/ to its slot ratio around its focal point,
applies the one photo grade from the design spec (2c), and writes <name>-<width>.webp plus one
<name>.jpg fallback into assets/images/<folder>/. Never upscales: a width wider than the crop is
skipped. Writes data/image-manifest.json with the real size of every file, which tools/build.py
reads to fill width, height and srcset. Rerunning changes nothing unless an input changed.

Usage: python tools/images.py [--force]   (from the site folder; needs Pillow, already installed)
"""
import json
import os
import sys

from PIL import Image, ImageEnhance, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOBS = os.path.join(ROOT, 'data', 'images.json')
MANIFEST = os.path.join(ROOT, 'data', 'image-manifest.json')
STOCK = os.path.join(ROOT, 'src', 'stock')
OUT = os.path.join(ROOT, 'assets', 'images')

FALLBACK_MAX = 1000   # the <img> fallback: the largest derivative at or under this width, as JPEG


# The grade's values. Was spec 2c's saturation .85, contrast 1.10 and a small per-channel cool gain, which left the stock
# colourful against the slate. (Checkpoint 2c, 4 Nov: "make it stronger so the red pickup and orange truck sit inside
# the slate palette.")
SAT_ALL = 0.42    # every other hue
SAT_GREEN = 0.24  # yellow-greens through teals (critic, rerun 1: leaves stayed vivid against the slate, and a teal tool case was the one loud colour left)
SAT_WARM = 0.06   # reds through oranges (trucks, brick). At .34 and .14 what was left of them read as pink
CONTRAST = 1.03   # was spec 2c's 1.10, then 1.10 with the tone map on top: photos went crunchy (critic, rerun 1)
TONE_MIX = 0.34   # how much of the slate tone map is laid over the photo
INK, SLATE = (15, 20, 28), (52, 61, 78)   # tokens: --c-ink, --c-slate
TONE_HIGH = (236, 237, 240)   # not --c-cream: cream's warm cast in the highlights tinted pale trucks and trim pink
TONE_MID = 72     # luminance that lands on the slate. Close to the slate's own grey, so mid tones keep their detail (90 crushed them)


def warm_lut(v):
    """Pillow's hue band runs 0 to 255, red at 0 and orange near 20. Full strength on reds and oranges, ramping out
    over yellow and magenta so no hard edge shows where a hue crosses the line."""
    if v <= 30 or v >= 236:
        return 255
    if v < 46:
        return int(255 * (46 - v) / 16)
    if v > 220:
        return int(255 * (v - 220) / 16)
    return 0


def green_lut(v):
    """Greens sit near 85 and teals near 125 on Pillow's hue band; the slate's own blue is at 155 and is left alone.
    Full strength from yellow-green to teal, ramping out on both sides."""
    if 46 <= v <= 135:
        return 255
    if 36 <= v < 46:
        return int(255 * (v - 36) / 10)
    if 135 < v <= 150:
        return int(255 * (150 - v) / 15)
    return 0


def grade(im):
    """One grade for every photo: desaturate (warm hues hardest), lift the contrast, then lay a tone map from
    ink through slate to cream over the result, so every photo shares the site's own shadows and highlights."""
    h, s, v = im.convert('HSV').split()
    base = s.point(lambda x: int(x * SAT_ALL))
    base = Image.composite(s.point(lambda x: int(x * SAT_GREEN)), base, h.point(green_lut))
    s = Image.composite(s.point(lambda x: int(x * SAT_WARM)), base, h.point(warm_lut))
    im = Image.merge('HSV', (h, s, v)).convert('RGB')
    im = ImageEnhance.Contrast(im).enhance(CONTRAST)
    tone = ImageOps.colorize(im.convert('L'), black=INK, white=TONE_HIGH, mid=SLATE, midpoint=TONE_MID)
    return Image.blend(im, tone, TONE_MIX)


def crop(im, ratio, focus, zoom=1):
    """Largest crop of the slot's ratio around the focal point. zoom above 1 tightens it, for keeping something out of
    frame (the pickup's number plate). Tightening lowers the crop's pixels, so check its size against the slot."""
    w, h = im.size
    if w / h > ratio:
        cw, ch = int(round(h * ratio / zoom)), int(round(h / zoom))
    else:
        cw, ch = int(round(w / zoom)), int(round(w / ratio / zoom))
    fx, fy = focus
    left = min(max(int(round(fx * w - cw / 2)), 0), w - cw)
    top = min(max(int(round(fy * h - ch / 2)), 0), h - ch)
    return im.crop((left, top, left + cw, top + ch))


def main():
    jobs = json.load(open(JOBS, encoding='utf-8'))['images']
    # Only cuts what is missing, one photo at a time, because this machine's memory is tight. After changing a crop or
    # the grade, run with --force to recut everything.
    old = json.load(open(MANIFEST, encoding='utf-8')) if os.path.exists(MANIFEST) and '--force' not in sys.argv else {}
    manifest = {}
    for job in jobs:
        had = old.get(job['name'])
        if had and all(os.path.exists(os.path.join(ROOT, w['file'])) for w in had['webp']):
            manifest[job['name']] = had
            continue
        src = os.path.join(STOCK, job['src'])
        if not os.path.exists(src):
            sys.exit('Missing original: ' + src)
        folder = os.path.join(OUT, job['folder'])
        os.makedirs(folder, exist_ok=True)
        im = Image.open(src).convert('RGB')
        im = grade(crop(im, job['ratio'], job['focus'], job.get('zoom', 1)))
        cw, ch = im.size
        entry = {'folder': job['folder'], 'crop': [cw, ch], 'webp': [], 'fallback': None}
        made = []
        for width in job['widths']:
            if width > cw:
                print('  skip %s-%d: crop is only %dpx wide (no upscaling)' % (job['name'], width, cw))
                continue
            height = int(round(width * ch / cw))
            made.append((width, height))
        if cw < job['widths'][-1] and (not made or made[-1][0] != cw):
            made.append((cw, ch))   # the list stopped short of the crop: offer the full crop as the top size
        for width, height in made:
            name = '%s-%d.webp' % (job['name'], width)
            path = os.path.join(folder, name)
            im.resize((width, height), Image.LANCZOS).save(path, 'WEBP', quality=job.get('quality', 78), method=6)
            entry['webp'].append({'file': 'assets/images/%s/%s' % (job['folder'], name), 'w': width, 'h': height})
        fb = [m for m in made if m[0] <= FALLBACK_MAX][-1]
        fb_name = '%s.jpg' % job['name']
        im.resize(fb, Image.LANCZOS).save(os.path.join(folder, fb_name), 'JPEG', quality=80, optimize=True, progressive=True)
        entry['fallback'] = {'file': 'assets/images/%s/%s' % (job['folder'], fb_name), 'w': fb[0], 'h': fb[1]}
        manifest[job['name']] = entry
        print('%s: crop %dx%d, %s' % (job['name'], cw, ch, ', '.join(str(m[0]) for m in made)))
    with open(MANIFEST, 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, indent=1)
        fh.write('\n')


if __name__ == '__main__':
    main()
