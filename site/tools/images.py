"""Quick Haul: image derivatives.

Reads data/images.json, crops each original in src/stock/ to its slot ratio around its focal point and writes
<name>-<width>.webp plus one <name>.jpg fallback into assets/images/<folder>/. Crop and resize only, full colour: no
desaturation, no tone map, no cool shift, no grain (Varun, 4 Nov: "full colour, not monochrome"; design/revision.md
section 6). The one thing added is the usual small unsharp after a big downscale, which touches edges, never colour.
Never upscales: a width wider than the crop is skipped. Writes data/image-manifest.json with the real size of every
file, which tools/build.py reads to fill width, height and srcset. Also cuts the logo's round mark at its native pixels.
Rerunning changes nothing unless an input changed.

Usage: python tools/images.py [--force] [--only=name,name]   (from the site folder; needs Pillow, already installed)
"""
import json
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOBS = os.path.join(ROOT, 'data', 'images.json')
MANIFEST = os.path.join(ROOT, 'data', 'image-manifest.json')
STOCK = os.path.join(ROOT, 'src', 'stock')
OUT = os.path.join(ROOT, 'assets', 'images')
FX = os.path.join(ROOT, 'assets', 'fx')
LOGO = os.path.join(os.path.dirname(ROOT), 'assets', 'logo.png')
MARK = os.path.join(OUT, 'brand', 'quickhaul-mark.png')

FALLBACK_MAX = 1000   # the <img> fallback: the largest derivative at or under this width, as JPEG

# Critic (revision r2): the fridge's source is soft (sharpness 183 against 2,362 and up on its neighbours). A stronger
# pass helps; only a new photo can fix it, so it stays on the open list. radius, percent, threshold, by original file.
EXTRA_SHARP = {'fridge-in-room.jpg': (2.2, 90, 1)}

