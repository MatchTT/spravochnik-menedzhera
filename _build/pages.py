from shell import *

P = {}

# ---------------- ГЛАВНАЯ ----------------
P['index.html'] = ('Главная', f'''
<div class="head"><h1>Справочник менеджера</h1><p>PromoPult · Рег1 — скрипты, инструкции и бонусы в одном месте</p></div>
{SEARCH}
<div class="grid">
  <a class="card" href="skripty.html"><svg><use href="#i-head"/></svg><div class="card-t">Скрипты продаж</div><div class="card-d">Алгоритмы звонков по воронкам</div></a>
  <a class="card" href="instrukcii.html"><svg><use href="#i-doc"/></svg><div class="card-t">Инструкции</div><div class="card-d">Как написать первым, статусы, вывод бонусов, агентства</div></a>
  <a class="card" href="bonusy.html"><svg><use href="#i-gift"/></svg><div class="card-t">Акции и бонусы</div><div class="card-d">Ставки, промокод <span data-b="code"></span>, калькулятор</div></a>
  <a class="card" href="shablony.html"><svg><use href="#i-chat"/></svg><div class="card-t">Шаблоны сообщений</div><div class="card-d">Salesbot после недозвона и мессенджеры по воронкам</div></a>
  <a class="card" href="obuchenie.html"><svg><use href="#i-cap"/></svg><div class="card-t">Обучение</div><div class="card-d">Бонусная программа, Рег1, мессенджеры, разбор звонков</div></a>
  <a class="card" href="voprosy.html"><svg><use href="#i-q"/></svg><div class="card-t">Вопросы и возражения</div><div class="card-d">Все ответы из обучений в одном месте</div></a>
</div>
<hr>
<h2 style="margin-top:0">Частые вопросы</h2>
<div class="faq" id="top-faq"></div>
<a class="more" href="voprosy.html">Все вопросы →</a>
''', True, '''<script>
document.addEventListener('DOMContentLoaded',function(){
  var box=document.getElementById('top-faq');
  FAQ.forEach(function(f,i){ if(!f.top) return;
    box.insertAdjacentHTML('beforeend','<details><summary>'+f.q+'</summary><div class="ans">'+bt(f.a)+'</div><div class="src">'+f.topic+(f.src?' · <a href="'+f.src.u+'">'+f.src.t+'</a>':'')+'</div></details>');
  });
});
</script>''')

