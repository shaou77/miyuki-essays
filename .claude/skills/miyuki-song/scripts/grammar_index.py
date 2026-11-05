#!/usr/bin/env python3
"""汇总已发布歌曲讲过的语法点，生成「已讲语法索引.md」，供新歌标注“回顾”。

用法（在仓库根目录）：
    python3 .claude/skills/miyuki-song/scripts/grammar_index.py
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = pathlib.Path(__file__).resolve().parents[1] / "已讲语法索引.md"
TAG = re.compile(r"<[^>]+>")

songs = re.findall(r"no:\s*(\d+),\s*slug:\s*\"([^\"]+)\",\s*title:\s*\"([^\"]+)\"",
                   (ROOT / "songs.js").read_text(encoding="utf-8"))
ruby = re.compile(r"\{([^|}]+)\|[^}]+\}")


def plain(x):
    return ruby.sub(lambda m: m.group(1), x).replace("<br>", " ")
out = ["# 已讲语法索引", "",
       "由 `scripts/grammar_index.py` 自动生成，请勿手改。新歌里再次出现下列语法时，标题后加“（回顾）”，",
       "并在说明里点出是哪首歌讲过的，例如“《二隻の舟》里讲过”。", ""]
for no, slug, title in sorted(songs, key=lambda x: int(x[0])):
    f = ROOT / "songs" / slug / "index.html"
    if not f.exists():
        continue
    s = f.read_text(encoding="utf-8")
    D = json.loads(re.search(r"var D=(\[.*?\]);\s*\n", s, re.S).group(1))
    out.append(f"## {no}. {plain(title)}（{slug}）")
    out.append("")
    for st in D:
        for l in st[1]:
            for g in l[6]:
                t = TAG.sub("", g[0]).strip()
                out.append(f"- {t}　〔{plain(l[1])}〕")
    out.append("")
OUT.write_text("\n".join(out), encoding="utf-8")
print(f"写入 {OUT}（{sum(1 for x in out if x.startswith('- '))} 条）")
