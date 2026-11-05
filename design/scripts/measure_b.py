# Phase B measurements: logo mark bounds on the wall, wall colour around it, Bio Sans text widths.
import sys
from PIL import Image, ImageFont
root = sys.argv[1]
im = Image.open(root + '/assets/logo.png').convert('RGB')
W, H = im.size
# mark = bright chrome pixels inside the wall photo (y 600 to 1000)
xs, ys = [], []
for y in range(600, 1000):
    for x in range(W):
        r, g, b = im.getpixel((x, y))
        if r + g + b > 330 and abs(r - b) < 40:
            xs.append(x); ys.append(y)
print('bright px', len(xs), 'bounds x', min(xs), max(xs), 'y', min(ys), max(ys))
# wall samples around the mark
for (x, y) in [(200, 700), (520, 700), (240, 950), (520, 950), (380, 640), (380, 975), (250, 800), (510, 800)]:
    print('wall', x, y, '#%02X%02X%02X' % im.getpixel((x, y)))
fd = root + '/assets/fonts/biosans/'
faces = {'light': 'Flat-it - BioSans-Light.otf', 'semi': 'Flat-it - BioSans-SemiBold.otf',
         'bold': 'Flat-it - Bio Sans Bold.otf', 'xbold': 'Flat-it - BioSans-ExtraBold.otf', 'reg': 'Flat-it - BioSans-Regular.otf'}
for k, f in faces.items():
    ft = ImageFont.truetype(fd + f, 100)
    asc, desc = ft.getmetrics()
    print(k, 'asc', asc, 'desc', desc, 'H cap bbox', ft.getbbox('H'), {s: round(ft.getlength(s), 1) for s in ['JUNK OUT', 'SPACE BACK', 'GARAGE AND BASEMENT', 'CLEAN OUTS', '$149', 'SERVICES']})