# ---------------- СКРИПТЫ ----------------
def row(u,t,dsc): return f'<a class="card" href="{u}"><div><div class="card-t">{t}</div><div class="card-d">{dsc}</div></div><span class="arrow">→</span></a>'
P['skripty.html'] = ('Скрипты продаж', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Скрипты продаж</h1><p>Выбери воронку — откроется алгоритм звонка</p></div>
<div class="list">
{row('reg1.html','Рег1: новые регистрации','Зарегистрировался, но не запустил рекламу')}
{row('vebinary.html','Участники вебинаров','Выясняем задачу и первый шаг')}
{row('pervyj-platezh.html','Заканчивается первый платёж','На балансе осталось на несколько дней')}
{row('otvaly.html','Отвалы','Реклама остановилась, баланс не пополняется')}
{row('pbn-ne-zapushen.html','PBN: создан, но не запущен','Начал настраивать и остановился')}
{row('pbn-26-37.html','PBN: 26 и 37 день','Посуточное списание, проект не должен остановиться')}
{row('obzvon-direkt-2025.html','Обзвон базы Директ 2025','Запускали Директ через платформу в 2025 году и перестали')}
</div>
<h2>Ещё по звонкам</h2>
<div class="list">
{row('voprosy.html#t-objections','Возражения','«Дорого», «подумаю», «нет времени» — готовые ответы')}
{row('obuchenie/razbor-zvonkov.html','Примеры хороших и слабых звонков','Разбор по 6 шагам')}
</div>
''')

# ---------------- БОНУСЫ ----------------
P['bonus-stavki.html'] = ('Ставки и промокод', '''
<a class="back" href="razdel-bonusy.html">← Бонусная программа</a>
<div class="head"><h1>Ставки и промокод</h1><p>Главные цифры на одном экране</p></div>
<a class="btn" href="https://promopult.ru/partners.html" target="_blank">Открыть калькулятор бонусов ↗</a>
<div class="facts">
  <div class="fact"><div class="fact-t">VK Реклама</div><div class="fact-v">до <span data-b="vk"></span>%</div><div class="fact-d">максимальная ставка</div></div>
  <div class="fact"><div class="fact-t">Яндекс Директ</div><div class="fact-v">до <span data-b="direct"></span>%</div><div class="fact-d">максимальная ставка</div></div>
  <div class="fact"><div class="fact-t">Промостраницы</div><div class="fact-v">до <span data-b="promo"></span>%</div><div class="fact-d">максимальная ставка</div></div>
  <div class="fact"><div class="fact-t">Яндекс Бизнес</div><div class="fact-v">до <span data-b="biz"></span>%</div><div class="fact-d">максимальная ставка</div></div>
  <div class="fact"><div class="fact-t">Авито</div><div class="fact-v">до <span data-b="avito"></span>%</div><div class="fact-d">максимальная ставка</div></div>
  <div class="fact"><div class="fact-t">Без промокода</div><div class="fact-v">−<span data-b="minus"></span> п.п.</div><div class="fact-d">от максимальной ставки</div></div>
</div>
<div class="box warn"><b>Не путаем:</b> до <span data-b="vk"></span>% — только по VK. По Яндекс Директу максимум <span data-b="direct"></span>%.</div>

<h2>Промокод <span data-b="code"></span></h2>
<div class="box accent">Даёт максимальные ставки из таблицы на <span data-b="days"></span> дней с момента активации, независимо от оборота. Лучше активировать <b>прямо перед запуском</b>. После — стандартная ставка (на <span data-b="minus"></span> п.п. ниже).</div>
<div class="step"><div class="num">1</div><div class="step-body"><div class="step-t">Называйте как эксклюзив</div><div class="say">«У меня для вас есть промокод — он даёт максимальные ставки на <span data-b="days"></span> дней. Это <span data-b="code"></span>.»</div></div></div>
<div class="step"><div class="num">2</div><div class="step-body"><div class="step-t">Сразу назовите конкретную сумму</div><div class="step-d">Посчитайте на калькуляторе под бюджет клиента. Называйте годовую сумму — она производит больше впечатления.</div></div></div>
<div class="step"><div class="num">3</div><div class="step-body"><div class="step-t">Объясните, когда активировать</div><div class="say">«Промокод действует <span data-b="days"></span> дней с момента активации, поэтому его лучше активировать прямо перед самим запуском.»</div></div></div>

<h2>Почему без промокода ниже</h2>
<div class="box">Закон 479-ФЗ от 26.12.2024, ст. 18.2 «О рекламе»: с 1 апреля 2025 года площадки отчисляют государству 3% доходов с интернет-рекламы. PromoPult получает меньше — поэтому базовая ставка ниже. <b>Сами эту тему первыми не поднимаем</b> — отвечаем, только если клиент спросит, и переводим на промокод.</div>

<h2>Как продавать</h2>
<div class="say">«Вы и так тратите деньги на рекламу — почему бы не получать бонусы с каждого рубля? Это ничего не меняет в ваших кампаниях, просто делает рекламу дешевле.»</div>
<div class="box" style="margin-top:12px"><b>Квалификация — три вопроса</b><ul><li>«Вы запускаете контекстную рекламу или таргет?»</li><li>«Вы работаете напрямую через Яндекс / VK или через какой-то сервис?» — если напрямую, это самый горячий сценарий</li><li>«Какой примерно бюджет в месяц?» — чтобы посчитать сумму на калькуляторе</li></ul></div>

<h2>Правила</h2>
<div class="grid">
<div class="box ok" style="margin:0"><b>Делаем</b><ul><li>Рассказываем о бонусах каждому клиенту с рекламным бюджетом</li><li>При упоминании Директа или VK — сразу предлагаем с цифрами</li><li>Показываем калькулятор, называем конкретные суммы</li><li>Собираем контакты заинтересованных в бесшовном переносе</li></ul></div>
<div class="box warn" style="margin:0"><b>Не делаем</b><ul><li>Не называем бонусы «кэшбэком» или «живыми деньгами»</li><li>Не торгуемся: индивидуальных условий нет</li><li>Не переманиваем клиентов Клик.Ру</li><li>Не предлагаем прямой аккаунт тем, кто уже работает через PromoPult</li></ul></div>
</div>
''')

# ---------------- ИНСТРУКЦИИ ----------------
P['instrukcii.html'] = ('Инструкции', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Инструкции</h1><p>Как сделать в amoCRM и на платформе</p></div>
<div class="list">
{row('instr-pervym.html','Как написать клиенту первым','WhatsApp, Telegram, MAX из amoCRM')}
{row('instr-statusy.html','Статусы сделок','Когда «Принимают решение», когда Fail')}
{row('instr-vyvod.html','Вывод бонусов клиенту','Перевод баллов, реквизиты, 2–3 дня')}
{row('instr-agentstvo.html','Статус агентства','Критерии и как поставить')}
{row('instr-salesbot.html','Salesbot: как отправить шаблон','Если что-то не получается — пошагово со скриншотами')}
</div>
''')

