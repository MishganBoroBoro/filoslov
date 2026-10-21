#!/usr/bin/env python3
"""Сборка сайта «Филослова» для GitHub Pages: главная, политика конфиденциальности, поддержка.

Политика берётся из ../AppStore/privacy-policy.md — правьте её там и пересобирайте:
    python3 build.py
"""
import pathlib
import markdown

ROOT = pathlib.Path(__file__).parent
POLICY = ROOT.parent / "AppStore" / "privacy-policy.md"
EMAIL = "mishganboroboro@gmail.com"

CSS = """
:root { --bg:#070b14; --bg2:#0d1526; --card:#111b30; --fg:#eef2fa; --muted:#9aa7bf; --gold:#f2c86b; --line:#22304d; }
* { box-sizing:border-box; }
html { -webkit-text-size-adjust:100%; }
body { margin:0; background:linear-gradient(180deg,var(--bg),var(--bg2)) fixed; color:var(--fg);
  font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif; }
a { color:var(--gold); }
.wrap { max-width:880px; margin:0 auto; padding:24px max(18px,env(safe-area-inset-left)) 64px; }
header.top { display:flex; align-items:center; flex-wrap:wrap; gap:12px; padding:8px 0 24px; }
header.top img { width:40px; height:40px; border-radius:10px; }
header.top a.brand { color:var(--fg); text-decoration:none; font-weight:800; font-size:20px; letter-spacing:-.01em; }
header.top nav { margin-left:auto; display:flex; gap:18px; font-size:15px; flex-wrap:wrap; }
header.top nav a { color:var(--muted); text-decoration:none; }
header.top nav a[aria-current] { color:var(--fg); }
.hero { display:grid; grid-template-columns:1.1fr .9fr; gap:32px; align-items:center; padding:24px 0 40px; }
.hero h1 { font-size:clamp(34px,6vw,52px); line-height:1.05; margin:0 0 14px; font-weight:900; letter-spacing:-.02em; text-wrap:balance; }
.hero h1 em { font-style:normal; color:var(--gold); }
.hero p { color:var(--muted); font-size:18px; margin:0 0 22px; max-width:46ch; }
.badge { display:inline-block; padding:12px 22px; border-radius:999px; background:#fff; color:#000; font-weight:700; text-decoration:none; }
.badge.soon { background:rgba(255,255,255,.12); color:var(--fg); }
.hero img { width:100%; max-width:300px; justify-self:center; border-radius:28px; box-shadow:0 20px 60px rgba(242,200,107,.18); }
.features { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin:8px 0 40px; }
.features div { background:var(--card); border:1px solid var(--line); border-radius:18px; padding:18px; }
.features b { display:block; margin-bottom:4px; }
.features span { color:var(--muted); font-size:15px; }
.shots { display:flex; gap:14px; overflow-x:auto; padding-bottom:8px; scroll-snap-type:x mandatory; }
.shots img { width:220px; flex:none; border-radius:22px; scroll-snap-align:start; border:1px solid var(--line); }
.doc { background:var(--card); border:1px solid var(--line); border-radius:20px; padding:8px 26px 26px; }
.doc h1 { font-size:28px; line-height:1.2; margin:24px 0 8px; }
.doc h2 { font-size:20px; margin:28px 0 8px; }
.doc table { width:100%; border-collapse:collapse; font-size:15px; display:block; overflow-x:auto; }
.doc th, .doc td { text-align:left; vertical-align:top; padding:8px 10px; border-bottom:1px solid var(--line); }
.doc th { color:var(--muted); font-weight:600; }
.doc hr { border:0; border-top:1px solid var(--line); margin:36px 0; }
.mail { font-size:20px; font-weight:700; user-select:all; }
footer { color:var(--muted); font-size:14px; margin-top:48px; border-top:1px solid var(--line); padding-top:18px; }
@media (max-width:720px) {
  header.top nav { margin-left:0; width:100%; gap:16px; font-size:14px; }
  .hero { grid-template-columns:1fr; } .hero img { max-width:240px; order:-1; }
  .features { grid-template-columns:1fr; } .doc { padding:4px 16px 18px; }
}
"""

def page(title, active, body, description="Филослов — филворды на русском для iPhone: 50 новых полей каждый день, рейтинг и наставник."):
    depth = "" if active == "home" else "../"
    items = [("home", depth or "./", "Игра"), ("privacy", depth + "privacy/", "Конфиденциальность"),
             ("support", depth + "support/", "Поддержка")]
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{href}"{cur if key == active else ""}>{label}</a>' for key, href, label in items)
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="color-scheme" content="dark">
<link rel="icon" href="{depth}img/icon.png">
<link rel="apple-touch-icon" href="{depth}img/apple-touch-icon.png">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <img src="{depth}img/icon.png" alt="">
  <a class="brand" href="{depth or './'}">Филослов</a>
  <nav>{nav}</nav>
</header>
{body}
<footer>© 2026 Боровинских Ольга Сергеевна · «Филослов» · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</div>
</body>
</html>
"""

HOME = f"""
<section class="hero">
  <div>
    <h1>Филворды, которые <em>радуются вместе с вами</em></h1>
    <p>Соединяйте буквы в слова. Каждый день — 50 новых полей, одни для всех, от простого к сложному. Набирайте очки, поднимайтесь в рейтинге и открывайте стили.</p>
    <span class="badge soon">Скоро в App Store</span>
  </div>
  <img src="img/03_mentor.jpg" alt="Экран победы: наставник в молниях и огне радуется решённому полю">
