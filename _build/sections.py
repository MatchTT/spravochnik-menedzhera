from shell import *

def row(u, t, dsc):
    return f'<a class="card" href="{u}"><div><div class="card-t">{t}</div><div class="card-d">{dsc}</div></div><span class="arrow">→</span></a>'

P = {}

P['index.html'] = ('Главная', f'''
<div class="head"><h1>Справочник менеджера</h1><p>PromoPult · Рег1 — всё для работы в одном месте</p></div>
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
<div class="head"><h1>Звонки</h1><p>Выбери воронку — откроется алгоритм звонка</p></div>
<h2 style="margin-top:0">Алгоритмы по воронкам</h2>
<div class="list">
{row('reg1.html','Рег1: новые регистрации','Зарегистрировался, но не запустил рекламу')}
{row('vebinary.html','Участники вебинаров','Выясняем задачу и первый шаг')}
{row('pervyj-platezh.html','Заканчивается первый платёж','На балансе осталось на несколько дней')}
{row('otvaly.html','Отвалы','Реклама остановилась, баланс не пополняется')}
{row('pbn-ne-zapushen.html','PBN: создан, но не запущен','Начал настраивать и остановился')}
{row('pbn-26-37.html','PBN: 26 и 37 день','Посуточное списание, проект не должен остановиться')}
{row('obzvon-direkt-2025.html','Обзвон базы Директ 2025','Запускали Директ через платформу в 2025 году и перестали')}
</div>
<h2>После звонка и для развития</h2>
<div class="list">
{row('voprosy.html#t-objections','Возражения','«Дорого», «подумаю», «нет времени» — готовые ответы')}
{row('instr-statusy.html','Статусы сделок','Когда «Принимают решение», когда Fail')}
{row('obuchenie/razbor-zvonkov.html','Примеры хороших и слабых звонков','Разбор по 6 шагам')}
</div>
''')

P['razdel-messendzhery.html'] = ('Мессенджеры', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Мессенджеры</h1><p>WhatsApp, Telegram, MAX и Salesbot</p></div>
<div class="list">
{row('instr-pervym.html','Как написать клиенту первым','WhatsApp, Telegram, MAX из amoCRM')}
{row('shablony-voronki.html','Шаблоны сообщений по воронкам','Рег1, отвалы, первый платёж, Wildberries — скопировать и отправить')}
{row('shablony-salesbot.html','Salesbot: какой шаблон отправить после недозвона','Таблица «ситуация → бот» и тексты, которые получит клиент')}
{row('instr-salesbot.html','Salesbot: как запустить бота','Если что-то не получается — пошагово со скриншотами')}
{row('obuchenie/messendzhery.html','Обучение: работа в мессенджерах','Полная версия — правила переписки, сценарии касаний, приоритеты каналов')}
</div>
''')

P['razdel-bonusy.html'] = ('Бонусная программа', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Бонусная программа</h1><p>Ставки, промокод, вывод бонусов, агентства</p></div>
<a class="btn" href="https://promopult.ru/partners.html" target="_blank">Открыть калькулятор бонусов ↗</a>
<div class="list">
{row('bonus-stavki.html','Ставки и промокод '+'<span data-b="code"></span>','Главные цифры, как продавать, что делаем и не делаем')}
{row('instr-vyvod.html','Вывод бонусов клиенту','Перевод баллов, реквизиты, 2–3 дня')}
{row('instr-agentstvo.html','Статус агентства','Критерии и как поставить')}
{row('voprosy.html#t-bonus','Вопросы про бонусы','Перенос аккаунта, кредитная линия, закон о 3%')}
{row('obuchenie/bonusnaya-programma.html','Обучение: бонусная программа','Полная версия — примеры расчёта, скрипты, возражения')}
</div>
''')