P['instr-pervym.html'] = ('Как написать клиенту первым', '''
<a class="back" href="razdel-messendzhery.html">← Мессенджеры</a>
<div class="head"><h1>Как написать клиенту первым</h1></div>
<div class="box warn">В карточке сделки должен быть добавлен контакт с номером телефона клиента. Без этого написать первым не получится. Дубли не создаём — если клиент уже есть в системе, используем существующий контакт.</div>
<h3>WhatsApp</h3>
<div class="step"><div class="num">1</div><div class="step-body"><div class="step-d">Открываем сделку в amoCRM → переходим в чат с клиентом</div></div></div>
<div class="step"><div class="num">2</div><div class="step-body"><div class="step-d">Нажимаем на номер телефона клиента в карточке</div></div></div>
<div class="step"><div class="num">3</div><div class="step-body"><div class="step-d">Выбираем канал Promopult (+796...) — наш WhatsApp</div><img class="shot" src="img/wa-1.jpg" alt="Выбор канала в amoCRM" style="max-width:420px"></div></div>
<div class="step"><div class="num">4</div><div class="step-body"><div class="step-d">Пишем сообщение и отправляем. <a href="https://docs.radist.online/ru/%D0%BD%D0%B0%D1%88%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/amocrm/waba-amocrm/kak-pisat-pervym-ne-s-shablonnogo-soobsheniya-v-amocrm/" target="_blank" style="text-decoration:underline">Подробная инструкция ↗</a></div></div></div>
<h3>MAX и Telegram по номеру телефона</h3>
<div class="step-d" style="margin-bottom:8px">Так же, как WhatsApp: сделка → чат → номер телефона клиента → в списке выбираем канал MAX или Telegram → пишем и отправляем. Клиент получит сообщение по номеру телефона. Инструкции: <a href="https://docs.radist.online/ru/%D0%BD%D0%B0%D1%88%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/amocrm/max/" target="_blank" style="text-decoration:underline">MAX ↗</a> · <a href="https://docs.radist.online/ru/%D0%BD%D0%B0%D1%88%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/amocrm/telegram/" target="_blank" style="text-decoration:underline">Telegram ↗</a></div>
<h3>Telegram по нику (@username)</h3>
<div class="step"><div class="num">1</div><div class="step-body"><div class="step-d">Открываем сделку в amoCRM</div></div></div>
<div class="step"><div class="num">2</div><div class="step-body"><div class="step-d">В карточке контакта вводим ник клиента в формате @username в поле Telegram</div></div></div>
<div class="step"><div class="num">3</div><div class="step-body"><div class="step-d">Переходим в чат → выбираем Telegram-канал → пишем и отправляем. <a href="https://disk.360.yandex.ru/i/KOsrGeHoPLNfGg" target="_blank" style="text-decoration:underline">Видеоинструкция ↗</a> · <a href="https://docs.radist.online/ru/%D0%BD%D0%B0%D1%88%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/amocrm/telegram/kak-pisat-na-username-klienta-telegram-v-amocrm/" target="_blank" style="text-decoration:underline">Текстовая ↗</a></div></div></div>
<div class="box">Входящее сообщение клиента в любом мессенджере автоматически создаёт задачу в очереди amoCRM. Вручную ничего делать не нужно. Отвечаем в рабочее время в течение 15–30 минут.</div>
''')

