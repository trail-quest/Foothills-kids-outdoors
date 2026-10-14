# Edit BRAND and re-run `python3 build.py` to rename the site everywhere.
BRAND = "Foothills Kids Outdoors"
SCENE = """<svg class="scene" viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8ecae6"/><stop offset=".7" stop-color="#e9f5db"/><stop offset="1" stop-color="#fefae0"/></linearGradient></defs>
<rect width="1200" height="300" fill="url(#sky)"/><circle cx="980" cy="80" r="60" fill="#ffb703" opacity=".25"/><circle cx="980" cy="80" r="42" fill="#ffb703"/>
<path d="M0 220 L120 120 L190 170 L300 60 L380 140 L470 80 L560 160 L660 50 L760 150 L850 90 L960 170 L1060 70 L1200 180 V300 H0Z" fill="#6c757d" opacity=".8"/>
<path d="M300 60 L330 88 L312 84 L300 96 L288 86 L272 84Z M660 50 L692 80 L672 76 L660 88 L648 78 L630 80Z M1060 70 L1090 98 L1072 94 L1060 106 L1048 96 L1032 98Z" fill="#fff"/>
<path d="M0 240 Q150 180 300 225 T600 215 T900 220 T1200 205 V300 H0Z" fill="#95d5b2"/>
<path d="M0 265 Q200 225 420 260 T820 250 T1200 245 V300 H0Z" fill="#52b788"/>
<g fill="#2d6a4f">""" + "".join(f'<path d="M{x} {y} l-{h*.35:.0f} {h} h{h*.7:.0f}z"/><rect x="{x-3}" y="{y+h}" width="6" height="10" fill="#7f5539"/>' for x,y,h in [(60,215,50),(95,228,38),(250,225,45),(520,232,40),(560,218,55),(760,228,42),(1110,215,52),(1150,230,36)]) + """</g>
<path d="M0 285 Q300 268 600 285 T1200 280 V300 H0Z" fill="#2d6a4f"/></svg>"""
GRASS = """<svg class="grass" viewBox="0 0 1200 60" preserveAspectRatio="none" aria-hidden="true"><path fill="#283618" d="M0 60 V40 """ + " ".join(f"L{i*20+10} {8+(i*37)%22} L{i*20+20} 40" for i in range(60)) + """ V60Z"/></svg>"""
ICON_PINE = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 5 12h4l-4 6h14l-4-6h4z" fill="#2d6a4f"/><rect x="11" y="18" width="2" height="4" fill="#7f5539"/></svg>'
ICONS = {
 "boot":'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h6v9l7 3v5H4V15z" fill="#7f5539"/><rect x="4" y="18" width="15" height="2" fill="#283618"/></svg>',
 "fish":'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12c4-6 11-6 15 0-4 6-11 6-15 0zm15 0 4-4v8z" fill="#219ebc"/><circle cx="7" cy="11" r="1" fill="#fff"/></svg>',
 "leaf":'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20C4 9 11 4 20 4c0 9-5 16-16 16zm0 0 9-9" fill="#52b788" stroke="#2d6a4f" stroke-width="1.5"/></svg>',
 "sun":'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="5" fill="#ffb703"/><g stroke="#ffb703" stroke-width="2"><path d="M12 1v4M12 19v4M1 12h4M19 12h4M4 4l3 3M17 17l3 3M4 20l3-3M17 7l3-3"/></g></svg>',
 "tent":'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 21h20z" fill="#dda15e"/><path d="M12 9l-4 12h8z" fill="#7f5539"/></svg>',
}
BASE = "https://trail-quest.github.io/Foothills-kids-outdoors/"
DESC = {
 "index.html":"Explore the Alberta Foothills with kids: trails, fishing, ranch life, wildlife and winter fun from Longview to Okotoks, High River and Kananaskis.",
 "directory.html":"A sourced directory of kids' and family outdoor activities in the Alberta Foothills, from trails and fishing to ranch life, archery and winter fun.",
 "fishing.html":"Family fishing spots in the Alberta Foothills and Kananaskis with official 2026 regulations: seasons, limits, bait bans and zones, plus Highwood River rules.",
 "calendar.html":"A month-by-month calendar of real family outdoor events and seasonal dates in the Alberta Foothills, from Okotoks and High River to Kananaskis.",
 "hunt.html":"Play the Foothills nature scavenger hunt on your phone. No printer, no account, works offline.",
 "scavenger-hunt.html":"A free printable nature scavenger hunt card for kids exploring the Alberta Foothills.",
 "leaders.html":"Planning tips, printables and a safety checklist for family groups, teachers and club leaders taking kids outdoors in the Foothills.",
 "sponsors.html":"Sponsor Foothills Kids Outdoors and help local families get outside. Contact us for rates.",
 "about.html":"About Foothills Kids Outdoors, a family guide to outdoor adventures for kids in the Alberta Foothills.",
}
SIGNUP = "https://foothills-kids-outdoors-ovmgv1.subscribepage.io/"
NAV = [("index.html","Home"),("directory.html","Directory"),("fishing.html","Fishing"),("calendar.html","Calendar"),("scavenger-hunt.html","Scavenger Hunt"),("leaders.html","Groups &amp; Leaders"),("sponsors.html","Sponsors"),("about.html","About")]
import html,re
E=html.escape
def page(fn,title,body,script="",full=None):
    full=full or f"{title} | {BRAND}"; d=DESC[fn]; url=BASE+("" if fn=="index.html" else fn)
    body=re.sub(r"<h2>(.*?)</h2>",r'<h2><span class="sign">\1</span></h2>',body,flags=re.S)
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a>' for h,t in NAV)
    open(fn,"w").write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(full)}</title>
<meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{E(full)}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}images/og-cover.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Rocky Mountains above golden Foothills and a river">
<meta name="twitter:site" content="@FoothillsKidsAB"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(full)}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{BASE}images/og-cover.jpg">
<link rel="icon" type="image/png" href="favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Luckiest+Guy&amp;display=swap"><link rel="stylesheet" href="style.css?v=6"></head><body>
<header class="hero-head">{SCENE}<div class="head-inner"><a class="brand" href="index.html"><img class="logo" src="images/logo.png" alt="Foothills Kids Outdoors" width="40" height="40"> <span class="brandname">{BRAND}</span></a><nav>{nav}</nav></div></header>
<main>{body}</main>
<footer>{GRASS}<div class="foot-inner"><p><strong>{BRAND}</strong> &middot; Kids' outdoor adventures around Longview &amp; the Foothills, Alberta</p><p>Follow us on <a href="https://www.facebook.com/FoothillsKidsOutdoors" rel="noopener">Facebook</a> and <a href="https://x.com/FoothillsKidsAB" rel="noopener">X</a></p><p><a class="btn btn-small" href="{SIGNUP}">✉️ Weekly newsletter</a></p><p>Directory details come from organizers' public pages and can change. Check with the organizer and official sources before heading out.</p></div></footer>{script}</body></html>''')
import json as _j
_PH={x["photo"]:x for x in _j.load(open("foothills-activities.json")) if x.get("photo")}
def _cr(p): x=_PH[p]; return f'<a href="{x["photo_credit_url"]}" rel="noopener">{x["photo_credit"]}</a>'
HERO="images/act/peter-lougheed.jpg"
TILES=[("trails","🥾 Trails &amp; Hikes","Kid-sized trails and family walks.","images/act/kananaskis-trails.jpg"),
("fishing","🎣 Fishing","Family fishing spots and kids' events.","images/act/highwood-river.jpg"),
("horses","🐴 Horses &amp; Ranch Life","Historic ranches and western heritage.","images/act/bar-u-ranch.jpg"),
("archery","🏹 Archery","Try target archery with a local club.","images/act/foothills-archery.jpg"),
("wildlife","🦌 Wildlife &amp; Nature","Nature centres, programs and wildlife spotting.","images/act/cross-programs.jpg"),
("winter","❄️ Winter Fun","Skating, skiing, tobogganing and snow play.","images/act/west-bragg-creek.jpg")]
tiles="".join(f'<a class="card hasphoto tile" href="directory.html?cat={k}#list"><figure class="cardphoto"><img src="{p}" alt="{E(_PH[p]['photo_alt'])}" width="800" height="450" loading="lazy" decoding="async"><figcaption>{_cr(p).replace("<a ","<span data-href=").replace("</a>","</span>")}</figcaption></figure><h3>{t}</h3><p>{d}</p></a>' for k,t,d,p in TILES)
page("index.html","Home",f'''<section class="hero photohero"><img class="herobg" src="{HERO}" alt="Snowy peaks above a lake in Peter Lougheed Provincial Park, Kananaskis" width="800" height="450" fetchpriority="high" decoding="async"><div class="herotext"><h1 class="herotitle">Foothills Kids <span class="accent">Outdoors</span></h1><p class="herotag">Adventure starts in the Foothills!</p><p class="herosub">Trails, rivers, ranches and wild places for the whole family 🏔️</p>
<p>From the Highwood River to the edge of Kananaskis, through ranch country from Longview to Okotoks and High River, find family-friendly trails, fishing, horses, wildlife and winter fun for kids of all ages.</p>
<form class="search herosearch" role="search" action="directory.html" method="get"><label for="hq">🔎 What do you want to do?</label><div class="searchrow"><input type="search" id="hq" name="q" placeholder="Try skating, fishing or Okotoks." required><button type="submit" class="btn qgo">Search</button></div></form>
<a class="btn" href="directory.html">Explore the Directory</a><a class="btn" href="calendar.html">See the Calendar</a><a class="btn" href="scavenger-hunt.html">Print a Scavenger Hunt</a></div><p class="herocredit">{_cr(HERO)}</p></section>
<section class="signup"><h2 class="signup-title">🗺️ Get a new scavenger hunt every week</h2><p>Subscribers get a fresh themed Foothills hunt each week, plus weekend outdoor ideas. Only in the newsletter. One email a week, unsubscribe anytime.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>
<section><h2>{ICONS['boot']} Find an adventure</h2><div class="grid tiles">{tiles}</div><p class="tilecredits">Photos via Wikimedia Commons: '''+" &middot; ".join(f'{t.split(" ",1)[1]}: {_cr(p)}' for k,t,d,p in TILES)+f'''</p></section>
<section><h2>{ICONS['leaf']} Why the Foothills</h2><div class="grid">
<div class="card"><h3>Mountains meet prairie</h3><p>Rolling hills, big skies and mountain views make every outing feel like an adventure.</p></div>
<div class="card"><h3>Rivers and creeks</h3><p>Clear water to explore, watch and learn to fish in.</p></div>
<div class="card"><h3>Ranch country</h3><p>Open land and a western heritage that kids can see up close.</p></div>
<div class="card"><h3>All four seasons</h3><p>Hiking in summer, colours in fall, snow play in winter, wildflowers in spring.</p></div></div></section>
<div class="card safety"><h2>⚠️ Foothills Safety</h2><ul>
<li><strong>Wildlife &amp; bears:</strong> make noise, keep kids close, never approach or feed animals, and know what to do if you meet a bear.</li>
<li><strong>Changing weather:</strong> conditions can shift quickly; pack layers, water and rain gear.</li>
<li><strong>River safety:</strong> water can be cold and fast; supervise kids closely near the bank.</li>
<li><strong>Tell someone your plan:</strong> share where you are going and when you will be back.</li></ul>
<p class="note">This is general guidance only. Check official sources (such as Alberta Parks and local advisories) for current conditions, closures and safety information before you go.</p></div>''',full="Foothills Kids Outdoors: Family Adventures in Alberta's Foothills")
import json,urllib.parse
CATKEY={"Trails & Hikes":("trails","🥾"),"Fishing":("fishing","🎣"),"Horses & Ranch Life":("horses","🐴"),"Archery":("archery","🏹"),"Wildlife & Nature":("wildlife","🦌"),"Winter Fun":("winter","❄️")}
E=html.escape
def realcard(x):
    k,ic=CATKEY[x["category"]]
    meta="".join(f"<li><strong>{l}:</strong> {E(v)}</li>" for l,v in [("Where",x["location"]),("Ages",x["ages"]),("When",x["season"]),("Cost",x.get("cost",""))] if v)
    adv=f'<p class="advisory">⚠️ {E(x["advisory"])} <a href="{E(x["advisory_source"])}" rel="noopener">Official advisory</a></p>' if x.get("advisory") else ""
    maplink=f'<a class="mapbtn" href="https://www.google.com/maps/search/?api=1&amp;query={urllib.parse.quote_plus(x["map"])}" target="_blank" rel="noopener">📍 Open in Maps</a>' if x.get("map") else ""
    img=f'<figure class="cardphoto"><img src="{E(x["photo"])}" alt="{E(x["photo_alt"])}" width="800" height="450" loading="lazy" decoding="async"><figcaption><a href="{E(x["photo_credit_url"])}" rel="noopener">{E(x["photo_credit"])}</a></figcaption>{"" if x.get("photo_place_specific",True) else '<span class="repphoto">Representative photo</span>'}</figure>' if x.get("photo") else ""
    slug=x["photo"].rsplit("/",1)[-1].rsplit(".",1)[0] if x.get("photo") else re.sub(r"[^a-z0-9]+","-",x["name"].lower()).strip("-")
    sea=f'<p class="seasonal">⚠️ {E(x["seasonal"])} <a href="{E(x["seasonal_source"])}" rel="noopener">{E(x.get("seasonal_label","Alberta Parks"))}</a></p>' if x.get("seasonal") else ""
    return f'<div class="card{" hasphoto" if img else ""}" id="{slug}" data-cat="{k}">{img}<span class="badge">{E(x["category"])}</span><h3>{ic} {E(x["name"])}</h3><p>{E(x["description"])}</p><ul class="meta">{meta}</ul>{sea}{adv}{maplink}<p class="org">By {E(x["organizer"])} &middot; <a href="{E(x["source"])}" rel="noopener">Source</a></p></div>'
REAL=json.load(open("foothills-activities.json"))
_c=[realcard(x) for x in REAL]
NEWS=f'<section class="signup gridsignup"><h2 class="signup-title">🗺️ Get a new scavenger hunt every week</h2><p>A fresh themed hunt each week, only in the newsletter.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>'
WSAFE='<div class="card winter-safety" id="winter-safety" data-cat="winter"><span class="badge">Winter Fun</span><h3>❄️ Winter safety</h3><ul><li><strong>Ice:</strong> at least 15 cm for one person and 20 cm for a group. Never go on storm ponds or moving water.</li><li><strong>Dress in layers</strong> and pack extra mitts and socks.</li><li><strong>Micro-spikes</strong> or ice cleats for icy trails.</li><li><strong>Check before you go:</strong> <a href="https://avalanche.ca/" rel="noopener">avalanche ratings</a> and road conditions on <a href="https://511.alberta.ca/" rel="noopener">511 Alberta</a>.</li><li><strong>Wildlife:</strong> stay well back and never feed animals.</li></ul><p class="org"><a href="https://parks.canada.ca/pn-np/ab/banff/activ/patinage-skating" rel="noopener">Parks Canada ice guidance</a></p></div>'
_wi=next(i for i,x in enumerate(REAL) if x["category"]=="Winter Fun")
AP="https://www.albertaparks.ca/parks/kananaskis/kananaskis-country/advisories-public-safety/trail-reports/"
def _ss(n,dist,note,src,q): return f'<li><strong>{n}</strong> ({dist}). {note} <span class="sslinks"><a href="{src}" rel="noopener">Trail report</a> <a class="mapbtn" href="https://www.google.com/maps/search/?api=1&amp;query={urllib.parse.quote_plus(q)}" target="_blank" rel="noopener">📍 Open in Maps</a></span></li>'
SNOW=('<div class="card snowshoe" id="snowshoeing" data-cat="winter"><span class="badge">Winter Fun</span><h3>❄️ Snowshoeing: easy family trails</h3>'
 '<h4>Rated Simple (Class 1) avalanche terrain</h4><p class="ssnote">Rated Simple (Class 1) in Alberta Parks\' <a href="https://www.albertaparks.ca/media/861187/2016_snowshoeing_brochure.pdf" rel="noopener">snowshoe brochure</a> (2016). Check current trail conditions and avalanche info before you go. All four need a Kananaskis Conservation Pass to park.</p><ul class="sslist">'
 +_ss("Troll Falls","about 1.4 to 1.7 km","Often packed and icy, so grippers may work better than snowshoes. See the <a href=\"#winter-troll-falls\">Troll Falls card</a>.",AP+"kananaskis-valley/troll-falls/","Troll Falls Trailhead, Kananaskis, AB")
 +_ss("Marsh Loop, Peter Lougheed","1.3 to 1.8 km loop","Best for the littlest kids.",AP+"peter-lougheed/marsh-loop-snowshoe/","Marsh Loop, Peter Lougheed Provincial Park, AB")
 +_ss("Hogarth Lakes Loop","3.9 km loop","Flat forest trail with lake views, off the Smith-Dorrien road (Hwy 742).",AP+"peter-lougheed/hogarth-lakes-loop-snowshoe/","Burstall Pass Day Use Area, Kananaskis, AB")
 +_ss("Elkwood Loop","3.4 km loop","Longer but flat, from the Elkwood Amphitheatre.",AP+"peter-lougheed/elkwood-loop-snowshoe/","Elkwood Amphitheatre, Peter Lougheed Provincial Park, AB")
 +'</ul><h4>Closer easy official snowshoe trails</h4><p class="ssnote">Official snowshoe trails with no published avalanche rating. Check trail reports and use your judgement.</p><ul class="sslist">'
 +_ss("Sandy McNabb Interpretive","1.7 km","Near Turner Valley, in the Sheep River area. Kananaskis Conservation Pass needed.",AP+"sheep-and-highwood/sandy-mcnabb-interpretive/","Sandy McNabb Day Use Area, Turner Valley, AB")
 +_ss("Snowshoe Hare East","winter-only trail","At West Bragg Creek. Kananaskis Conservation Pass needed.",AP+"west-bragg-creek/snowshoe-hare-east-winter/","West Bragg Creek Day Use Area, Bragg Creek, AB")
 +_ss("Canmore Nordic Centre snowshoe loop","about 2.5 to 3 km","Follow the orange signs, and stay off the groomed ski trails. Kananaskis Conservation Pass needed.","https://albertaparks.ca/parks/kananaskis/canmore-nordic-centre-pp/activities/other-winter-activities/","Canmore Nordic Centre, Canmore, AB")
 +'</ul><p class="ssrent"><strong>Rent kid snowshoes</strong> (prices as of Oct 2026): <a href="https://kananaskisoutfitters.com/rentals/winter-rentals/" rel="noopener">Kananaskis Outfitters</a> $10 for 2 hours or $16 a day (Kananaskis Village); <a href="https://sportsrent.ca/snowshoe-rentals-calgary/" rel="noopener">Sports Rent Calgary</a> $17 a day.</p></div>')
_c.insert(_wi,SNOW+WSAFE)
cards="".join(_c[:9])+NEWS+"".join(_c[9:])
btns="".join(f'<button data-f="{k}"{" class=on" if k=="all" else ""}>{v}</button>' for k,v in [("all","All"),("trails","Trails &amp; Hikes"),("fishing","Fishing"),("horses","Horses &amp; Ranch Life"),("archery","Archery"),("wildlife","Wildlife &amp; Nature"),("winter","Winter Fun")])
page("directory.html","Directory",f'''<h1>{ICONS['leaf']} Adventure Directory</h1><p>Real places and programs around the Foothills, from public pages by the organizers named on each card.</p><p class="note"><strong>Details change, check with the organizer</strong> (dates, hours, fees and closures) before you go.</p>
<form class="search" role="search" onsubmit="return false"><label for="q">🔎 What do you want to do?</label><div class="searchrow"><input type="search" id="q" name="q" placeholder="Try skating, fishing or Okotoks." autocomplete="off" aria-describedby="qcount"><button type="button" id="qclear" class="qclear" aria-label="Clear search" hidden>&times;</button></div><p id="qcount" class="qcount" aria-live="polite"></p></form>
<div class="filters" role="group" aria-label="Filter listings">{btns}</div><p id="hwban" class="hwban" hidden>🎃 Looking for Halloween events? <a href="calendar.html#halloween">See the October calendar</a></p><p id="nomatch" class="nomatch" hidden>No matches yet. Try &#39;winter&#39; or <button type="button" id="qreset" class="linkbtn">browse all</button>.</p><div class="grid" id="list">{cards}</div>''',
'''<script>(()=>{const qi=document.getElementById('q'),qc=document.getElementById('qclear'),nm=document.getElementById('nomatch'),cnt=document.getElementById('qcount'),cards=[...document.querySelectorAll('#list .card')],gs=document.querySelector('#list .gridsignup');let f='all';const norm=t=>t.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');cards.forEach(c=>c.dataset.txt=norm(c.textContent.replace(/\\s+/g,' ')));
const SYN={sled:['toboggan','sled'],sledding:['toboggan','sled'],tobogganing:['toboggan'],skate:['skat'],skates:['skat'],horse:['horse','ranch','rodeo'],horses:['horse','ranch','rodeo'],fish:['fish'],toddler:['toddler','stroller','easy'],toddlers:['toddler','stroller','easy'],stroller:['toddler','stroller','easy'],strollers:['toddler','stroller','easy']},HW=/hallowe+n|pumpkin|trick.?or.?treat|costume|spooky/,hb=document.getElementById('hwban');
function apply(){const raw=norm(qi.value.trim()),w=raw.split(/\\s+/).filter(Boolean);hb.hidden=!HW.test(raw);let n=0;cards.forEach(c=>{const ok=(f==='all'||c.dataset.cat===f)&&w.every(x=>(SYN[x]||[x]).some(y=>c.dataset.txt.includes(y)));c.hidden=!ok;if(ok)n++});qc.hidden=!qi.value;nm.hidden=n>0;if(gs)gs.hidden=w.length>0;cnt.textContent=w.length?(n?n+(n===1?' match':' matches'):'No matches'):'';const u=new URL(location);if(w.length)u.searchParams.set('q',qi.value.trim());else u.searchParams.delete('q');history.replaceState(null,'',u)}
window._fkoApply=apply;qi.addEventListener('input',apply);qc.onclick=()=>{qi.value='';apply();qi.focus()};document.getElementById('qreset').onclick=()=>{qi.value='';apply();qi.focus()};
document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filters button').forEach(x=>x.classList.toggle('on',x===b));f=b.dataset.f;apply()});const iq=new URLSearchParams(location.search).get('q');if(iq){qi.value=iq;apply()}})();(()=>{const q=new URLSearchParams(location.search).get('cat');const qb=q&&document.querySelector('.filters button[data-f="'+q+'"]');if(qb)qb.click()})();(()=>{const h=decodeURIComponent(location.hash.slice(1));const c=h&&document.getElementById(h);if(c&&c.classList.contains('card')){c.classList.add('flash');setTimeout(()=>c.classList.remove('flash'),2600)}})()</script>''')
from fishspots import SPOTS
def _spot(x):
    q=urllib.parse.quote_plus(x["map"])
    rows="".join(f"<dt>{k}</dt><dd>{v}</dd>" for k,v in [("Season",x["season"]),("Limits",x["limits"]),("Bait",x["bait"]),("Closures",x["closures"]),("Zone","ES1 (Eastern Slopes)")])
    img=f'<figure class="cardphoto"><img src="{E(x["photo"])}" alt="{E(x["photo_alt"])}" width="800" height="450" loading="lazy" decoding="async"><figcaption><a href="{E(x["photo_credit_url"])}" rel="noopener">{E(x["photo_credit"])}</a></figcaption>{"" if x.get("photo_place_specific",True) else '<span class="repphoto">Representative photo</span>'}</figure>' if x.get("photo") else ""
    return f'<div class="card spot{" hasphoto" if img else ""}" id="{x["id"]}">{img}<h3>🎣 {x["name"]}</h3><p class="area">📍 {x["area"]}</p><p>{x["why"]}</p><dl class="regbox">{rows}</dl><p class="spotlinks"><a class="regbtn" href="{x["src"]}" rel="noopener">📘 Official regulations</a> <small>({x["srcname"]})</small></p><a class="mapbtn" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">📍 Open in Maps</a></div>'
