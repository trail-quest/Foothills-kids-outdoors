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
NAV = [("index.html","Home"),("directory.html","Directory"),("fishing.html","Fishing"),("calendar.html","Calendar"),("scavenger-hunt.html","Scavenger Hunt"),("leaders.html","Groups &amp; Leaders"),("sponsors.html","Sponsors"),("about.html","About")]
def page(fn,title,body,script=""):
    body=body.replace("<h2>",'<h2><span class="sign">').replace("</h2>","</span></h2>")
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a>' for h,t in NAV)
    open(fn,"w").write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {BRAND}</title><link rel="stylesheet" href="style.css"></head><body>
<header class="hero-head">{SCENE}<div class="head-inner"><a class="brand" href="index.html">{ICON_PINE} {BRAND}</a><nav>{nav}</nav></div></header>
<main>{body}</main>
<footer>{GRASS}<div class="foot-inner"><p><strong>{BRAND}</strong> &middot; Kids' outdoor adventures around Longview &amp; the Foothills, Alberta</p><p>Follow us on <a href="https://www.facebook.com/FoothillsKidsOutdoors" rel="noopener">Facebook</a></p><p>v1 prototype. Directory details come from organizers' public pages and can change; check with the organizer and official sources before heading out.</p></div></footer>{script}</body></html>''')
EX='<span class="badge">example listing</span>'
page("index.html","Home",f'''<section class="hero"><h1>Explore the Alberta Foothills with your kids! 🏔️</h1>
<p>From the Highwood River to the edge of Kananaskis, through ranch country from Longview to Okotoks and High River, find family-friendly trails, fishing, horses, wildlife and winter fun for kids of all ages.</p>
<a class="btn" href="directory.html">Explore the Directory</a><a class="btn" href="scavenger-hunt.html">Print a Scavenger Hunt</a></section>
<div class="grid">
<div class="card"><h2>{ICONS['boot']} Trails</h2><p>Kid-sized trails and family walks.</p></div>
<div class="card"><h2>{ICONS['fish']} Fishing</h2><p>A kid-friendly <a href="fishing.html">Highwood River summary</a>.</p></div>
<div class="card"><h2>{ICONS['tent']} Ranch &amp; Wildlife</h2><p>Horses, ranch life and nature spotting. <a href="leaders.html">Group resources</a>.</p></div>
<div class="card"><h2>{ICONS['sun']} Season Calendar</h2><p>See the <a href="calendar.html">monthly outing ideas</a>.</p></div></div>
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
<p class="note">This is general guidance only. Check official sources (such as Alberta Parks and local advisories) for current conditions, closures and safety information before you go.</p></div>''')
import json,html
CATKEY={"Trails & Hikes":("trails","🥾"),"Fishing":("fishing","🎣"),"Horses & Ranch Life":("horses","🐴"),"Archery":("archery","🏹"),"Wildlife & Nature":("wildlife","🦌"),"Winter Fun":("winter","❄️")}
E=html.escape
def realcard(x):
    k,ic=CATKEY[x["category"]]
    meta="".join(f"<li><strong>{l}:</strong> {E(v)}</li>" for l,v in [("Where",x["location"]),("Ages",x["ages"]),("When",x["season"])] if v)
    adv=f'<p class="advisory">⚠️ {E(x["advisory"])} <a href="{E(x["advisory_source"])}" rel="noopener">Official advisory</a></p>' if x.get("advisory") else ""
    return f'<div class="card" data-cat="{k}"><span class="badge">{E(x["category"])}</span><h3>{ic} {E(x["name"])}</h3><p>{E(x["description"])}</p><ul class="meta">{meta}</ul>{adv}<p class="org">By {E(x["organizer"])} &middot; <a href="{E(x["source"])}" rel="noopener">Source</a></p></div>'
REAL=json.load(open("foothills-activities.json"))
cards="".join(realcard(x) for x in REAL)
btns="".join(f'<button data-f="{k}"{" class=on" if k=="all" else ""}>{v}</button>' for k,v in [("all","All"),("trails","Trails &amp; Hikes"),("fishing","Fishing"),("horses","Horses &amp; Ranch Life"),("archery","Archery"),("wildlife","Wildlife &amp; Nature"),("winter","Winter Fun")])
page("directory.html","Directory",f'''<h1>{ICONS['leaf']} Adventure Directory</h1><p>Real places and programs around the Foothills, from public pages by the organizers named on each card.</p><p class="note"><strong>Details change, check with the organizer</strong> (dates, hours, fees and closures) before you go.</p>
<div class="filters" role="group" aria-label="Filter listings">{btns}</div><div class="grid" id="list">{cards}</div>''',
'''<script>document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filters button').forEach(x=>x.classList.toggle('on',x===b));const f=b.dataset.f;document.querySelectorAll('#list .card').forEach(c=>c.hidden=f!=='all'&&c.dataset.cat!==f)})</script>''')
page("fishing.html","Fishing",'''<div class="water"><svg class="bobber" viewBox="0 0 40 60" aria-hidden="true"><line x1="20" y1="0" x2="20" y2="14" stroke="#16405e" stroke-width="2"/><circle cx="20" cy="30" r="14" fill="#fff8e7" stroke="#16405e" stroke-width="2"/><path d="M6 30a14 14 0 0 0 28 0z" fill="#e63946"/></svg><h1>🎣 Highwood River: Kids' Fishing Summary</h1><p>Cast your line, wait for the bite, and let most trout swim free!</p></div><div class="grid fish-grid">
<div class="card"><h2>📅 Season</h2><p>Most of the Highwood is open <strong>June 16 to October 31</strong>. Seasons differ by stretch: the last 500 m before the Bow River is open all year, and Storm Creek is closed all year.</p></div>
<div class="card"><h2>🚫 Bait Ban</h2><p>No bait on any part of the Highwood. Use <strong>unscented</strong> lures or flies only (no scented lures or PowerBait).</p></div>
<div class="card"><h2>🐟 Trout</h2><p><strong>Most trout must be released.</strong> In the upper headwaters you may keep up to 2 brook trout. Mountain whitefish can be kept on some stretches at some times, so check the limits.</p></div>
<div class="card"><h2>🧒 Licence</h2><p>Kids <strong>under 16</strong> do not need a fishing licence, but they still follow the rules. Adults 16 to 64 who fish need a licence.</p></div></div>
<p class="note"><strong>Check before you go:</strong> Always check the official 2026 Alberta Guide to Sport Fishing Regulations before fishing. The Highwood River rules are in the <a href="https://www.albertaregulations.ca/fishingregs/ES1-Rivers.pdf" rel="noopener">official Eastern Slopes (ES1) rivers table</a>. This page is a kid-friendly summary, not legal advice.</p>''')
rows=[("Sat, Oct 17, 2026","10 AM &ndash; 2 PM","Fall colours hike and leaf-rubbing collection"),
("Sat, Nov 7, 2026","10 AM &ndash; noon","Animal tracks and signs walk before the snow sticks"),
("Sat, Dec 12, 2026","10 AM &ndash; noon","Winter bird count and pine cone feeders"),
("Sat, Jan 30, 2027","10 AM &ndash; 2 PM","Snowshoe or winter walk with a hot-chocolate stop"),
("Sat, Feb 13, 2027","10 AM &ndash; noon","Snow tracking and build-a-quinzhee demo"),
("Sat, Mar 13, 2027","10 AM &ndash; noon","Early-spring melt walk: listen for running water"),
("Sat, Apr 24, 2027","10 AM &ndash; noon","Earth Day trail clean-up (pack it out!)"),
("May 2027","Open","Your choice: spring wildflower walk or first fishing trip")]
tr="".join(f"<tr><td>{d}</td><td>{t}</td><td>{e}</td></tr>" for d,t,e in rows)
page("calendar.html","Calendar",f'''<h1>🗓️ Family Outdoor Activity Ideas by Month</h1>
<p>A suggested schedule of one outing a month for families or groups, with a seasonal idea for each. Pick the dates that work for you!</p>
<p class="note">These are <strong>suggestions</strong>, not organized events. Check weather, trail conditions and closures before you go.</p>
<table><tr><th>Suggested date</th><th>Time</th><th>Seasonal activity idea</th></tr>{tr}</table>''')
finds=["A pine cone","Animal tracks","A feather","Three different kinds of leaves","Something red","Animal sign (scat, chewed stick, nest)","A smooth, round rock","Moss or lichen","A spider web","A bird (see or hear it)","Something that smells good","A fish in the water","Litter that doesn't belong (pack it out!)","The tallest tree you can see","A trail made by an animal"]
li="".join(f"<li>{f}</li>" for f in finds)
page("scavenger-hunt.html","Scavenger Hunt",f'''<p class="noprint"><button class="btn" onclick="print()">🖨️ Print this card</button></p>
<div class="hunt"><h1>🏅 {BRAND} Scavenger Quest</h1><p>Explorer or team names: ______________________ Date: __________</p><p>When you spot something, check the box. Work together and keep your eyes open!</p><ul>{li}</ul>
<p><strong>Find 10 to earn your Trail Explorer badge!</strong></p><p>Leave No Trace: look, don't take. Leave nature the way you found it.</p><p>Bonus: how many sounds can you hear in 60 silent seconds? _____</p></div>''')
page("leaders.html","Leaders",'''<h1>🧭 Groups &amp; Leaders</h1><p>For anyone leading kids outdoors: family groups, school classes, and club or youth leaders.</p><div class="grid">
<div class="card"><h2>Plan an outing</h2><p>Use the <a href="directory.html">directory</a> and <a href="calendar.html">calendar</a> to pick an age-appropriate activity.</p></div>
<div class="card"><h2>Printables</h2><p>Grab the <a href="scavenger-hunt.html">scavenger hunt card</a> for your group.</p></div>
<div class="card"><h2>Safety checklist</h2><ul><li>Adult-to-kid ratios</li><li>Permission forms</li><li>First-aid kit</li><li>Weather &amp; wildlife check</li></ul></div>
<div class="card"><h2>Share your group</h2><p>Listing submissions are coming in a future version.</p></div></div>''')
page("sponsors.html","Sponsors",'''<h1>🤝 Sponsor the Adventure</h1><p>Help local kids get outside. Tiers below are placeholders; pricing and benefits will be confirmed later.</p><div class="grid">
<div class="card"><span class="badge">Tier</span><h2>🌱 Trail Buddy</h2><p>Starting at $___</p><p>Name on sponsors page.</p></div>
<div class="card"><span class="badge">Tier</span><h2>🌲 Trail Guide</h2><p>Starting at $___</p><p>Logo on sponsors page and a printable.</p></div>
<div class="card"><span class="badge">Tier</span><h2>⛰️ Summit Partner</h2><p>Starting at $___</p><p>Featured placement on the home page.</p></div></div>
<p class="note">No prices or benefits are final. Contact details coming soon.</p>''')
page("about.html","About",f'''<h1>About {BRAND}</h1><p>{BRAND} is a family-friendly directory of outdoor activities for kids of all ages, from toddlers to teens, around Longview and the Foothills, Alberta, made for parents, grandparents and group leaders.</p>
<p>It's built in the same playful spirit as the kid games <em>Trail Quest</em> and <em>Gone Fishin'</em>: every outing is a quest, and every kid earns a badge.</p>
<p class="note">This is a v1 prototype. Example listings and sample events are placeholders. Always check official sources for rules, closures and conditions.</p>''')
