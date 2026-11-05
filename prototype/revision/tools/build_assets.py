#!/usr/bin/env python3
"""Quick Haul: assets for the revision prototype (2026-11-04).

Colour photo treatment under test: crop and resize only. No desaturation, no tone map, no cool shift, no grain. This is
what site/tools/images.py becomes once Varun signs off on design/revision.md. Originals stay untouched in site/src/stock/.
Also copies the site's fonts and cuts the logo's circle at its native pixels (no resampling, so nothing softer than the file).

Usage: python tools/build_assets.py            all of it (from prototype/revision; needs Pillow, already installed)
       python tools/build_assets.py svc- page-  only the photo jobs whose names start with these, leaving everything else alone
"""
import json
import os
import shutil
import sys

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROJECT = os.path.dirname(os.path.dirname(ROOT))
STOCK = os.path.join(PROJECT, 'site', 'src', 'stock')
OUT = os.path.join(ROOT, 'assets', 'images')
FONTS = os.path.join(ROOT, 'assets', 'fonts')
FX = os.path.join(ROOT, 'assets', 'images', 'brand')
NEW = os.path.join(ROOT, 'stock-new')   # photos downloaded in revision round 2, each in its own folder. Stock, must-replace, logged in design/revision.md

# name, source, ratio (w/h), focus (x, y as 0 to 1), zoom, widths. Focus values reuse site/data/images.json where the
# plate and badge crops were already worked out (placeholders.md): pickup plate and Isuzu badge, SMEG badge, Elliot mark.
JOBS = [
    ('hero-yard', 'backyard-lawn-deck.jpg', 16 / 9, (.5, .46), 1, (1000, 1600, 2200)),
    ('hero-yard-phone', 'backyard-lawn-deck.jpg', .62, (.68, .5), 1, (500, 800)),
    ('tile-junk', 'pickup-trash-bags.jpg', 1.6, (.44, .36), 1.44, (500, 900, 1500)),
    ('tile-mattress', 'man-carrying-mattress.jpg', 1.3, (.62, .5), 1, (500, 800, 1100)),
    ('tile-sofa', 'sofa-by-door.jpg', 1, (.4, .74), 1, (400, 700, 900)),
    # Badge painted out (RETOUCH below), so the crop can show the fridge's top and both handles instead of a pale door (critic r2-1)
    ('tile-fridge', 'fridge-in-room.jpg', 1, (.6, .44), 1, (400, 700, 900)),
    ('tile-yard', 'yard-waste-truck.jpg', 1, (.62, .62), 1, (400, 700, 900)),
    # Critic r1: the box room read as a sneaker stockroom (Nike and FILA lids). Critic r2-2: the tidy tool wall read as garage organising. The tile's line is "Clear the floor and get the room back", so it takes the cleared floor
    ('tile-garage', 'basement-cleared.jpg', 1.3, (.5, .62), 1, (500, 800, 1100)),
    # Critic r2-2: the building site read as construction, and its board stamps and machine name needed cropping round. An old shed is what Shawn's demo line names
    ('tile-demo', 'shed-weathered.jpg', 1.7, (.52, .56), 1, (500, 900, 1500)),
    # The two crops line up on the floor: wall and floor meet at about the same height, so the divider doesn't jump between rooms
    ('compare-before', 'garage-clutter-before.jpg', 1.6, (.45, .66), 1.1, (700, 1300, 2000)),
    # Critic r1: the old crop was full of ladders and bins, so this one starts past the ladders. Critic r2-1: a finished basement promises a renovation. Critic r2-2: a bare grey basement looked colourless beside the warm "before". This is a garage for a garage, cream wall to cream wall, concrete floor to concrete floor. Still two different rooms until Shawn sends a real pair; no free matched pair turned up (searched 2026-11-04). This crop also keeps the Yakima mark on the far right out of frame
    ('compare-after', 'garage-after.jpg', 1.6, (.525, .82), 1.6, (700, 1300, 1500)),
    # Critic r1: an old Chevy said nothing about towns. Critic r2: the Le Havre rooftops didn't read as MA or NH. Critic r2-2: a fenced yard said little about towns either, and repeated the hero's. A real New England street, in the service region. Must-replace
    ('towns-street', os.path.join(NEW, 'portsmouth-street', 'portsmouth-street.jpg'), 1.05, (.62, .62), 1, (500, 800, 1100)),
    # Critic r2: the garage wall repeated the clean-outs tile. Plain joists at 14% are texture, not a second picture
    ('footer-joists', 'basement-unfinished.jpg', 2.4, (.5, .3), 1, (1400,)),
    # Revision round 2, inner-page prototype. The banner wants a real street for the truck to park on: Portsmouth, NH, in the service region (Varun's default at checkpoint R1 allows a New England street). The wide crop keeps the road at the bottom right, where the truck parks.
    ('page-street', os.path.join(NEW, 'portsmouth-street', 'portsmouth-street.jpg'), 2.3, (.5, .68), 1, (1000, 1600, 2200)),
    # Phones: the road and the two far houses, so the truck stands on tarmac rather than on a shingle wall
    ('page-street-phone', os.path.join(NEW, 'portsmouth-street', 'portsmouth-street.jpg'), .74, (.74, .6), 1, (500, 800)),
    # Services bands. Same plate and badge rules as the tiles above (placeholders.md)
    # Anchored to the top of the photo: the plate and the tailgate badge sit below this crop
    ('svc-junk', 'pickup-trash-bags.jpg', 2.1, (.5, .28), 1.26, (700, 1300, 2000)),
    # Tight on the bench and the yellow mower: the orange mower's maker name (Ariens) stays out of frame
    ('svc-garage', 'garage-clutter-before.jpg', 1.14, (.2, .62), 1.34, (500, 800, 1100)),
    # Portrait: a fridge, a chair and a man under a mattress all stand upright, and a landscape crop left the fridge as a pale slab (critic r2-1)
    ('svc-sofa', 'sofa-by-door.jpg', .86, (.4, .72), 1, (400, 700, 900)),
    ('svc-fridge', 'fridge-in-room.jpg', .86, (.6, .51), 1, (400, 700, 900)),
    ('svc-mattress', 'man-carrying-mattress.jpg', .86, (.61, .5), 1, (400, 700, 900)),
    # The orange truck over the heap of branches: a heap alone filled the frame and read as texture, not a job
    ('svc-yard', 'yard-waste-truck.jpg', 1.5, (.5, .62), 1, (500, 800, 1200)),
    ('svc-shed', 'shed-weathered.jpg', 1.5, (.52, .56), 1, (500, 800, 1200)),
]

