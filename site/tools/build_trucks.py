#!/usr/bin/env python3
"""Quick Haul: the redrawn truck set (revision round, 2026-11-04).

One drawing, every variant. Writes standalone SVGs to assets/trucks/ and, for tools/build.py to pull into pages, the
shared inline sprite and each inline truck to src/partials/trucks/. Run it before tools/build.py when the drawing changes.

The truck is the one in Quick Haul's logo: a cab-forward medium-duty truck with a slatted dump body, a tandem
rear axle and a heap of junk, facing right. Drawn side-on at 150 units to the metre from real medium-duty
proportions (wheelbase about 3.9m, cab 1.8m long, 0.8m tyres), so it holds up large. Chrome like the logo; the
load is the only colour. Our own drawing: nothing traced or copied.

Usage: python tools/build_trucks.py   (from the site folder)
"""
import math
import os
import re


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'assets', 'trucks')
PARTS = os.path.join(ROOT, 'src', 'partials', 'trucks')

VIEW = '0 62 1064 558'     # room for the tallest load and the ground shadow
INK = '#0F141C'
# The heap's outline: an old canvas tarp over the load. Curved, so no flat black shape with hard corners shows behind it (critic r2)
PILE = 'M62 262C58 238 80 208 110 192C140 176 176 170 210 156C240 144 266 136 300 128C340 118 382 108 430 106C472 106 502 118 538 128C582 138 624 146 660 160C690 172 712 190 718 216L722 262Z'


def n(v):
    return ('%.2f' % v).rstrip('0').rstrip('.')


def rr(x, y, w, h, r=0, fill='none', extra=''):
    rx = ' rx="%s"' % n(r) if r else ''
    return '<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s"%s/>' % (n(x), n(y), n(w), n(h), rx, fill, ' ' + extra if extra else '')


def ln(d, stroke, width=1.0, extra=''):
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s/>' % (d, stroke, n(width), ' ' + extra if extra else '')


def pth(d, fill, extra=''):
    return '<path d="%s" fill="%s"%s/>' % (d, fill, ' ' + extra if extra else '')


def cir(cx, cy, r, fill='none', extra=''):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"%s/>' % (n(cx), n(cy), n(r), fill, ' ' + extra if extra else '')


def at(x, y, rot=0, s=1):
    t = 'translate(%s %s)' % (n(x), n(y))
    if rot:
        t += ' rotate(%s)' % n(rot)
    if s != 1:
        t += ' scale(%s)' % n(s)
    return t


def grp(transform, *parts):
    return '<g transform="%s">%s</g>' % (transform, ''.join(parts))


# ===== Paint =====
def stops(*pairs):
    out = []
    for p in pairs:
        o, c = p[0], p[1]
        a = ' stop-opacity="%s"' % n(p[2]) if len(p) > 2 else ''
        out.append('<stop offset="%s" stop-color="%s"%s/>' % (n(o), c, a))
    return ''.join(out)


def lin(i, x1, y1, x2, y2, *pairs, user=False):
    u = ' gradientUnits="userSpaceOnUse"' if user else ''
    return '<linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s"%s>%s</linearGradient>' % (i, n(x1), n(y1), n(x2), n(y2), u, stops(*pairs))


def rad(i, *pairs, cx=.5, cy=.5, r=.5):
    return '<radialGradient id="%s" cx="%s" cy="%s" r="%s">%s</radialGradient>' % (i, n(cx), n(cy), n(r), stops(*pairs))


PAINT = ''.join([
    # brushed chrome on the cab: bright sky at the top, a dark horizon at the belt line, ground bounce under it (the logo's own metal)
    lin('qh-cab', 0, 262, 0, 484, (0, '#F4F5F5'), (.08, '#E4E6E7'), (.3, '#C9CCCF'), (.5, '#A9ADB3'), (.525, '#7A7F88'), (.555, '#D3D5D8'), (.74, '#A8ACB2'), (1, '#6F747D'), user=True),
    lin('qh-sheen', 758, 262, 1036, 420, (0, '#fff', 0), (.2, '#fff', .46), (.33, '#fff', .03), (.56, '#fff', .34), (.66, '#fff', 0), (.88, '#fff', .16), (1, '#fff', 0), user=True),
    lin('qh-bumper', 0, 0, 0, 1, (0, '#F2F3F3'), (.3, '#C4C7CB'), (.48, '#7F848C'), (.54, '#DADCDE'), (.8, '#9A9EA5'), (1, '#5F646D')),
    lin('qh-rail', 0, 0, 0, 1, (0, '#F7F8F8'), (.3, '#D2D4D7'), (.66, '#9A9EA5'), (1, '#6A6F78')),
    lin('qh-post', 0, 0, 1, 0, (0, '#EEEFEF'), (.3, '#CDD0D3'), (.76, '#94989F'), (1, '#60656E')),
    lin('qh-dark', 0, 0, 0, 1, (0, '#434A58'), (.38, '#262B35'), (1, '#12151B')),
    lin('qh-darkSide', 0, 0, 1, 0, (0, '#3B414E'), (.5, '#20242D'), (1, '#10131A')),
    lin('qh-glass', 0, 0, 1, 1, (0, '#566680'), (.42, '#2D3648'), (1, '#161B26')),
    lin('qh-screen', 0, 0, 0, 1, (0, '#BCCADB'), (.34, '#7E8EA3'), (.7, '#3C4759'), (1, '#222938')),
    # the body's far side: mid steel, so black bags and dark furniture separate from it (critic r1: they vanished against near-black)
    lin('qh-inside', 0, 0, 0, 1, (0, '#7D8696'), (.5, '#5D6677'), (1, '#343B48')),
    lin('qh-tank', 0, 0, 0, 1, (0, '#5B616C'), (.2, '#ECEEEF'), (.3, '#FFFFFF'), (.54, '#B4B8BE'), (.84, '#6C717B'), (1, '#383D47')),
    lin('qh-stack', 0, 0, 1, 0, (0, '#6E737C'), (.3, '#F7F7F6'), (.62, '#B9BCC2'), (1, '#5E636C')),
    lin('qh-rim', 0, 0, 1, 1, (0, '#FAFAF9'), (.42, '#BEC1C6'), (.74, '#80858E'), (1, '#DADBDD')),
    rad('qh-tyre', (0, '#161A21'), (.64, '#0E1116'), (.8, '#2B3039'), (.93, '#171A21'), (1, '#090B0F')),
    rad('qh-dish', (0, '#CDD0D4'), (.62, '#8E939B'), (.86, '#4A505A'), (1, '#262B34')),
    rad('qh-dishDeep', (0, '#50565F'), (.6, '#2A2F38'), (1, '#0F1217')),
    rad('qh-hub', (0, '#FFFFFF'), (.5, '#D3D5D9'), (1, '#7D828B'), cx=.38, cy=.34, r=.72),
    rad('qh-lamp', (0, '#FFFFFF'), (.4, '#F3F6FA'), (.8, '#B7C2CF'), (1, '#6E7A8A'), cx=.42, cy=.42, r=.62),
    lin('qh-amber', 0, 0, 0, 1, (0, '#FFC766'), (.55, '#F29A1E'), (1, '#B4640A')),
    lin('qh-red', 0, 0, 0, 1, (0, '#F0564A'), (.55, '#C4241C'), (1, '#7E100C')),
    rad('qh-contact', (0, INK, .62), (.62, INK, .3), (1, INK, 0)),
    lin('qh-inShade', 0, 0, 0, 1, (0, INK, .28), (.3, INK, .08), (.72, INK, .16), (1, INK, .42)),
    # the load
    lin('qh-kraft', 0, 0, 1, 0, (0, '#CFA471'), (.72, '#BC8F5B'), (1, '#94693C')),
    lin('qh-bag', 0, 0, 1, 1, (0, '#474E5C'), (.42, '#20242C'), (1, '#0E1116')),
    lin('qh-fridge', 0, 0, 1, 0, (0, '#D3EDE2'), (.62, '#AFD8C7'), (1, '#7FAA99')),
    lin('qh-teal', 0, 0, 0, 1, (0, '#4A9EA2'), (1, '#2B6E72')),
    lin('qh-tealDeep', 0, 0, 0, 1, (0, '#347F83'), (1, '#1F5356')),
    lin('qh-rust', 0, 0, 0, 1, (0, '#D9754E'), (1, '#A84A30')),
    lin('qh-rustDeep', 0, 0, 0, 1, (0, '#B8573A'), (1, '#7E3522')),
    lin('qh-mattress', 0, 0, 0, 1, (0, '#F7F3EA'), (1, '#D8D1C1')),
    lin('qh-heapShade', 0, 0, 0, 1, (0, INK, 0), (1, INK, .5)),
    '<pattern id="qh-quilt" width="34" height="34" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0H34M0 0V34" fill="none" stroke="#B9B3A3" stroke-width="1.2"/><circle cx="0" cy="0" r="1.9" fill="#A7A08E"/></pattern>',
    lin('qh-canvas', 0, 0, 0, 1, (0, '#5A6372'), (.55, '#39404E'), (1, '#20252E')),
    '<clipPath id="qh-pileClip"><path d="%s"/></clipPath>' % PILE,
    lin('qh-walnut', 0, 0, 0, 1, (0, '#946239'), (1, '#6E4526')),
    lin('qh-shade', 0, 0, 1, 0, (0, '#F6DA8B'), (.7, '#E8BE5C'), (1, '#BF9238')),
    lin('qh-plank', 0, 0, 0, 1, (0, '#E7CFA4'), (1, '#BF9F6C')),
    lin('qh-tarp', 0, 0, 1, 1, (0, '#4A92D8'), (1, '#225A99')),
    lin('qh-tv', 0, 0, 0, 1, (0, '#B4B3AC'), (1, '#7E7E79')),
])


