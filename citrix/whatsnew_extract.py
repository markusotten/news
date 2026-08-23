"""Phase 4 What's New extraction/hashing method for the citrix-product-update skill.

Committed to the repo (2026-08-23) after the same hash scheme had to be
re-derived from the prose description in .skill-bugs.md on four separate
prior runs (2026-08-16/17, 2026-08-21, 2026-08-22, 2026-08-23), each time
reproducing the entry *counts* correctly but landing near-zero hash overlap
against the previous run's cache due to small, undocumented formatting
differences in the reimplementation. Import this module directly (or run it
as a CLI against one saved HTML file) instead of rewriting the method from
description again. See the `phase4-cache-hash-scheme-unreproducible` entry
in .skill-bugs.md for the full history.

Usage as a library (see citrix/whatsnew_run.py for the full Phase 4 driver):
    from whatsnew_extract import parse_html, extract_entries, hash_entry
    root = parse_html(html_text)
    style, entries = extract_entries(root, host)   # host e.g. "docs.citrix.com"
    hashes = [hash_entry(title, body) for title, body in entries]

CLI usage (debugging one page):
    python3 whatsnew_extract.py <saved.html> <host>
"""
import re, hashlib, json, sys
from html.parser import HTMLParser

STRIP_TAGS = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
CALLOUT_LABELS = {'note', 'important', 'benefits', 'warning', 'tip', 'caution',
                   'prerequisites', 'requirements', 'limitations', 'example', 'examples'}
DENYLIST_HEADINGS = {'new and enhanced features', 'fixed issues', 'known issues',
                      'removed features', 'deprecated features', 'requirement', 'removed'}


class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent')
    def __init__(self, tag, attrs, parent=None):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []  # list of Node or str
        self.parent = parent


