#!/usr/bin/env python3
"""检查一首歌的解读页是否符合项目规范。

用法（在仓库根目录）：
    python3 .claude/skills/miyuki-song/scripts/check_song.py songs/<slug>/index.html
不带参数则检查 songs/ 下全部页面。只用 Python 标准库。
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
POS_OK = {"名", "动", "助", "副", "形", "代", "句型", "助动", "连体", "终助", "疑", "接续",
          "补助动", "句", "后缀", "な形", "数量", "接尾", "形动", "叹"}
RUBY = re.compile(r"\{([^|}]+)\|([^}]+)\}")
KANA = re.compile(r"^[぀-ヿー・]+$")


def songs_js_slugs():
    p = ROOT / "songs.js"
    if not p.exists():
        return {}
    txt = p.read_text(encoding="utf-8")
    return {m.group(2): int(m.group(1)) for m in re.finditer(r"no:\s*(\d+),\s*slug:\s*\"([^\"]+)\"", txt)}


def check(path):
    errs, warns = [], []
    s = pathlib.Path(path).read_text(encoding="utf-8")
    slug = pathlib.Path(path).parent.name

    if "{{" in s:
        errs.append("还有未替换的模板占位符 {{…}}")
    if s.count('<a href="../../">⌂ 首页</a>') < 2:
        errs.append("两处 <nav class=\"toc\"> 都要有 <a href=\"../../\">⌂ 首页</a>")
    m = re.search(r'<a href="\.\./\.\./">中岛美雪解读</a> · 第 (\d+) 首', s)
    if not m:
        errs.append("页脚缺少：<a href=\"../../\">中岛美雪解读</a> · 第 N 首")
    nums = songs_js_slugs()
    if slug not in nums:
        errs.append(f"songs.js 里没有 slug \"{slug}\" 这一项")
    elif m and int(m.group(1)) != nums[slug]:
        errs.append(f"页脚写第 {m.group(1)} 首，但 songs.js 里 no 是 {nums[slug]}")
    for needed in ('id="v-main"', 'id="v-study"', 'id="LY"', 'id="SD"', 'id="cheat"', 'id="bg"', 'id="lyrics"'):
        if needed not in s:
            errs.append(f"缺少元素 {needed}")

    dm = re.search(r"var D=(\[.*?\]);\s*\n", s, re.S)
    if not dm:
        errs.append("找不到 `var D=[...];`（必须单独成行并以 ; 结尾）")
        return errs, warns
    try:
        D = json.loads(dm.group(1))
    except json.JSONDecodeError as e:
        errs.append(f"D 不是合法 JSON（只能用双引号、不能有尾逗号）：{e}")
        return errs, warns

    seen, full = set(), set()
    nlines = 0
    for si, st in enumerate(D):
        if not (isinstance(st, list) and len(st) in (2, 3) and isinstance(st[0], str)):
            errs.append(f"第 {si+1} 段格式应为 [标题, [行…]] 或 [标题, [行…], true]")
            continue
        skip = len(st) == 3 and st[2] is True
        for l in st[1]:
            nlines += 1
            if len(l) != 8:
                errs.append(f"{l[0] if l else '?'}：每行必须正好 8 个元素，现在 {len(l)} 个")
                continue
            lid, ja, roma, zh, lit, words, gram, ref = l
            where = f"[{lid}]"
            if lid in seen:
                errs.append(f"{where} id 重复")
            seen.add(lid)
            if not zh.strip():
                errs.append(f"{where} 缺意译（第 4 项）")
            if "{" in RUBY.sub("", ja) or "}" in RUBY.sub("", ja):
                errs.append(f"{where} ruby 写法有误：{ja}")
            for kan, kana in RUBY.findall(ja):
                if not KANA.match(kana):
                    warns.append(f"{where} 注音「{kana}」不是纯假名")
            if ref:
                if ref not in full:
                    errs.append(f"{where} 引用 \"{ref}\" 不存在或不在它前面（只能引用前面有完整讲解的行）")
            else:
                if skip:
                    errs.append(f"{where} 所在段落标了 true（不进学习页），那么每行都必须有引用 id")
                if not roma.strip() or not lit.strip():
                    errs.append(f"{where} 完整讲解行需要罗马音和直译")
                if not words:
                    errs.append(f"{where} 单词表为空")
                if not gram:
                    warns.append(f"{where} 没有语法点")
                for w in words:
                    if len(w) != 4:
                        errs.append(f"{where} 单词项应为 [词, 读音, 词性, 释义]：{w}")
                    elif w[2] not in POS_OK:
                        warns.append(f"{where} 词性「{w[2]}」不在常用列表里")
                for g in gram:
                    if len(g) != 2:
                        errs.append(f"{where} 语法项应为 [标题, 说明]：{g}")
                full.add(lid)
    print(f"  {len(D)} 段，{nlines} 行，其中 {len(full)} 行有完整讲解")
    return errs, warns


def main():
    paths = sys.argv[1:] or sorted(str(p) for p in (ROOT / "songs").glob("*/index.html"))
    bad = 0
    for p in paths:
        print(f"== {p}")
        errs, warns = check(p)
        for w in warns:
            print("  ⚠", w)
        for e in errs:
            print("  ✗", e)
        if not errs:
            print("  ✓ 通过")
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