# ===== Wheels =====
def wheel_parts(deep):
    """Centred on 0,0, radius 60. deep: the rear axles' deep-dish steel wheel. Otherwise the front wheel, dished outward."""
    s = [cir(0, 0, 60, 'url(#qh-tyre)')]
    # tread blocks at the shoulder, so the outline is not a perfect circle
    s.append(cir(0, 0, 59.2, 'none', 'stroke="#07090C" stroke-width="2.4" stroke-dasharray="5.3 2.45"'))
    # sidewall: bead rings and raised lettering blocks, low contrast
    s.append(cir(0, 0, 53, 'none', 'stroke="#3E444F" stroke-opacity=".55" stroke-width="1"'))
    s.append(cir(0, 0, 47.6, 'none', 'stroke="#454B56" stroke-opacity=".55" stroke-width="2.6" stroke-dasharray="9 2 5 2 12 2 4 2 7 26 11 2 6 2 9 28"'))
    s.append(cir(0, 0, 42.4, 'none', 'stroke="#000" stroke-opacity=".7" stroke-width="2.2"'))
    # rim
    s.append(cir(0, 0, 38.6, 'url(#qh-rim)'))
    s.append(cir(0, 0, 38.6, 'none', 'stroke="#20242C" stroke-width="1.2"'))
    s.append(cir(0, 0, 35.2, 'none', 'stroke="#fff" stroke-opacity=".6" stroke-width="1"'))
    s.append(cir(0, 0, 32, 'url(#qh-dishDeep)' if deep else 'url(#qh-dish)'))
    # hand holes
    for i in range(8):
        s.append('<ellipse cx="0" cy="-26" rx="3.7" ry="5.4" fill="#0B0D12" transform="rotate(%d)"/>' % (i * 45 + 22.5))
    # hub
    if deep:
        s.append(cir(0, 0, 21, 'url(#qh-rim)'))
        s.append(cir(0, 0, 21, 'none', 'stroke="#14171D" stroke-width="1"'))
        s.append(cir(0, 0, 11.5, 'url(#qh-dish)'))
        s.append(cir(0, 0, 6.6, 'url(#qh-hub)', 'stroke="#2A2F38" stroke-width=".8"'))
        lug_r = 16.2
    else:
        s.append(cir(0, 0, 22, 'url(#qh-rim)'))
        s.append(cir(0, 0, 22, 'none', 'stroke="#14171D" stroke-width="1"'))
        s.append(cir(0, 0, 11, 'url(#qh-hub)', 'stroke="#2A2F38" stroke-width=".8"'))
        s.append(cir(0, 0, 4.4, '#8A8F97'))
        lug_r = 16.6
    for i in range(10):
        a = math.radians(i * 36)
        x, y = lug_r * math.cos(a), lug_r * math.sin(a)
        s.append(cir(x, y, 2.5, '#EDEEEF', 'stroke="#23272F" stroke-width=".7"'))
        s.append(cir(x - .5, y - .5, .9, '#fff'))
    return ''.join(s)


# light on the tyre stays put when the wheel turns
WHEEL_LIGHT = ln('M-44 -28A52.6 52.6 0 0 1 8 -52', '#fff', 5, 'stroke-opacity=".1" stroke-linecap="round"') + ln('M-34 19A39 39 0 0 1 -32 -22', '#fff', 1.6, 'stroke-opacity=".45" stroke-linecap="round"')


# ===== Under the truck: frame, tank, box, springs, fender, stack =====
def chassis():
    s = []
    # exhaust stack, behind the cab shield
    s.append(rr(746, 200, 10, 280, 0, 'url(#qh-stack)'))
    s.append(pth('M746 200L756 190V200Z', '#6E737C'))
    s.append(rr(743.5, 300, 15, 112, 2, 'url(#qh-darkSide)'))
    for y in range(308, 404, 13):
        s.append(rr(746.5, y, 9, 6, 1.5, '#0C0F14'))
    s.append(rr(742.5, 296, 17, 4, 1, 'url(#qh-rail)'))
    s.append(rr(742.5, 412, 17, 4, 1, 'url(#qh-rail)'))
    # frame rail
    s.append(rr(30, 470, 936, 29, 0, 'url(#qh-dark)'))
    s.append(rr(30, 470, 936, 1.4, 0, '#6A7180'))
    for x in range(440, 760, 18):
        s.append(cir(x, 477.5, 1.7, '#6A7180'))
        s.append(cir(x, 491.5, 1.7, '#4C5360'))
    # leaf spring between the rear axles
    s.append(pth('M238 496L252 516H328L342 496Z', '#171B22'))
    for i, c in enumerate(['#2E343F', '#262B35', '#1E2229']):
        y = 512 + i * 4.6
        s.append(ln('M236 %s Q290 %s 344 %s' % (n(y - 7), n(y + 12), n(y - 7)), c, 4, 'stroke-linecap="round"'))
    s.append(rr(280, 516, 20, 22, 2, '#14171D'))
    # small air tank ahead of the rear axles
    s.append(rr(431, 508, 34, 34, 13, 'url(#qh-dark)'))
    s.append(rr(444, 499, 6, 9, 0, '#14171D'))
    # fuel tank with straps and filler
    for x in (510, 596):
        s.append(rr(x, 498, 6, 6, 0, '#14171D'))
    s.append(rr(548, 479, 18, 8, 2, 'url(#qh-rail)'))
    s.append(rr(471, 487, 166, 70, 30, 'url(#qh-tank)'))
    s.append(rr(476, 490, 156, 64, 26, 'none', 'stroke="#3A3F49" stroke-opacity=".35" stroke-width="1"'))
    s.append(rr(506, 484.5, 8.5, 75, 2, 'url(#qh-darkSide)'))
    s.append(rr(592, 484.5, 8.5, 75, 2, 'url(#qh-darkSide)'))
    # battery and tool box
    s.append(rr(652, 498, 86, 60, 3, 'url(#qh-dark)'))
    s.append(rr(652, 498, 86, 1.4, 0, '#6A7180'))
    s.append(rr(657, 505, 76, 47, 1, 'none', 'stroke="#000" stroke-opacity=".55" stroke-width="1.2"'))
    s.append(rr(687, 502, 16, 8, 1.5, 'url(#qh-rail)'))
    for y in (528, 534, 540):
        s.append(rr(665, y, 28, 2.4, 1, '#0B0D12'))
    # front wheel well, seen under the cab's arch, behind the wheel
    s.append(pth('M782 492A80 80 0 0 1 942 492V516H782Z', '#0A0C10'))
    s.append(rr(800, 500, 124, 14, 2, '#161A21'))
    # underrun guard, tail lamp, rear hinge
    s.append(pth('M56 499L34 542H46L68 499Z', '#1A1E26'))
    s.append(rr(8, 540, 58, 13, 2, '#1F232B'))
    for x in range(10, 64, 16):
        s.append(rr(x, 542.5, 8, 8, 0, '#D4372C'))
        s.append(rr(x + 8, 542.5, 8, 8, 0, '#F2F2F0'))
    s.append(cir(46, 479, 9, 'url(#qh-rail)', 'stroke="#14171D" stroke-width="1"'))
    s.append(cir(46, 479, 3, '#14171D'))
    return ''.join(s)


def rear_fender():
    s = [pth('M152 508C152 485 172 470 200 470H380C408 470 428 485 428 508H420C420 491 402 478 380 478H200C178 478 160 491 160 508Z', 'url(#qh-dark)')]
    s.append(ln('M154 500C157 483 176 471 200 471H380C404 471 423 483 426 500', '#7A8190', 1.1))
    # mud flap behind the last axle
    s.append(pth('M130 482H153V562Q153 568 147 568H136Q130 568 130 562Z', 'url(#qh-darkSide)'))
    s.append(ln('M133 486V560', '#fff', 1, 'stroke-opacity=".1"'))
    s.append(rr(130, 556, 23, 7, 1, 'url(#qh-rail)'))
    return ''.join(s)


