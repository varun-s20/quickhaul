import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
targets = sys.argv[2:]
def d(a, b): return sum((x-y)**2 for x, y in zip(a, b))
for t in targets:
    tr = tuple(int(t.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    best = None
    for y in range(605, 995, 2):
        for x in range(5, 731, 2):
            p = im.getpixel((x, y))
            # prefer a pixel whose 5x5 neighbourhood is uniform, so the marker sits on a real patch
            dd = d(p, tr)
            if dd < 60:
                nb = [im.getpixel((x+i, y+j)) for i in (-2, 0, 2) for j in (-2, 0, 2)]
                spread = max(d(n, tr) for n in nb)
                score = dd + spread/4
                if best is None or score < best[0]:
                    best = (score, x, y, p)
    if best:
        s, x, y, p = best
        print(f'{t}: x {x} y {y-600} (frame coords, 736x400) pct {100*x/736:.1f}% {100*(y-600)/400:.1f}% actual #{p[0]:02X}{p[1]:02X}{p[2]:02X}')
    else:
        print(t, 'no close patch')
