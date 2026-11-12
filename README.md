# 中岛美雪作品解读

中岛美雪（中島みゆき）歌曲的背景解读、中日对照翻译，以及面向日语初学者的逐句语法拆解。

## 目录结构

```
index.html          首页导航
songs.js            歌曲列表（新增歌曲时在这里加一项）
assets/             共用样式 site.css、图标、图片（miyuki.webp 是首页照片）
songs/<slug>/       每首歌一个子页面
```

## 新增歌曲

手动步骤：

1. 新建 `songs/<slug>/index.html`（目录里加 `<a href="../../">⌂ 首页</a>`，页脚写“第 N 首”）。
2. 在 `songs.js` 里加一项。
3. 提交并推送，Cloudflare 会自动重新部署。

## 部署

纯静态网站，无需构建。用 **Cloudflare Pages** 连接本仓库自动部署（推送到 main 即发布）：

- 网址：https://miyuki-essays.pages.dev
- Pages 设置：框架预设 None，构建命令留空，构建输出目录 `/`
- `_redirects` 把 README.md、CLAUDE.md 跳回首页，不对外展示

不要用 Cloudflare Workers（`*.workers.dev` 在中国大陆被封锁，`*.pages.dev` 可正常访问）。
