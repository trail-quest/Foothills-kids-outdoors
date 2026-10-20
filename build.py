import html,re
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
 "directory.html":"Kids' and family outdoor activities in Okotoks, High River, Turner Valley, Bragg Creek and Kananaskis: trails, fishing, ranch life, archery and winter fun.",
 "fishing.html":"Family fishing spots in the Alberta Foothills and Kananaskis with official 2026 regulations: seasons, limits, bait bans and zones, plus Highwood River rules.",
 "calendar.html":"A month-by-month calendar of real family outdoor events and seasonal dates in the Alberta Foothills, from Okotoks and High River to Kananaskis.",
 "hunt.html":"A free nature scavenger hunt kids can play on a phone on trails around Okotoks, High River, Bragg Creek and Kananaskis. No printer or account needed.",
 "scavenger-hunt.html":"A free printable nature scavenger hunt card for kids of all ages exploring the Foothills and Kananaskis, from Calgary-area towns to Longview.",
 "leaders.html":"Planning tips, printables and a safety checklist for family groups, teachers and club leaders taking kids outdoors around Okotoks, High River and Kananaskis.",
 "sponsors.html":"Sponsor Foothills Kids Outdoors, a free outdoor guide for families in Longview, Turner Valley, Black Diamond, High River and Okotoks. Contact us for rates.",
 "hunt-01-fall-colours.html":"Fall Colours Quest: a printable fall nature scavenger hunt for kids in the Alberta Foothills, from Foothills Kids Outdoors.",
 "hunt-02-first-snow.html":"First Snow Quest: a printable early-winter nature scavenger hunt for kids in the Alberta foothills, from Foothills Kids Outdoors.",
 "volunteer.html":"Family volunteering in the Alberta Foothills: kid-friendly cleanups, tree planting, bird counts and trail care around Okotoks, High River and Kananaskis.",
 "about.html":"About Foothills Kids Outdoors, a family guide to outdoor adventures for kids of all ages around Longview and the Foothills, south of Calgary.",
}
SIGNUP = "https://foothills-kids-outdoors-ovmgv1.subscribepage.io/"
OGIMG = BASE+"images/act/peter-lougheed.jpg"; OGALT = "Snowy peaks above a lake in Peter Lougheed Provincial Park, Kananaskis"
COMPACT = f'<section class="signup compact"><h2 class="signup-title">🗺️ Get a new scavenger hunt every week</h2><p>One email a week, unsubscribe anytime.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>'
DONEBOX = f'<section class="signup compact donehunt"><h2 class="signup-title">Done the hunt? Want a new one next week?</h2><p>We send a fresh themed scavenger hunt every week. One email a week, unsubscribe anytime.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>'
import urllib.parse as _u
def share(url,title):
    q=_u.quote(url,safe=""); t=_u.quote(title,safe="")
    return (f'<p class="share"><span class="sharelbl">Share:</span> <a href="https://www.facebook.com/sharer/sharer.php?u={q}" target="_blank" rel="noopener">Facebook</a> '
            f'<a href="mailto:?subject={t}&amp;body={q}">Email</a> <button type="button" class="sharecopy" data-url="{url}" data-title="{html.escape(title)}">Copy link</button></p>')
SHJS = """<script>document.addEventListener('click',async e=>{const b=e.target.closest('.sharecopy');if(!b)return;const url=b.dataset.url,title=b.dataset.title;if(navigator.share){try{await navigator.share({title,url})}catch(err){}return}try{await navigator.clipboard.writeText(url);b.textContent='Copied!'}catch(err){prompt('Copy this link:',url);return}setTimeout(()=>b.textContent='Copy link',1800)})</script>"""
NAV = [("index.html","Home"),("directory.html","Directory"),("fishing.html","Fishing"),("camping-foothills.html","Camping"),("gardening.html","Gardening"),("calendar.html","Calendar"),("scavenger-hunt.html","Scavenger Hunt"),("volunteer.html","Volunteer"),("leaders.html","Groups &amp; Leaders")]
E=html.escape
PAGES=[]
def page(fn,title,body,script="",full=None,ogimg=None,ogalt=None,ogw=None,ogh=None,navcur=None):
    OGIMG=ogimg or globals()["OGIMG"]; OGALT=ogalt or globals()["OGALT"]
    full=full or f"{title} | {BRAND}"; PAGES.append(fn); d=DESC[fn]; url=BASE+("" if fn=="index.html" else fn)
    body=re.sub(r"<h2>(.*?)</h2>",r'<h2><span class="sign">\1</span></h2>',body,flags=re.S)
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==(navcur or fn) else ""}>{t}</a>' for h,t in NAV)
    open(fn,"w").write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(full)}</title>
<meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{E(full)}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{OGIMG}"><meta property="og:image:width" content="{ogw or (1200 if ogimg else 800)}"><meta property="og:image:height" content="{ogh or (630 if ogimg else 450)}"><meta property="og:image:alt" content="{OGALT}">
<meta name="twitter:site" content="@FoothillsKidsAB"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(full)}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{OGIMG}"><meta name="twitter:image:alt" content="{OGALT}">
<link rel="icon" type="image/png" href="favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Luckiest+Guy&amp;display=swap"><link rel="stylesheet" href="style.css?v=11"></head><body>
<header class="hero-head">{SCENE}<div class="head-inner"><a class="brand" href="index.html"><img class="logo" src="images/logo.png" alt="Foothills Kids Outdoors" width="40" height="40"> <span class="brandname">{BRAND}</span></a><div class="navwrap" id="navwrap"><button type="button" class="menubtn" aria-expanded="false" aria-controls="mainnav"><span aria-hidden="true">☰</span> Menu</button><nav id="mainnav" class="mainnav" aria-label="Main">{nav}</nav><a class="newsbtn" href="https://foothills-kids-outdoors-ovmgv1.subscribepage.io/" data-goatcounter-click="menu-newsletter-signup">✉️ Free newsletter</a></div><script>(function(){{var w=document.getElementById('navwrap'),b=w.querySelector('.menubtn');w.classList.add('js');b.addEventListener('click',function(){{var o=w.classList.toggle('open');b.setAttribute('aria-expanded',o)}})}})()</script></div></header>
<main>{body}</main>
<footer>{GRASS}<div class="foot-inner"><p class="footlinks"><a href="about.html">About</a> &middot; <a href="sponsors.html">Sponsors</a></p><p class="social"><a href="https://www.facebook.com/FoothillsKidsOutdoors" target="_blank" rel="noopener" aria-label="Foothills Kids Outdoors on Facebook"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path fill="currentColor" d="M13.5 22v-8.2h2.8l.4-3.2h-3.2V8.5c0-.9.3-1.6 1.6-1.6h1.7V4.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.2h2.8V22h3.4z"/></svg></a><a href="https://x.com/FoothillsKidsAB" target="_blank" rel="noopener" aria-label="Foothills Kids Outdoors on X"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M17.8 3h3.1l-6.8 7.8 8 10.6h-6.3l-4.9-6.4L5.3 21.4H2.2l7.3-8.3L1.8 3h6.4l4.4 5.9L17.8 3zm-1.1 16.5h1.7L7.4 4.8H5.5l11.2 14.7z"/></svg></a></p><p><strong>{BRAND}</strong> &middot; Kids' outdoor adventures in the foothills, Alberta</p><p>Follow us on <a href="https://www.facebook.com/FoothillsKidsOutdoors/" rel="noopener">Facebook</a> and <a href="https://x.com/FoothillsKidsAB" rel="noopener">X</a></p><p><a class="btn btn-small" href="{SIGNUP}">✉️ Weekly newsletter</a></p><p>Directory details come from organizers' public pages and can change. Check with the organizer and official sources before heading out.</p></div></footer>{script}{SHJS if "sharecopy" in body else ""}<script data-goatcounter="https://foothillskids.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script></body></html>''')
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
<div class="herosignup"><h2 class="signup-title">🗺️ Get a new scavenger hunt every week</h2><p>A fresh themed Foothills hunt for kids of all ages, plus weekend outdoor ideas. One email a week, unsubscribe anytime.</p><a class="btn btn-sun" href="{SIGNUP}">Sign me up, it's free</a></div>
<a class="btn" href="directory.html">Explore the Directory</a><a class="btn" href="calendar.html">See the Calendar</a><a class="btn" href="scavenger-hunt.html">Print a Scavenger Hunt</a><a class="btn" href="camping-foothills.html">Family Camping</a><a class="btn" href="camping-crown-land.html">Crown Land Camping Guide</a></div><p class="herocredit">{_cr(HERO)}</p></section>
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
<p class="note">This is general guidance only. Check official sources (such as Alberta Parks and local advisories) for current conditions, closures and safety information before you go.</p></div>''',full="Kids' Outdoor Adventures near Okotoks, High River & Longview | Foothills Kids Outdoors")
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
    return f'<div class="card{" hasphoto" if img else ""}" id="{slug}" data-cat="{k}">{img}<span class="badge">{E(x["category"])}</span><h3>{ic} {E(x["name"])}</h3><p>{E(x["description"])}</p><ul class="meta">{meta}</ul>{sea}{adv}{maplink}<p class="org">By {E(x["organizer"])} &middot; <a href="{E(x["source"])}" rel="noopener">Source</a></p>{share(BASE+"directory.html#"+slug,x["name"]+" | "+BRAND)}</div>'
REAL=json.load(open("foothills-activities.json"))
_c=[realcard(x) for x in REAL]
NEWS=f'<section class="signup gridsignup"><h2 class="signup-title">🗺️ Get a new scavenger hunt every week</h2><p>A fresh themed hunt each week, only in the newsletter.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>'
WSAFE='<div class="card winter-safety" id="winter-safety" data-cat="winter"><span class="badge">Winter Fun</span><h3>❄️ Winter safety</h3><ul><li><strong>Ice:</strong> at least 15 cm for one person and 20 cm for a group. Never go on storm ponds or moving water.</li><li><strong>Dress in layers</strong> and pack extra mitts and socks.</li><li><strong>Micro-spikes</strong> or ice cleats for icy trails.</li><li><strong>Check before you go:</strong> <a href="https://avalanche.ca/" rel="noopener">avalanche ratings</a> and road conditions on <a href="https://511.alberta.ca/" rel="noopener">511 Alberta</a>.</li><li><strong>Wildlife:</strong> stay well back and never feed animals.</li></ul><p class="org"><a href="https://parks.canada.ca/pn-np/ab/banff/activ/patinage-skating" rel="noopener">Parks Canada ice guidance</a></p></div>'
BRING='<aside class="card bring" id="what-to-bring"><h2>🎒 What to bring</h2><ul class="bringlist"><li>🧥 <strong>Layers:</strong> foothills weather flips fast, so pack a warm layer and a rain shell.</li><li>💧 <strong>Water</strong> for everyone, plus 🍎 <strong>snacks</strong> to keep little legs going.</li><li>☀️ <strong>Sun or snow gear by season:</strong> sunscreen, hats and bug spray in summer; a toque, mitts and spare socks in winter.</li><li>🩹 <strong>A small first-aid kit</strong> and any meds your kids need.</li><li>🐻 <strong>Bear spray</strong> on Kananaskis and backcountry trails (and know how to use it).</li><li>🗑️ <strong>A bag to pack out garbage</strong>, and a charged phone.</li></ul></aside>'
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
_sh=lambda h,i,t:h[:h.rfind("</div>")]+share(BASE+"directory.html#"+i,t+" | "+BRAND)+"</div>"
_c.insert(_wi,_sh(SNOW,"snowshoeing","Easy family snowshoe trails")+_sh(WSAFE,"winter-safety","Winter safety for families"))
cards="".join(_c[:9])+NEWS+"".join(_c[9:])
btns="".join(f'<button data-f="{k}"{" class=on" if k=="all" else ""}>{v}</button>' for k,v in [("all","All"),("trails","Trails &amp; Hikes"),("fishing","Fishing"),("horses","Horses &amp; Ranch Life"),("archery","Archery"),("wildlife","Wildlife &amp; Nature"),("winter","Winter Fun")])
page("directory.html","Directory",full="Kids' Outdoor Activities in Okotoks, High River, Bragg Creek & Kananaskis | Foothills Kids Outdoors",body=f'''<h1>{ICONS['leaf']} Adventure Directory</h1><p>Real places and programs around the Foothills, from public pages by the organizers named on each card.</p><p class="note"><strong>Details change, check with the organizer</strong> (dates, hours, fees and closures) before you go.</p>
<form class="search" role="search" onsubmit="return false"><label for="q">🔎 What do you want to do?</label><div class="searchrow"><input type="search" id="q" name="q" placeholder="Try skating, fishing or Okotoks." autocomplete="off" aria-describedby="qcount"><button type="button" id="qclear" class="qclear" aria-label="Clear search" hidden>&times;</button></div><p id="qcount" class="qcount" aria-live="polite"></p></form>
<div class="filters" role="group" aria-label="Filter listings">{btns}</div><p id="hwban" class="hwban" hidden>🎃 Looking for Halloween events? <a href="calendar.html#halloween">See the October calendar</a></p><p id="nomatch" class="nomatch" hidden>No matches yet. Try &#39;winter&#39; or <button type="button" id="qreset" class="linkbtn">browse all</button>.</p>{BRING}<div class="grid" id="list">{cards}</div>''',
script='''<script>(()=>{const qi=document.getElementById('q'),qc=document.getElementById('qclear'),nm=document.getElementById('nomatch'),cnt=document.getElementById('qcount'),cards=[...document.querySelectorAll('#list .card')],gs=document.querySelector('#list .gridsignup');let f='all';const norm=t=>t.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');cards.forEach(c=>{const k=c.cloneNode(true);k.querySelectorAll('.share').forEach(x=>x.remove());c.dataset.txt=norm(k.textContent.replace(/\\s+/g,' '))});
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
page("fishing.html","Fishing",'''<div class="water"><svg class="bobber" viewBox="0 0 40 60" aria-hidden="true"><line x1="20" y1="0" x2="20" y2="14" stroke="#16405e" stroke-width="2"/><circle cx="20" cy="30" r="14" fill="#fff8e7" stroke="#16405e" stroke-width="2"/><path d="M6 30a14 14 0 0 0 28 0z" fill="#e63946"/></svg><h1>🎣 Highwood River: Kids' Fishing Summary</h1><p>Cast your line, wait for the bite, and let most trout swim free!</p></div>'''+share(BASE+"fishing.html","Kids' fishing in the Foothills | "+BRAND)+'''<div class="grid fish-grid">
<div class="card"><h2>📅 Season</h2><p>Most of the Highwood is open <strong>June 16 to October 31</strong>. Seasons differ by stretch: the last 500 m before the Bow River is open all year, and Storm Creek is closed all year.</p></div>
<div class="card"><h2>🚫 Bait Ban</h2><p>No bait on any part of the Highwood. Use <strong>unscented</strong> lures or flies only (no scented lures or PowerBait).</p></div>
<div class="card"><h2>🐟 Trout</h2><p><strong>Most trout must be released.</strong> In the upper headwaters you may keep up to 2 brook trout. Mountain whitefish can be kept on some stretches at some times, so check the limits.</p></div>
<div class="card"><h2>🧒 Licence</h2><p>Kids <strong>under 16</strong> do not need a fishing licence, but they still follow the rules. Anglers 16 to 64 need a sportfishing licence. Alberta residents 65 and over don't (<a href="https://www.albertaregulations.ca/fishingregs/licensing.html" rel="noopener">official licensing page</a>).</p></div></div>
<p class="note"><strong>Check before you go:</strong> Always check the official 2026 Alberta Guide to Sport Fishing Regulations before fishing. The Highwood River rules are in the <a href="https://www.albertaregulations.ca/fishingregs/ES1-Rivers.pdf" rel="noopener">official Eastern Slopes (ES1) rivers table</a>. This page is a kid-friendly summary, not legal advice.</p>'''+FISHSEC+BRING+COMPACT,full="Family Fishing near High River, Turner Valley & Kananaskis | Foothills Kids Outdoors")
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
page("calendar.html","Calendar",ogimg=BASE+"images/og-halloween.jpg",ogalt="Pumpkin field below wooded hills",ogw=1200,ogh=630,full="Family Outdoor Events in Okotoks, High River & Diamond Valley | Foothills Kids Outdoors",body=f'''<h1>🗓️ Foothills Family Events Calendar</h1>
<p>Real dated events and seasonal dates for families around Okotoks, High River, Turner Valley, Black Diamond, Longview and Kananaskis, from organizers\' own pages.</p>
<p class="note"><strong>Dates change.</strong> Events can be cancelled or moved for weather and other reasons, so check with the organizer (use each <em>Details</em> link) before you go.</p>
<div class="cal"><p class="cal-group" role="heading" aria-level="2">Coming up: next 3 months</p>{soon}<p class="cal-group" role="heading" aria-level="2">Later this season</p>{later}<p id="noev" hidden>No upcoming events listed right now. Check back soon!</p></div>
<section class="signup"><h2 class="signup-title">✉️ Get the weekly newsletter</h2><p>Get a new Foothills scavenger hunt every week, plus outdoor ideas for families. One email a week, unsubscribe anytime.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>''',
script='''<script>(()=>{const d=new Date(),t=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');document.querySelectorAll('.ev').forEach(li=>{if(li.dataset.last<t)li.hidden=true});document.querySelectorAll('.month').forEach(m=>{if(!m.querySelector('.ev:not([hidden])'))m.hidden=true});const all=document.querySelectorAll('.ev'),hid=document.querySelectorAll('.ev[hidden]');document.getElementById('noev').hidden=!(all.length&&all.length===hid.length)})()</script>''')
finds=["A pine cone","Animal tracks","A feather","Three different kinds of leaves","Something red","Animal sign (scat, chewed stick, nest)","A smooth, round rock","Moss or lichen","A spider web","A bird (see or hear it)","Something that smells good","A fish in the water","Litter that doesn't belong (pack it out!)","The tallest tree you can see","A trail made by an animal"]
li="".join(f"<li>{f}</li>" for f in finds)
page("scavenger-hunt.html","Scavenger Hunt",f'''<p class="note noprint newsletter-line">✉️ This is our starter hunt. Want a new themed hunt every week? <a href="{SIGNUP}">Get the weekly newsletter</a></p>
<div class="noprint hunt-choose"><a class="btn btn-play" href="hunt.html">📱 Play on your phone, no printer needed</a> <button class="btn" onclick="print()">🖨️ Print this card</button></div>
<div class="hunt"><h1>🏅 {BRAND} Scavenger Quest</h1><p>Explorer or team names: ______________________ Date: __________</p><p>When you spot something, check the box. Work together and keep your eyes open!</p><ul>{li}</ul>
<p><strong>Find 10 to earn your Trail Explorer badge!</strong></p><p>Leave No Trace: look, don't take. Leave nature the way you found it.</p><p>Bonus: how many sounds can you hear in 60 silent seconds? _____</p></div>'''+DONEBOX,full="Free Printable Kids' Nature Scavenger Hunt for the Calgary-Area Foothills | Foothills Kids Outdoors")
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
page("hunt.html","Phone Scavenger Hunt",f'''<div class="phunt"><h1>📱 Scavenger Quest</h1><p class="newsletter-line">✉️ This is our free starter hunt. Want a new hunt every week? <a href="{SIGNUP}">Get the weekly newsletter.</a></p><p>Tap an item when you spot it. Your progress saves on this phone only. Nothing is uploaded, no account needed.</p>{share(BASE+"hunt.html","Phone nature scavenger hunt for kids | "+BRAND)}
<div class="hprog"><div class="hbarwrap" role="progressbar" aria-label="Items found" aria-valuemin="0" aria-valuemax="{len(finds)}" aria-valuenow="0"><div id="hbar" class="hbar"></div></div><p id="htxt" class="htxt" aria-live="polite">0 of {len(finds)} found</p></div>
<ul class="hlist">{cards}</ul>
<div id="hdone" class="hdone" tabindex="-1" hidden><h2>🎉 You did it!</h2><p>Every item found. Want a new hunt every week? <a href="{SIGNUP}">Get the weekly newsletter.</a></p></div>
<p class="hfoot">Leave No Trace: look, don't take.</p>
<p><button type="button" id="hreset" class="btn">↺ Start over</button> <a href="scavenger-hunt.html">🖨️ Prefer paper? Print the card</a></p></div><div id="confetti" aria-hidden="true"></div>'''+DONEBOX,HJS,full="Phone Nature Scavenger Hunt for Kids: Okotoks to Kananaskis | Foothills Kids Outdoors")
page("leaders.html","Leaders",'''<h1>🧭 Groups &amp; Leaders</h1><p>For anyone leading kids outdoors: family groups, school classes, and club or youth leaders.</p><div class="grid">
<div class="card"><h2>Plan an outing</h2><p>Use the <a href="directory.html">directory</a> and <a href="calendar.html">calendar</a> to pick an age-appropriate activity.</p></div>
<div class="card"><h2>Printables</h2><p>Grab the <a href="scavenger-hunt.html">scavenger hunt card</a> for your group.</p></div>
<div class="card"><h2>Safety checklist</h2><ul><li>Adult-to-kid ratios</li><li>Permission forms</li><li>First-aid kit</li><li>Weather &amp; wildlife check</li></ul></div>
<div class="card"><h2>Share your group</h2><p>Know a great kids\' outdoor spot or program? Tell us on <a href="https://www.facebook.com/FoothillsKidsOutdoors/" rel="noopener">Facebook</a>. Always check details with the organizer before an outing.</p></div></div>'''+COMPACT,full="Taking Kids' Groups Outdoors in the Calgary-Area Foothills | Foothills Kids Outdoors")
page("sponsors.html","Sponsors",'''<h1>🤝 Sponsor the Adventure</h1><p>Help local kids get outside by supporting a free Foothills outdoor guide for families.</p><div class="grid">
<div class="card"><span class="badge">Tier</span><h2>🌱 Trail Buddy</h2><p>Name on sponsors page.</p></div>
<div class="card"><span class="badge">Tier</span><h2>🌲 Trail Guide</h2><p>Logo on sponsors page and a printable.</p></div>
<div class="card"><span class="badge">Tier</span><h2>⛰️ Summit Partner</h2><p>Featured placement on the home page.</p></div></div>
<p class="note"><strong>Contact us for rates.</strong> Message us on <a href="https://www.facebook.com/FoothillsKidsOutdoors/" rel="noopener">Facebook</a> to talk about sponsoring.</p>'''+COMPACT,full="Sponsor a Family Outdoor Guide for Longview, Turner Valley & High River | Foothills Kids Outdoors")
page("about.html","About",f'''<h1>About {BRAND}</h1><p>{BRAND} is a family-friendly directory of outdoor activities for kids of all ages, from toddlers to teens, around Longview and the Foothills, Alberta, made for parents, grandparents and group leaders.</p>
<p>Our goal is simple: help families get outside together and make every outing feel like an adventure, whether that's a new trail, a first fish or a scavenger hunt.</p>
<p class="note">Directory listings link to each organizer\'s public page. Details change, so check with the organizer and official sources for rules, closures and conditions before you go.</p>'''+COMPACT,full="About Foothills Kids Outdoors: Kids' Outdoor Guide for Longview & the Foothills")

