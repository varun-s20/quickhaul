# B3 readability check: sample the bare hero ground (text hidden) behind the headline and the lede,
# in 6 zones each, and report the worst contrast for cream (headline) and chrome (lede) text.
import sys
sys.path.insert(0, 'design/scripts')
from PIL import Image
from contrast import cr
im = Image.open(sys.argv[1]).convert('RGB')
def hx(p): return '#%02X%02X%02X' % p
def zones(box, n):
    x0, y0, x1, y1 = box; w = (x1 - x0) / n
    return [(int(x0 + i * w), y0, int(x0 + (i + 1) * w), y1) for i in range(n)]
for name, box, fg in [('headline', tuple(map(int, sys.argv[2].split(','))), 'F7EFEC'), ('lede', tuple(map(int, sys.argv[3].split(','))), 'D5D4D3')]:
    worst = 99
    for z in zones(box, 6):
        px = [im.getpixel((x, y)) for x in range(z[0], z[2], 2) for y in range(z[1], z[3], 2)]
        bright = max(px, key=sum); dark = min(px, key=sum)
        avg = tuple(sum(c[i] for c in px) // len(px) for i in range(3))
        c_b = cr(fg, hx(bright)); worst = min(worst, c_b)
        print(f'{name} zone x{z[0]}-{z[2]}: avg {hx(avg)} brightest {hx(bright)} darkest {hx(dark)} -> {fg} on brightest {c_b:.2f}')
    print(f'{name}: worst {worst:.2f}')
