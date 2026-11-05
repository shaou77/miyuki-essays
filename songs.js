/*
 * 歌曲目录 —— 首页的卡片全部由这里生成。
 * 新增一首歌：
 *   1. 把解读页放到 songs/<slug>/index.html（slug 用英文/罗马字，小写、连字符）
 *   2. 在下面数组末尾加一项，no 顺延即可
 * ruby 写法与子页面一致：{漢字|かな}
 */
window.SONGS = [
  {
    no: 1, slug: "nisekino-fune",
    title: "{二隻|にせき}の{舟|ふね}", zh: "两叶孤舟", year: 1992,
    source: "专辑《EAST ASIA》· 舞台《夜会》主题曲",
    blurb: "《夜会》的灵魂之歌。两只船，即使分隔，也是一体：一出近七分钟的小小舞台剧。",
    tags: ["夜会", "海", "羁绊"]
  },
  {
    no: 2, slug: "east-asia",
    title: "EAST ASIA", zh: "东亚", year: 1992,
    source: "专辑《EAST ASIA》开篇曲",
    blurb: "镜头从“我与你”拉远到“我与我所在的这片土地”，视野辽阔的近七分钟长曲。",
    tags: ["土地", "家国", "弦乐"]
  },
  {
    no: 3, slug: "mabataki-mo-sezu",
    title: "{瞬|まばた}きもせず", zh: "目不转睛", year: 1998,
    source: "电影《学校III》主题曲",
    blurb: "写给被时代甩下、重新出发的普通人：就算世界不赞美你，我也要赞美你。",
    tags: ["电影", "人生", "鼓励"]
  },
  {
    no: 4, slug: "sejou",
    title: "{世情|せじょう}", zh: "人间冷暖", year: 1978,
    source: "专辑《愛していると云ってくれ》· 电视剧《3年B组金八先生》插曲",
    blurb: "学生运动退潮之后，一首冷眼看“世间”的歌。口号的浪潮，与想让时间停下的人。",
    tags: ["时代", "社会", "金八先生"]
  },
  {
    no: 5, slug: "utahime",
    title: "{歌姫|うたひめ}", zh: "歌姬", year: 1982,
    source: "专辑《寒水鱼》终曲",
    blurb: "深夜，一杯便宜的酒，一首歌姬的歌。长约八分钟的专辑终曲，副歌像潮水一次次涨上来。",
    tags: ["寒水鱼", "海", "歌者"]
  },
  {
    no: 6, slug: "headlight-taillight",
    title: "ヘッドライト・テールライト", zh: "前灯 · 尾灯", year: 2000,
    source: "NHK《Project X 挑战者们》片尾曲 · 专辑《短篇集》",
    blurb: "写给在现场埋头苦干的无名者：他们的名字也许被忘了，但旅途还没有结束。",
    tags: ["Project X", "旅途", "纪录片"]
  }
];