VBADGE={"light-up-longview":"Happening now: Sun Oct 18, 2026","millarville-mras":"Happening now: Christmas Market Nov 5-8 &amp; 12-15","alberta-highway-cleanup":"Spring 2027","sheep-river-bird-count":"Coming up: Dec–Jan","high-river-bird-count":"Coming up: Dec–Jan","okotoks-cleanup":"Spring 2027 dates TBA","calgary-pathway-cleanup":"Spring 2027 dates TBA"}
VYOUNG={"okotoks-litter-free","junior-forest-wardens"}
def _vol(i,n,org,d,age,when,links):
    l=" &middot; ".join(f'<a href="{E(u)}" rel="noopener">{t}</a>' for t,u in links)
    bd=(f'<span class="badge">{VBADGE[i]}</span> ' if i in VBADGE else "")+('<span class="badge">Good for young kids</span>' if i in VYOUNG else "")
    return f'<div class="card" id="{i}">{bd}<h3>{n}</h3><p>{d}</p><ul class="meta"><li><strong>Organizer:</strong> {org}</li><li><strong>Ages:</strong> {age}</li><li><strong>When:</strong> {when}</li></ul>{f'<p class="org">{l}</p>' if l else ""}<p class="note">Last checked: Oct 14, 2026</p></div>'