FISHSEC='<section id="family-fishing-spots"><h2>🗺️ Family fishing spots</h2><p class="note"><strong>Regulations change, so always check the official regs before you go.</strong> Last checked against the 2026 Alberta Guide to Sport Fishing Regulations on <strong>October 14, 2026</strong>. Licence: anglers 16 to 64 need one; kids under 16 don\'t (<a href="https://www.albertaregulations.ca/fishingregs/licensing.html" rel="noopener">licensing</a>). No barbless-hook rule is listed for these waters. Ice fishing is not allowed on flowing water in ES zones; see <a href="https://www.albertaregulations.ca/fishingregs/general-regs.html" rel="noopener">general regulations</a>. All spots are in watershed unit <a href="https://www.albertaregulations.ca/fishingregs/es1.html" rel="noopener">ES1</a>.</p><div class="grid spots">'+"".join(_spot(x) for x in SPOTS)+'</div></section>'
page("fishing.html","Fishing",'''<div class="water"><svg class="bobber" viewBox="0 0 40 60" aria-hidden="true"><line x1="20" y1="0" x2="20" y2="14" stroke="#16405e" stroke-width="2"/><circle cx="20" cy="30" r="14" fill="#fff8e7" stroke="#16405e" stroke-width="2"/><path d="M6 30a14 14 0 0 0 28 0z" fill="#e63946"/></svg><h1>🎣 Highwood River: Kids' Fishing Summary</h1><p>Cast your line, wait for the bite, and let most trout swim free!</p></div><div class="grid fish-grid">
<div class="card"><h2>📅 Season</h2><p>Most of the Highwood is open <strong>June 16 to October 31</strong>. Seasons differ by stretch: the last 500 m before the Bow River is open all year, and Storm Creek is closed all year.</p></div>
<div class="card"><h2>🚫 Bait Ban</h2><p>No bait on any part of the Highwood. Use <strong>unscented</strong> lures or flies only (no scented lures or PowerBait).</p></div>
<div class="card"><h2>🐟 Trout</h2><p><strong>Most trout must be released.</strong> In the upper headwaters you may keep up to 2 brook trout. Mountain whitefish can be kept on some stretches at some times, so check the limits.</p></div>
<div class="card"><h2>🧒 Licence</h2><p>Kids <strong>under 16</strong> do not need a fishing licence, but they still follow the rules. Anglers 16 to 64 need a sportfishing licence. Alberta residents 65 and over don't (<a href="https://www.albertaregulations.ca/fishingregs/licensing.html" rel="noopener">official licensing page</a>).</p></div></div>
<p class="note"><strong>Check before you go:</strong> Always check the official 2026 Alberta Guide to Sport Fishing Regulations before fishing. The Highwood River rules are in the <a href="https://www.albertaregulations.ca/fishingregs/ES1-Rivers.pdf" rel="noopener">official Eastern Slopes (ES1) rivers table</a>. This page is a kid-friendly summary, not legal advice.</p>'''+FISHSEC)
import datetime as _dt
EV=sorted(json.load(open("events.json")),key=lambda e:(e["start"],e["title"]))
_D=lambda d:_dt.date.fromisoformat(d)
def _fmt(e):
    a=_D(e["start"]); f=lambda d:d.strftime("%a, %b ")+str(d.day)+d.strftime(", %Y")
    if not e.get("end"): return f(a)
    b=_D(e["end"]); return f(a)+" &ndash; "+f(b)