# ===== The dump body =====
POST_W = 14.0
BAY = 71.5
POSTS = [24 + i * (POST_W + BAY) for i in range(9)]


def bed_back():
    """Inside face of the far side; everything in the load sits in front of this."""
    s = [rr(30, 258, 694, 180, 0, 'url(#qh-inside)')]
    for x in POSTS:
        s.append(rr(x + 3, 258, 8, 180, 0, '#2B313C', 'opacity=".6"'))
    s.append(rr(30, 330, 694, 3, 0, '#2B313C', 'opacity=".5"'))
    s.append(rr(30, 426, 694, 12, 0, '#232831'))
    return ''.join(s)


def bed_side():
    # the load inside the body sits in shade; what rises above the rail is in the sun
    s = [rr(30, 272, 694, 166, 0, 'url(#qh-inShade)')]
    # shade the load falls into, under the top rail and on the inside of each post
    for x in POSTS[:-1]:
        s.append(rr(x + POST_W, 272, BAY, 7, 0, INK, 'opacity=".42"'))
        s.append(rr(x + POST_W, 272, 5, 154, 0, INK, 'opacity=".22"'))
    # posts
    for x in POSTS:
        s.append(rr(x, 266, POST_W, 166, 0, 'url(#qh-post)'))
        s.append(rr(x, 266, 1, 166, 0, '#fff', 'opacity=".6"'))
        s.append(rr(x + POST_W - 1, 266, 1, 166, 0, '#20242C', 'opacity=".7"'))
        for y in (281, 417):
            s.append(cir(x + POST_W / 2, y, 2.3, '#6E737C', 'stroke="#23272F" stroke-width=".6"'))
            s.append(cir(x + POST_W / 2 - .5, y - .5, .8, '#fff'))
    # top rail, cap and channel
    s.append(rr(22, 252, 702, 20, 2, 'url(#qh-rail)'))
    s.append(rr(22, 252, 702, 1.4, 0, '#fff', 'opacity=".9"'))
    s.append(rr(24, 262.5, 698, 2.6, 0, '#343A45'))
    s.append(rr(24, 265.1, 698, 1, 0, '#fff', 'opacity=".55"'))
    s.append(rr(22, 271, 702, 1.4, 0, '#20242C', 'opacity=".75"'))
    # lower rail with rope hooks and conspicuity tape
    s.append(rr(22, 426, 702, 26, 1, 'url(#qh-rail)'))
    s.append(rr(22, 426, 702, 1.2, 0, '#fff', 'opacity=".85"'))
    s.append(rr(22, 451, 702, 1.4, 0, '#20242C', 'opacity=".8"'))
    x = 28.0
    i = 0
    while x < 716:
        s.append(rr(x, 435.5, 26, 8, 0, '#D4372C' if i % 2 == 0 else '#F4F4F2'))
        x += 26
        i += 1
    s.append(rr(28, 435.5, 688, 8, 0, 'none', 'stroke="#20242C" stroke-opacity=".3" stroke-width=".8"'))
    # sill and cross members under the floor
    s.append(rr(24, 452, 698, 18, 0, 'url(#qh-dark)'))
    for x in POSTS:
        s.append(rr(x - 1, 452, 16, 22, 1, 'url(#qh-darkSide)'))
        s.append(pth('M%s 452v5a3 3 0 0 0 6 0v-5' % n(x + 4), 'none', 'stroke="#8D929A" stroke-width="1.5"'))
    # headboard and the cab shield over the roof
    s.append(rr(722, 232, 22, 220, 0, 'url(#qh-post)'))
    s.append(rr(722, 232, 1, 220, 0, '#fff', 'opacity=".6"'))
    s.append(rr(743, 232, 1, 220, 0, '#20242C', 'opacity=".7"'))
    for y in (262, 300, 340, 380, 420):
        s.append(cir(733, y, 2.4, '#6E737C', 'stroke="#23272F" stroke-width=".6"'))
    s.append(pth('M744 240H786L744 268Z', 'url(#qh-darkSide)'))
    s.append(pth('M716 224H792Q798 224 798 229V238Q798 241 794 241H716Z', 'url(#qh-dark)'))
    s.append(ln('M716 224.8H792', '#858C9A', 1.2))
    # rear post and lamps
    s.append(rr(24, 252, 15, 200, 0, 'url(#qh-post)'))
    s.append(rr(24, 252, 1, 200, 0, '#fff', 'opacity=".6"'))
    s.append(rr(26, 245, 12, 7, 1.5, 'url(#qh-red)'))
    s.append(rr(11, 455, 26, 20, 3, '#14171D'))
    s.append(rr(13, 457, 22, 7.5, 1.5, 'url(#qh-red)'))
    s.append(rr(13, 465.5, 11, 7.5, 1.5, 'url(#qh-amber)'))
    s.append(rr(24.5, 465.5, 10.5, 7.5, 1.5, '#E9ECEF'))
    return ''.join(s)


# ===== The cab =====
CAB_SHELL = 'M758 482V288Q758 266 780 264L966 262C984 262 997 266 1003 277L1025 370C1030 392 1034 424 1036 470V482H917.1A80 80 0 0 0 806.9 482Z'
DOOR = 'M826 284L966 282Q974 282 978 288L1000 372Q1004 392 1004 416V452H826Z'
GLASS = 'M842 297L958 296Q966 296 968 303L986 374L842 376Z'


