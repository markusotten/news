"""Phase 4 driver: fetch every fetchable product's What's New URL, extract
entries with the standing method in whatsnew_extract.py, and diff against
citrix/.whatsnew-cache.json.

Reads citrix/citrix-products.md for the product list (skips rows marked
`none`, `unverified:` or `unresolved`), fetches each URL with curl, extracts
entries, and reports which hashes are new. Special-cased handling for known
thin/stub pages (currently: uberAgent, whose What's New URL redirects to a
version-index stub — this script follows the stub's "About <newest version>"
link automatically) lives in `SPECIAL_CASES` below; extend it if a future run
finds another product doing the same thing.

Usage:
    cd citrix && python3 whatsnew_run.py [--fetch-dir DIR]

Writes extraction_results.json (all entries + hashes, for inspection) into
--fetch-dir. Does NOT itself update .whatsnew-cache.json or the daily note —
that stays a deliberate step in the skill run so a bad extraction doesn't
silently overwrite the cache.
"""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
from whatsnew_extract import parse_html, extract_entries, hash_entry


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def load_products(catalog_path):
    text = Path(catalog_path).read_text(encoding='utf-8')
    rows = re.findall(r'^\| (.+?) \| (\S+) \| (.+?) \|\s*$', text, re.M)
    out = []
    for name, docs_url, wn in rows:
        wn = wn.strip()
        if name == 'Product' or name.startswith('---'):
            continue
        if wn == 'none' or wn.startswith('unverified') or wn == 'unresolved':
            continue
        out.append((name, wn))
    return out


def fetch(url, out_path):
    return subprocess.run(
        ['curl', '-sS', '-m', '25', '-L', '-o', str(out_path), '-w', '%{http_code}'],
        capture_output=True, text=True,
    ).stdout.strip() + subprocess.run(
        ['curl', '-sS', '-m', '25', '-L', '-o', str(out_path), '-w', '%{http_code}', url],
        capture_output=True, text=True,
    ).stdout.strip()


def curl_to(url, out_path, timeout=25):
    r = subprocess.run(
        ['curl', '-sS', '-m', str(timeout), '-L', '-o', str(out_path), '-w', '%{http_code}', url],
        capture_output=True, text=True,
    )
    return r.stdout.strip()


# Known stub/redirect pages that need a follow-up fetch to reach real content.
# Each entry: product name -> function(fetch_dir) -> path to the real content
# file to extract from (already fetched by the function).
def _uberagent_follow(fetch_dir):
    stub = fetch_dir / 'uberagent.html'
    text = stub.read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'href="(/en-us/uberagent/[^"]*whats-new/[^"]+)"', text)
    if not m:
        return stub  # fall back to stub itself if the link shape changed
    real_url = 'https://docs.citrix.com' + m.group(1)
    real_path = fetch_dir / 'uberagent-latest.html'
    curl_to(real_url, real_path)
    return real_path


SPECIAL_CASES = {
    'uberAgent': _uberagent_follow,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--catalog', default=str(Path(__file__).parent / 'citrix-products.md'))
    ap.add_argument('--fetch-dir', default='/tmp/whatsnew-fetch')
    args = ap.parse_args()

    fetch_dir = Path(args.fetch_dir)
    fetch_dir.mkdir(parents=True, exist_ok=True)

    products = load_products(args.catalog)
    results = {}
    for name, url in products:
        fetch_url = url.split('#')[0]
        host = urlparse(fetch_url).netloc
        fn = fetch_dir / (slugify(name) + '.html')
        code = curl_to(fetch_url, fn)
        content_path = fn
        if name in SPECIAL_CASES:
            content_path = SPECIAL_CASES[name](fetch_dir)
        html_text = content_path.read_text(encoding='utf-8', errors='ignore')
        root = parse_html(html_text)
        style, entries = extract_entries(root, host)
        hashes = [hash_entry(t, b) for t, b in entries]
        results[name] = {
            'url': url, 'http_code': code, 'style': style,
            'entries': entries, 'hashes': hashes,
        }
        print(f"{code}\t{name}\t{style}\t{len(entries)}")

    import json
    json.dump(results, open(fetch_dir / 'extraction_results.json', 'w'), indent=2)
    print(f"\nWrote {fetch_dir / 'extraction_results.json'}")


if __name__ == '__main__':
    main()