P['instr-statusy.html'] = ('Статусы сделок', '''
<a class="back" href="razdel-zvonki.html">← Звонки</a>
<div class="head"><h1>Статусы сделок</h1></div>
<table>
<tr><th>Ситуация</th><th>Статус</th></tr>
<tr><td>Пополнил баланс</td><td><b>Успех</b> — ставится автоматически, вручную не ставим</td></tr>
<tr><td>Есть интерес, баланс не пополнен</td><td>Остаётся в <b>Рег2</b>, дожимаем</td></tr>
<tr><td>Нецелевой, но диалог был и помогли</td><td><b>Принимают решение</b></td></tr>
<tr><td>Объективный отказ или недозвон</td><td><b>Fail</b></td></tr>
</table>
<div class="box"><b>«Принимают решение»</b> — диалог состоялся, задача услышана, рассказали о платформе или направили презентацию, дальнейшие звонки не планируются. Подходит, если клиент:<ul><li>изучает, а не покупает: студент, сотрудник конкурента</li><li>решал разовую техническую задачу</li><li>зарегистрировался ради реферальной программы</li><li>запустил только бесплатный инструмент (биддер, мониторинг позиций)</li><li>«динамо»: минимум 3 звонка, всё обещает и ничего не делает, или попросил больше не звонить</li></ul></div>
<div class="box warn">Нельзя ставить «Принимают решение» «на всякий случай», если не дошли до финала и не знаете, что думает клиент. Это незавершённый звонок. «Подумаю» без даты = отказ, который мы не зафиксировали.</div>
<div class="box"><b>Fail — нормально:</b> технический недозвон (несколько попыток, номер недоступен, автоответчик), обрыв в начале разговора, объективный отказ (нет бизнеса, сайта, бюджета; бизнес закрывается).<br><b>Fail — плохо:</b> нецелевому не рассказали о платформе и просто слили; клиент сказал «просто посмотреть», а менеджер не докопался до задачи. Сначала попытка — рассказал о платформе, направил презентацию — и только потом Fail.</div>
<div class="box"><b>Воронка «Сделать первый звонок после воронки 0».</b> Клиент попадает сюда через сутки после статуса «Объяснено, ждём запуск». Не знакомим заново — уточняем, что остановило: «[Имя], мы разговаривали в [день]. Скажите — что остановило от запуска? Давайте разберём прямо сейчас и сделаем первый шаг». Единственный целевой результат — пополнение баланса.</div>
''')

