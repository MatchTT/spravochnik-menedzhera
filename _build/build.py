import sys
sys.path.insert(0, '/home/claude/build')
from shell import page, SEARCH
import algos, pages, shablony, sections, verbatim

OUT = '/home/claude/site/'

VOPROSY_BODY = f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Вопросы и возражения</h1><p>Ответы из всех обучений и памяток. Ищите по слову или выберите тему.</p></div>
{SEARCH.replace('id="q"','id="fq"').replace('id="results"','id="fres"')}
<div class="tags" id="tags"></div>
<div class="faq" id="list"></div>
'''
VOPROSY_JS = '''<script>
document.addEventListener('DOMContentLoaded',function(){
  var topic='', q='';
  var h=location.hash.slice(1);
  if(h.indexOf('t-')===0){ var ix=TOPIC_IDS.indexOf(h.slice(2)); if(ix>-1) topic=TOPICS[ix]; }
  try{ q=sessionStorage.getItem('q')||''; sessionStorage.removeItem('q'); }catch(err){}
  var inp=document.getElementById('fq'); inp.value=q;
  var tags=document.getElementById('tags');
  tags.innerHTML=['Все'].concat(TOPICS).map(function(t){return '<button data-t="'+(t==='Все'?'':t)+'">'+t+'</button>';}).join('');
  function render(){
    tags.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-t')===topic);});
    var words=norm(inp.value.trim()).split(/\\s+/).filter(Boolean);
    var html='', last='';
    TOPICS.forEach(function(tp){
      if(topic && tp!==topic) return;
      FAQ.forEach(function(f,i){
        if(f.topic!==tp) return;
        var text=norm(f.q+' '+bt(f.a)+' '+(f.k||''));
        if(!words.every(function(w){return text.indexOf(w)>-1;})) return;
        if(last!==tp){ html+='<div class="topic-h">'+tp+'</div>'; last=tp; }
        html+='<details id="v'+i+'"><summary>'+f.q+'</summary><div class="ans">'+bt(f.a)+'</div>'+(f.src?'<div class="src">Источник: <a href="'+f.src.u+'">'+f.src.t+'</a></div>':'')+'</details>';
      });
    });
    document.getElementById('list').innerHTML=html||'<p style="color:var(--text2);margin-top:12px">Ничего не нашлось. Попробуйте другое слово или тему «Все».</p>';
    if(location.hash.indexOf('#v')===0){var el=document.querySelector(location.hash); if(el){el.open=true; el.scrollIntoView({block:'center'});}}
  }
  tags.onclick=function(e){var b=e.target.closest('button'); if(!b) return; topic=b.getAttribute('data-t'); render();};
  inp.oninput=render;
  render();
});
</script>'''

ALL = {}
for mod in (algos, pages, shablony, sections, verbatim):
    for fn, v in mod.P.items():
        ALL[fn] = v
ALL['voprosy.html'] = ('Вопросы и возражения', VOPROSY_BODY, True, VOPROSY_JS)

for fn, v in ALL.items():
    title, body = v[0], v[1]
    faq = v[2] if len(v) > 2 else False
    js = v[3] if len(v) > 3 else ''
    if 'id="q"' in body and not faq:
        faq = True  # поиск по вопросам нужен везде, где есть строка поиска
    open(OUT + fn, 'w', encoding='utf-8').write(page(title, body, faq, js))
    print('ok', fn)
