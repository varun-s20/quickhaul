import sys
from PIL import Image
src = sys.argv[1]
im = Image.open(src).convert('RGB')
band = im.crop((0, 600, 736, 1000))
def km(img, k=8, label=''):
    q = img.quantize(colors=k, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[:k*3]
    counts = sorted(q.getcolors(), reverse=True)
    tot = sum(c for c, _ in counts)
    print('--', label)
    for c, i in counts:
        r, g, b = pal[i*3:i*3+3]
        print(f'#{r:02X}{g:02X}{b:02X}  {100*c/tot:5.1f}%')
km(band, 8, 'whole frame')
mark = im.crop((255, 675, 490, 920))
km(mark, 10, 'logo mark box')
wall = im.crop((520, 610, 730, 990))
km(wall, 5, 'wall right side')
# luminance extremes inside the mark
px = list(mark.getdata())
lum = lambda p: 0.2126*p[0]+0.7152*p[1]+0.0722*p[2]
px.sort(key=lum)
n = len(px)
for pct in (0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99):
    p = px[int(pct*(n-1))]
    print(f'p{int(pct*100):02d} #{p[0]:02X}{p[1]:02X}{p[2]:02X}')
