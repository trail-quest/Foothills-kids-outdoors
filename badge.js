(function(){
var KEY='fko-scav-checks',BKEY='fko-scav-badge',GOAL=10;
var hunt=document.querySelector('.hunt');if(!hunt)return;
var items=hunt.querySelectorAll('ul li'),ul=hunt.querySelector('ul');
var saved={};try{saved=JSON.parse(localStorage.getItem(KEY))||{}}catch(e){}
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
hunt.classList.add('js-checks');ul.setAttribute('role','group');ul.setAttribute('aria-label','Scavenger hunt items, tap to check');
var status=document.createElement('p');status.className='hunt-status noprint';
status.innerHTML='<span class="hunt-count" aria-live="polite"></span> <button type="button" class="btn btn-small seebadge">🏅 See my badge</button>';
ul.parentNode.insertBefore(status,ul.nextSibling);
var count=status.querySelector('.hunt-count'),see=status.querySelector('.seebadge');
var ov=document.getElementById('bdg-overlay');
function n(){var c=0;items.forEach(function(li){if(li.getAttribute('aria-checked')==='true')c++});return c}
function update(){var c=n();count.textContent=c>=GOAL?'⭐ '+c+' found! You earned your Trail Explorer badge!':c+' of '+GOAL+' found';
 if(localStorage.getItem(BKEY))see.classList.add('on');}
function confetti(){if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
 var box=document.createElement('div');box.className='bdg-confetti';box.setAttribute('aria-hidden','true');
 var cols=['#ffb703','#52b788','#2d6a4f','#dda15e','#a8dadc','#e63946'];
 for(var i=0;i<70;i++){var p=document.createElement('i');p.style.left=Math.random()*100+'%';p.style.background=cols[i%cols.length];
  p.style.animationDuration=(1.8+Math.random()*1.8)+'s';p.style.animationDelay=(Math.random()*.6)+'s';box.appendChild(p)}
 document.body.appendChild(box);setTimeout(function(){box.remove()},4500)}
var last;
function open(party){last=document.activeElement;ov.hidden=false;document.body.style.overflow='hidden';ov.querySelector('.bdg-close').focus();if(party)confetti()}
function close(){ov.hidden=true;document.body.style.overflow='';see.classList.add('on');if(last&&last.focus)last.focus()}
items.forEach(function(li,i){li.setAttribute('role','checkbox');li.tabIndex=0;li.setAttribute('aria-checked',saved[i]?'true':'false');
 function toggle(){var on=li.getAttribute('aria-checked')!=='true';li.setAttribute('aria-checked',on);saved[i]=on;store(KEY,JSON.stringify(saved));
  if(n()>=GOAL&&!localStorage.getItem(BKEY)){store(BKEY,new Date().toISOString());update();open(true)}else update()}
 li.addEventListener('click',toggle);li.addEventListener('keydown',function(e){if(e.key===' '||e.key==='Enter'){e.preventDefault();toggle()}})});
see.addEventListener('click',function(){open(false)});
ov.querySelector('.bdg-close').addEventListener('click',close);
ov.querySelector('.bdg-done').addEventListener('click',close);
ov.addEventListener('click',function(e){if(e.target===ov)close()});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!ov.hidden)close()});
update();
})();
