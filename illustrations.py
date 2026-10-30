from math import sin,cos,pi
from pathlib import Path
A=Path(__file__).parent/'dist/assets'
INK='#24241f'; RED='#d74220'; PAPER='#f5f0e6'
def hero():
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 480" role="img" aria-labelledby="title desc"><title id="title">The tree of verified knowledge</title><desc id="desc">A botanical graph grows from Lean's logical foundation. Branches connect data, types, proofs and knowledge beneath a vermilion sun.</desc><defs><pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><path d="M0 0V5" stroke="{INK}" stroke-width="1"/></pattern></defs>'''
 for i in range(24):
  a=i*pi/12; x=282+cos(a)*66;y=121+sin(a)*66;X=282+cos(a)*88;Y=121+sin(a)*88
  s+=f'<path d="M{x:.1f} {y:.1f} L{X:.1f} {Y:.1f}" stroke="{RED}" stroke-width="{4 if i%2 else 7}"/>'
 s+=f'<circle cx="282" cy="121" r="52" fill="{RED}"/><text x="282" y="136" fill="{PAPER}" text-anchor="middle" font-family="Georgia,serif" font-size="45">⊢</text>'
 # double-lined trunk and branches
 paths=['M267 403 C267 343 263 291 278 235','M281 403 C279 350 281 286 287 232','M272 348 C220 322 174 279 143 228','M276 313 C319 296 354 256 381 216','M274 374 C321 364 368 339 408 300','M264 376 C218 365 182 352 151 321','M276 279 C243 260 220 224 208 191']
 for p in paths:s+=f'<path d="{p}" stroke="{INK}" stroke-width="5" fill="none"/>'
 nodes=[(143,228,18),(381,216,20),(408,300,16),(151,321,15),(208,191,14),(278,235,13),(341,344,11),(215,310,11)]
 for x,y,r in nodes:s+=f'<circle cx="{x}" cy="{y}" r="{r+5}" fill="{PAPER}" stroke="{INK}" stroke-width="2"/><circle cx="{x}" cy="{y}" r="{r-5}" fill="{RED}"/>'
 # cut-paper leaves
 for x,y,flip in [(247,341,-1),(223,322,1),(189,289,-1),(176,270,1),(303,300,1),(329,275,-1),(355,249,1),(314,364,-1),(361,340,1),(219,363,-1),(179,345,1),(241,257,1)]:
  s+=f'<path d="M{x} {y} q{flip*5} -29 {flip*31} -34 q{-flip*1} 29 {-flip*31} 34Z" fill="{INK}"/><path d="M{x} {y} l{flip*23} -26" stroke="{PAPER}" stroke-width="1"/>'
 # wheat/botanical margins
 for bx,by,flip in [(68,401,1),(467,402,-1),(105,404,-1),(441,404,1)]:
  s+=f'<path d="M{bx} {by} q{flip*8} -58 0 -116" fill="none" stroke="{INK}" stroke-width="2"/>'
  for j in range(5):
   y=by-15-j*18
   s+=f'<path d="M{bx} {y} q-24 -1 -22 -21 q22 3 22 21 M{bx} {y-7} q24 -1 22 -21 q-22 3 -22 21" fill="{RED if j%3==0 else INK}"/>'
 s+=f'<path d="M57 413 Q270 389 485 413 M90 422 Q270 403 453 422" fill="none" stroke="{INK}" stroke-width="2"/>'
 for x,y,label in [(90,193,'DATA'),(365,179,'TYPES'),(406,274,'PROOFS'),(164,156,'RULES')]:s+=f'<text x="{x}" y="{y}" font-family="monospace" font-size="10" letter-spacing="2" fill="{INK}">{label}</text>'
 s+=f'<text x="276" y="451" font-family="monospace" font-size="10" text-anchor="middle" letter-spacing="3" fill="{INK}">ROOTED IN LOGIC. CHECKED IN LEAN.</text><path d="M34 41h55M34 41v55M504 41h-55M504 41v55M34 449v-55M34 449h22M504 449v-55M504 449h-22" stroke="{INK}" fill="none"/></svg>'
 return s

def mini(n):
 start=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 145" aria-hidden="true"><g fill="none" stroke="{INK}" stroke-width="1.6">'
 if n%3==0:
  start+='<path d="M105 111V45H181V82H255V35M105 82H255M181 45V20"/>'
  for x,y in [(105,111),(105,45),(181,45),(181,82),(255,82),(255,35),(181,20)]:start+=f'<circle cx="{x}" cy="{y}" r="9" fill="{RED if x==181 else PAPER}"/>'
 elif n%3==1:
  start+='<path d="M95 100L143 42L195 100L249 42M95 100H249M143 42H249M195 100L249 100"/>'
  for x,y in [(95,100),(143,42),(195,100),(249,42),(249,100)]:start+=f'<circle cx="{x}" cy="{y}" r="13" fill="{PAPER}"/>'
  start+=f'<circle cx="195" cy="100" r="7" fill="{RED}"/>'
 else:
  start+=f'<rect x="75" y="35" width="66" height="76"/><path d="M88 54h38M88 65h27M88 76h33M160 73h39m-7-6 7 6-7 6"/><circle cx="246" cy="73" r="39"/><path d="m225 73 14 14 26-29" stroke="{RED}" stroke-width="5"/>'
 return start+'</g></svg>'

def pipeline():
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1050 295" role="img" aria-labelledby="t d"><title id="t">A certificate crosses the trust boundary</title><desc id="d">Data and proposed claims enter search, which produces a certificate. A verified checker accepts evidence under formal semantics. Storage adapters are independent of this proof pipeline.</desc><rect width="1050" height="295" fill="{PAPER}"/><g font-family="monospace" font-size="13" text-anchor="middle" fill="{INK}">'
 for x,title,sub in [(20,'DATA + CLAIM','RDF graph / query'),(285,'SEARCH','Elpi / other producer'),(550,'CERTIFICATE','Derivation DAG'),(815,'CHECK','Verified Lean checker')]:
  s+=f'<rect x="{x}" y="90" width="215" height="100" fill="none" stroke="{RED if x==815 else INK}" stroke-width="2"/><text x="{x+107}" y="130">{title}</text><text x="{x+107}" y="158" font-size="10">{sub}</text>'
  if x<815:s+=f'<path d="M{x+224} 140h30m-8-6 8 6-8 6" fill="none" stroke="{INK}"/>'
 s+=f'<path d="M790 55V230" stroke="{RED}" stroke-dasharray="5 5"/><text x="790" y="35" fill="{RED}" font-size="11">TRUST BOUNDARY</text><text x="420" y="230" font-size="11">SEARCH MAY BE WRONG. EVIDENCE MUST CHECK.</text><text x="922" y="230" font-size="11">ENTAILMENT</text><text x="525" y="276" font-size="10">Guarantees depend on the formal model, axioms, inputs, and execution path.</text></g></svg>'
 return s
A.mkdir(parents=True,exist_ok=True)
(A/'knowledge-tree.svg').write_text(hero())
(A/'proof-pipeline.svg').write_text(pipeline())
for i in range(3):(A/f'article-{i}.svg').write_text(mini(i))
(A/'favicon.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50"><rect width="50" height="50" rx="5" fill="{PAPER}"/><path d="M15 9v32M15 25h25" stroke="{RED}" stroke-width="5"/><circle cx="40" cy="25" r="5" fill="{INK}"/></svg>')