def cab():
    s = []
    # shell and metal
    s.append(pth(CAB_SHELL, 'url(#qh-cab)'))
    s.append(pth(CAB_SHELL, 'url(#qh-sheen)'))
    # roof gutter and the top light
    s.append(ln('M782 265.2L964 263.2', '#fff', 1.6))
    s.append(ln('M766 276L972 274', '#8F949C', 1.1))
    s.append(ln('M766 277.2L972 275.2', '#fff', .8, 'stroke-opacity=".8"'))
    # rear corner, panel break behind the door
    s.append(ln('M769 278V478', '#AEB2B8', .9))
    # louvres on the rear quarter
    for i, y in enumerate(range(396, 442, 9)):
        s.append(rr(778, y, 38, 4.2, 2, '#23272F'))
        s.append(rr(778, y + 4.4, 38, 1, 0, '#fff', 'opacity=".55"'))
    # door
    s.append(pth(DOOR, 'none', 'stroke="#fff" stroke-opacity=".7" stroke-width="1" transform="translate(1 1)"'))
    s.append(pth(DOOR, 'none', 'stroke="#23272F" stroke-width="1.5"'))
    # belt moulding
    s.append(ln('M760 381.4H1000', '#7D828B', 1.2))
    s.append(ln('M760 382.8H1002', '#fff', 1, 'stroke-opacity=".85"'))
    s.append(ln('M827 436H1003', '#9398A0', .9))
    s.append(ln('M827 437.1H1003', '#fff', .8, 'stroke-opacity=".7"'))
    # side glass
    s.append('<clipPath id="qh-sideGlass"><path d="%s"/></clipPath>' % GLASS)
    s.append(pth(GLASS, 'url(#qh-glass)'))
    s.append('<g clip-path="url(#qh-sideGlass)">')
    s.append(pth('M866 376V344Q866 326 884 326H898Q914 326 914 344L916 376Z', '#0B0E14', 'opacity=".62"'))
    s.append(pth('M878 326Q878 310 890 310Q902 310 902 326Z', '#0B0E14', 'opacity=".62"'))
    s.append('<ellipse cx="962" cy="360" rx="6" ry="20" fill="none" stroke="#0B0E14" stroke-width="3.4" opacity=".65" transform="rotate(-14 962 360)"/>')
    s.append(pth('M842 346L902 297H934L842 374Z', '#fff', 'opacity=".12"'))
    s.append(pth('M912 376L968 303L976 336L942 376Z', '#fff', 'opacity=".08"'))
    s.append(pth('M842 296H968V301H842Z', '#fff', 'opacity=".16"'))
    s.append('</g>')
    s.append(pth(GLASS, 'none', 'stroke="#10131A" stroke-width="3" stroke-linejoin="round"'))
    s.append(ln('M944 375L969 306', '#10131A', 3.2))
    # windscreen seen edge-on, with the sky in it
    s.append(pth('M986 278C991 278 996 279 999 285L1023 372H1006Z', 'url(#qh-screen)'))
    s.append(pth('M986 278C991 278 996 279 999 285L1023 372H1006Z', 'none', 'stroke="#10131A" stroke-width="2.4" stroke-linejoin="round"'))
    s.append(ln('M1006 372L1026 376', '#14171D', 2.4))
    # sun visor and roof lights
    s.append(pth('M960 262L1012 266Q1018 267 1018 272L1000 270L960 267Z', 'url(#qh-dark)'))
    for x in (903, 933, 963):
        s.append(rr(x - 1, 259.5, 16, 3.5, 1, '#20242C'))
        s.append(rr(x, 254.5, 14, 6, 2, 'url(#qh-amber)'))
    # grab handle
    s.append(rr(813.6, 303, 6.8, 74, 3.4, '#14171D'))
    s.append(rr(814.4, 303.8, 4.6, 72, 2.3, 'url(#qh-stack)'))
    # door handle and lock
    s.append(rr(842, 392, 40, 14, 5, '#3A404B'))
    s.append(rr(846, 395, 32, 7, 3.5, 'url(#qh-rail)', 'stroke="#23272F" stroke-width=".7"'))
    s.append(cir(890, 399, 3.2, 'url(#qh-hub)', 'stroke="#23272F" stroke-width=".7"'))
    # no decal on the door: the round logo badge read as stuck on (Shawn, 10 Nov)
    # front corner: indicator, headlamp, marker, grille ribs
    s.append(pth('M1008 384L1028 381L1030 396L1009 400Z', 'url(#qh-amber)', 'stroke="#20242C" stroke-width="1"'))
    s.append(pth('M1008 403L1030.5 399Q1036 418 1036 438L1008 440Q1004.5 420 1008 403Z', '#20242C'))
    s.append(pth('M1010 405.5L1029 402Q1033.5 418 1033.5 436L1010 437.5Q1007.2 420 1010 405.5Z', 'url(#qh-lamp)'))
    s.append(cir(1020, 420, 8.5, 'url(#qh-hub)', 'stroke="#7D828B" stroke-width=".8"'))
    s.append(rr(1011, 444, 14, 5.5, 1.5, 'url(#qh-amber)', 'stroke="#20242C" stroke-width=".7"'))
    for y in (453, 459.5, 466):
        s.append(rr(1011, y, 25, 3.8, 1, '#1A1E26'))
    # step in the sill
    s.append(rr(946, 457, 54, 21, 2, '#10131A'))
    s.append(rr(946, 455.5, 54, 3.6, 1, 'url(#qh-rail)'))
    s.append(rr(950, 467.5, 46, 2.6, 1, '#9398A0'))
    # arch trim, cab bottom edge
    s.append(ln('M806.9 482A80 80 0 0 1 917.1 482', '#14171D', 5.2))
    s.append(ln('M758 482.4H806.9', '#14171D', 2.6))
    s.append(ln('M917.1 482.4H958', '#14171D', 2.6))
    # front mud flap
    s.append(pth('M772 484H795V562Q795 568 789 568H778Q772 568 772 562Z', 'url(#qh-darkSide)'))
    s.append(ln('M775 488V560', '#fff', 1, 'stroke-opacity=".1"'))
    s.append(rr(772, 556, 23, 7, 1, 'url(#qh-rail)'))
    # bumper with fog lamp
    s.append(pth('M956 482H1040Q1049 482 1049 491V514Q1049 523 1040 523H956Q950 523 950 516V489Q950 482 956 482Z', 'url(#qh-bumper)'))
    s.append(ln('M956 482.6H1040Q1048 482.6 1048.4 490', '#fff', 1.2))
    s.append(rr(952, 499, 40, 5.6, 2, '#14171D'))
    s.append(rr(952, 516, 94, 11, 3, 'url(#qh-dark)'))
    s.append(cir(1029, 501, 9.5, '#14171D'))
    s.append(cir(1029, 501, 7.4, 'url(#qh-lamp)'))
    # mirror arms and heads
    s.append(ln('M966 300L1003 302', '#14171D', 2.8))
    s.append(ln('M986 354L1003 346', '#14171D', 2.8))
    s.append(rr(1000, 288, 21, 60, 7, 'url(#qh-darkSide)', 'stroke="#090B0F" stroke-width="1"'))
    s.append(ln('M1005 295V341', '#fff', 1.6, 'stroke-opacity=".32" stroke-linecap="round"'))
    s.append(ln('M1012 348V353', '#14171D', 2.4))
    s.append(rr(1004, 353, 16, 19, 6, 'url(#qh-darkSide)', 'stroke="#090B0F" stroke-width="1"'))
    return ''.join(s)


# ===== The load: what Shawn takes, in side view at the same scale =====
def sofa(x, y, ground=True):
    """ground: the flat shadow it casts on the bed under it in the load. Standing alone, a soft contact shadow does the job, as on the other items."""
    return grp(at(x, y),
        '<ellipse cx="118" cy="128" rx="128" ry="7" fill="%s" opacity=".45"/>' % INK if ground else rr(100, 82, 36, 16, 0, '#1B4A4D'),   # standing alone: fills the notch between the two seat cushions, where the page showed through
        rr(14, 2, 208, 84, 16, 'url(#qh-tealDeep)'),
        rr(22, 8, 94, 60, 10, 'url(#qh-teal)'), rr(120, 8, 94, 60, 10, 'url(#qh-teal)'),
        ln('M30 14H108', '#fff', 1.6, 'stroke-opacity=".3" stroke-linecap="round"'), ln('M128 14H206', '#fff', 1.6, 'stroke-opacity=".3" stroke-linecap="round"'),
        ln('M46 30Q68 38 92 30M144 34Q168 42 192 34', '#123E40', 1.4, 'stroke-opacity=".45" stroke-linecap="round"'),
        rr(26, 60, 184, 6, 3, '#123E40', 'opacity=".5"'),
        rr(32, 62, 86, 34, 9, 'url(#qh-teal)'), rr(118, 62, 86, 34, 9, 'url(#qh-teal)'),
        ln('M40 67H110', '#fff', 1.8, 'stroke-opacity=".34" stroke-linecap="round"'), ln('M126 67H196', '#fff', 1.8, 'stroke-opacity=".34" stroke-linecap="round"'),
        rr(0, 36, 36, 78, 15, 'url(#qh-tealDeep)'), rr(200, 36, 36, 78, 15, 'url(#qh-tealDeep)'),
        ln('M8 44Q18 39 28 44', '#fff', 1.8, 'stroke-opacity=".3" stroke-linecap="round"'), ln('M208 44Q218 39 228 44', '#fff', 1.8, 'stroke-opacity=".3" stroke-linecap="round"'),
        rr(30, 95, 176, 19, 3, '#1B4A4D'),
        rr(16, 112, 12, 16, 1, '#5B3A1E'), rr(208, 112, 12, 16, 1, '#5B3A1E'))


def armchair(x, y, ground=True):
    return grp(at(x, y),
        '<ellipse cx="56" cy="118" rx="62" ry="6" fill="%s" opacity=".45"/>' % INK if ground else '',
        rr(14, 0, 84, 80, 14, 'url(#qh-rustDeep)'),
        rr(22, 6, 68, 54, 10, 'url(#qh-rust)'),
        ln('M30 12H82', '#fff', 1.6, 'stroke-opacity=".3" stroke-linecap="round"'),
        ln('M36 34Q56 42 76 34', '#5E2615', 1.4, 'stroke-opacity=".45" stroke-linecap="round"'),
        rr(24, 54, 64, 5, 2.5, '#5E2615', 'opacity=".5"'),
        rr(26, 56, 60, 30, 8, 'url(#qh-rust)'),
        ln('M34 61H78', '#fff', 1.6, 'stroke-opacity=".32" stroke-linecap="round"'),
        rr(0, 36, 27, 68, 12, 'url(#qh-rustDeep)'), rr(85, 36, 27, 68, 12, 'url(#qh-rustDeep)'),
        rr(22, 86, 68, 17, 3, '#6A2C1B'),
        rr(12, 102, 9, 16, 1, '#5B3A1E'), rr(91, 102, 9, 16, 1, '#5B3A1E'))