P['instr-vyvod.html'] = ('Вывод бонусов клиенту', '''
<a class="back" href="razdel-bonusy.html">← Бонусная программа</a>
<div class="head"><h1>Вывод бонусов клиенту</h1></div>
<div class="box warn">Прямой вывод на карту недоступен — Яндекс запрещает выплачивать вознаграждение конечным рекламодателям. Поэтому говорим «бонусы» и «баллы», не «кэшбэк». Вернуть бонусы обратно на баланс PromoPult тоже нельзя.</div>
<div class="opts" style="margin-bottom:12px"><div class="opt"><b>Вариант 1. </b>Пополнить рекламный кабинет WB Продвижение — доступно прямо в интерфейсе. Предлагаем селлерам в первую очередь.</div><div class="opt"><b>Вариант 2. </b>Перевод баллов на наш аккаунт → деньги на реквизиты клиента за 2–3 дня, без комиссий.</div></div>
<div class="say">«У вас накопились бонусы — отлично. Вывести их можно через обмен с другим пользователем нашей системы: вы переводите баллы на аккаунт, а вам отправляют деньги. Я подскажу нужный аккаунт — это займёт пару минут.»</div>
<div class="step"><div class="num">1</div><div class="step-body"><div class="step-t">Передать клиенту ID нашего аккаунта</div><div class="step-d">Уточнить сумму баллов для перевода. Клиент делает перевод в разделе вывода: «Перевод баллов сторонним пользователям».</div></div></div>
<div class="step"><div class="num">2</div><div class="step-body"><div class="step-t">Убедиться, что клиент сделал перевод</div><div class="step-d">Если не написал в течение дня — напомнить: «Как прошёл перевод? Если нужна помощь с интерфейсом — подскажу пошагово». Не ждать пассивно.</div></div></div>
<div class="step"><div class="num">3</div><div class="step-body"><div class="step-t">Получить реквизиты и передать на обработку</div><div class="step-d">Сумма, ID отправителя, реквизиты клиента (карта, WebMoney и т.д.).</div></div></div>
<div class="step"><div class="num">4</div><div class="step-body"><div class="step-t">Подтвердить получение</div><div class="step-d">Через 2–3 дня: «Деньги пришли? Всё в порядке?»</div></div></div>
<div class="box">Кнопки WebMoney и Мир в разделе вывода у конечного клиента выводят только реферальный доход, не партнёрские бонусы. Исключение — агентства.</div>
''')

P['instr-agentstvo.html'] = ('Статус агентства', '''
<a class="back" href="razdel-bonusy.html">← Бонусная программа</a>
<div class="head"><h1>Статус агентства</h1></div>
<div class="box accent">Агентству Яндекс разрешает делиться вознаграждением напрямую — у него открыт прямой вывод на WebMoney, карту и другие способы, без перевода баллов.</div>
<div class="box"><b>Три критерия</b><ul><li>Минимум 3 прямых аккаунта Яндекс Директа — заведённых именно через PromoPult</li><li>Нет одного доминирующего бюджета (нельзя 90 000 ₽ на один сайт и по 5 000 на два «для галочки»)</li><li>Есть страница или сайт агентства — хотя бы промостраница, где указано, что ИП / ООО / физлицо оказывает услуги по контекстной рекламе</li></ul></div>
<div class="step"><div class="num">1</div><div class="step-body"><div class="step-d">Клиент присылает подтверждение: название, сайт/страница, три клиента у нас. <b>Сохранить это сообщение.</b></div></div></div>
<div class="step"><div class="num">2</div><div class="step-body"><div class="step-d">Профиль пользователя → «Прочие параметры» → «Дискаунтер-тип» → «Агентство». Делает только администратор.</div></div></div>
<div class="step"><div class="num">3</div><div class="step-body"><div class="step-d">У клиента открывается прямой вывод. Цель проверки — не уличить клиента, а формально соблюсти процедуру на случай проверки Яндекса.</div></div></div>
''')

