"""Validate local pages, or deployed bytes with --live (standard library only)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, sys, urllib.request, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
HOST = 'https://getsayso.netlify.app'
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.feed(text)
    def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))
urls=[n.text for n in ET.parse(ROOT/'sitemap.xml').iter() if n.tag.endswith('}loc')]
assert len(urls)==len(set(urls))==12
assert 'Sitemap: '+HOST+'/sitemap.xml' in (ROOT/'robots.txt').read_text()
for url in urls:
    assert url.startswith(HOST+'/')
    path=urlsplit(url).path
    f=ROOT/path.lstrip('/')/'index.html'
    text=f.read_text(); p=Page(text)
    assert sum(t=='h1' for t,a in p.tags)==1, url
    assert [a['href'] for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[url], url
    assert any(t=='meta' and a.get('name')=='robots' and 'noindex' not in a.get('content','') for t,a in p.tags), url
    for t,a in p.tags:
        if t=='img': assert 'alt' in a, (url,a)
        for key in ('href','src','poster'):
            ref=a.get(key,''); parts=urlsplit(ref)
            if parts.netloc or parts.scheme or not parts.path: continue
            target=ROOT/unquote(parts.path).lstrip('/') if ref.startswith('/') else f.parent/unquote(parts.path)
            if target.is_dir(): target=target/'index.html'
            assert target.exists(), (url,ref)
            if parts.fragment: assert 'id="'+parts.fragment+'"' in target.read_text(), (url,ref)
    import re
    for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S): json.loads(data)
    if '--live' in sys.argv:
        with urllib.request.urlopen(url) as r:
            assert r.status==200 and 'noindex' not in r.headers.get('X-Robots-Tag',''),url
            assert r.read()==f.read_bytes(), 'Live bytes differ: '+url
        with urllib.request.urlopen(url.replace(HOST,'https://sayso-app.netlify.app')) as r: assert r.url==url, r.url
    print('PASS',path)
print('PASS: sitemap, robots, canonicals, internal links/anchors, image alternatives, JSON-LD'+(', deployed bytes and legacy redirects' if '--live' in sys.argv else ''))
