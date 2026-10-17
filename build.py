#!/usr/bin/env python3
"""Gabungkan data/qa.json + template.html -> index.html (satu file, siap online)."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    data = json.load(open(os.path.join(HERE, "data", "qa.json"), encoding="utf-8"))
    meta, items = data["meta"], data["items"]
    keep = ("id", "q", "a", "p", "k", "s", "rd", "by", "d", "n", "kasus", "kw")
    items = [{k: e[k] for k in keep if k in e} for e in items]
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    js = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    for ph in ("/*__DATA__*/[]", "/*__META__*/{}"):
        if ph not in tpl:
            sys.exit(f"placeholder {ph} tidak ada di template")
    out = tpl.replace("/*__DATA__*/[]", js(items)).replace("/*__META__*/{}", js(meta))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
    print(f"index.html: {len(items)} entri, {len(out)/1024:.0f} KB")

if __name__ == "__main__":
    main()
