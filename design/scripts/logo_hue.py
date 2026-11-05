import sys, colorsys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGB')
mark = im.crop((255, 675, 490, 920))
px = list(mark.getdata())
hs = []
for p in px:
    h, l, s = colorsys.rgb_to_hls(*(c/255 for c in p))
    hs.append((s*(1-abs(2*l-1)), h, l, p))
hs.sort(reverse=True)
print('most chromatic pixels in the mark:')
for c, h, l, p in hs[:12:2]:
    print(f'#{p[0]:02X}{p[1]:02X}{p[2]:02X} hue {h*360:5.0f} light {l:.2f} chroma {c:.3f}')
# hue of bright chrome (l>0.7)
bright = [p for _, _, l, p in hs if l > 0.72]
r = sum(p[0] for p in bright)/len(bright); g = sum(p[1] for p in bright)/len(bright); b = sum(p[2] for p in bright)/len(bright)
print('mean bright chrome', '#%02X%02X%02X' % (round(r), round(g), round(b)), len(bright))
mid = [p for _, _, l, p in hs if 0.4 < l < 0.6]
r = sum(p[0] for p in mid)/len(mid); g = sum(p[1] for p in mid)/len(mid); b = sum(p[2] for p in mid)/len(mid)
print('mean mid chrome', '#%02X%02X%02X' % (round(r), round(g), round(b)), len(mid))
dark = [p for _, _, l, p in hs if l < 0.09]
r = sum(p[0] for p in dark)/len(dark); g = sum(p[1] for p in dark)/len(dark); b = sum(p[2] for p in dark)/len(dark)
print('mean deep shadow', '#%02X%02X%02X' % (round(r), round(g), round(b)), len(dark))