VOL=[
("light-up-longview","🎄 Light Up Longview","Light Up Longview committee (Village of Longview)","The Light Up Longview committee is setting up the village\'s Christmas lights in the campground and around the village, and invites all villagers to help. A hot lunch is served as a thank-you. Meet at the Longview campground cookhouse.","Families welcome; kids with a parent.","Sunday, October 18, 2026, 10 AM to 2 PM.",[]),
("millarville-mras","🐎 Millarville Racing &amp; Agricultural Society volunteers","Millarville Racing &amp; Agricultural Society","Help with setup, admissions, parking, hospitality and vendor help at the Christmas Market, Farmers\' Market, Canada Day Races and the Priddis &amp; Millarville Fair. Free to volunteer, and volunteers get free admission to the society\'s events. Contact the office through the volunteer page.","Volunteers range \"from students to seniors.\" No minimum age given, check with organizer.","Christmas Market Nov 5 to 8 and Nov 12 to 15, 2026. The Summer Market runs Saturdays in summer and the Fair is in August.",[("Millarville volunteer page","https://millarvilleracetrack.com/become-a-volunteer/"),("Christmas Market dates","https://millarvilleracetrack.com/annual-christmas-market/")]),
("diamond-valley-volunteer","🏘️ Town of Diamond Valley volunteer interest form","Town of Diamond Valley","Black Diamond and Turner Valley families can fill in a free volunteer interest form for town events (summer and winter), parks and recreation and community groups. The town gets in touch when a good fit comes up.","Check with organizer.","Year-round sign-up.",[("Diamond Valley volunteering page","https://www.diamondvalley.town/201/Volunteering"),("Volunteer interest form","https://www.diamondvalley.town/FormCenter/Volunteering-6/Volunteer-Service-Application-Form-47")]),
("alberta-highway-cleanup","🛣️ Alberta Highway Cleanup","Alberta Transportation and Economic Corridors (through registered non-profit groups)","A yearly roadside litter pickup on provincial highways, including around Longview, Turner Valley and Black Diamond. Families can\'t sign up on their own; they join through a participating non-profit group, such as Junior Forest Wardens. Everyone must complete safety training first. Groups earn money for their organization.","9 and older. 1 adult for every 2 kids under 14, and 1 adult for every 5 kids aged 14 to 18.","First or second Saturday in May each year (2026 was May 2).",[("Alberta Highway Cleanup page","https://www.alberta.ca/alberta-highway-cleanup-programs")]),
("okotoks-cleanup","🌱 Okotoks Community Clean Up and Tree Planting","Town of Okotoks (with Parks &amp; Recreation)","A spring cleanup of the Sheep River valley plus tree planting. There's a cleanup BINGO card with prizes and a free volunteer BBQ. Tree planters bring shovels, gloves, closed-toe shoes and eye protection.","Open to individuals and families. No minimum age given, check with organizer.","Every spring. The 2026 event was Saturday, May 9; the 2027 date isn't posted yet.",[("Town of Okotoks event page","https://www.okotoks.ca/your-community/living-okotoks/community-event-calendar/community-clean-and-tree-planting-2026")]),
("okotoks-litter-free","🗑️ Okotoks Litter-Free Community cleanup kits","Town of Okotoks","Pick up a free kit (gloves, bags and a rec coupon) and do a family litter pick in a park or along a pathway whenever it suits you. Register your cleanup and the town collects the bags. Stay back from busy roads and never pick up needles or glass.","Check with organizer.","Year-round.",[("Town of Okotoks Litter-Free page","https://www.okotoks.ca/your-community/amenities/parks-pathways-playgrounds/litter-free-community")]),
("calgary-pathway-cleanup","🏞️ Calgary Pathway and River Cleanup","City of Calgary (Calgary Parks)","A citywide cleanup of pathways and riverbanks that has run every year since 1967, and was started by a 12-year-old! Registration is required.","12 and older; 12 to 17-year-olds must come with a parent or guardian. Not for kids under 12.","Every year in early May (2026 was May 1 to 3). Registration opens early in the year.",[("City of Calgary registration page","https://www.calgary.ca/volunteer/pathway-river-cleanup-registration.html")]),
("sheep-river-bird-count","🐦 Sheep River Christmas Bird Count","Local count circle, Christmas Bird Count (Birds Canada)","A one-day winter bird census around Okotoks, Turner Valley and Black Diamond. Walk a route with a team, or count birds at your backyard feeder. All skill levels welcome, from the youngest birder up.","Check with organizer.","Count season is December 14, 2026 to January 5, 2027. The 2026 circle date isn't posted yet (last year's was Dec 28).",[("Birds Canada Christmas Bird Count","https://www.birdscanada.org/programs/christmas-bird-count"),("Alberta circle list","https://naturecounts.ca/apps/cbc/compilers.jsp?lang=EN&prov=AB")]),
("high-river-bird-count","🦅 High River Christmas Bird Count","Local count circle, Christmas Bird Count (Birds Canada)","The same friendly winter bird census for the High River circle. Great for curious kids with binoculars.","Check with organizer.","Count season is December 14, 2026 to January 5, 2027. The 2026 date isn't posted yet (last year's was Dec 16).",[("Alberta circle list","https://naturecounts.ca/apps/cbc/compilers.jsp?lang=EN&prov=AB")]),
("fkc-trail-care","🥾 Friends of Kananaskis Country: Volunteer Trail Care","Friends of Kananaskis Country, with Alberta Parks","Trail care days on Kananaskis trails, from litter pickup to clearing deadfall. Set up a volunteer profile first to get the list of upcoming days. Trail work can be physical, so ask whether a day suits kids.","Check with organizer.","Days are posted through the season by email and on their calendar.",[("Friends of Kananaskis Country volunteer page","https://kananaskis.org/how-to-help/volunteer-programs/"),("Alberta Parks volunteering","https://albertaparks.ca/parks/kananaskis/kananaskis-country/volunteering/")]),
("junior-forest-wardens","🌲 Junior Forest Wardens (Kananaskis projects)","Junior Forest Wardens, Bragg Creek club (listed by Alberta Parks)","An outdoor club for young people and their families. The local club helps with projects in Kananaskis, like removing buffaloberry shrubs.","Ages 6 to 18 and their families.","Check with organizer.",[("Alberta Parks volunteering page","https://albertaparks.ca/parks/kananaskis/kananaskis-country/volunteering/")]),
("cross-conservation","🦌 Ann &amp; Sandy Cross Conservation Area volunteers","Ann &amp; Sandy Cross Conservation Area","Help care for the land, support nature education programs and welcome visitors at this conservation area west of Okotoks. A volunteer application form is required.","Check with organizer.","Year-round.",[("Cross Conservation volunteer page","https://www.crossconservation.org/about/volunteer/")]),
]
page("volunteer.html","Volunteer",f'''<h1>🌿 Volunteer with your kids</h1><p>Giving back outdoors is one of the best family adventures. Around the Alberta foothills, families can plant trees, pick up litter along the river, count winter birds and help care for trails. Kids learn to look after the places they love, and everyone gets fresh air together.</p>
<p class="note"><strong>Dates change, so always confirm with the organizer.</strong> Ages, dates and sign-up rules come from each organizer's own page and can change from year to year. Use the links on each card to check before you go.</p>
<div class="grid">'''+"".join(_vol(*v) for v in VOL)+'</div><p>Make a weekend of it: pair a volunteer day with a night at one of our <a href="camping-foothills.html">Foothills family campgrounds</a>, or try <a href="camping-crown-land.html">crown land camping with kids</a>.</p><p>Know a family-friendly volunteer day near you? <a href="mailto:foothillsoutdoor1@gmail.com">Tell us</a>.</p>'+f'<section class="signup compact"><h2 class="signup-title">✉️ Get new volunteer days in your inbox</h2><p>Family volunteer days and outdoor ideas in our weekly email. One email a week, unsubscribe anytime.</p><a class="btn" href="{SIGNUP}">Sign me up</a></section>',full="Volunteer with Your Kids in the Alberta Foothills | Foothills Kids Outdoors",ogimg=BASE+"images/og-volunteer.png",ogalt="Illustration of mountains, green foothills and pine trees under a sunny sky")