def box(x, y, w, h, rot=0, label=True, slab=True):
    """slab: the shadow it casts on its neighbours in the load. Standing alone on a card or a fold it read as a hard grey rectangle down one side (critic, FAQ r1), so there it's off and a soft contact shadow does the job."""
    t = w * .15
    parts = [rr(5, 4, w, h, 2, INK, 'opacity=".3"')] if slab else []
    parts += [rr(0, 0, w, h, 2, 'url(#qh-kraft)'),
             rr(0, 0, w, 1.6, 0, '#F0D9B5', 'opacity=".8"'),
             rr(0, 0, w, h, 2, 'none', 'stroke="#6F4E2A" stroke-opacity=".55" stroke-width="1"'),
             ln('M0 %s H%s' % (n(h * .2), n(w)), '#7E5A33', 1, 'stroke-opacity=".6"'),
             ln('M%s %s L%s %s' % (n(w * .86), n(h * .3), n(w * .95), n(h * .86)), '#7E5A33', 1, 'stroke-opacity=".35"'),
             rr(w / 2 - t / 2, 0, t, h * .34, 0, '#E4CDA8', 'opacity=".85"')]
    if label:
        parts += [rr(w * .08, h * .52, w * .3, h * .26, 1, '#F6F2EA'),
                  ln('M%s %sH%s M%s %sH%s' % (n(w * .12), n(h * .6), n(w * .34), n(w * .12), n(h * .69), n(w * .28)), '#3A404C', 1.2),
                  ln('M%s %sV%s M%s %sV%s' % (n(w * .74), n(h * .76), n(h * .55), n(w * .84), n(h * .76), n(h * .55)), '#5E4426', 1.6),
                  ln('M%s %sl%s -%sl%s %s M%s %sl%s -%sl%s %s' % (n(w * .74 - 3), n(h * .6), n(3), n(4), n(3), n(4), n(w * .84 - 3), n(h * .6), n(3), n(4), n(3), n(4)), '#5E4426', 1.6)]
    return grp(at(x, y, rot), *parts)


def bag(x, y, s=1, rot=0, tone='url(#qh-bag)'):
    return grp(at(x, y, rot, s),
        pth('M10 92C-6 74 -2 38 26 24C35 19 39 16 43 8L38 0H62L57 8C61 16 65 19 74 24C102 38 106 74 90 92C68 98 32 98 10 92Z', tone),
        rr(41, 7, 18, 4, 1, '#4B5160'),
        ln('M44 12C40 28 32 36 24 48M56 12C60 28 66 34 74 44M50 14C50 34 48 44 44 62', '#000', 1.2, 'stroke-opacity=".5"'),
        ln('M18 46C24 36 32 30 40 27', '#fff', 3.4, 'stroke-opacity=".34" stroke-linecap="round"'),
        ln('M14 70C14 62 16 56 19 52', '#fff', 2.2, 'stroke-opacity=".22" stroke-linecap="round"'),
        ln('M70 80C78 74 84 66 85 58', '#fff', 1.8, 'stroke-opacity=".16" stroke-linecap="round"'))


def mattress(x, y, rot=0, w=290, h=214, stain=True, soft=False):
    """Stood on its side: a quilted face with a piped, striped border, so it reads as a mattress, not a curtain (critic r1).
    soft: standing alone at some size, where the blue edge and dark handle read as a giant tablet (critic, FAQ r2). A rounder shape with a ticking edge, the same quilt, no handle."""
    if soft:
        return grp(at(x, y, rot),
                   rr(0, 0, w, h, 30, '#DCD5C6'),
                   rr(1.5, 1.5, w - 3, h - 3, 28.5, 'none', 'stroke="#8FA2B3" stroke-opacity=".6" stroke-width="3" stroke-dasharray="2 5"'),
                   rr(0, 0, w, h, 30, 'none', 'stroke="#B4AA95" stroke-width="1.2"'),
                   rr(10, 10, w - 20, h - 20, 22, 'url(#qh-mattress)'),
                   rr(10, 10, w - 20, h - 20, 22, 'url(#qh-quilt)'),
                   rr(10, 10, w - 20, h - 20, 22, 'none', 'stroke="#BDB39E" stroke-width="1.4"'))
    parts = [rr(0, 0, w, h, 18, '#6F8398'),
             rr(3, 3, w - 6, h - 6, 15, '#A9BCCC'),
             rr(11, 11, w - 22, h - 22, 10, 'url(#qh-mattress)'),
             rr(11, 11, w - 22, h - 22, 10, 'url(#qh-quilt)'),
             rr(11, 11, w - 22, h - 22, 10, 'none', 'stroke="#fff" stroke-opacity=".75" stroke-width="1.4"'),
             rr(w / 2 - 30, h - 8, 60, 5, 2.5, '#47596C')]
    if stain:
        parts.append('<ellipse cx="%s" cy="%s" rx="38" ry="19" fill="#8A6A3C" opacity=".16" transform="rotate(-18 %s %s)"/>' % (n(w * .66), n(h * .36), n(w * .66), n(h * .36)))
    return grp(at(x, y, rot), *parts)


def fridge(x, y, rot=0, slab=True):
    return grp(at(x, y, rot),
        rr(5, 3, 86, 196, 9, INK, 'opacity=".28"') if slab else '',
        rr(0, 0, 86, 196, 9, 'url(#qh-fridge)'),
        rr(0, 0, 86, 196, 9, 'none', 'stroke="#55786A" stroke-width="1.2"'),
        rr(0, 60, 86, 3, 0, '#3F5A4F'),
        rr(8, 26, 5.4, 28, 2.7, '#3A404B'),
        rr(8, 70, 5.4, 46, 2.7, '#3A404B'),
        rr(62, 6, 6, 182, 3, '#fff', 'opacity=".5"'),
        rr(32, 88, 18, 15, 1, '#F4D35E'), rr(36, 86, 10, 4, 1, '#C2382F'),
        rr(6, 180, 74, 9, 1, '#23272F'),
        ln('M12 184.5H74', '#5E636C', 1, 'stroke-dasharray="3 2"'))


def dresser(x, y, rot=0, slab=True):
    parts = ([rr(4, 4, 136, 100, 2, INK, 'opacity=".3"')] if slab else []) + [rr(-5, 0, 142, 9, 2, '#A06B3F'), rr(-5, 0, 142, 1.8, 0, '#D8A873', 'opacity=".9"'), rr(0, 9, 132, 92, 1, 'url(#qh-walnut)')]
    for yy in (15, 43, 71):
        parts.append(rr(8, yy, 116, 24, 1.5, '#8D5D36', 'stroke="#54351C" stroke-width="1"'))
        parts.append(ln('M10 %sH122' % n(yy + 2), '#fff', 1, 'stroke-opacity=".14"'))
        parts.append(cir(36, yy + 12, 3.2, '#E4C37A', 'stroke="#54351C" stroke-width=".6"'))
        parts.append(cir(96, yy + 12, 3.2, '#E4C37A', 'stroke="#54351C" stroke-width=".6"'))
    parts += [pth('M5 101H18L14 113H8Z', '#54351C'), pth('M114 101H127L124 113H118Z', '#54351C')]
    return grp(at(x, y, rot), *parts)


def tv(x, y, rot=0):
    return grp(at(x, y, rot),
        ln('M48 0L28 -32M48 0L70 -30', '#8D929A', 1.8, 'stroke-linecap="round"'),
        rr(0, 0, 100, 80, 7, 'url(#qh-tv)'),
        rr(8, 8, 66, 62, 12, '#11151C'),
        pth('M14 18Q30 10 50 12L24 56Q14 40 14 18Z', '#fff', 'opacity=".12"'),
        cir(87, 20, 4.6, '#C9CCD1'), cir(87, 37, 4.6, '#C9CCD1'),
        rr(80, 50, 14, 2, 0, '#14171D'), rr(80, 55, 14, 2, 0, '#14171D'), rr(80, 60, 14, 2, 0, '#14171D'))


def lamp(x, y, rot=0):
    return grp(at(x, y, rot),
        # a rect, not a stroked line: a gradient on a perfectly vertical line has no box to fill, so the pole never painted (critic r2: the shade hovered)
        rr(-1.9, -104, 3.8, 104, 0, 'url(#qh-stack)'),
        pth('M-14 -146H14L28 -100H-28Z', 'url(#qh-shade)'),
        ln('M-28 -100H28', '#9D7524', 1.6),
        ln('M-14 -146H14', '#FBEFC9', 1.4))


def bike(x, y, rot=0):
    w = []
    for cx in (36, 158):
        w.append(cir(cx, 60, 33, 'none', 'stroke="#191D25" stroke-width="4.4"'))
        w.append(cir(cx, 60, 29.6, 'none', 'stroke="#B7BBC1" stroke-width="1.2"'))
        sp = []
        for i in range(10):
            a = math.radians(i * 18)
            sp.append('M%s %sL%s %s' % (n(cx - 29 * math.cos(a)), n(60 - 29 * math.sin(a)), n(cx + 29 * math.cos(a)), n(60 + 29 * math.sin(a))))
        w.append(ln(' '.join(sp), '#B7BBC1', .7))
        w.append(cir(cx, 60, 3.6, '#7D828B'))
    frame = ln('M36 60L92 62L76 18L138 14M138 14L142 28L92 62M36 60L76 18M142 28L158 60', '#C2382F', 4.6, 'stroke-linejoin="round" stroke-linecap="round"')
    bits = ln('M138 14L136 0Q148 -6 156 2', '#23272F', 3.2, 'stroke-linecap="round"') + rr(62, 7, 28, 6, 3, '#191D25') + ln('M76 18L74 12', '#23272F', 3) + cir(92, 62, 7.5, '#3A404B', 'stroke="#14171D" stroke-width="1"')
    return grp(at(x, y, rot), *w, frame, bits)