P['instr-salesbot.html'] = ('Salesbot: как отправить шаблон', '''
<a class="back" href="razdel-messendzhery.html">← Мессенджеры</a>
<div class="head"><h1>Salesbot: как отправить шаблон</h1></div>
<div class="box accent">Боты — только для недозвона (кроме «ВБ · инструкции», он отправляется после разговора). Сразу после первого недозвона отправляем шаблон по недозвону. Бот сам подставит имя клиента и ваше имя.</div>
<div class="box warn"><b>Строго по порядку:</b> сначала контакт, потом чат. Если просто добавить номер и сразу искать бота, Salesbot в списке не появится.</div>
<div class="step"><div class="num">1</div><div class="step-body"><div class="step-t">Добавьте контакт</div><div class="step-d">В сделке нажмите «Добавить контакт» и впишите номер телефона. В поле имени — только имя с большой буквы, например «Ирина». Имя берём то, что клиент указал при регистрации.</div>
<div class="opts"><div class="opt"><b>Имя есть и корректное → </b>вписываем. Сообщение придёт именное: «Ирина, добрый день!»</div><div class="opt"><b>Имени нет, оно на английском или странное (логин, почта, набор символов) → </b>поле оставляем пустым. Сообщение придёт без имени.</div></div></div></div>
<div class="step"><div class="num">2</div><div class="step-body"><div class="step-t">Откройте чат</div><div class="step-d">Внизу сделки нажмите на синее слово «Примечание» и выберите «Чат».</div><img class="shot" src="img/salesbot-1.webp" alt="Меню: Чат, E-mail, Примечание, Задача"></div></div>
<div class="step"><div class="num">3</div><div class="step-body"><div class="step-t">Выберите Salesbot</div><div class="step-d">Появится «Чат для …». Нажмите на эту надпись и в блоке «Боты» выберите Salesbot.</div><img class="shot" src="img/salesbot-2.webp" alt="Блок Боты → Salesbot"></div></div>
<div class="step"><div class="num">4</div><div class="step-body"><div class="step-t">Нажмите стрелочку ˅</div><div class="step-d">Рядом с «Чат для Salesbot».</div><img class="shot" src="img/salesbot-3.webp" alt="Стрелочка справа от Salesbot"></div></div>
<div class="step"><div class="num">5</div><div class="step-body"><div class="step-t">Выберите шаблон</div><div class="step-d">Сначала мессенджер, потом сценарий. Например, «/WA· Обратный звонок». Какой выбрать — <a href="shablony-salesbot.html" style="text-decoration:underline">таблица в Шаблонах</a>.</div><img class="shot" src="img/salesbot-4.webp" alt="Список шаблонов"></div></div>
<div class="step"><div class="num">6</div><div class="step-body"><div class="step-t">Нажмите «Запуск» и проверьте статус</div><div class="step-d">Через несколько секунд в ленте сделки появится синее сообщение «SalesBot (название бота)».</div><img class="shot" src="img/salesbot-5.webp" alt="Сообщение доставлено">
<div class="opts"><div class="opt"><b>✓ Доставлено — </b>всё хорошо, клиент получил сообщение.</div><div class="opt"><b>Ошибка — </b>мессенджер не принял сообщение. Пробуем следующий мессенджер.<img class="shot" src="img/salesbot-6.webp" alt="Ошибка" style="max-width:260px"></div><div class="opt"><b>Не видно сообщения — </b>обновите страницу (F5). Запускать бота повторно не нужно.</div></div></div></div>
<div class="box"><b>Правила отправки</b><ul><li>Пишем в один мессенджер, не во все сразу</li><li>Шаблон выбираем по ситуации клиента</li><li>В имя контакта — только имя, без фамилии, компании, почты или ника</li><li>Есть вопрос или не хватает бота — приходите к Лилии с предложениями</li></ul></div>
''')

# ---------------- ОБУЧЕНИЕ ----------------
P['obuchenie.html'] = ('Обучение', f'''
<a class="back" href="index.html">← Главная</a>
<div class="head"><h1>Обучение</h1><p>Полные версии обучений</p></div>
<div class="list">
{row('obuchenie/voronka-reg1.html','Работа с воронкой Рег1','Алгоритм, типы клиентов, возражения, разбор 922 звонков, статусы')}
{row('obuchenie/bonusnaya-programma.html','Бонусная программа PromoPult','Как продавать, примеры расчёта, возражения, вывод бонусов, агентства')}
{row('obuchenie/messendzhery.html','Работа в мессенджерах','Правила переписки, сценарии касаний, шаблоны, приоритеты каналов')}
{row('obuchenie/razbor-zvonkov.html','Примеры хороших и слабых звонков','Разбор по 6 ключевым шагам')}
</div>
''')

for _k in ('index.html','skripty.html','instrukcii.html','obuchenie.html'):
    P.pop(_k, None)