# Newsletter-only subscriber hunt (not in NAV or sitemap)
_S=lambda t:re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
FC=["⭐ A fallen golden or brown **trembling aspen** leaf on the ground (round with a pointy tip). Look up: are most aspen branches bare now?",
"⭐ A white aspen trunk with black marks (they look like eyes!)",
"⭐ Bright red-orange **wild rose hips** (wild rose is Alberta's flower)",
"⭐ A **black-billed magpie**: black and white with a long tail",
"⭐ Hear a **black-capped chickadee** say \"chick-a-dee-dee-dee\"",
"⭐ White **snowberry** berries on a bare shrub (don't eat; they can make you sick)",
"⭐ A leaf that is three colours at once",
"⭐⭐ **Red-osier dogwood**: bright red stems near water or wet ground",
"⭐⭐ **Balsam poplar**: big buds that are sticky and smell sweet (just sniff, don't pick)",
"⭐⭐ **Chokecherry** shrub: look for leftover dark, dried cherries or bare stems of the clusters, and smooth reddish-brown bark with tiny lines (look only, don't eat)",
"⭐⭐ **Saskatoon** shrub: find a fallen rounded leaf with teeth on the top half only, or a shrub with smooth grey bark",
"⭐⭐ A tree that stays green: is it a spruce (sharp, square needles), pine (needles in pairs/bundles) or fir (flat, soft)? Circle: spruce / pine / fir (firs are rarer down low; you might find one closer to the mountains)",
"⭐⭐ A **mule deer** or signs it was browsing: nibbled twig tips. Bonus: big ears, white rump, black-tipped tail",
"⭐⭐ Geese flying in a \"V\" or honking overhead (some Canada geese stay all winter!). Count them: ____"]
assert len(FC)==14
_fcli="".join(f'<li><span class="fcbox" aria-hidden="true"></span><span>{_S(E(x,quote=False))}</span></li>' for x in FC)
FCICONS=["🍂","🌳","🌹","🐦","🎶","⚪","🍁","🔴","🌱","🍒","🫐","🌲","🦌","🪿"]
assert len(FCICONS)==len(FC)
_fccards="".join(f'<li><button type="button" class="hcard" aria-pressed="false" data-i="{i}"><span class="hi" aria-hidden="true">{FCICONS[i]}</span><span class="ht">{_S(E(x,quote=False))}</span><span class="hc" aria-hidden="true">✓</span></button></li>' for i,x in enumerate(FC))
FCJS=HJS.replace("fko-hunt-quest-v1","fko-hunt-01-fall-colours-v1")
assert FCJS!=HJS
FCCSS="""<style>
.phunt .fcline{font-weight:600}
.phunt .fcsafe{border:4px solid #e85d04;background:#fff3e6;border-radius:16px;padding:.7rem 1rem;margin:.8rem 0;font-size:1.05em}
.phunt .fcbadge{font-size:1.15em}
.fcprint{display:none}
@media print{
@page{size:letter;margin:.4in}
.hero-head,header,footer,nav,.signup,.noprint,.share,.hprog,.hdone,#confetti,.htoast{display:none!important}
body{background:#fff!important;font-size:9.6pt;line-height:1.25}
main{padding:0!important;margin:0!important;max-width:none!important}
.phunt{max-width:none;border:2px solid #000;padding:.3in .4in}
.phunt h1{font-size:17pt;margin:0 0 4pt;color:#000}
.phunt p{margin:3pt 0}
.phunt .fcsafe{border:3px solid #000;background:#fff;padding:4pt 7pt;margin:5pt 0;font-size:10pt;border-radius:6px}
.phunt .hlist{display:block;margin:4pt 0}
.phunt .hlist li{margin:2pt 0}
.phunt .hcard{min-height:0!important;padding:0!important;border:0!important;box-shadow:none!important;background:#fff!important;color:#000!important;font-size:9.6pt!important;gap:6pt!important;align-items:flex-start!important}
.phunt .hcard .hi{display:none}
.phunt .hcard .ht::before{content:"";flex:0 0 auto;display:inline-block;width:.95em;height:.95em;border:2px solid #000;border-radius:3px;margin-right:6pt;vertical-align:-2pt}
.phunt .hcard .hc{display:none!important}
.phunt .hcard[aria-pressed=true] .ht{text-decoration:none}.phunt .hcard .ht::after{content:none!important}
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
</style>"""
page("hunt-01-fall-colours.html","Fall Colours Quest",FCCSS+f'''<div class="phunt"><h1>🍂 Fall Colours Quest</h1><p class="newsletter-line noprint">✉️ This is this week's subscriber hunt from the {BRAND} newsletter. Thanks for reading!</p><p class="noprint">Tap an item when you spot it. Your progress saves on this phone only. Nothing is uploaded, no account needed. Or print it.</p>
<p class="fcline">Explorer/team: ____________________ &nbsp;Date: ________ &nbsp;Where: ____________________</p>
<p class="fcsafe">🧡 <strong>Safety:</strong> Fall is hunting season in the foothills. Wear bright colours (blaze orange is great), stay on marked trails, keep an adult along. Never taste wild berries. Give wildlife lots of space.</p>
<p>⭐ = easy (ages 6–8) · ⭐⭐ = harder (ages 10–13). Check the box when you find it!</p>
<div class="hprog"><div class="hbarwrap" role="progressbar" aria-label="Items found" aria-valuemin="0" aria-valuemax="{len(FC)}" aria-valuenow="0"><div id="hbar" class="hbar"></div></div><p id="htxt" class="htxt" aria-live="polite">0 of {len(FC)} found</p></div>
<ul class="hlist">{_fccards}</ul>
<div id="hdone" class="hdone" tabindex="-1" hidden><h2>🎉 You did it!</h2><p>Every item found. Watch your inbox for next week's hunt.</p></div>
<p class="fcbadge"><strong>Find 10 to earn your Fall Colours badge!</strong></p>
<p class="hfoot">🍂 <strong>Leave No Trace:</strong> Take photos and drawings, not leaves or berries. <strong>Don't pick anything in provincial parks or natural areas</strong>, where it isn't allowed. Stay on trails.</p>
<p>Bonus: draw your favourite leaf on the back and colour it in.</p>
<p class="noprint"><button type="button" id="hreset" class="btn">↺ Start over</button> <button type="button" class="btn" onclick="print()">🖨️ Print this hunt</button></p></div><div id="confetti" aria-hidden="true"></div>'''+DONEBOX,FCJS,full="Fall Colours Quest: Subscriber Scavenger Hunt 01 | Foothills Kids Outdoors")
PAGES.remove("hunt-01-fall-colours.html")

