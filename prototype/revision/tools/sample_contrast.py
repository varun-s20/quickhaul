#!/usr/bin/env python3
"""Reads a screenshot taken with the hero's text hidden and reports the contrast of cream text over the worst pixels in each zone.

Usage: python tools/sample_contrast.py <shot.png> <name:x0,y0,x1,y1> [<name:x0,y0,x1,y1> ...]
Worst case is the 99.5th percentile brightest pixel, so one stray highlight does not decide it, and also the absolute brightest.
"""
import sys

from PIL import Image

CREAM = (247, 239, 236)


def lin(c):
    c /= 255
    return c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4


def lum(rgb):
    return .2126 * lin(rgb[0]) + .7152 * lin(rgb[1]) + .0722 * lin(rgb[2])


def ratio(a, b):
    hi, lo = max(a, b), min(a, b)
    return (hi + .05) / (lo + .05)


def main():
    im = Image.open(sys.argv[1]).convert('RGB')
    fg = lum(CREAM)
    for arg in sys.argv[2:]:
        name, box = arg.split(':')
        crop = im.crop(tuple(int(v) for v in box.split(',')))
        values = sorted(lum(p) for p in crop.getdata())
        p995 = values[int(len(values) * .995) - 1]
        print('%-18s p99.5 %.2f:1   brightest %.2f:1   median %.2f:1' % (name, ratio(fg, p995), ratio(fg, values[-1]), ratio(fg, values[len(values) // 2])))


if __name__ == '__main__':
    main()
