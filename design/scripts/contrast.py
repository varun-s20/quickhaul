import sys
def lin(c):
    c = c/255
    return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
def L(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def cr(a, b):
    la, lb = sorted((L(a), L(b)), reverse=True)
    return (la+0.05)/(lb+0.05)
if __name__ == '__main__':
    for fg, bg in (p.split(':') for p in sys.argv[1:]):
        print(f'{fg} on {bg}: {cr(fg, bg):.2f}')
