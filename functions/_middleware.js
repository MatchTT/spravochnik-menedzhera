// Вход на сайт по общему паролю.
// Пароль можно поменять в настройках Cloudflare Pages: переменная SITE_PASSWORD.
// Если переменная не задана, действует пароль ниже.
const DEFAULT_PASSWORD = 'pp-nbmr9gg2';
const COOKIE = 'spr_auth';

async function sha(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function loginPage(error) {
  return new Response(`<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Вход — Справочник менеджера</title>
<style>body{font-family:system-ui,sans-serif;background:#f6f6f7;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0;color:#18181b}
form{background:#fff;border:1px solid #e4e4e7;border-radius:14px;padding:28px;width:100%;max-width:340px}
h1{font-size:20px;margin:0 0 4px}p{color:#71717a;font-size:14px;margin:0 0 18px}
input{width:100%;box-sizing:border-box;padding:12px 14px;border:1px solid #e4e4e7;border-radius:10px;font-size:15px;margin-bottom:12px}
button{width:100%;padding:12px;border:none;border-radius:10px;background:#18181b;color:#fff;font-size:15px;cursor:pointer}
.err{color:#dc2626;font-size:13px;margin:-4px 0 12px}</style></head><body>
<form method="POST" action="/__login"><h1>Справочник менеджера</h1><p>PromoPult · Рег1. Введите пароль.</p>
${error ? '<div class="err">Неверный пароль</div>' : ''}
<input type="password" name="password" placeholder="Пароль" autofocus required>
<button type="submit">Войти</button></form></body></html>`, { status: 401, headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' } });
}

export async function onRequest(context) {
  const { request, env, next } = context;
  const password = env.SITE_PASSWORD || DEFAULT_PASSWORD;
  const token = await sha('spr:' + password);
  const url = new URL(request.url);

  // служебные файлы сайта наружу не отдаём
  if (url.pathname.startsWith('/_build') || url.pathname.startsWith('/functions') || url.pathname === '/README.md') {
    return new Response('Not found', { status: 404 });
  }

  if (url.pathname === '/__login' && request.method === 'POST') {
    const form = await request.formData();
    if (form.get('password') === password) {
      return new Response(null, { status: 303, headers: {
        'location': '/',
        'set-cookie': `${COOKIE}=${token}; Path=/; Max-Age=2592000; HttpOnly; Secure; SameSite=Lax`
      }});
    }
    return loginPage(true);
  }

  const cookies = request.headers.get('cookie') || '';
  if (cookies.split(/;\s*/).includes(`${COOKIE}=${token}`)) {
    return next();
  }
  return loginPage(false);
}
