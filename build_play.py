import re, os, json, html, sys
sys.path.insert(0, "/home/claude/game")
import bank
SITE = "/home/claude/site"

# slug -> title, for the "Source:" links
titles = {}
for fn in os.listdir(f"{SITE}/pages"):
    c = open(f"{SITE}/pages/{fn}").read()
    m = re.search(r"<title>(.*?) \| Ask Palantir</title>", c)
    titles[fn[:-5]] = html.unescape(m.group(1)) if m else fn[:-5]
for f in bank.F:
    assert f["src"] in titles, f["src"]

data = json.dumps({"facts": bank.F, "titles": titles}, ensure_ascii=False).replace("</", "<\\/")
js = open("/home/claude/game/play_js.txt").read()
import datetime, os
_d = datetime.datetime.strptime(os.environ["EPOCH"], "%Y-%m-%d") if os.environ.get("EPOCH") else datetime.datetime.utcnow()
js = js.replace("__EPOCH__", f"{_d.year}, {_d.month-1}, {_d.day}")
print("epoch (puzzle #1):", _d.date())

css = """
<style>
.game-article{max-width:640px}
.game{margin:1.2rem 0 1.6rem}
.g-card{background:#fff;border:1px solid var(--rule,#DCE1E8);border-radius:12px;padding:1.4rem 1.3rem 1.5rem}
.g-kicker{font-family:var(--mono,monospace);font-size:.78rem;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-soft,#51607a);margin:0 0 .7rem}
.g-big{font-size:1.45rem;font-weight:700;line-height:1.25;margin:0 0 .6rem}
.g-statement{font-size:1.25rem;line-height:1.4;font-weight:600;margin:.9rem 0 1.1rem}
.g-choices{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
.g-btn{font:inherit;font-weight:700;min-height:52px;padding:.7rem 1rem;border-radius:9px;border:2px solid var(--ink,#16233A);background:#fff;color:var(--ink,#16233A);cursor:pointer}
.g-btn small{font-weight:400;opacity:.7}
.g-btn:focus-visible{outline:3px solid var(--accent,#C40410);outline-offset:2px}
.g-btn:hover:not(:disabled){background:#f1f4f8}
.g-primary{background:var(--accent,#C40410);border-color:var(--accent,#C40410);color:#fff}
.g-primary:hover:not(:disabled){background:#a8030d}
.g-btn:disabled{cursor:default}
.g-choice.is-right{border-color:#1e7a46;background:#e7f4ec;color:#14532d}
.g-choice.is-wrong{border-color:var(--accent,#C40410);background:#fdecee;color:#8f0310}
.g-choice:disabled:not(.is-right):not(.is-wrong){opacity:.55}
.g-feedback{margin-top:1rem}
.g-feedback p{margin:.5rem 0}
.g-verdict{font-weight:700}
.g-verdict.ok{color:#14532d}.g-verdict.bad{color:#8f0310}
.g-source{font-size:.92rem}
.g-hint{font-size:.85rem;color:var(--ink-soft,#51607a);margin:1rem 0 0}
.g-progress{display:flex;gap:.4rem;margin:0 0 .4rem}
.g-dot{width:2.2rem;height:.5rem;border-radius:3px;background:#dce1e8}
.g-dot.ok{background:#1e7a46}.g-dot.bad{background:var(--accent,#C40410)}.g-dot.cur{background:var(--ink,#16233A)}
.g-score{font-size:2.6rem;font-weight:800;line-height:1;margin:.2rem 0 .5rem}
.g-grid{font-size:1.6rem;letter-spacing:.15rem;margin:.2rem 0 .8rem}
.g-streak{font-weight:600}
.g-share{background:#f4f6f9;border:1px solid var(--rule,#DCE1E8);border-radius:8px;padding:.7rem .8rem;white-space:pre-wrap;font-size:.9rem;margin:.8rem 0}
.g-copied{font-size:.9rem;color:#14532d}
.g-next,.g-brush,.g-more{margin:.8rem 0 0}
.g-review{margin:1rem 0 0}
.g-review summary{cursor:pointer;font-weight:600}
.g-item{border-top:1px solid var(--rule,#DCE1E8);margin-top:.8rem;padding-top:.6rem}
.g-item p{margin:.35rem 0}
.g-item-head{font-weight:600}
.game-note{font-size:.92rem;color:var(--ink-soft,#51607a)}
@media (max-width:480px){.g-choices{grid-template-columns:1fr}.g-feedback .g-primary{width:100%}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>
"""

main = f"""<main>
  <p class="eyebrow">Daily game</p>
  <article class="game-article">
    <h1>Daily Palantir Fact-or-Fiction</h1>
    <p class="lede">Five statements about documented Palantir facts. Decide whether each is fact or fiction, and every answer links to the source article. A new set arrives each day.</p>
    <div id="game" class="game"><noscript><p>This game needs JavaScript. In the meantime, <a href="index.html">browse the articles</a>.</p></noscript></div>
    <p class="game-note">Questions cover documented facts only: dates, figures, contracts, and attributed statements. They never ask you to rule on contested questions such as whether Palantir is ethical. Your streak and results are stored only in this browser. See the <a href="privacy-policy.html">Privacy Policy</a>.</p>
  </article>
  <script type="application/json" id="bank">{data}</script>
  <script>
{js}
  </script>
</main>"""

page = open(f"{SITE}/faq.html").read()
page = re.sub(r"<script type=\"application/ld\+json\">.*?</script>\s*", "", page, flags=re.DOTALL)
page = re.sub(r"<title>.*?</title>", "<title>Daily Palantir Fact-or-Fiction | Ask Palantir</title>", page, count=1)
page = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="A 30-second daily game: five true-or-false statements about documented Palantir facts, each linked to its source. Keep your streak and share your score.">', page, count=1)
page = page.replace('https://askpalantir.com/faq.html', 'https://askpalantir.com/play.html')
page = page.replace("reflect-arc-faq", "reflect-arc-play")
page = re.sub(r"<main>.*?</main>", lambda m: main, page, count=1, flags=re.DOTALL)
page = page.replace("</head>", css + "</head>", 1)
open(f"{SITE}/play.html", "w").write(page)
print("play.html:", len(page), "bytes;", len(bank.F), "facts")
