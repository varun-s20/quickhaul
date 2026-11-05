#!/usr/bin/env python3
"""Prints the first-load weight of the revision prototype's homepage, raw and gzipped, so the numbers in revision.md are measured."""
import gzip
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEXT = ['index.html', 'assets/global.css', 'assets/global.js', 'assets/trucks/_sprite.svgfrag', 'assets/trucks/truck-full.svg']
BINARY = ['assets/fonts/biosans-extrabold.otf', 'assets/fonts/biosans-light.otf', 'assets/fonts/biosans-semibold.otf', 'assets/fonts/biosans-regular.otf', 'assets/fonts/robotomono-latin.woff2', 'assets/images/brand/quickhaul-mark.png', 'assets/images/hero-yard-1600.webp', 'assets/images/hero-yard-phone-800.webp', 'assets/images/hero-yard-phone-500.webp']
for name in TEXT:
    raw = open(os.path.join(ROOT, name), 'rb').read()
    print('%-44s %5d KB raw  %5d KB gzip' % (name, len(raw) // 1024, len(gzip.compress(raw, 9)) // 1024))
for name in BINARY:
    print('%-44s %5d KB' % (name, os.path.getsize(os.path.join(ROOT, name)) // 1024))