# Same rule as the crops: no brand on stock. Hover and other window widths show more of a photo than its resting crop does,
# so a mark has to go from the file, not just from one view (critic, home r2: the Isuzu badge came out from behind a tile's pill).
# Boxes are x0, y0, x1, y1 in the source's pixels, and leave room round the mark for the feather. The ways of filling one:
# - left to right, the default: a blend between the surface on its left and on its right, row by row. For smooth surfaces. A patch
#   copied from further along showed as a grey square on the fridge, because its door brightens from left to right.
# - 't', from the surface above only, column by column: where neither side nor below will do (the bucket, between a stick and a tyre).
# - 'c', dx, dy, and optionally inset, feather: a copy from that far away, for a surface with texture of its own (the tailgate, whose
#   blend came out as a dark smudge with a hard edge).
# - 'cb', dxL, dyL, dxR, dyR: copies from both sides, blended across, for foliage in changing light (the hedge is lit on the sign's left
#   and shaded on its right, so a copy from either side alone showed as a rectangle).
# - 'flat', (r, g, b): a printed label on something round. One colour, with the columns' own light and dark kept, so it stays a can and loses its print.
# - 'ink', [points], delta: letters on a flat coloured part whose edges run at an angle, so no box fits. Inside the polygon, any pixel more than
#   delta from the polygon's median brightness is grown over from its clean neighbours (the trimmer's blade cover).
# Beyond revision.md's "the only one", which was the fridge: logged in content/placeholders.md. Small labels on bottles and boxes in the before photo's clutter are left.
RETOUCH = {
    'fridge-in-room.jpg': [(1222, 618, 1300, 702), (1352, 618, 1436, 702), (1493, 618, 1560, 702), (1620, 618, 1697, 702)],
    # ARIENS, its gear emblem, the engine's Kawasaki label, Cub Cadet, the Benjamin Moore bucket. HEDGE SWEEP and its mark on the trimmer's blade cover (critic, Services r2)
    'garage-clutter-before.jpg': [(1440, 1183, 1582, 1216), (1486, 1224, 1538, 1274), (1476, 1153, 1560, 1172), (927, 1021, 1018, 1047), (712, 1152, 760, 1206, 't'), (420, 972, 556, 1020, 'ink', [(424, 1001), (550, 976), (553, 993), (427, 1018)], 22)],
    # Rain Bird: the box leaves 4px round the letters. The first try left them faint but legible, because the feather ate into a box this short
    # Reviews shows the whole wall (critic, Reviews r1: less floor), so five Spikeball tags, Clicgear and Yakima come out too. Each polygon stays inside its tag, so the net and the wall aren't touched
    'garage-after.jpg': [(979, 818, 1044, 840), (1192, 485, 1222, 547, 'ink', [(1197, 485), (1222, 487), (1218, 547), (1192, 546)], 40), (1068, 568, 1133, 615, 'ink', [(1073, 568), (1133, 588), (1125, 615), (1068, 596)], 40), (1280, 578, 1345, 617, 'ink', [(1280, 590), (1342, 578), (1345, 602), (1286, 617)], 40), (1105, 686, 1163, 750, 'ink', [(1105, 732), (1145, 686), (1163, 702), (1122, 750)], 40), (1236, 688, 1292, 754, 'ink', [(1236, 702), (1262, 688), (1292, 740), (1268, 754)], 40), (2022, 690, 2096, 716, 'ink', [(2022, 690), (2096, 690), (2096, 716), (2022, 716)], 30), (2046, 1170, 2092, 1256, 'ink', [(2056, 1170), (2092, 1170), (2082, 1256), (2046, 1256)], 30)],
    # ISUZU D-MAX on the tailgate, right against the tail light. SATELLITE and the small badge on the door (critic, Services r2: both read at 2560), each copied from further along the same rows, so the door's light stripe runs on
    'pickup-trash-bags.jpg': [(317, 1182, 470, 1266, 'c', 155, 0, 6, 3), (2524, 930, 2576, 958, 'c', -60, 0, 3, 2), (2580, 930, 2616, 956, 'c', 36, 0, 3, 2)],
    # the house's number, because nothing on a page that says local should point at a real address somewhere else
    'fall-house-drive.jpg': [(1958, 1142, 1994, 1168)],
    # WD-40 (three bands of the can), Kjeldsens (line of type, oval, either side of the saw's frame), Berol Dexter, Shelby, Piedmont, Ironman
    'cellar-shelves.jpg': [(706, 716, 805, 1016, 'flat', (58, 72, 112)), (1130, 983, 1296, 1018, 'ink', [(1130, 983), (1296, 996), (1296, 1018), (1130, 1018)], 26), (1290, 980, 1350, 1036, 'c', -70, 0, 6, 3), (1372, 985, 1392, 1032, 'c', 22, 0, 3, 2), (82, 740, 140, 770, 't'), (215, 148, 310, 192, 'ink', [(215, 148), (310, 148), (310, 192), (215, 192)], 26), (212, 440, 296, 488, 'ink', [(212, 440), (296, 440), (296, 488), (212, 488)], 26), (790, 610, 870, 645, 'ink', [(790, 610), (870, 610), (870, 645), (790, 645)], 26)],
    # John Deere on the snowblower's hood, the Crock-Pot box, the old oven's two plates, Silverwood on the crate, the script on the white box
    'storage-room-clutter.jpg': [(408, 945, 462, 1040, 'c', 55, 5, 6, 5), (1462, 788, 1486, 840), (1556, 786, 1680, 814, 'ink', [(1556, 786), (1680, 786), (1680, 814), (1556, 814)], 30), (1570, 576, 1636, 606), (1422, 920, 1465, 935, 'ink', [(1422, 920), (1465, 920), (1465, 935), (1422, 935)], 30), (942, 886, 988, 944)],
    # a ring of bricks heaped with sticks on the lawn: this crop is the after in Reviews' yard pair (critic, Reviews r2: a leftover pile under "cleared and ready to use"). Fence and grass line from along the same rows, grass from below
    'backyard-lawn-deck.jpg': [(695, 838, 880, 892, 'c', -190, 0, 8, 6), (690, 880, 885, 965, 'c', 0, 95, 8, 6)],
    # a graffitied German "private property" sign and its number plates, on a site for New England. The bare post stays
    'man-carrying-mattress.jpg': [(1758, 652, 1962, 1024, 'cb', -115, 110, 190, 40)],
}


