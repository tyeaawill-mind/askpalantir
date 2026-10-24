import re, os, html, sys
sys.path.insert(0, "/home/claude/game")
import importlib, bank
importlib.reload(bank)
PAGES = "/home/claude/site/pages"

def norm(s):
    s = html.unescape(s).lower()
    for a, b in [("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u00a0", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()

def page_text(slug):
    p = os.path.join(PAGES, slug + ".html")
    if not os.path.exists(p):
        return None
    c = open(p).read()
    m = re.search(r"<article>(.*?)</article>", c, re.DOTALL)
    body = m.group(1) if m else c
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.DOTALL)
    return norm(re.sub(r"<[^>]+>", " ", body))

cache = {}
bad = 0
for f in bank.F:
    t = cache.setdefault(f["src"], page_text(f["src"]))
    if t is None:
        print("MISSING PAGE:", f["id"], f["src"]); bad += 1; continue
    for e in f["ev"]:
        if norm(e) not in t:
            print("EVIDENCE NOT FOUND:", f["id"], "|", f["src"], "|", e); bad += 1
print(f"checked {len(bank.F)} facts, {bad} problems")