# Critic r2: the fridge's source is soft (sharpness 183 against 2,362 and up on its neighbours). A stronger pass helps; only a new photo can fix it, so it stays on the open list.
EXTRA_SHARP = {'tile-fridge': (2.2, 90, 1), 'svc-fridge': (2.2, 90, 1)}

# Same rule as the crops: no brand on stock. The door is smooth, so each letter of the fridge's badge is filled with a blend between the door on its left and on its right, row by row, feathered.
# A patch copied from further along showed as a grey square, because the door brightens from left to right. Boxes are x0, y0, x1, y1 in the source's pixels. Must-replace like the rest.
RETOUCH = {'fridge-in-room.jpg': [(1222, 618, 1300, 702), (1352, 618, 1436, 702), (1493, 618, 1560, 702), (1620, 618, 1697, 702)]}


def retouch(im, name):
    for x0, y0, x1, y1 in RETOUCH.get(name, ()):
        size = (x1 - x0, y1 - y0)
        left = im.crop((x0 - 4, y0, x0, y1)).resize((1, size[1]), Image.BOX).resize(size).filter(ImageFilter.BoxBlur(4))
        right = im.crop((x1, y0, x1 + 4, y1)).resize((1, size[1]), Image.BOX).resize(size).filter(ImageFilter.BoxBlur(4))
        across = Image.linear_gradient('L').rotate(90, expand=True).resize(size)
        mask = Image.new('L', size, 0)
        ImageDraw.Draw(mask).rectangle((4, 4, size[0] - 5, size[1] - 5), fill=255)
        im.paste(Image.composite(right, left, across), (x0, y0), mask.filter(ImageFilter.GaussianBlur(2)))
    return im


def crop(im, ratio, focus, zoom):
    w, h = im.size
    cw, ch = (h * ratio, h) if w / h > ratio else (w, w / ratio)
    cw, ch = cw / zoom, ch / zoom
    x = min(max(focus[0] * w - cw / 2, 0), w - cw)
    y = min(max(focus[1] * h - ch / 2, 0), h - ch)
    return im.crop((int(round(x)), int(round(y)), int(round(x + cw)), int(round(y + ch))))


