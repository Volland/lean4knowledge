from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0;self.missing_alt=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in d:self.ids.add(d['id'])
  for key in ['src','href']:
   if key in d:self.links.append(d[key])
  if tag=='img' and 'alt' not in d:self.missing_alt.append(d)
pages={}
for p in ROOT.rglob('*.html'):
 page=Page();page.feed(p.read_text());pages[p.resolve()]=page
errors=[]
for p,page in pages.items():
 if page.h1!=1:errors.append(f'{p}: expected 1 h1, got {page.h1}')
 if page.missing_alt:errors.append(f'{p}: missing alt')
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  t=(ROOT/u.path.lstrip('/')) if u.path.startswith('/') else p.parent/u.path
  if not u.path:t=p
  if t.is_dir():t=t/'index.html'
  t=t.resolve()
  if not t.exists():errors.append(f'{p}: missing {link}')
  elif u.fragment and t in pages and unquote(u.fragment) not in pages[t].ids:errors.append(f'{p}: missing anchor {link}')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML pages; internal links, assets, anchors, headings, and image alternatives')