def chair(x, y, rot=0):
    """A wooden kitchen chair, upright, so its back and seat read at once (it read as a ladder upside down)."""
    return grp(at(x, y, rot),
        rr(6, -66, 6.5, 66, 2, '#A97741'), rr(61.5, -66, 6.5, 66, 2, '#94673A'),
        rr(4, -70, 66, 11, 4, '#C7915A'), rr(4, -70, 66, 2, 1, '#E3B57F', 'opacity=".9"'),
        rr(10, -46, 54, 5, 1.5, '#B9834C'), rr(10, -29, 54, 5, 1.5, '#B9834C'),
        rr(-2, 0, 78, 10, 3, '#C7915A'), rr(-2, 0, 78, 2, 1, '#E3B57F', 'opacity=".9"'),
        rr(4, 10, 7, 58, 2, '#A97741'), rr(63, 10, 7, 58, 2, '#94673A'))


def branches(x, y, s=1, rot=0, flip=False):
    leaf = []
    spots = [(-58, -118, -40, '#4F8A3C'), (-40, -100, 20, '#6AA84F'), (-28, -130, -20, '#3C6E2F'), (-70, -92, 30, '#3C6E2F'), (-16, -106, 50, '#6AA84F'),
             (-50, -74, -60, '#4F8A3C'), (-84, -120, -10, '#6AA84F'), (-94, -98, -50, '#4F8A3C'), (-30, -78, 70, '#3C6E2F'), (-66, -138, 10, '#4F8A3C'),
             (-104, -134, 30, '#3C6E2F'), (-46, -146, -30, '#6AA84F'), (-12, -136, 30, '#4F8A3C'), (-112, -108, 10, '#6AA84F'), (-8, -86, 10, '#4F8A3C')]
    for lx, ly, a, c in spots:
        leaf.append('<ellipse cx="%s" cy="%s" rx="13" ry="6.2" fill="%s" transform="rotate(%s %s %s)"/>' % (n(lx), n(ly), c, n(a), n(lx), n(ly)))
    stem = ln('M0 0C-14 -40 -28 -64 -60 -112M-30 -58C-22 -80 -22 -100 -18 -124M-44 -82C-66 -94 -84 -96 -104 -112M-54 -100C-56 -118 -52 -130 -50 -142', '#6B4A2B', 3.2, 'stroke-linecap="round"')
    return grp(at(x, y, rot, s) + (' scale(-1 1)' if flip else ''), stem, *leaf)


def planks(x, y, rot=0):
    return grp(at(x, y, rot),
        rr(0, 0, 310, 13, 1, 'url(#qh-plank)'), rr(0, 0, 310, 1.4, 0, '#fff', 'opacity=".5"'), rr(304, 0, 6, 13, 0, '#A98B5C'),
        cir(20, 6.5, 1.3, '#5E4426'), cir(120, 6.5, 1.3, '#5E4426'), cir(240, 6.5, 1.3, '#5E4426'),
        grp(at(26, -22, 3), rr(0, 0, 280, 12, 1, '#D7DCE0'), rr(0, 0, 280, 1.2, 0, '#fff', 'opacity=".7"'), rr(0, 9, 280, 3, 0, '#A9B0B6'), rr(276, 0, 4, 12, 0, '#C9B48E')))


def tarp(x, y, rot=0):
    return grp(at(x, y, rot),
        pth('M0 84L18 40L54 14L96 2L132 10L170 30L196 62L224 96L176 92L150 104L104 96L72 106L34 92Z', 'url(#qh-tarp)'),
        pth('M54 14L44 56L52 96L72 106L66 60L78 8Z', '#1D4F88', 'opacity=".62"'),
        pth('M132 10L138 52L132 100L150 104L156 56L150 20Z', '#1D4F88', 'opacity=".55"'),
        pth('M96 2L102 44L98 90L104 96L114 46L110 4Z', '#6EB0EA', 'opacity=".35"'),
        ln('M12 62C22 40 38 24 58 16', '#fff', 2, 'stroke-opacity=".3" stroke-linecap="round"'),
        cir(8, 80, 2.6, '#E7E9EC'), cir(70, 100, 2.6, '#E7E9EC'), cir(150, 98, 2.6, '#E7E9EC'), cir(216, 92, 2.6, '#E7E9EC'))


def tyre_item(x, y, s=1):
    return grp(at(x, y, 0, s),
        cir(0, 0, 40, 'url(#qh-tyre)'),
        cir(0, 0, 39.6, 'none', 'stroke="#07090C" stroke-width="2.2" stroke-dasharray="5 2.4"'),
        cir(0, 0, 18, '#1B2029'), cir(0, 0, 18, 'none', 'stroke="#3E444F" stroke-width="1.2"'))


def bucket(x, y, rot=0):
    return grp(at(x, y, rot),
        ln('M2 2C6 -22 44 -22 48 2', '#8D929A', 1.8),
        pth('M0 2H50L44 50H6Z', '#E07B2A'), pth('M36 2H50L44 50H34Z', '#B85F1C'),
        rr(-1.5, 0, 53, 5, 1.5, '#F09A52'))


# The three things that can't go on the truck, for Services' "What we can't take" band. Same hand and same paint as the load, and each stands on its own contact shadow.
def paint_can(x, y):
    return grp(at(x, y),
        '<ellipse cx="46" cy="104" rx="58" ry="7" fill="url(#qh-contact)"/>',
        ln('M3 14C8 -24 84 -24 89 14', '#8D929A', 2.6),
        cir(3, 14, 3.2, '#6E737C'), cir(89, 14, 3.2, '#6E737C'),
        rr(0, 8, 92, 96, 3, 'url(#qh-stack)'),
        rr(0, 28, 92, 56, 0, 'url(#qh-teal)'),
        rr(0, 28, 92, 3, 0, '#fff', 'opacity=".22"'),
        rr(16, 42, 60, 28, 2, '#F7F3EA'),
        rr(23, 49, 46, 4, 0, '#1F5356'), rr(23, 58, 30, 3, 0, '#1F5356', 'opacity=".6"'),
        # paint that has run down the side, from under the lid
        pth('M58 10H80V34C80 39 77 41 74.5 41C72 41 70 39 70 35V26C70 23 66 23 66 26V29C66 33 60 33 60 29Z', '#D9754E'),
        rr(-2, 3, 96, 10, 3, '#D3D5D8'), rr(-2, 3, 96, 2.6, 1, '#F7F7F6'),
        rr(-1, 96, 94, 8, 2, '#9A9EA5'), rr(-1, 96, 94, 2, 0, '#fff', 'opacity=".4"'))


def propane_tank(x, y):
    return grp(at(x, y),
        '<ellipse cx="43" cy="170" rx="54" ry="7" fill="url(#qh-contact)"/>',
        # the foot ring, then the tank over it
        pth('M12 146H74V164Q74 170 68 170H18Q12 170 12 164Z', '#20242D'),
        rr(22, 158, 42, 6, 3, '#3B414E'),
        rr(0, 32, 86, 126, 38, 'url(#qh-tarp)'),
        rr(10, 54, 9, 84, 4.5, '#fff', 'opacity=".3"'),
        rr(0, 92, 86, 2.4, 0, INK, 'opacity=".2"'),
        # warning label with a flame
        rr(25, 72, 38, 42, 3, '#F7F3EA'),
        pth('M44 78C50 86 55 91 55 98C55 104 50 108 44 108C38 108 33 104 33 98C33 94 35 91 38 88C38 92 40 94 42 93C43 89 42 84 44 78Z', '#E07B2A'),
        pth('M44 92C47 96 49 98 49 101C49 104 47 106 44 106C41 106 39 104 39 101C39 98 42 96 44 92Z', '#F4D35E'),
        # the collar, with its carrying slot, and the valve inside it
        pth('M10 44V24Q10 12 22 12H64Q76 12 76 24V44Q43 32 10 44Z', 'url(#qh-rail)'),
        rr(24, 19, 38, 10, 5, '#2A2F38'),
        rr(36, 2, 14, 12, 1.5, '#8D929A'),
        rr(29, -4, 28, 7, 3.5, '#C4241C'), rr(29, -4, 28, 2, 1, '#fff', 'opacity=".35"'))