def photos(only=()):
    os.makedirs(OUT, exist_ok=True)
    manifest = {}
    manifest_path = os.path.join(OUT, 'manifest.json')
    if only and os.path.exists(manifest_path):
        with open(manifest_path, encoding='utf-8') as fh:
            manifest = json.load(fh)
    for old in os.listdir(OUT):
        if old.endswith(('.webp', '.jpg')) and (not only or old.startswith(tuple(only))):
            os.remove(os.path.join(OUT, old))
    for name, src, ratio, focus, zoom, widths in JOBS:
        if only and not name.startswith(tuple(only)):
            continue
        with Image.open(os.path.join(STOCK, src)) as raw:
            im = crop(retouch(raw.convert('RGB'), src), ratio, focus, zoom)
        made = []
        for w in widths:
            if w > im.width:
                continue
            h = round(w * im.height / im.width)
            # the usual small unsharp after a big downscale: it touches edges only, never colour (critic r1: the fridge looked soft beside its neighbours)
            part = im.resize((w, h), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1, percent=55, threshold=2))
            if name in EXTRA_SHARP:
                r, p, t = EXTRA_SHARP[name]
                part = part.filter(ImageFilter.UnsharpMask(radius=r, percent=p, threshold=t))
            part.save(os.path.join(OUT, '%s-%d.webp' % (name, w)), 'WEBP', quality=78, method=5)
            made.append([w, h])
        # jpg fallback at the middle size
        fw, fh = made[len(made) // 2] if len(made) > 1 else made[0]
        im.resize((fw, fh), Image.LANCZOS).save(os.path.join(OUT, name + '.jpg'), 'JPEG', quality=80, optimize=True, progressive=True)
        manifest[name] = {'src': os.path.basename(src), 'crop': list(im.size), 'files': made, 'fallback': [fw, fh]}
        im.close()
        print(name, im.size if False else '', made)
    current = set(job[0] for job in JOBS)
    manifest = dict((k, v) for k, v in manifest.items() if k in current)
    with open(os.path.join(OUT, 'manifest.json'), 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, indent=1)


def logo():
    os.makedirs(FX, exist_ok=True)
    with Image.open(os.path.join(PROJECT, 'assets', 'logo.png')) as raw:
        src = raw.convert('RGB')
    cx, cy, r = 372, 798.6, 117    # the mark in the phone screenshot, as measured for the built site
    box = (int(round(cx - r)), int(round(cy - r)), int(round(cx + r)), int(round(cy + r)))
    mark = src.crop(box)           # native pixels, untouched
    size = mark.width
    ss = 4
    # hard inner disc with a short soft rim, so the screenshot's wall melts into the slate badge behind it
    mask = Image.new('L', (size * ss, size * ss), 0)
    d = ImageDraw.Draw(mask)
    steps = 10
    outer = size * ss / 2
    inner = outer * .94
    for i in range(steps + 1):
        rad = outer - (outer - inner) * i / steps
        v = int(255 * (i / steps))
        d.ellipse((outer - rad, outer - rad, outer + rad, outer + rad), fill=v)
    mark.putalpha(mask.resize((size, size), Image.LANCZOS))
    mark.save(os.path.join(FX, 'quickhaul-mark.png'), 'PNG', optimize=True)
    print('logo mark', mark.size, os.path.getsize(os.path.join(FX, 'quickhaul-mark.png')) // 1024, 'KB')


def fonts():
    os.makedirs(FONTS, exist_ok=True)
    site = os.path.join(PROJECT, 'site', 'assets', 'fonts')
    for f in ('biosans-light.otf', 'biosans-semibold.otf', 'biosans-extrabold.otf', 'robotomono-latin.woff2'):
        shutil.copyfile(os.path.join(site, f), os.path.join(FONTS, f))
    # Regular is new to the site: Bio Sans takes over body text in this direction. From the same supplied set.
    shutil.copyfile(os.path.join(PROJECT, 'assets', 'fonts', 'biosans', 'Flat-it - BioSans-Regular.otf'), os.path.join(FONTS, 'biosans-regular.otf'))
    print('fonts copied')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        photos(sys.argv[1:])
    else:
        fonts()
        logo()
        photos()