</section>
<section class="features">
  <div><b>50 филвордов дня</b><span>Обновляются каждый вечер в 19:00 по Москве. Чем дальше, тем сложнее и тем больше очков.</span></div>
  <div><b>Четыре наставника</b><span>Мыслитель, мастер кунг-фу, учёный монах и жрец радуются победам, у каждого своя подсказка и ульта.</span></div>
  <div><b>Шут Пиррон</b><span>Каждое пятое поле — бой с боссом: он прячет длину слов, выжигает клетки, подсовывает обманки и хохочет над ошибками.</span></div>
  <div><b>Рейтинг дня и недели</b><span>Game Center покажет ваше место и «топ X%». Топ-1% открывает «Легенду».</span></div>
</section>
<section class="shots" aria-label="Скриншоты">
  <img src="img/01_daily.jpg" alt="Главный экран: 50 филвордов дня в трёх этапах">
  <img src="img/03_mentor.jpg" alt="Наставник радуется победе">
  <img src="img/09_boss.jpg" alt="Бой с боссом: Шут Пиррон">
  <img src="img/08_ult.jpg" alt="Ульта наставника на поле «Вершины»">
  <img src="img/07_mentors.jpg" alt="Мастер кунг-фу — один из четырёх наставников">
  <img src="img/04_rating.jpg" alt="Рейтинг дня: топ-2%">
  <img src="img/06_legend.jpg" alt="Экран ачивки «Легенда»">
</section>
"""

SUPPORT = f"""
<div class="doc">
<h1>Поддержка</h1>
<p>Вопрос, идея, ошибка или неуместная реклама — напишите нам, ответим в течение нескольких дней:</p>
<p class="mail">{EMAIL}</p>
<p>Пожаловаться на рекламу можно и прямо в игре: <b>Настройки → «Пожаловаться на рекламу»</b>. Опишите, что было в объявлении.</p>
<h2>Частые вопросы</h2>
<h2>Как собирать слова?</h2>
<p>Проведите пальцем по соседним буквам — по горизонтали или вертикали, с поворотами. Отпустите палец, и слово засчитается, если оно спрятано на поле. Каждая буква принадлежит ровно одному слову.</p>
<h2>Когда появляются новые «Филворды дня»?</h2>
<p>Каждый вечер в 19:00 по Москве — сразу 50 полей, одни для всех игроков. Поля открываются по порядку, каждое решается один раз.</p>
<h2>Как считаются очки?</h2>
<p>За каждую клетку поля — 40 очков, умноженных на этап дня (×1 для полей 1–20, ×1,25 для 21–40, ×1,5 для 41–50) и на скорость (до ×2 быстрее нормы). Неверные слова, подсказки и ульта немного снижают результат.</p>
<h2>Кто такой Шут Пиррон?</h2>
<p>Злодей «Филослова». Каждое пятое поле дня (5, 10 … 50) — бой с ним, всего 10 боёв. Он прячет длину слов и выжигает клетки — буква под огнём не видна, а с каждым боем добавляет проказы: слова-обманки, зеркальное поле, сожжённые подсказки, раскалённые клетки. Найденное слово и подсказка гасят огонь. Расстановка одинакова у всех игроков.</p>
<h2>Что такое ульта наставника?</h2>
<p>Шкала силы копится найденными буквами. С 80% ульту можно взять за ролик, на 100% — бесплатно; после неё шкала сгорает. Одна ульта на поле. У «Филвордов дня» своя шкала и своя копилка подсказок.</p>
<h2>Не вижу себя в рейтинге</h2>
<p>Рейтинг ведёт Game Center. Войдите в него в <b>Настройках iPhone → Game Center</b> и откройте экран «Рейтинг» в игре — очки, набранные без интернета, отправятся автоматически.</p>
<h2>Пропал прогресс</h2>
<p>Прогресс хранится только на iPhone. Если удалить игру, он удаляется вместе с ней; рекорды в Game Center сохраняются.</p>
<h2>Можно без рекламы?</h2>
<p>Игра бесплатная, её поддерживает реклама. Первая игра — без межстраничной рекламы, ролики за подсказку вы включаете сами.</p>
<p><a href="../privacy/">Политика конфиденциальности</a></p>
</div>
"""

def main():
    (ROOT / "index.html").write_text(page("Филослов — филворды для iPhone", "home", HOME), encoding="utf-8")
    md = POLICY.read_text(encoding="utf-8").replace("# Filoslov Privacy Policy (English)", '<a id="en"></a>\n\n# Filoslov Privacy Policy (English)')
    policy = markdown.markdown(md, extensions=["tables"])
    body = '<p><a href="#en">English version</a></p><div class="doc">' + policy + "</div>"
    (ROOT / "privacy").mkdir(exist_ok=True)
    (ROOT / "privacy" / "index.html").write_text(
        page("Политика конфиденциальности — Филослов", "privacy", body), encoding="utf-8")
    (ROOT / "support").mkdir(exist_ok=True)
    (ROOT / "support" / "index.html").write_text(page("Поддержка — Филослов", "support", SUPPORT), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("")
    print("ok")

if __name__ == "__main__":
    main()
