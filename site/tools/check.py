"""Quick Haul: static checks on the built site. Standard library only.

Fails (exit 1) on: em or en dashes, AI attribution, lorem or template text, missing or several h1s,
images without alt, srcset without sizes, inline style attributes or <style> in pages, duplicate ids,
anchors that point at a missing id (on this page or another), missing local files or pages, classes with
no rule in global.css, unbalanced braces in global.css, duplicate titles or descriptions, a missing
canonical, unlabelled form controls, and em or en dashes in accessible names.

Usage (from the site folder): python tools/check.py
"""
import os
import posixpath
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHIPPED_EXT = ('.html', '.css', '.js', '.json', '.svg', '.xml', '.txt')
SKIP_DIRS = {'src', 'tools', 'data', 'docs'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))

    handle_startendtag = handle_starttag


def shipped_files():
    for dirpath, dirs, files in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        if rel.split(os.sep)[0] in SKIP_DIRS:
            continue
        for f in files:
            if f.endswith(SHIPPED_EXT):
                yield os.path.join(dirpath, f)


def built_pages():
    pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]
    area = os.path.join(ROOT, 'service-area')
    if os.path.isdir(area):
        pages += ['service-area/' + f for f in os.listdir(area) if f.endswith('.html')]
    return sorted(pages)


def main():
    fails = []
    # ---- text tells in every shipped text file ----
    for path in shipped_files():
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding='utf-8').read()
        for n, line in enumerate(text.splitlines(), 1):
            if '—' in line or '–' in line:
                fails.append('%s:%d em or en dash' % (rel, n))
            if re.search(r'lorem|ipsum|\bTODO\b|\bFIXME\b|\[insert|\[your ', line, re.I):
                fails.append('%s:%d placeholder text' % (rel, n))
            if re.search(r'generated (with|by) (ai|claude|chatgpt)|claude|chatgpt|openai|anthropic|co-authored-by|name="generator"', line, re.I):
                fails.append('%s:%d AI attribution' % (rel, n))
    css = open(os.path.join(ROOT, 'assets', 'global.css'), encoding='utf-8').read()
    if css.count('{') != css.count('}'):
        fails.append('global.css: unbalanced braces')
    css_classes = set(re.findall(r'\.(-?[A-Za-z][\w-]*)', re.sub(r'url\([^)]*\)', '', css)))
    for ref in re.findall(r'url\("?([^")]+)"?\)', css):
        if not ref.startswith(('data:', '#')) and not os.path.exists(os.path.join(ROOT, 'assets', ref)):
            fails.append('global.css: missing ' + ref)
    # ---- parse every page once, then check links across pages ----
    pages = built_pages()
    parsed = {}
    for name in pages:
        html = open(os.path.join(ROOT, name), encoding='utf-8').read()
        p = Page()
        p.feed(html)
        parsed[name] = (html, p)
    ids_by_page = {n: {a.get('id') for t, a, _ in p.tags if a.get('id')} for n, (_, p) in parsed.items()}
    titles, descs = {}, {}
    for name, (html, p) in parsed.items():
        ids = [a.get('id') for t, a, _ in p.tags if a.get('id')]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            fails.append('%s: duplicate ids %s' % (name, ', '.join(sorted(dup))))
        if sum(1 for t, _, _ in p.tags if t == 'h1') != 1:
            fails.append('%s: must have exactly one h1' % name)
        if re.search(r'<style[\s>]', html):
            fails.append('%s: <style> block' % name)
        title = re.search(r'<title>(.*?)</title>', html)
        desc = re.search(r'<meta name="description" content="([^"]*)"', html)
        if not title:
            fails.append('%s: no title' % name)
        else:
            titles.setdefault(title.group(1), []).append(name)
        if desc:
            descs.setdefault(desc.group(1), []).append(name)
        elif name != '404.html':
            fails.append('%s: no description' % name)
        if not re.search(r'<link rel="canonical" href="https?://', html):
            fails.append('%s: no canonical' % name)
        labelled = {a.get('for') for t, a, _ in p.tags if t == 'label' and a.get('for')}
        base = posixpath.dirname(name)
        for t, a, line in p.tags:
            where = '%s:%d <%s>' % (name, line, t)
            if 'style' in a:
                fails.append(where + ' inline style')
            if t == 'img' and 'alt' not in a:
                fails.append(where + ' no alt')
            if t == 'source' and 'srcset' in a and 'sizes' not in a:
                fails.append(where + ' srcset without sizes')
            if t in ('button', 'a') and a.get('aria-label') == '':
                fails.append(where + ' empty aria-label')
            if t in ('input', 'select', 'textarea') and a.get('type') not in ('radio', 'checkbox', 'hidden'):
                if a.get('id') not in labelled and not a.get('aria-label') and not a.get('aria-labelledby'):
                    fails.append(where + ' no label')
            if t == 'input' and a.get('type') == 'file' and 'data-needs-endpoint' not in html:
                fails.append(where + ' file input with no endpoint gate')
            for cls in (a.get('class') or '').split():
                if cls not in css_classes and cls not in ('js',):
                    fails.append('%s class "%s" has no rule in global.css' % (where, cls))
            for attr in ('href', 'src', 'srcset', 'action'):
                val = a.get(attr)
                if not val:
                    continue
                for ref in [v.strip().split(' ')[0] for v in val.split(',')] if attr == 'srcset' else [val]:
                    if re.match(r'(https?:|tel:|mailto:|data:)', ref):
                        continue
                    target, _, frag = ref.partition('#')
                    if not target:
                        if frag and frag not in ids:
                            fails.append(where + ' anchor #%s has no target' % frag)
                        continue
                    target = target.split('?')[0]
                    resolved = target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(base, target))
                    if not os.path.exists(os.path.join(ROOT, resolved)):
                        fails.append(where + ' missing file ' + ref)
                    elif frag and resolved in ids_by_page and frag not in ids_by_page[resolved]:
                        fails.append(where + ' %s has no #%s' % (resolved, frag))
    for label, seen in (('title', titles), ('description', descs)):
        for text, names in seen.items():
            if len(names) > 1:
                fails.append('duplicate %s on %s' % (label, ', '.join(names)))
    print('Pages checked (%d): %s' % (len(pages), ', '.join(pages)))
    if fails:
        print('FAIL (%d)' % len(fails))
        for f in fails:
            print('  ' + f)
        sys.exit(1)
    print('PASS')


if __name__ == '__main__':
    main()
