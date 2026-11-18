ICONS = '''<svg style="display:none" aria-hidden="true">
<symbol id="i-head" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 14v-2a9 9 0 0 1 18 0v2"/><path d="M21 15a2 2 0 0 1-2 2h-1v-5h1a2 2 0 0 1 2 2z"/><path d="M3 15a2 2 0 0 0 2 2h1v-5H5a2 2 0 0 0-2 2z"/><path d="M18 17v1a3 3 0 0 1-3 3h-3"/></symbol>
<symbol id="i-doc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/></symbol>
<symbol id="i-gift" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></symbol>
<symbol id="i-cap" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 9 12 4 2 9l10 5 10-5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></symbol>
<symbol id="i-q" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14"/><path d="M12 17h.01"/></symbol>
<symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></symbol>
</svg>'''

SEARCH = '''<div class="search"><div class="search-box"><svg><use href="#i-search"/></svg><input id="q" placeholder="Поиск: «дорого», «промокод», «PBN», «недозвон»…" autocomplete="off"></div><div class="results" id="results"></div></div>'''

def page(title, body, faq=False, extra_js=''):
    js = '<script src="assets/app.js"></script>\n'
    if faq:
        js += '<script src="assets/faq.js"></script>\n'
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Справочник менеджера</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{ICONS}
<div class="wrap">
{body}
<div class="foot">Справочник менеджера PromoPult · Рег1</div>
</div>
{js}{extra_js}
</body>
</html>
'''

def say(t): return f'<div class="say">{t}</div>'
def ul(*items): return '<ul class="l">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def opt(b, t): return f'<div class="opt"><b>{b}</b>{t}</div>'
def opts(*o): return '<div class="opts">' + ''.join(o) + '</div>'
def step(n, title, inner):
    return f'<div class="step"><div class="num">{n}</div><div class="step-body"><div class="step-t">{title}</div>{inner}</div></div>'
def d(t): return f'<div class="step-d">{t}</div>'
def label(t): return f'<div class="label">{t}</div>'

SUPPORT = step('★', 'Если были обращения в поддержку',
    d('Перед звонком посмотреть обращения и понять, насколько они актуальны (свежие / старые).') +
    say('«Вижу, что вы обращались по вопросу [тема], коллеги помогли. Подскажите, всё ли было понятно?»') +
    say('«Вижу, что у вас есть вопрос по [тема]. Я уточню у коллег и вернусь к вам с обратной связью»') +
    say('«Вижу, что вы уже обратились в поддержку, коллеги занимаются вашим вопросом. Я со своей стороны проконтролирую»') +
    d('<b>Важно:</b> не дублируем поддержку, не уходим в технические детали, не решаем вопрос самостоятельно.'))

def algo(title, sub, goal, check, steps, rules, back='razdel-zvonki.html', back_t='Звонки'):
    out = f'<a class="back" href="{back}">← {back_t}</a>'
    out += f'<div class="head"><h1>{title}</h1><p>{sub}</p></div>'
    if goal: out += f'<div class="goal"><b>Цель:</b> {goal}</div>'
    if check: out += '<div class="box"><b>Перед звонком проверить</b><ul>' + ''.join(f'<li>{c}</li>' for c in check) + '</ul></div>'
    out += ''.join(steps)
    if rules: out += '<div class="box accent" style="margin-top:18px"><b>Ключевые правила</b><ul>' + ''.join(f'<li>{r}</li>' for r in rules) + '</ul></div>'
    return out
