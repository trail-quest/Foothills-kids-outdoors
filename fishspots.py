# Family fishing spots: regs from 2026 Alberta Guide to Sport Fishing Regulations (checked Oct 14, 2026)
R="https://www.albertaregulations.ca/fishingregs/"
L1=R+"ES1-Lakes.pdf"; RV=R+"ES1-Rivers.pdf"; PT=R+"fish-stocking.html"
PTREG=dict(season="Open all year",limits="5 trout (any size), 3 northern pike, 15 yellow perch",bait="Bait allowed",closures="None listed")
SPOTS=[
dict(id="chain-lakes-reservoir",name="Chain Lakes Reservoir",area="Chain Lakes Provincial Park, west of Nanton",why="On Alberta's put-and-take trout stocking list, so catchable trout are stocked.",map="Chain Lakes Provincial Park, AB",src=PT,srcname="Put &amp; Take stocked lakes list (ES1)",**PTREG),
dict(id="mount-lorette-ponds",name="Mount Lorette Ponds",area="Kananaskis Country (Hwy 40)",why="Small, calm ponds with their own special stocked-pond rules. A good size for first casts.",map="Mount Lorette Ponds, Kananaskis, AB",src=L1,srcname="ES1 lakes table",season="Open all year",limits="2 trout total; 3 walleye, 3 pike, 15 perch",bait="Bait allowed (no bait fish)",closures="None listed"),
dict(id="sibbald-lake",name="Sibbald Lake",area="Kananaskis Country (Hwy 68, west of Calgary)",why="Stocked put-and-take trout lake.",map="Sibbald Lake, Kananaskis, AB",src=PT,srcname="Put &amp; Take stocked lakes list (ES1)",**PTREG),
dict(id="sibbald-meadows-pond",name="Sibbald Meadows Pond",area="Kananaskis Country (Hwy 68)",why="Stocked put-and-take trout pond.",map="Sibbald Meadows Pond, Kananaskis, AB",src=PT,srcname="Put &amp; Take stocked lakes list (ES1)",**PTREG),
dict(id="mclean-pond",name="McLean Pond",area="McLean Creek area, south of Bragg Creek",why="Stocked put-and-take trout pond.",map="McLean Pond, Kananaskis, AB",src=PT,srcname="Put &amp; Take stocked lakes list (ES1)",**PTREG),
dict(id="glenmore-reservoir",name="Glenmore Reservoir",area="Southwest Calgary",why="A big fishery right in the city, with a season that closes for winter.",map="Glenmore Reservoir, Calgary, AB",src=L1,srcname="ES1 lakes table",season="May 1 to Oct 31",limits="5 trout; 5 mountain whitefish over 30 cm; 3 pike; 15 perch",bait="Bait allowed (no bait fish)",closures="Closed Nov 1 to Apr 30"),
dict(id="wedge-pond",name="Wedge Pond",area="Kananaskis Country (Hwy 40)",why="A small pond for practising your cast. Trophy-only harvest, so it's mostly catch and release.",map="Wedge Pond, Kananaskis, AB",src=L1,srcname="ES1 lakes table",season="Open all year",limits="1 trout over 50 cm; 0 Arctic grayling",bait="Bait ban",closures="None listed"),
dict(id="lower-kananaskis-lake",name="Lower Kananaskis Lake",area="Peter Lougheed Provincial Park, Kananaskis",why="Big mountain lake. A good spot for older kids learning lure fishing.",map="Lower Kananaskis Lake, AB",src=L1,srcname="ES1 lakes table",season="Open all year (except the closed bay)",limits="1 trout total. Rainbow and cutthroat trout must be over 50 cm to keep.",bait="Bait ban",closures="Northwest bay closed all year"),
dict(id="upper-kananaskis-lake",name="Upper Kananaskis Lake",area="Peter Lougheed Provincial Park, Kananaskis",why="Mountain lake with day-use areas; mostly catch and release.",map="Upper Kananaskis Lake, AB",src=L1,srcname="ES1 lakes table",season="Open all year; within 100 m of Rawson Creek inlet open Jul 16 to May 31 only",limits="1 trout total. Rainbow and cutthroat trout must be over 50 cm to keep.",bait="Bait ban",closures="Rawson Creek inlet area closed Jun 1 to Jul 15"),
dict(id="sheep-river-regs",name="Sheep River",area="Turner Valley / Black Diamond (Diamond Valley) and upstream",why="The town's recommended family river. Catch and release for trout.",map="Sheep River, Diamond Valley, AB",src=RV,srcname="ES1 rivers table",season="Jun 16 to Oct 31 (open stretches)",limits="0 trout; 5 mountain whitefish over 30 cm (Gorge Creek down to the Highwood)",bait="Bait ban",closures="Indian Oils Day-use bridge down to Gorge Creek: closed all year"),
dict(id="highwood-river-regs",name="Highwood River",area="Kananaskis to High River and the Bow",why="Classic Foothills river. Our summary is above.",map="Highwood River, High River, AB",src=RV,srcname="ES1 rivers table",season="Mostly Jun 16 to Oct 31; varies by stretch",limits="Varies by stretch; see official regs",bait="Bait ban",closures="Storm Creek closed all year"),
]
# Card photos from Wikimedia Commons (photo_place_specific False = representative photo, labelled on the card)
PHOTOS={
 "chain-lakes-reservoir": {
  "photo": "images/act/fish-chain-lakes-reservoir.jpg",
  "photo_alt": "Chain Lakes Reservoir among grassy rolling foothills",
  "photo_credit": "Photo: Royalbroil, CC BY-SA 4.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Chain_Lakes_Reservoir_at_Chain_Lakes_Provincial_Park_from_Cowboy_Trail_AB22.jpg",
  "photo_license": "CC BY-SA 4.0",
  "photo_license_url": "https://creativecommons.org/licenses/by-sa/4.0",
  "photo_place_specific": True
 },
 "sibbald-lake": {
  "photo": "images/act/fish-sibbald-lake.jpg",
  "photo_alt": "A calm forest pond lined with spruce trees in Kananaskis Country",
  "photo_credit": "Photo: davebloggs007 (Flickr), CC BY 2.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Beaver_Ponds_kananaskis_country_Alberta_Canada_(9328001527).jpg",
  "photo_license": "CC BY 2.0",
  "photo_license_url": "https://creativecommons.org/licenses/by/2.0",
  "photo_place_specific": False
 },
 "sibbald-meadows-pond": {
  "photo": "images/act/fish-sibbald-meadows-pond.jpg",
  "photo_alt": "A beaver dam holding back a quiet pond in Kananaskis Country",
  "photo_credit": "Photo: davebloggs007 (Flickr), CC BY 2.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Beaver_ponds_Kananaskis_Alberta_Canada_(26589259893).jpg",
  "photo_license": "CC BY 2.0",
  "photo_license_url": "https://creativecommons.org/licenses/by/2.0",
  "photo_place_specific": False
 },
 "mclean-pond": {
  "photo": "images/act/fish-mclean-pond.jpg",
  "photo_alt": "Calm water of McLean Creek pond with spruce trees reflected",
  "photo_credit": "Photo: davebloggs007 (Flickr), CC BY 2.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Maclean_creek_pond_Alberta_Canada_(34039338134).jpg",
  "photo_license": "CC BY 2.0",
  "photo_license_url": "https://creativecommons.org/licenses/by/2.0",
  "photo_place_specific": True
 },
 "mount-lorette-ponds": {
  "photo": "images/act/fish-mount-lorette-ponds.jpg",
  "photo_alt": "Snowy path and footbridge at Mount Lorette Ponds below Mount Lorette",
  "photo_credit": "Photo: davebloggs007 (Flickr), CC BY 2.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Lorette_ponds_Kananaskis_Alberta_Canada_(32419821035).jpg",
  "photo_license": "CC BY 2.0",
  "photo_license_url": "https://creativecommons.org/licenses/by/2.0",
  "photo_place_specific": True
 },
 "glenmore-reservoir": {
  "photo": "images/act/fish-glenmore-reservoir.jpg",
  "photo_alt": "Sailboats on Glenmore Reservoir in Calgary under a blue sky",
  "photo_credit": "Photo: Qyd, CC BY-SA 3.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Glenmore_Reservoir_Calgary.JPG",
  "photo_license": "CC BY-SA 3.0",
  "photo_license_url": "http://creativecommons.org/licenses/by-sa/3.0/",
  "photo_place_specific": True
 },
 "wedge-pond": {
  "photo": "images/act/fish-wedge-pond.jpg",
  "photo_alt": "Sunrise peaks reflected in still Wedge Pond",
  "photo_credit": "Photo: Ltncanada, CC BY-SA 4.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Wedge_pond_AB_sunrise.jpg",
  "photo_license": "CC BY-SA 4.0",
  "photo_license_url": "https://creativecommons.org/licenses/by-sa/4.0",
  "photo_place_specific": True
 },
 "lower-kananaskis-lake": {
  "photo": "images/act/fish-lower-kananaskis-lake.jpg",
  "photo_alt": "Blue water of Lower Kananaskis Lake below snowy peaks",
  "photo_credit": "Photo: AvogadroK, CC BY-SA 4.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Lower_Kananaskis_Lake_02.jpg",
  "photo_license": "CC BY-SA 4.0",
  "photo_license_url": "https://creativecommons.org/licenses/by-sa/4.0",
  "photo_place_specific": True
 },
 "upper-kananaskis-lake": {
  "photo": "images/act/fish-upper-kananaskis-lake.jpg",
  "photo_alt": "Upper Kananaskis Lake seen between dark evergreens below mountains",
  "photo_credit": "Photo: davebloggs007 (Flickr), CC BY 2.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Upper_Kananaskis_Lake_(27628089273).jpg",
  "photo_license": "CC BY 2.0",
  "photo_license_url": "https://creativecommons.org/licenses/by/2.0",
  "photo_place_specific": True
 },
 "sheep-river-regs": {
  "photo": "images/act/fish-sheep-river.jpg",
  "photo_alt": "The Sheep River rushing through a rocky forested gorge",
  "photo_credit": "Photo: SaltedSturgeon, CC BY-SA 4.0",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Sheep_River,_Alberta.jpg",
  "photo_license": "CC BY-SA 4.0",
  "photo_license_url": "https://creativecommons.org/licenses/by-sa/4.0",
  "photo_place_specific": True
 },
 "highwood-river-regs": {
  "photo": "images/act/fish-highwood-river.jpg",
  "photo_alt": "The Highwood River flowing over gravel bars through forest in Kananaskis Country",
  "photo_credit": "Photo: Wheateater, Public domain",
  "photo_credit_url": "https://commons.wikimedia.org/wiki/File:Highwood_River_AB.JPG",
  "photo_license": "Public domain",
  "photo_license_url": "",
  "photo_place_specific": True
 }
}
for _s in SPOTS: _s.update(PHOTOS.get(_s["id"],{}))