class TreeBuilder(HTMLParser):
    VOID = {'br','img','hr','meta','link','input','area','base','col','embed',
            'param','source','track','wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root', {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, parent=self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        node = Node(tag, attrs, parent=self.stack[-1])
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag):
        # pop back to matching tag if present
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def parse_html(html_text):
    tb = TreeBuilder()
    tb.feed(html_text)
    return tb.root


def strip_tags(node):
    new_children = []
    for c in node.children:
        if isinstance(c, str):
            new_children.append(c)
        elif c.tag in STRIP_TAGS:
            continue
        else:
            strip_tags(c)
            new_children.append(c)
    node.children = new_children


def find_all(node, tag, results=None):
    if results is None:
        results = []
    for c in node.children:
        if isinstance(c, str):
            continue
        if c.tag == tag:
            results.append(c)
        find_all(c, tag, results)
    return results


def find_first(node, predicate):
    for c in node.children:
        if isinstance(c, str):
            continue
        if predicate(c):
            return c
        r = find_first(c, predicate)
        if r is not None:
            return r
    return None


def get_text(node):
    parts = []
    def walk(n):
        if isinstance(n, str):
            parts.append(n)
            return
        if n.tag == 'br':
            parts.append(' ')
        for c in n.children:
            walk(c)
    walk(node)
    text = ''.join(parts)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def has_class(node, cls):
    c = node.attrs.get('class', '')
    return cls in c.split()


def is_ancestor_tag(node, tag):
    p = node.parent
    while p is not None:
        if p.tag == tag:
            return True
        p = p.parent
    return False


def first_element_child(node):
    for c in node.children:
        if isinstance(c, str):
            if c.strip():
                return None  # non-empty text before element -> not "first child"
            continue
        return c
    return None


def extract_entries(root, host):
    strip_tags(root)

    if host in ('docs.citrix.com', 'docs.xenserver.com'):
        region = find_first(root, lambda n: has_class(n, 'sub-content-main'))
        if region is None:
            body = find_first(root, lambda n: n.tag == 'body')
            region = body if body is not None else root
    else:
        body = find_first(root, lambda n: n.tag == 'body')
        region = body if body is not None else root

    # narrative style detection: 3+ <p> whose first element child is <strong>,
    # excluding p nested in li/td, excluding callout labels
    all_p = find_all(region, 'p')
    narrative_candidates = []
    for p in all_p:
        if is_ancestor_tag(p, 'li') or is_ancestor_tag(p, 'td'):
            continue
        fc = first_element_child(p)
        if fc is None or fc.tag != 'strong':
            continue
        strong_text = get_text(fc).strip().rstrip(':').strip()
        if strong_text.lower() in CALLOUT_LABELS:
            continue
        if not strong_text:
            continue
        narrative_candidates.append((p, fc, strong_text))

    entries = []
    style = None
    if len(narrative_candidates) >= 3:
        style = 'narrative'
        for p, fc, title in narrative_candidates:
            full_text = get_text(p)
            title_text = title
            rest = full_text
            # remove the leading title text once
            if rest.startswith(title):
                rest = rest[len(title):]
            rest = rest.lstrip(': ').strip()
            entries.append((title_text, rest))
    else:
        # heading based: try h4, h3, h2, pick level with MOST headings (>1)
        best_level = None
        best_headings = []
        for level in ('h4', 'h3', 'h2'):
            heads = find_all(region, level)
            filtered = [h for h in heads if get_text(h).strip().lower() not in DENYLIST_HEADINGS
                        and get_text(h).strip()]
            if len(filtered) > 1:
                if best_level is None or len(filtered) > len(best_headings):
                    best_level = level
                    best_headings = filtered
        if best_headings:
            style = 'heading'
            for h in best_headings:
                title_text = get_text(h)
                # gather following sibling text nodes until next heading of same/higher level
                body_text = collect_following_text(h)
                first_line = first_line_of(body_text)
                entries.append((title_text, first_line))
        else:
            # single-entry fallback
            h1 = find_first(region, lambda n: n.tag == 'h1')
            if h1 is None:
                h1 = find_first(root, lambda n: n.tag == 'h1')
            p_count_narrative_check = len(all_p)
            if h1 is not None:
                style = 'single'
                title_text = get_text(h1)
                # first <p> after h1 anywhere in region
                first_p = None
                for p in all_p:
                    if get_text(p):
                        first_p = p
                        break
                body_text = get_text(first_p) if first_p is not None else ''
                entries.append((title_text, body_text))

    return style, entries


def collect_following_text(heading_node):
    """Collect text of siblings following heading_node within its parent until
    another heading tag of level <=? Simplify: until next h2/h3/h4 sibling or end."""
    parent = heading_node.parent
    if parent is None:
        return ''
    idx = None
    for i, c in enumerate(parent.children):
        if c is heading_node:
            idx = i
            break
    if idx is None:
        return ''
    texts = []
    for c in parent.children[idx+1:]:
        if isinstance(c, str):
            continue
        if c.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            break
        t = get_text(c)
        if t:
            texts.append(t)
        if len(' '.join(texts)) > 400:
            break
    return ' '.join(texts)


def first_line_of(text):
    text = text.strip()
    if not text:
        return ''
    # split on sentence-ish boundary: first '. ' or newline already collapsed
    m = re.search(r'(.{0,300}?[.!?])(\s|$)', text)
    if m:
        return m.group(1).strip()
    return text[:300].strip()


def hash_entry(title, first_line):
    key = f"{title.strip().lower()}|{first_line.strip().lower()}"
    return hashlib.md5(key.encode('utf-8')).hexdigest()[:12]


if __name__ == '__main__':
    import sys
    fn = sys.argv[1]
    host = sys.argv[2]
    html_text = open(fn, encoding='utf-8', errors='ignore').read()
    root = parse_html(html_text)
    style, entries = extract_entries(root, host)
    print("STYLE:", style, "COUNT:", len(entries))
    for t, b in entries[:10]:
        print("-", t, "::", b[:120])