def car_battery(x, y):
    return grp(at(x, y),
        '<ellipse cx="64" cy="92" rx="74" ry="7" fill="url(#qh-contact)"/>',
        # terminals
        rr(19, -4, 20, 13, 2, '#C4241C'), rr(19, -4, 20, 3, 1, '#fff', 'opacity=".35"'),
        rr(89, -4, 20, 13, 2, '#343B48'), rr(89, -4, 20, 3, 1, '#fff', 'opacity=".25"'),
        rr(0, 18, 128, 74, 4, 'url(#qh-dark)'),
        rr(-3, 8, 134, 15, 3, '#3B414E'), rr(-3, 8, 134, 2.4, 1, '#6E737C'),
        # plus and minus on the lid
        rr(24, 14, 10, 2.6, 0, '#F7F3EA'), rr(27.7, 10.3, 2.6, 10, 0, '#F7F3EA'),
        rr(94, 14, 10, 2.6, 0, '#F7F3EA'),
        # the label
        rr(13, 36, 102, 42, 3, 'url(#qh-amber)'),
        rr(23, 46, 58, 5, 0, INK, 'opacity=".75"'), rr(23, 56, 82, 3, 0, INK, 'opacity=".5"'), rr(23, 63, 44, 3, 0, INK, 'opacity=".5"'))


def canvas_tarp():
    folds = 'M120 190C150 206 170 232 176 258M226 152C236 186 230 226 238 258M300 130C318 170 316 220 326 258M392 110C396 150 410 206 404 258M470 110C474 150 462 214 470 258M556 134C560 170 574 220 568 258M640 152C636 190 650 230 644 258'
    return (pth(PILE, 'url(#qh-canvas)')
            + ln(folds, '#12151B', 2.4, 'stroke-opacity=".55" stroke-linecap="round"')
            + '<g transform="translate(3 0)">%s</g>' % ln(folds, '#fff', 1.4, 'stroke-opacity=".12" stroke-linecap="round"')
            + ln('M112 192C200 170 320 140 430 120C520 122 620 150 690 176', '#C9B48E', 1.6, 'stroke-opacity=".75" stroke-dasharray="7 2"'))


# (id, level, drawing), back to front. A level's items show from that load up.
LOAD = [
    ('pile', 4, canvas_tarp()),
    ('lamp', 4, lamp(672, 218, 7)),
    ('branches', 4, branches(150, 256, 1.06, 0)),
    ('branchesB', 4, branches(70, 262, .84, 8, True)),
    ('planks', 4, planks(116, 172, -8)),
    ('chair', 4, chair(238, 172, -9)),
    ('mattress', 3, mattress(116, 224, -3)),
    ('fridge', 3, fridge(36, 242, 0)),
    ('bagA', 3, bag(128, 352, .98)),
    ('tv', 4, tv(352, 126, -8)),
    ('boxTopA', 4, box(330, 202, 92, 62, -4)),
    ('boxTopB', 4, box(428, 192, 74, 70, 5, False)),
    ('bike', 4, bike(424, 104, -9)),
    ('bagTopA', 4, bag(126, 186, .78, -8)),
    ('tarp', 4, tarp(488, 166, 2)),
    ('dresser', 4, dresser(572, 142, -5)),
    ('tyre', 4, tyre_item(306, 226, .78)),
    ('heapShade', 4, '<rect x="34" y="214" width="690" height="40" fill="url(#qh-heapShade)" clip-path="url(#qh-pileClip)"/>'),
    ('boxB', 2, box(258, 296, 82, 66, -3)),
    ('boxA', 2, box(248, 356, 100, 82)),
    ('bagE', 2, bag(136, 366, .8)),
    ('bagC', 2, bag(204, 370, .74)),
    ('chairSeat', 1, armchair(350, 320)),
    ('boxSmall', 2, box(374, 276, 62, 46, 2, False)),
    ('sofa', 1, sofa(470, 310)),
    ('bucket', 2, bucket(572, 322, -3)),
]


def load_defs():
    return ''.join('<g id="qh-i-%s">%s</g>' % (i, d) for i, _, d in LOAD)


# ===== Truck groups =====
def truck_defs():
    d = [PAINT,
         '<g id="qh-wheelF">%s</g>' % wheel_parts(False),
         '<g id="qh-wheelR">%s</g>' % wheel_parts(True),
         '<g id="qh-wheelLight">%s</g>' % WHEEL_LIGHT,
         '<g id="qh-chassis">%s</g>' % chassis(),
         '<g id="qh-fender">%s</g>' % rear_fender(),
         '<g id="qh-back">%s</g>' % bed_back(),
         '<g id="qh-side">%s</g>' % bed_side(),
         '<g id="qh-cabin">%s</g>' % cab(),
         '<g id="qh-shadow">%s</g>' % SHADOW,
         load_defs(),
         '<g id="qh-load-full">%s</g>' % uses(4)]
    return ''.join(d)


WHEELS = [('qh-wheelR', 220, 540), ('qh-wheelR', 360, 540), ('qh-wheelF', 862, 540)]


def wheels_markup(cls=''):
    out = []
    c = ' class="%s"' % cls if cls else ''
    for ref, x, y in WHEELS:
        out.append('<g transform="translate(%d %d)"><use%s href="#%s"/><use href="#qh-wheelLight"/></g>' % (x, y, c, ref))
    return ''.join(out)


# Two shadows: one falling behind the truck on whatever it stands in front of (the lawn, in the hero), so it stops reading as a sticker (critic r1),
# and the contact shadow on the band it parks on.
SHADOW = '<ellipse cx="520" cy="574" rx="530" ry="46" fill="url(#qh-contact)" opacity=".62"/>' \
         + '<ellipse cx="520" cy="602" rx="540" ry="15" fill="url(#qh-contact)"/>' \
         + ''.join('<ellipse cx="%d" cy="601" rx="72" ry="7" fill="%s" opacity=".5"/>' % (x, INK) for _, x, _ in WHEELS)


def uses(level):
    return ''.join('<use href="#qh-i-%s"/>' % i for i, lv, _ in LOAD if lv <= level)


def truck_body(level):
    return (SHADOW + '<use href="#qh-chassis"/>' + wheels_markup().replace('<use href="#qh-wheelLight"/>', '<use href="#qh-wheelLight"/>')
            + '<use href="#qh-fender"/><use href="#qh-back"/>' + uses(level) + '<use href="#qh-side"/><use href="#qh-cabin"/>')


def hero_svg():
    """Inline, piled high: the page's script rolls it in and spins the wheels by the distance it travels."""
    return ('<svg class="m-truck" viewBox="%s" role="img" aria-label="The Quick Haul truck, piled high with a sofa, boxes, a mattress, a dresser, a bike and yard waste" data-truck-roll>'
            '<use href="#qh-shadow"/><g class="m-truck__body"><use href="#qh-chassis"/></g>%s'
            '<g class="m-truck__body"><use href="#qh-fender"/><use href="#qh-back"/><use href="#qh-load-full"/><use href="#qh-side"/><use href="#qh-cabin"/></g></svg>'
            % (VIEW, wheels_markup('m-truck__spin')))


def gauge_svg():
    """Inline, every item its own element, so a load can drop in piece by piece. Starts at 1/8; works without the script."""
    items = []
    for i, lv, _ in LOAD:
        off = ' -off' if lv > 1 else ''
        items.append('<use class="m-truck__item%s" data-truck-level="%d" href="#qh-i-%s"/>' % (off, lv, i))
    return ('<svg class="m-truck -gauge" viewBox="%s" role="img" aria-label="The Quick Haul truck carrying an eighth of a load" data-truck-gauge>'
            '<use href="#qh-shadow"/><g class="m-truck__body"><use href="#qh-chassis"/></g>%s'
            '<g class="m-truck__body"><use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/></g></svg>'
            % (VIEW, wheels_markup(), ''.join(items)))


