from shell import *

def row(u, t, dsc):
    d = f'<div class="card-d">{dsc}</div>' if dsc else ''
    return f'<a class="card" href="{u}"><div><div class="card-t">{t}</div>{d}</div><span class="arrow">→</span></a>'

P = {}

P['index.html'] = ('Главная', f'''
<div class="head"><h1>Справочник менеджера</h1></div>
{SEARCH}
<div class="grid">
  <a class="card" href="razdel-zvonki.html"><svg><use href="#i-head"/></svg><div class="card-t">Звонки</div><div class="card-d">Алгоритмы по воронкам, статусы сделок, разбор звонков</div></a>
  <a class="card" href="razdel-messendzhery.html"><svg><use href="#i-chat"/></svg><div class="card-t">Мессенджеры</div><div class="card-d">Как написать первым, шаблоны, Salesbot, правила переписки</div></a>
  <a class="card" href="razdel-bonusy.html"><svg><use href="#i-gift"/></svg><div class="card-t">Бонусная программа</div><div class="card-d">Ставки, промокод <span data-b="code"></span>, калькулятор, вывод бонусов, агентства</div></a>
  <a class="card" href="voprosy.html"><svg><use href="#i-q"/></svg><div class="card-t">Вопросы и возражения</div><div class="card-d">Готовые ответы по всем темам с поиском</div></a>
</div>
''', True)

P['razdel-zvonki.html'] = ('Звонки', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Звонки</h1></div>
<div class="list">
{row('reg1.html','Алгоритм звонка PromoPult','')}
{row('vebinary.html','Звонки участникам вебинаров','')}
{row('pervyj-platezh.html','Алгоритм звонка — воронка «Заканчивается первый платеж»','')}
{row('otvaly.html','Алгоритм звонка — воронка «Отвалы»','')}
{row('pbn-ne-zapushen.html','Алгоритм звонка — воронка «PBN проект создан, но не запущен»','')}
{row('pbn-26-37.html','Алгоритм звонка — PBN (26 и 37 день)','')}
{row('obzvon-direkt-2025.html','Методичка: обзвон базы клиентов Яндекс Директ 2025','')}
{row('instr-statusy.html','Воронки и статусы — как работать правильно','')}
{row('obuchenie/razbor-zvonkov.html','Примеры хороших и слабых звонков','')}
{row('voprosy.html#t-objections','Возражения','')}
</div>
''')

P['razdel-messendzhery.html'] = ('Мессенджеры', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Мессенджеры</h1></div>
<div class="list">
{row('instr-pervym.html','Как написать первым — WhatsApp, Telegram, MAX','')}
{row('shablony-voronki.html','Шаблоны сообщений по воронкам','')}
{row('instr-salesbot.html','Salesbot: шаблоны в мессенджеры за один клик','')}
{row('shablony-salesbot.html','Шаблоны сообщений Salesbot для воронки рег.1','')}
{row('obuchenie/messendzhery.html','Работа в мессенджерах WhatsApp · Telegram · MAX','')}
</div>
''')

P['razdel-bonusy.html'] = ('Бонусная программа', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Бонусная программа</h1></div>
<a class="btn" href="https://promopult.ru/partners.html" target="_blank">Открыть калькулятор бонусов ↗</a>
<div class="list">
{row('bonus-stavki.html','Шпаргалка: ключевые факты','')}
{row('instr-vyvod.html','Как работает вывод бонусов — важно знать каждому','')}
{row('instr-agentstvo.html','Агентства — отдельные правила и статус','')}
{row('obuchenie/bonusnaya-programma.html','Бонусная программа PromoPult — обучение для менеджеров по продажам','')}
{row('voprosy.html#t-bonus','Вопросы про бонусы','')}
</div>
''')