def ink_out(im, x0, y0, size, points, delta):
    """Replaces whatever stands out from the polygon's median brightness with an average of the clean pixels around it, so the part's own colour runs over the letters. Small areas only: plain Python."""
    part = im.crop((x0, y0, x0 + size[0], y0 + size[1]))
    inside = Image.new('L', size, 0)
    ImageDraw.Draw(inside).polygon([(x - x0, y - y0) for x, y in points], fill=255)
    px, grey, mask = part.load(), part.convert('L').load(), inside.load()
    w, h = size
    cells = [(x, y) for y in range(h) for x in range(w) if mask[x, y]]
    median = sorted(grey[c] for c in cells)[len(cells) // 2]
    todo = {c for c in cells if abs(grey[c] - median) > delta}
    # grown by 2px, for the letters' soft edges
    for _ in range(2):
        todo |= {(x + dx, y + dy) for x, y in todo for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= x + dx < w and 0 <= y + dy < h and mask[x + dx, y + dy]}
    clean = {c: px[c] for c in cells if c not in todo}
    for x, y in todo:
        near = []
        for r in (6, 12, 24, 48):   # wide enough to be smooth: a small reach left the letters' blocks showing as blotches
            near = [clean[(x + dx, y + dy)] for dx in range(-r, r + 1) for dy in range(-r, r + 1) if (x + dx, y + dy) in clean]
            if len(near) >= 40:
                break
        px[x, y] = tuple(sum(c[i] for c in near) // len(near) for i in range(3))
    im.paste(part, (x0, y0), inside.filter(ImageFilter.GaussianBlur(1)))


def retouch(im, name):
    for box in RETOUCH.get(name, ()):
        x0, y0, x1, y1 = box[:4]
        mode = box[4] if len(box) > 4 else 'h'
        size = (x1 - x0, y1 - y0)
        if mode == 'ink':
            ink_out(im, x0, y0, size, box[5], box[6])
            continue
        inset, feather = 4, 2
        if mode == 'c':
            fill = im.crop((x0 + box[5], y0 + box[6], x1 + box[5], y1 + box[6]))
            inset, feather = box[7:9] if len(box) > 7 else (10, 7)
        elif mode == 'cb':
            near = im.crop((x0 + box[5], y0 + box[6], x1 + box[5], y1 + box[6]))
            far = im.crop((x0 + box[7], y0 + box[8], x1 + box[7], y1 + box[8]))
            # all the far copy from 60% across, so the near one fades out before it could reach what's being covered
            fill = Image.composite(far, near, Image.linear_gradient('L').rotate(90, expand=True).resize(size).point(lambda v: min(255, int(v / .6))))
            inset, feather = 10, 7
        elif mode == 'flat':
            shade = im.crop((x0, y0, x1, y1)).convert('L').resize((size[0], 1), Image.BOX).filter(ImageFilter.BoxBlur(3)).resize(size)
            top = shade.getextrema()[1] or 1
            fill = ImageChops.multiply(Image.new('RGB', size, box[5]), shade.point(lambda v: min(255, v * 255 // top)).convert('RGB'))
            inset, feather = 3, 2
        elif mode == 't':
            fill = im.crop((x0, y0 - 4, x1, y0)).resize((size[0], 1), Image.BOX).resize(size).filter(ImageFilter.BoxBlur(4))
        else:
            left = im.crop((x0 - 4, y0, x0, y1)).resize((1, size[1]), Image.BOX).resize(size).filter(ImageFilter.BoxBlur(4))
            right = im.crop((x1, y0, x1 + 4, y1)).resize((1, size[1]), Image.BOX).resize(size).filter(ImageFilter.BoxBlur(4))
            fill = Image.composite(right, left, Image.linear_gradient('L').rotate(90, expand=True).resize(size))
        mask = Image.new('L', size, 0)
        ImageDraw.Draw(mask).rectangle((inset, inset, size[0] - inset - 1, size[1] - inset - 1), fill=255)
        im.paste(fill, (x0, y0), mask.filter(ImageFilter.GaussianBlur(feather)))
    return im


def crop(im, ratio, focus, zoom=1):
    """Largest crop of the slot's ratio around the focal point. zoom above 1 tightens it, for keeping something out of
    frame (the pickup's number plate). Tightening lowers the crop's pixels, so check its size against the slot."""
    w, h = im.size
    if w / h > ratio:
        cw, ch = h * ratio / zoom, h / zoom
    else:
        cw, ch = w / zoom, w / ratio / zoom
    fx, fy = focus
    x = min(max(fx * w - cw / 2, 0), w - cw)
    y = min(max(fy * h - ch / 2, 0), h - ch)
    return im.crop((int(round(x)), int(round(y)), int(round(x + cw)), int(round(y + ch))))


def logo_mark():
    """The mark in the phone screenshot at its native 234px, hard inner disc with a short soft rim, so the screenshot's
    wall melts into the slate badge behind it. No resampling of the mark itself: nothing softer than the file."""
    os.makedirs(os.path.dirname(MARK), exist_ok=True)
    with Image.open(LOGO) as raw:
        src = raw.convert('RGB')
    cx, cy, r = 372, 798.6, 117   # measured on the screenshot for the built site
    mark = src.crop((int(round(cx - r)), int(round(cy - r)), int(round(cx + r)), int(round(cy + r))))
    size = mark.width
    ss = 4
    mask = Image.new('L', (size * ss, size * ss), 0)
    draw = ImageDraw.Draw(mask)
    outer, inner, steps = size * ss / 2, size * ss / 2 * .94, 10
    for i in range(steps + 1):
        rad = outer - (outer - inner) * i / steps
        draw.ellipse((outer - rad, outer - rad, outer + rad, outer + rad), fill=int(255 * (i / steps)))
    mark.putalpha(mask.resize((size, size), Image.LANCZOS))
    mark.save(MARK, 'PNG', optimize=True)
    print('logo mark %dx%d' % mark.size)


def main():
    force = '--force' in sys.argv
    if force or not os.path.exists(MARK):
        logo_mark()
    jobs = json.load(open(JOBS, encoding='utf-8'))['images']
    # Only cuts what is missing, one photo at a time, because this machine's memory is tight. After changing a crop,
    # run with --force to recut everything.
    old = json.load(open(MANIFEST, encoding='utf-8')) if os.path.exists(MANIFEST) and not force else {}
    only = next((a.split('=', 1)[1].split(',') for a in sys.argv if a.startswith('--only=')), [])
    manifest = {}
    for job in jobs:
        had = old.get(job['name'])
        if had and job['name'] not in only and all(os.path.exists(os.path.join(ROOT, w['file'])) for w in had['webp']):
            manifest[job['name']] = had
            continue
        src = os.path.join(STOCK, job['src'])
        if not os.path.exists(src):
            sys.exit('Missing original: ' + src)
        fx = job.get('fx', False)   # a decorative file only the CSS uses, so it goes to assets/fx/ and needs no fallback (conventions)
        folder = FX if fx else os.path.join(OUT, job['folder'])
        web = 'assets/fx' if fx else 'assets/images/' + job['folder']
        os.makedirs(folder, exist_ok=True)
        with Image.open(src) as raw:
            im = crop(retouch(raw.convert('RGB'), job['src']), job['ratio'], job['focus'], job.get('zoom', 1))
        cw, ch = im.size
        entry = {'folder': web, 'crop': [cw, ch], 'webp': [], 'fallback': None}
        made = []
        for width in job['widths']:
            if width > cw:
                print('  skip %s-%d: crop is only %dpx wide (no upscaling)' % (job['name'], width, cw))
                continue
            made.append((width, int(round(width * ch / cw))))
        if cw < job['widths'][-1] and (not made or made[-1][0] != cw):
            made.append((cw, ch))   # the list stopped short of the crop: offer the full crop as the top size
        for width, height in made:
            name = '%s-%d.webp' % (job['name'], width)
            part = im.resize((width, height), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1, percent=55, threshold=2))
            if job['src'] in EXTRA_SHARP:
                part = part.filter(ImageFilter.UnsharpMask(*EXTRA_SHARP[job['src']]))
            part.save(os.path.join(folder, name), 'WEBP', quality=job.get('quality', 78), method=5)
            entry['webp'].append({'file': '%s/%s' % (web, name), 'w': width, 'h': height})
        if not fx:
            limit = job.get('fallback_max', FALLBACK_MAX)
            fb = [m for m in made if m[0] <= limit][-1]
            fb_name = '%s.jpg' % job['name']
            im.resize(fb, Image.LANCZOS).save(os.path.join(folder, fb_name), 'JPEG', quality=80, optimize=True, progressive=True)
            entry['fallback'] = {'file': '%s/%s' % (web, fb_name), 'w': fb[0], 'h': fb[1]}
        im.close()
        manifest[job['name']] = entry
        print('%s: crop %dx%d, %s' % (job['name'], cw, ch, ', '.join(str(m[0]) for m in made)))
    with open(MANIFEST, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(manifest, fh, indent=1)
        fh.write('\n')


if __name__ == '__main__':
    main()