def banner_svg():
    """Inner page banners: a truck carrying what suits the page, standing still. Only Home's is piled high and backs in, so a banner never reads as a second hero (critic r2-1). Services: half a load."""
    return ('<svg class="m-truck" viewBox="%s" role="img" aria-label="The Quick Haul truck, half loaded, parked on the street">'
            '<use href="#qh-shadow"/><use href="#qh-chassis"/>%s<use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, wheels_markup(), uses(3)))


LOAD_LABELS = {1: 'an eighth of a load', 2: 'a quarter of a load', 3: 'half a load', 4: 'a full load, piled high'}


def row_svg(level):
    """The Services price row: the same truck at each load, drawn from the page's one sprite rather than four 75 KB files. Level 4 is the same full body as Commercial's banner, no heap and no "piled high", because this row is never on Home (Varun's ruling, batch d)."""
    if level == 4:
        return banner_full_svg().replace(', parked on the street', '')
    return ('<svg class="m-truck" viewBox="%s" role="img" aria-label="The Quick Haul truck with %s"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, LOAD_LABELS[level], wheels_markup(), uses(level)))


# Inner banners: a load that suits the page (revision.md section 5). Words: copy.md, Truck labels. Services' half load is banner_svg above.
BANNER_LOADS = {
    'truck-banner-eighth': (1, 'The Quick Haul truck with a small load, parked on the street'),
    'truck-banner-quarter': (2, 'The Quick Haul truck, a quarter loaded, parked on the street'),
}


def banner_load_svg(level, label):
    return ('<svg class="m-truck" viewBox="%s" role="img" aria-label="%s"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, label, wheels_markup(), uses(level)))


def banner_full_svg():
    """Commercial: a full body, not a heap. The half load with boxes over the sofa, up to the rail and no higher, so "piled high" stays Home's (Studio Lead's ruling on Donate, 5 Nov; revision.md section 5) while copy.md's label, "with a full load", stays true. revision.md's table names truck-full here, the one row that disagrees with its own rule."""
    over = box(462, 262, 88, 56) + box(552, 268, 74, 50, 2, False) + box(628, 260, 84, 58, -1)
    return ('<svg class="m-truck" viewBox="%s" role="img" aria-label="The Quick Haul truck with a full load, parked on the street"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/>%s%s<use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, wheels_markup(), uses(3), over))


def banner_empty_svg():
    """The 404: decorative, no label (copy.md, Truck labels)."""
    return ('<svg class="m-truck" viewBox="%s" aria-hidden="true" focusable="false"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/><use href="#qh-side"/><use href="#qh-cabin"/></svg>'
            % (VIEW, wheels_markup()))


# Donate's load: a quarter, all of it below the rail. It was the high heap with the dresser, bike and lamp taken off; Studio Lead's ruling, 5 Nov: "piled high" belongs to Home alone (revision.md section 5). Lighter also leaves the dresser and bike as the drawing's one idea, the good stuff set apart.
DONATE_LOAD = 2


def banner_donate_svg():
    """Donate: the same drawing as truck-donate.svg, inline, with the dresser and bike at the curb and a light load in the body."""
    load = uses(DONATE_LOAD)
    return ('<svg class="m-truck" viewBox="-400 62 1464 558" role="img" aria-label="The Quick Haul truck with a dresser and a bike set apart at the curb"><g class="m-truck__rig"><use href="#qh-shadow"/><use href="#qh-chassis"/>%s'
            '<use href="#qh-fender"/><use href="#qh-back"/>%s<use href="#qh-side"/><use href="#qh-cabin"/></g>'
            '<g class="m-truck__curb"><ellipse cx="-214" cy="602" rx="190" ry="10" fill="url(#qh-contact)"/>%s</g></svg>'
            % (wheels_markup(), load, curb_items(-392)))


def inline_parts(sprite):
    """The fragments tools/build.py pulls in with {{> truck-...}}. Generated: edit this script, not those files."""
    os.makedirs(PARTS, exist_ok=True)
    parts = [('truck-sprite', sprite), ('truck-hero', hero_svg()), ('truck-gauge', gauge_svg()), ('truck-banner', banner_svg())]
    parts += [('truck-row-%d' % level, row_svg(level)) for level in LOAD_LABELS]
    parts += [(key, banner_load_svg(level, label)) for key, (level, label) in BANNER_LOADS.items()]
    parts += [('truck-banner-full', banner_full_svg()), ('truck-banner-empty', banner_empty_svg()), ('truck-banner-donate', banner_donate_svg())]
    for key, value in parts:
        with open(os.path.join(PARTS, key + '.html'), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(value + '\n')


def standalone(view, body, defs, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-label="%s"><defs>%s</defs>%s</svg>\n' % (view, title, defs, body))


# ===== Curb art: the good stuff set apart beside the truck (Donate), and single items (section art) =====
def curb_items(x0):
    return dresser(x0, 488, 0, slab=False) + bike(x0 + 158, 500, 0)


def item_files(paint):
    def wrap(view, body, title):
        return standalone(view, body, paint, title)

    def foot(cx, cy, rx, ry=4.5):
        """The soft shadow where an item meets the card or the fold, the truck's own. Inside each file's viewBox."""
        return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="url(#qh-contact)"/>' % (n(cx), n(cy), n(rx), n(ry))
    return {
        'item-sofa.svg': wrap('-6 -6 248 142', foot(118, 129, 122, 5.5) + sofa(0, 0, ground=False), 'A sofa'),
        'item-armchair.svg': wrap('-6 -6 124 132', foot(56, 119, 60, 5) + armchair(0, 0, ground=False), 'An armchair'),
        # Leaning right on whatever stands beside it, on its bottom right corner: stood square on its own it read as a framed picture. 5 degrees, 250 by 190 so it isn't the biggest thing on the shelf; the numbers put that corner at 236, 205
        'item-mattress.svg': wrap('-16 -10 272 223', foot(118, 206, 128, 5) + mattress(3.5, -6.1, 5, w=250, h=190, soft=True), 'A mattress'),
        'item-fridge.svg': wrap('-6 -6 98 208', foot(43, 197, 48) + fridge(0, 0, slab=False), 'A fridge'),
        'item-dresser.svg': wrap('-10 -6 152 126', foot(66, 114, 72) + dresser(0, 0, slab=False), 'A dresser'),
        'item-dresser-tv.svg': wrap('-10 -118 152 238', foot(66, 114, 72) + dresser(0, 0, slab=False) + tv(16, -80), 'An old television on a dresser'),
        'item-bags.svg': wrap('-8 -6 216 110', foot(96, 98, 100, 5) + bag(0, 2) + bag(96, 8, .9), 'Trash bags'),
        'item-boxes.svg': wrap('-6 -6 190 158', foot(91, 145, 92, 5) + box(4, 62, 104, 82, slab=False) + box(102, 84, 76, 60, slab=False) + box(26, 0, 70, 62, -3, False, slab=False), 'Moving boxes'),
        'item-bike.svg': wrap('-2 -10 200 112', foot(97, 96, 96) + bike(0, 0), 'An old bike'),
        'item-tv.svg': wrap('-6 -38 112 124', foot(50, 81, 54) + tv(0, 0), 'An old television'),
        'item-branches.svg': wrap('-126 -158 136 164', foot(-18, 1, 26, 3.5) + branches(0, 0), 'Cut branches'),
        'item-paint.svg': wrap('-14 -16 120 132', paint_can(0, 0), 'A can of paint'),
        'item-propane.svg': wrap('-14 -8 114 188', propane_tank(0, 0), 'A propane tank'),
        'item-battery.svg': wrap('-14 -8 156 110', car_battery(0, 0), 'A car battery'),
    }


def main():
    os.makedirs(OUT, exist_ok=True)
    defs = truck_defs()
    variants = [('truck-empty.svg', 0, 'The Quick Haul truck, empty'),
                ('truck-eighth.svg', 1, 'The Quick Haul truck with an eighth of a load'),
                ('truck-quarter.svg', 2, 'The Quick Haul truck with a quarter of a load'),
                ('truck-half.svg', 3, 'The Quick Haul truck half full'),
                ('truck-full.svg', 4, 'The Quick Haul truck piled high')]
    written = {}
    for name, level, title in variants:
        written[name] = standalone(VIEW, truck_body(level), defs, title)
    # banner art: the same truck cropped to the cab and the front of the load, for narrow banners
    written['truck-nose.svg'] = standalone('560 72 504 548', truck_body(4), defs, 'The front of the Quick Haul truck, piled high')
    # section art for Donate: the good stuff set apart at the curb, in front of the empty end of the truck
    # The dresser and bike stand at the curb, and the light load (DONATE_LOAD) has neither on it (critic r1: they were on the pile as well)
    donate_body = truck_body(DONATE_LOAD)
    written['truck-donate.svg'] = standalone('-400 62 1464 558', donate_body + '<ellipse cx="-214" cy="602" rx="190" ry="10" fill="url(#qh-contact)"/>' + curb_items(-392), defs, 'The Quick Haul truck, with a dresser and a bike set apart at the curb')
    written.update(item_files(PAINT))
    for name, svg in written.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(svg)
    # the shared inline sprite and the inline trucks, for the pages
    sprite = '<svg class="qh-sprite" width="0" height="0" aria-hidden="true" focusable="false"><defs>%s</defs></svg>' % defs
    inline_parts(sprite)
    print('wrote', len(written), 'files;', 'truck-full.svg', os.path.getsize(os.path.join(OUT, 'truck-full.svg')) // 1024, 'KB;', 'sprite', len(sprite) // 1024, 'KB')


if __name__ == '__main__':
    main()