# Newsletter-only subscriber hunt 02 (not in NAV or sitemap). Text: trailhead-ops/hunt-02-first-snow.md (DRAFT)
FS=["⭐ **Frost or snow** on grass, a fence or a car roof. Is it sparkly or fluffy?",
"⭐ A **frozen puddle** (look from the edge and tap it with a stick, but don't stand on it!). Do you see bubbles trapped inside?",
"⭐ Your **breath** making a cloud in the cold air",
"⭐ A **common raven**: all black and bigger than a crow. Listen for a deep \"croak\"",
"⭐ A **snowflake** caught on a dark mitten. No snow? Find a seed head with frost on it, or a leaf with a frosty edge",
"⭐ A **spruce cone** on the ground (long and papery, not hard like a pine cone)",
"⭐ A **bare tree** with an empty bird nest you can see now that the leaves are gone (look only)",
"⭐⭐ A **red squirrel midden**: a pile of chewed spruce-cone scales under a spruce tree",
"⭐⭐ **Bohemian waxwings**: a flock of soft grey-brown birds with a crest, often eating berries in town trees",
"⭐⭐ **Mule deer vs white-tailed deer**: tail with a black tip = mule deer; a big white \"flag\" tail = white-tail. Which one did you see?",
"⭐⭐ A **deer bed**: an oval patch of flattened grass or melted snow where a deer rested",
"⭐⭐ **Snow on one side** of a tree or hill only. Which way does it face? (Hint: the sunny south side melts first.) No snow? Find the side where frost lasts longest",
"⭐⭐ **Icicles** or ice along a creek edge (look from the bank only)",
"⭐⭐ **Days are getting shorter**: notice what time it gets dark tonight, then check again in a week. Is it earlier?"]
assert len(FS)==14
FSICONS=["❄️","🧊","😮‍💨","🐦‍⬛","🧤","🌲","🪹","🐿️","🐦","🦌","🌾","⛰️","💧","🌇"]
assert len(FSICONS)==len(FS)
_fscards="".join(f'<li><button type="button" class="hcard" aria-pressed="false" data-i="{i}"><span class="hi" aria-hidden="true">{FSICONS[i]}</span><span class="ht">{_S(E(x,quote=False))}</span><span class="hc" aria-hidden="true">✓</span></button></li>' for i,x in enumerate(FS))
FSJS=HJS.replace("fko-hunt-quest-v1","fko-hunt-02-first-snow-v1")
assert FSJS!=HJS
page("hunt-02-first-snow.html","First Snow Quest",FCCSS+f'''<div class="phunt"><h1>❄️ First Snow Quest</h1><p class="newsletter-line noprint">✉️ This is this week's subscriber hunt from the {BRAND} newsletter. Thanks for reading!</p><p class="noprint">Tap an item when you spot it. Your progress saves on this phone only. Nothing is uploaded, no account needed. Or print it.</p>
<p class="fcline">Explorer/team: ____________________ &nbsp;Date: ________ &nbsp;Where: ____________________</p>
<p class="fcsafe">🧡 <strong>Safety:</strong> It's hunting season in the foothills. Wear bright colours (blaze orange is great) and stay on marked trails. <strong>Never walk on early ice</strong>: AHS recommends at least 15 cm before walking or skating, and river ice is never safe to trust. Dress warm in layers, with a toque and mitts and spare socks. Always stay with an adult. Give deer, birds and all wildlife lots of space (bears are still awake until late November). Never taste berries or snow off plants.</p>
<p>⭐ = easy (ages 6–8) · ⭐⭐ = harder (ages 10–13). Check the box when you find it!</p>
<div class="hprog"><div class="hbarwrap" role="progressbar" aria-label="Items found" aria-valuemin="0" aria-valuemax="{len(FS)}" aria-valuenow="0"><div id="hbar" class="hbar"></div></div><p id="htxt" class="htxt" aria-live="polite">0 of {len(FS)} found</p></div>
<ul class="hlist">{_fscards}</ul>
<div id="hdone" class="hdone" tabindex="-1" hidden><h2>🎉 You did it!</h2><p>Every item found. Watch your inbox for next week's hunt.</p></div>
<p class="fcbadge"><strong>Find 10 to earn your First Snow badge!</strong></p>
<p class="hfoot">❄️ <strong>Leave No Trace:</strong> Take photos and drawings, not cones or nests. <strong>Don't pick or take anything in provincial parks or natural areas.</strong> Stay on trails, and leave the squirrel's winter food where you found it.</p>
<p>Bonus: draw your best snowflake (or frost pattern) on the back. Real snowflakes have 6 sides!</p>
<p class="noprint"><button type="button" id="hreset" class="btn">↺ Start over</button> <button type="button" class="btn" onclick="print()">🖨️ Print this hunt</button></p></div><div id="confetti" aria-hidden="true"></div>'''+DONEBOX,FSJS,full="First Snow Quest: Subscriber Scavenger Hunt 02 | Foothills Kids Outdoors")
PAGES.remove("hunt-02-first-snow.html")

exec(open("camping.py").read())
exec(open("gardening.py").read())
_ORDER=["index.html","directory.html","calendar.html","fishing.html","scavenger-hunt.html","hunt.html","volunteer.html","camping-foothills.html","camping-crown-land.html","gardening.html","leaders.html","sponsors.html","about.html"]
assert sorted(_ORDER)==sorted(PAGES)
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{BASE}{"" if p=="index.html" else p}</loc><lastmod>{_dt.date.today().isoformat()}</lastmod></url>\n' for p in _ORDER)+'</urlset>\n')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")

# Calendar preview photo credit (seasonal pumpkin image)
_cf=open("calendar.html").read()
if "Visitor7" not in _cf:
    open("calendar.html","w").write(_cf.replace("</main>",'<p class="note" style="font-size:.8em">Preview photo: <a href="https://commons.wikimedia.org/wiki/File:Pumpkin_Patch_(Winchester,_Oregon).jpg" rel="noopener">Visitor7</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" rel="noopener">CC BY-SA 3.0</a> (cropped)</p></main>',1))
