# 中岛美雪解读 · 给 Claude 的说明

这是一个纯静态网站（无构建）：中岛美雪歌曲的背景解读、中日对照翻译、面向日语初学者的逐句语法拆解。
用户 Nick 是日语初学者，所有内容用简体中文写。

## 目录

```
index.html                     首页（卡片由 songs.js 生成）
songs.js                       歌曲目录：新增歌曲在数组末尾加一项
assets/                        图标；放 assets/miyuki.jpg 可替换首页插画
songs/<slug>/index.html        每首歌一个解读页
.claude/skills/miyuki-song/    制作新歌解读页的完整工作流（SKILL.md）、模板、校验脚本
```

## 做新歌

**一律按 `.claude/skills/miyuki-song/SKILL.md` 的工作流来做**，从 `template.html` 复制开始，
不改动共用的 CSS 和渲染脚本，这样每首歌的风格才能保持一致。

要点速记：
- 歌词常是 UTF-16 的 .lrc：`iconv -f UTF-16 -t UTF-8`；里面自带的中文翻译不要用。
- 三部分：壹 创作背景与歌曲含义 / 贰 歌词中日对照（信达雅）/ 叁 跟着歌词学日语（独立视图）。
- 歌词数据写在页面底部的 `var D=[...]`（合法 JSON），每行 8 项；重复的句子用第 8 项引用第一次出现的 id。
- 前几首讲过的语法标“（回顾）”，查 `.claude/skills/miyuki-song/已讲语法索引.md`。
- 完成后：`python3 .claude/skills/miyuki-song/scripts/check_song.py songs/<slug>/index.html`
  和 `python3 .claude/skills/miyuki-song/scripts/grammar_index.py`，再提交推送（Cloudflare Pages 自动部署）。

## 已有歌曲

| 第 N 首 | 歌名 | slug |
|---|---|---|
| 1 | 二隻の舟 | nisekino-fune |
| 2 | EAST ASIA | east-asia |
| 3 | 瞬きもせず | mabataki-mo-sezu |
| 4 | 世情 | sejou |
| 5 | 歌姫 | utahime |
| 6 | ヘッドライト・テールライト | headlight-taillight |
