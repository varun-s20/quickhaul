import sys, colorsys
from PIL import Image
sys.path.insert(0, 'design/scripts')
from contrast import cr  # noqa
im = Image.open('assets/logo.png').convert('RGB')
# overlay zone on the plain wall, right of the mark: frame x 72-98%, y 18-84%
x0, x1 = int(.72*736), int(.98*736); y0, y1 = 600+int(.18*400), 600+int(.84*400)
px = [im.getpixel((x, y)) for y in range(y0, y1, 2) for x in range(x0, x1, 2)]
lum = lambda p: 0.2126*p[0]+0.7152*p[1]+0.0722*p[2]
px.sort(key=lum)
hx = lambda p: '#%02X%02X%02X' % p
print('zone darkest', hx(px[0]), 'median', hx(px[len(px)//2]), 'p99', hx(px[int(.99*len(px))]), 'brightest', hx(px[-1]))
for fg in ('#F7EFEC', '#D5D4D3', '#9DB0CC'):
    print(fg, 'vs brightest wall', round(cr(fg, hx(px[-1])), 2), 'vs p99', round(cr(fg, hx(px[int(.99*len(px))])), 2), 'vs median', round(cr(fg, hx(px[len(px)//2])), 2))
# steel accent derivation
r, g, b = (int('323E54'[i:i+2], 16)/255 for i in (0, 2, 4))
h, l, s = colorsys.rgb_to_hls(r, g, b)
print('source #323E54 hue', round(h*360), 'light', round(l, 3), 'sat', round(s, 3))
r2, g2, b2 = colorsys.hls_to_rgb(h, .71, .30)
print('lifted to L .71 S .30:', '#%02X%02X%02X' % (round(r2*255), round(g2*255), round(b2*255)))