def _ev(e):
    dl=f' &middot; <a href="directory.html#{e["slug"]}">See in directory</a>' if e.get("slug") else ""
    rec=f'<p class="ev-rec">🔁 {E(e["recurring"])}</p>' if e.get("recurring") else ""
    last=e.get("end") or ("9999-12-31" if e.get("recurring") else e["start"])
    return f'<li class="ev" data-last="{last}"><p class="ev-date">{_fmt(e)}</p><h3>{E(e["title"])}</h3><p class="ev-town">📍 {E(e["town"])}</p>{rec}<p>{E(e["description"])}</p><p class="ev-links"><a href="{E(e["source"])}" rel="noopener">Details</a>{dl}</p></li>'
_months={}
for e in EV: _months.setdefault(e["start"][:7],[]).append(e)
def _mblock(m,evs):
    t=_dt.date.fromisoformat(m+"-01").strftime("%B %Y")
    return f'<section class="month" data-month="{m}" id="{"halloween" if m.endswith("-10") else "m-"+m}"><h2>🗓️ {t}</h2><ul class="evlist">{"".join(_ev(e) for e in evs)}</ul></section>'
TODAY=_dt.date(2026,10,13); _soon=[f"{(TODAY.year*12+TODAY.month-1+i)//12}-{(TODAY.month-1+i)%12+1:02d}" for i in range(3)]
soon="".join(_mblock(m,v) for m,v in _months.items() if m in _soon)
later="".join(_mblock(m,v) for m,v in _months.items() if m>_soon[-1])
page("calendar.html","Calendar",f'''<h1>🗓️ Foothills Family Events Calendar</h1>
<p>Real dated events and seasonal dates for families around Okotoks, High River, Turner Valley, Black Diamond, Longview and Kananaskis, from organizers\' own pages.</p>
<p class="note"><strong>Dates change.</strong> Events can be cancelled or moved for weather and other reasons, so check with the organizer (use each <em>Details</em> link) before you go.</p>
<div class="cal"><p class="cal-group" role="heading" aria-level="2">Coming up: next 3 months</p>{soon}<p class="cal-group" role="heading" aria-level="2">Later this season</p>{later}<p id="noev" hidden>No upcoming events listed right now. Check back soon!</p></div>
<section class="signup"><h2 class="signup-title">✉️ Get the weekly newsletter</h2><p>Get a new Foothills scavenger hunt every week, plus outdoor ideas for families. One email a week, unsubscribe anytime.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>''',
'''<script>(()=>{const d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');document.querySelectorAll('.ev').forEach(li=>{if(li.dataset.last<t)li.hidden=true});document.querySelectorAll('.month').forEach(m=>{if(!m.querySelector('.ev:not([hidden])'))m.hidden=true});const all=document.querySelectorAll('.ev'),hid=document.querySelectorAll('.ev[hidden]');document.getElementById('noev').hidden=!(all.length&&all.length===hid.length)})()</script>''')
finds=["A pine cone","Animal tracks","A feather","Three different kinds of leaves","Something red","Animal sign (scat, chewed stick, nest)","A smooth, round rock","Moss or lichen","A spider web","A bird (see or hear it)","Something that smells good","A fish in the water","Litter that doesn't belong (pack it out!)","The tallest tree you can see","A trail made by an animal"]
li="".join(f"<li>{f}</li>" for f in finds)
page("scavenger-hunt.html","Scavenger Hunt",f'''<p class="note noprint newsletter-line">✉️ This is our starter hunt. Want a new themed hunt every week? <a href="{SIGNUP}">Get the weekly newsletter</a></p>
<div class="noprint hunt-choose"><a class="btn btn-play" href="hunt.html">📱 Play on your phone, no printer needed</a> <button class="btn" onclick="print()">🖨️ Print this card</button></div>
<div class="hunt"><h1>🏅 {BRAND} Scavenger Quest</h1><p>Explorer or team names: ______________________ Date: __________</p><p>When you spot something, check the box. Work together and keep your eyes open!</p><ul>{li}</ul>
<p><strong>Find 10 to earn your Trail Explorer badge!</strong></p><p>Leave No Trace: look, don't take. Leave nature the way you found it.</p><p>Bonus: how many sounds can you hear in 60 silent seconds? _____</p></div>''')
ICONS=["🌲","🐾","🪶","🍂","🍎","🪺","🪨","🌿","🕸️","🐦","🌸","🐟","🗑️","🌳","🦌"]
cards="".join(f'<li><button type="button" class="hcard" aria-pressed="false" data-i="{i}"><span class="hi" aria-hidden="true">{ICONS[i]}</span><span class="ht">{f}</span><span class="hc" aria-hidden="true">✓</span></button></li>' for i,f in enumerate(finds))
HJS=r"""<script>(()=>{const K='fko-hunt-quest-v1',b=[...document.querySelectorAll('.hcard')],n=b.length;let s;try{s=JSON.parse(localStorage.getItem(K))||[]}catch(e){s=[]}
const bar=document.getElementById('hbar'),txt=document.getElementById('htxt'),done=document.getElementById('hdone');
let T;function toast(m){let t=document.querySelector('.htoast');if(!t){t=document.createElement('div');t.className='htoast';t.setAttribute('role','status');document.body.appendChild(t)}t.textContent=m;t.classList.add('show');clearTimeout(T);T=setTimeout(()=>t.classList.remove('show'),1400)}
function save(){try{localStorage.setItem(K,JSON.stringify(s))}catch(e){}}
function draw(cel){b.forEach(x=>x.setAttribute('aria-pressed',s.includes(+x.dataset.i)));const c=s.length;bar.style.width=(100*c/n)+'%';bar.parentNode.setAttribute('aria-valuenow',c);txt.textContent=c+' of '+n+' found';done.hidden=c<n;if(c===n&&cel)confetti()}
function confetti(){const box=document.getElementById('confetti');box.innerHTML='';const cols=['#e63946','#f4a261','#2a9d8f','#264653','#ffb703','#8338ec'];for(let i=0;i<80;i++){const p=document.createElement('i');p.style.left=Math.random()*100+'%';p.style.background=cols[i%6];p.style.animationDelay=Math.random()*.8+'s';p.style.animationDuration=2+Math.random()*2+'s';box.appendChild(p)}setTimeout(()=>box.innerHTML='',5000);done.focus()}
b.forEach(x=>x.addEventListener('click',()=>{const i=+x.dataset.i;s=s.includes(i)?s.filter(v=>v!==i):[...s,i];save();x.classList.remove('pop');void x.offsetWidth;if(s.includes(i)){x.classList.add('pop');toast('✅ Found: '+x.querySelector('.ht').textContent)}else toast('Unchecked');if(navigator.vibrate)navigator.vibrate(40);draw(true)}));
document.getElementById('hreset').addEventListener('click',()=>{if(confirm('Start over? This clears every item you found.')){s=[];save();draw()}});draw()})()</script>"""
page("hunt.html","Phone Scavenger Hunt",f'''<div class="phunt"><h1>📱 Scavenger Quest</h1><p class="newsletter-line">✉️ This is our free starter hunt. Want a new hunt every week? <a href="{SIGNUP}">Get the weekly newsletter.</a></p><p>Tap an item when you spot it. Your progress saves on this phone only. Nothing is uploaded, no account needed.</p>
<div class="hprog"><div class="hbarwrap" role="progressbar" aria-label="Items found" aria-valuemin="0" aria-valuemax="{len(finds)}" aria-valuenow="0"><div id="hbar" class="hbar"></div></div><p id="htxt" class="htxt" aria-live="polite">0 of {len(finds)} found</p></div>
<ul class="hlist">{cards}</ul>
<div id="hdone" class="hdone" tabindex="-1" hidden><h2>🎉 You did it!</h2><p>Every item found. Want a new hunt every week? <a href="{SIGNUP}">Get the weekly newsletter.</a></p></div>
<p class="hfoot">Leave No Trace: look, don't take.</p>
<p><button type="button" id="hreset" class="btn">↺ Start over</button> <a href="scavenger-hunt.html">🖨️ Prefer paper? Print the card</a></p></div><div id="confetti" aria-hidden="true"></div>''',HJS)
page("leaders.html","Leaders",'''<h1>🧭 Groups &amp; Leaders</h1><p>For anyone leading kids outdoors: family groups, school classes, and club or youth leaders.</p><div class="grid">
<div class="card"><h2>Plan an outing</h2><p>Use the <a href="directory.html">directory</a> and <a href="calendar.html">calendar</a> to pick an age-appropriate activity.</p></div>
<div class="card"><h2>Printables</h2><p>Grab the <a href="scavenger-hunt.html">scavenger hunt card</a> for your group.</p></div>
<div class="card"><h2>Safety checklist</h2><ul><li>Adult-to-kid ratios</li><li>Permission forms</li><li>First-aid kit</li><li>Weather &amp; wildlife check</li></ul></div>
<div class="card"><h2>Share your group</h2><p>Know a great kids\' outdoor spot or program? Tell us on <a href="https://www.facebook.com/FoothillsKidsOutdoors" rel="noopener">Facebook</a>. Always check details with the organizer before an outing.</p></div></div>''')
page("sponsors.html","Sponsors",'''<h1>🤝 Sponsor the Adventure</h1><p>Help local kids get outside by supporting a free Foothills outdoor guide for families.</p><div class="grid">
<div class="card"><span class="badge">Tier</span><h2>🌱 Trail Buddy</h2><p>Name on sponsors page.</p></div>
<div class="card"><span class="badge">Tier</span><h2>🌲 Trail Guide</h2><p>Logo on sponsors page and a printable.</p></div>
<div class="card"><span class="badge">Tier</span><h2>⛰️ Summit Partner</h2><p>Featured placement on the home page.</p></div></div>
<p class="note"><strong>Contact us for rates.</strong> Message us on <a href="https://www.facebook.com/FoothillsKidsOutdoors" rel="noopener">Facebook</a> to talk about sponsoring.</p>''')
page("about.html","About",f'''<h1>About {BRAND}</h1><p>{BRAND} is a family-friendly directory of outdoor activities for kids of all ages, from toddlers to teens, around Longview and the Foothills, Alberta, made for parents, grandparents and group leaders.</p>
<p>Our goal is simple: help families get outside together and make every outing feel like an adventure, whether that's a new trail, a first fish or a scavenger hunt.</p>
<p class="note">Directory listings link to each organizer\'s public page. Details change, so check with the organizer and official sources for rules, closures and conditions before you go.</p>''')
