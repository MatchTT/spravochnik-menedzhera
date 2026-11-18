/* ============================================================
   ЦИФРЫ БОНУСНОЙ ПРОГРАММЫ — МЕНЯТЬ ТОЛЬКО ЗДЕСЬ.
   Они сами подставятся на все страницы сайта.
   ============================================================ */
var BONUS = {
  direct: 8,      // Яндекс Директ, максимум, %
  vk: 19,         // VK Реклама, максимум, %
  promo: 13,      // Промостраницы, максимум, %
  biz: 13,        // Яндекс Бизнес, максимум, %
  avito: 5,       // Авито, максимум, %
  code: 'PPDISC', // промокод
  days: 30,       // сколько дней действует промокод
  minus: 3        // на сколько п.п. ниже ставка без промокода
};

/* Страницы сайта — для поиска */
var PAGES = [
  {t:'Звонки', d:'Алгоритмы по воронкам, статусы, разбор звонков', u:'razdel-zvonki.html', k:'звонок алгоритм воронка скрипт'},
  {t:'Алгоритм звонка PromoPult', d:'Рег1, 11 шагов', u:'reg1.html', k:'рег1 регистрация новые новичок'},
  {t:'Звонки участникам вебинаров', d:'Рабочая шпаргалка', u:'vebinary.html', k:'вебинар запись эфир лид форма'},
  {t:'Алгоритм звонка — воронка «Заканчивается первый платеж»', d:'Звонки', u:'pervyj-platezh.html', k:'платеж баланс пополнение зак1 оплата счет'},
  {t:'Алгоритм звонка — воронка «Отвалы»', d:'Звонки', u:'otvaly.html', k:'отвал остановка возобновление минус отрицательный баланс'},
  {t:'Алгоритм звонка — воронка «PBN проект создан, но не запущен»', d:'Звонки', u:'pbn-ne-zapushen.html', k:'pbn пбн seo ссылки гарантия'},
  {t:'Алгоритм звонка — PBN (26 и 37 день)', d:'Звонки', u:'pbn-26-37.html', k:'pbn пбн 26 37 биллинг посуточный гарантия'},
  {t:'Методичка: обзвон базы клиентов Яндекс Директ 2025', d:'Звонки', u:'obzvon-direkt-2025.html', k:'директ 2025 реактивация база обзвон'},
  {t:'Воронки и статусы — как работать правильно', d:'Звонки', u:'instr-statusy.html', k:'статус fail принимают решение рег2 воронка amocrm'},
  {t:'Мессенджеры', d:'Как написать первым, шаблоны, Salesbot', u:'razdel-messendzhery.html', k:'мессенджер переписка whatsapp telegram max'},
  {t:'Как написать первым — WhatsApp, Telegram, MAX', d:'Мессенджеры', u:'instr-pervym.html', k:'whatsapp telegram max ватсап телеграм макс написать первым'},
  {t:'Шаблоны сообщений по воронкам', d:'Мессенджеры', u:'shablony-voronki.html', k:'шаблон сообщение текст'},
  {t:'Шаблоны сообщений Salesbot для воронки рег.1', d:'Мессенджеры', u:'shablony-salesbot.html', k:'salesbot салесбот бот недозвон шаблон'},
  {t:'Salesbot: шаблоны в мессенджеры за один клик', d:'Мессенджеры', u:'instr-salesbot.html', k:'salesbot салесбот бот запустить'},
  {t:'Бонусная программа', d:'Ставки, промокод, вывод, агентства', u:'razdel-bonusy.html', k:'бонус бонусная программа'},
  {t:'Шпаргалка: ключевые факты', d:'Бонусная программа', u:'bonus-stavki.html', k:'бонус ставка процент промокод ppdisc калькулятор'},
  {t:'Как работает вывод бонусов — важно знать каждому', d:'Бонусная программа', u:'instr-vyvod.html', k:'вывод бонусы баллы перевод карта деньги'},
  {t:'Агентства — отдельные правила и статус', d:'Бонусная программа', u:'instr-agentstvo.html', k:'агентство дискаунтер статус'},
  {t:'Вопросы и возражения', d:'Готовые ответы по всем темам', u:'voprosy.html', k:'вопрос ответ возражение'}
];

function fillBonus(){
  document.querySelectorAll('[data-b]').forEach(function(el){
    var v = BONUS[el.getAttribute('data-b')];
    if(v !== undefined) el.textContent = v;
  });
}

/* подставить цифры в текст: {direct} → 8 */
function bt(s){ return s.replace(/\{(\w+)\}/g, function(m,k){ return BONUS[k] !== undefined ? BONUS[k] : m; }); }

function copyText(btn, text){
  var done = function(){ btn.textContent = 'Скопировано'; btn.classList.add('done'); setTimeout(function(){ btn.textContent = 'Копировать'; btn.classList.remove('done'); }, 1500); };
  if(navigator.clipboard){ navigator.clipboard.writeText(text).then(done, function(){ fallback(); }); } else { fallback(); }
  function fallback(){ var ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); try{ document.execCommand('copy'); done(); }catch(e){} ta.remove(); }
}

function norm(s){ return (s||'').toLowerCase().replace(/ё/g,'е'); }

function initSearch(){
  var input = document.getElementById('q');
  var box = document.getElementById('results');
  if(!input || !box) return;
  input.addEventListener('input', function(){
    var q = norm(input.value.trim());
    if(q.length < 2){ box.classList.remove('on'); box.innerHTML = ''; return; }
    var words = q.split(/\s+/);
    var hit = function(text){ text = norm(text); return words.every(function(w){ return text.indexOf(w) > -1; }); };
    var out = [];
    PAGES.forEach(function(p){ if(hit(p.t+' '+p.d+' '+p.k)) out.push('<a href="'+p.u+'"><div class="r-t">'+p.t+'</div><div class="r-d">'+p.d+'</div></a>'); });
    if(typeof FAQ !== 'undefined'){
      FAQ.forEach(function(f,i){ if(hit(f.q+' '+bt(f.a)+' '+(f.k||''))) out.push('<a href="voprosy.html#v'+i+'"><div class="r-t">'+f.q+'</div><div class="r-d">'+f.topic+'</div></a>'); });
    }
    box.innerHTML = out.length ? out.slice(0,12).join('') : '<div class="empty">Ничего не нашлось. Попробуйте другое слово.</div>';
    box.classList.add('on');
  });
  input.addEventListener('keydown', function(e){
    if(e.key === 'Enter' && input.value.trim()){ try{ sessionStorage.setItem('q', input.value.trim()); }catch(err){} location.href = 'voprosy.html'; }
  });
  document.addEventListener('click', function(e){ if(!e.target.closest('.search')) box.classList.remove('on'); });
}

document.addEventListener('DOMContentLoaded', function(){ fillBonus(); initSearch(); });
