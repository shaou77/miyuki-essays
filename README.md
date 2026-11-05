# 中岛美雪作品解读

中岛美雪（中島みゆき）歌曲的背景解读、中日对照翻译，以及面向日语初学者的逐句语法拆解。

## 目录结构

```
index.html          首页导航
songs.js            歌曲列表（新增歌曲时在这里加一项）
assets/             图标、图片（放入 assets/miyuki.jpg 可替换首页插画）
songs/<slug>/       每首歌一个子页面
```

## 新增歌曲

完整工作流、页面模板和校验脚本在 `.claude/skills/miyuki-song/`。在本仓库里打开 Claude Code，说“用 miyuki-song 技能做《歌名》，歌词在 xxx.lrc”即可。手动步骤：

1. 新建 `songs/<slug>/index.html`（目录里加 `<a href="../../">⌂ 首页</a>`，页脚写“第 N 首”）。
2. 在 `songs.js` 里加一项。
3. 提交并推送，Cloudflare Pages 会自动重新部署。

## 部署

纯静态网站，无需构建。Cloudflare Pages 连接本仓库：构建命令留空，输出目录填 `/`。
