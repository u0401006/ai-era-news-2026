#!/usr/bin/env python3
"""Build AI時代的新聞工作 deck — v2, driven by the Google Drive MD source.

Outputs: presentation.html (single-file, references ./assets/ via symlink).
"""
import base64
from pathlib import Path
from urllib.parse import quote

OUT = Path(__file__).parent
LOGO_PATH = Path("/Users/capo/.claude/skills/cna-medialab-presentation/assets/中央通訊社全藍.png")
ASSETS = "./assets"


def media(fn: str) -> str:
    return f"{ASSETS}/{quote(fn, safe='')}"


logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")

# ============================================================
# Slide definitions — mapped from the MD outline
# ============================================================
YELLOW = "#F4CC2F"

SLIDES = [
    # 0. Title
    {
        "kind": "title",
        "title": "AI 時代的<br><span class='hl'>新聞工作</span>",
        "subtitle": "當機器也能寫稿、生圖、上字幕",
        "footer": "中央社媒體實驗室 · 2026 海外特派員營",
    },
    # 1. Opening video
    {
        "kind": "video-hero",
        "src": media("jiming_opening.mp4"),
        "title": "大家好",
        "speaker": "志明主播開場。讓 AI 自己說 hello。",
    },

    # ─── Part 1 ───
    {"kind": "divider", "num": "Part 1", "title": "AI 大浪來了<br>媒體受衝擊"},

    # 少時不讀書長大當記者 (section hook)
    {
        "kind": "text",
        "eyebrow": "自嘲",
        "title": "少時不讀書<br>長大當記者",
        "body": "——如今這句話還成立嗎？",
    },

    # 2026年，不好的開局 — 四個裁員數字 2x2
    {
        "kind": "number-grid",
        "title": "2026 年<br>不好的開局",
        "cards": [
            {"num": "300", "label": "Washington Post",
             "body": "華郵裁編採人員<br>關體育版、圖書版<br>撤中東、印澳駐外"},
            {"num": "2,000", "label": "BBC",
             "body": "裁約 1,800–2,000 人<br>10 人中 1 人離職<br>2 年省新台幣 214 億"},
            {"num": "17,163", "label": "美國媒體 2025",
             "body": "LAT、NBC、CBS 輪番清算<br>廣告下降、受眾轉社群"},
            {"num": "關鍵+TVBS", "label": "台灣",
             "body": "內容農場潮退<br>電視台也開始縮編"},
        ],
    },

    # 完蛋了，這些職業都要失業啦 — 圖 + 迪士尼 bullet
    {
        "kind": "image-with-bullet",
        "src": media("AI_job_replace.png"),
        "title": "完蛋了<br>這些職業都要失業啦",
        "caption": "翻譯蹲完記者蹲，記者蹲完工程師蹲",
        "bullet": {
            "label": "迪士尼 / Snap",
            "body": "迪士尼裁 1,000 人，漫威裁員 8%；Snap 母公司裁 16%——理由都是「AI 快速發展」",
        },
    },

    # 其實，我更忙了 (DW)
    {
        "kind": "image",
        "src": media("DW_ai.png"),
        "title": "其實，我更忙了",
        "caption": "德國之聲 AI 發展主管的現場分享",
    },

    # AI 熱詞
    {
        "kind": "tags",
        "title": "AI 熱詞<br>你聽過幾個？",
        "groups": [
            ("對話式", ["ChatGPT", "Claude", "Gemini", "Grok", "Perplexity"]),
            ("生成式", ["Midjourney", "Nano Banana", "Seedance"]),
            ("開發向", ["Copilot", "Vibe Coding", "Claude Code", "Agentic Coding", "Harness Coding"]),
            ("內部生態", ["OpenClaw", "Hermes Agent"]),
        ],
    },

    # ─── Part 2 ───
    {"kind": "divider", "num": "Part 2", "title": "你的識讀能力<br>幾級？"},

    # Literacy
    {
        "kind": "text",
        "eyebrow": "li·te·ra·cy",
        "title": "古老的這個字",
        "body": "過去是「識字」——讀得懂文。<br>現在是<span class='hl'>獲取、理解、創造、傳達</span>資訊的綜合能力。<br>媒體識讀、金融知識、電腦素養，都是它的延伸。",
    },

    # 這張照片哪裡怪 1 — 總統年輕化
    {
        "kind": "compare2",
        "title": "這張照片哪裡怪？<br><small>同一個 prompt，兩年差距</small>",
        "left": {"src": media("a_younger_president_in_the_white_house_oval_office_2024.png"), "label": "2024"},
        "right": {"src": media("a_younger_president_in_the_white_house_oval_office_2026.png"), "label": "2026"},
        "speaker": "模型對「年輕總統」的腦中印象正在改變。我們沒察覺。",
    },

    # 凱特王妃 context + 2 圖
    {
        "kind": "compare2-with-context",
        "title": "這張照片哪裡怪？",
        "context": "凱特王妃術後首張官方照疑遭修改，<span class='hl'>美聯、路透、法新</span>等多家媒體撤稿。原意在平息公眾對凱特健康情形的臆測，卻引來更多紛擾——撤圖主因：修改幅度過大、有數位改造痕跡。未有跡象顯示照片為偽造。",
        "left": {"src": media("kate1.png"), "label": "官方發布照"},
        "right": {"src": media("kate2.jpg"), "label": "被標出的修圖處"},
    },

    # ─── Part 3 ───
    {"kind": "divider", "num": "Part 3", "title": "新聞倫理的新課題<br><small>這樣可以嗎？</small>"},

    # 這樣可以嗎 · 一 TVBS
    {
        "kind": "image",
        "src": media("TVBS.jpg"),
        "title": "這樣可以嗎 · 一",
        "caption": "做得出來的請舉手——媒體用 AI 生成當主圖",
    },

    # 這樣可以嗎 · 二 櫻花
    {
        "kind": "compare2",
        "title": "這樣可以嗎 · 二",
        "left": {"src": media("sakura.png"), "label": "有一個小 mark"},
        "right": {"src": media("sakura-gen.png"), "label": "我只是想要⋯⋯對焦"},
        "speaker": "手機上一鍵美化，連新聞攝影都要問一次「這還算真實嗎？」",
    },

    # 這樣可以嗎 · 三 原況照片
    {
        "kind": "video",
        "src": media("realtime-photo.mov"),
        "title": "這樣可以嗎 · 三",
        "caption": "仔細看——它長高了。iPhone 原況照片也能被改造",
    },

    # 理解 LLM 原理
    {
        "kind": "image",
        "src": media("WhatsLLM.png"),
        "title": "理解 LLM 的原理",
        "caption": "你一定要知道——它是接龍引擎",
    },

    # 它哪天說不定幫你個大忙
    {
        "kind": "image",
        "src": media("dirty-data.png"),
        "title": "它哪天說不定<br>幫你個大忙",
        "caption": "Garbage In, Garbage Out——餵它什麼，就吐出什麼",
    },

    # ─── Part 4 (MD typo: labeled Part3) ───
    {"kind": "divider", "num": "Part 4", "title": "中央社媒體實驗室的<br>AI 應用"},

    # 比賽就是這樣 metaphor
    {
        "kind": "text",
        "eyebrow": "比喻",
        "title": "比賽就是這樣",
        "body": "好像跑步、游泳一樣——<br>還不是你做什麼，他就做什麼？<br><br><span class='hl'>但全球華文媒體</span>，用過飛鴿傳書又用過 AI 的，<br>只有<span class='hl'>中央社</span>。",
    },

    # 志明編輯助手 + context
    {
        "kind": "video-with-context",
        "src": media("jiming_combine.mp4"),
        "title": "志明編輯助手",
        "context": "以往不同新聞領域、不同語種的新聞，需要不同職務的人處理。<br>但是——有了助手？",
        "caption": "綜合外電報導？交給志明",
    },

    # Agents 時代
    {
        "kind": "video",
        "src": media("agent-line.mp4"),
        "title": "Agents 時代來臨",
        "caption": "組一張圖，你還先開 Photoshop？",
    },

    # 零點擊 1/3 fake
    {
        "kind": "video",
        "src": media("fake.mov"),
        "title": "零點擊時代 · 1/3",
        "caption": "假流量示範——機器觀看、機器分享、機器留言",
    },

    # 零點擊 2/3 AskCNA
    {
        "kind": "video",
        "src": media("AskCNA.mov"),
        "title": "零點擊時代 · 2/3",
        "caption": "Ask CNA——把 40 年社稿資料庫變成對話介面",
    },

    # 零點擊 3/3 cna-mcp
    {
        "kind": "image",
        "src": media("cna-mcp.png"),
        "title": "零點擊時代 · 3/3",
        "caption": "在 Claude、ChatGPT 就能直接問中央社",
    },

    # ─── 結語 ───
    {"kind": "divider", "num": "結 語", "title": "新聞的未來？"},

    # 民主社會可以沒有新聞嗎？
    {
        "kind": "image-big-question",
        "src": media("AI_combo.png"),
        "title": "民主社會<br>可以沒有<span class='hl'>新聞</span>嗎？",
        "caption": "記者在現場",
    },

    # 學習在 AI 時代，你的準備是什麼
    {
        "kind": "text",
        "eyebrow": "準 備",
        "title": "學習在 AI 時代<br>你的準備是什麼？",
    },

    # 要不要學程式 (1)
    {
        "kind": "image-with-lead",
        "src": media("mav_council_3.png"),
        "title": "要不要學程式？",
        "lead": "至少，你要<span class='hl'>會問 AI</span>。問哪個？",
        "caption": "小孩子才做選擇，我全都問",
    },

    # 要不要學程式 (2)
    {
        "kind": "image-with-lead",
        "src": media("mav_council-ojisan.png"),
        "title": "要不要學程式？",
        "lead": "Prompt: 仿照間諜家家酒的三大角色，把臉改成中年男子",
        "caption": "世界萬物皆有名字，有名字才能開始",
    },

    # 大叔說教時間 — 魔法論 + ending
    {
        "kind": "image-with-lead",
        "src": media("ending.png"),
        "title": "大叔說教時間",
        "lead": "所謂的魔法就是<span class='hl'>想像</span>的世界——<br>無法想像的事情就無法用「魔法」重現　⇐ AI",
        "caption": "參加「我是海外特派員」，增廣見聞",
    },

    # End slide
    {
        "kind": "text",
        "big": True,
        "title": "動手用 AI<br>才是<span class='hl'>識讀</span>的開始",
        "subtitle": "Q & A · Thank you",
        "footer": "中央社媒體實驗室 · Media Lab",
    },
]


# ============================================================
# Renderer
# ============================================================
def render_slide(idx: int, s: dict) -> str:
    k = s["kind"]
    notes = s.get("speaker", "")
    notes_html = f'<div class="speaker-notes">{notes}</div>' if notes else ""

    if k == "title":
        return f'''<section class="slide s-title" data-idx="{idx}">
  <div class="brand-mark"><img src="data:image/png;base64,{logo_b64}" alt="CNA"></div>
  <h1>{s["title"]}</h1>
  <p class="subtitle">{s.get("subtitle","")}</p>
  <div class="tag">{s.get("footer","")}</div>
  {notes_html}
</section>'''

    if k == "divider":
        return f'''<section class="slide s-divider" data-idx="{idx}">
  <div class="divider-num">{s["num"]}</div>
  <h2 class="divider-title">{s["title"]}</h2>
  {notes_html}
</section>'''

    if k == "text":
        eyebrow = f'<div class="eyebrow">{s["eyebrow"]}</div>' if s.get("eyebrow") else ""
        body = f'<p class="body">{s["body"]}</p>' if s.get("body") else ""
        sub = f'<p class="subtitle">{s["subtitle"]}</p>' if s.get("subtitle") else ""
        footer = f'<div class="tag">{s["footer"]}</div>' if s.get("footer") else ""
        big = " big" if s.get("big") else ""
        return f'''<section class="slide s-text{big}" data-idx="{idx}">
  {eyebrow}<h2>{s["title"]}</h2>{body}{sub}{footer}
  {notes_html}
</section>'''

    if k == "image":
        cap = f'<p class="caption">{s["caption"]}</p>' if s.get("caption") else ""
        title = f'<h2>{s["title"]}</h2>' if s.get("title") else ""
        return f'''<section class="slide s-image" data-idx="{idx}">
  {title}
  <figure><img src="{s["src"]}" alt=""></figure>
  {cap}
  {notes_html}
</section>'''

    if k == "video":
        cap = f'<p class="caption">{s["caption"]}</p>' if s.get("caption") else ""
        title = f'<h2>{s["title"]}</h2>' if s.get("title") else ""
        return f'''<section class="slide s-video" data-idx="{idx}">
  {title}
  <figure><video src="{s["src"]}" controls preload="metadata" playsinline></video></figure>
  {cap}
  {notes_html}
</section>'''

    if k == "video-hero":
        return f'''<section class="slide s-video-hero" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <figure><video src="{s["src"]}" controls preload="metadata" playsinline></video></figure>
  {notes_html}
</section>'''

    if k == "compare2":
        l, r = s["left"], s["right"]
        return f'''<section class="slide s-compare" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <div class="compare-grid">
    <figure><img src="{l["src"]}" alt=""><figcaption>{l["label"]}</figcaption></figure>
    <figure><img src="{r["src"]}" alt=""><figcaption>{r["label"]}</figcaption></figure>
  </div>
  {notes_html}
</section>'''

    if k == "compare2-with-context":
        l, r = s["left"], s["right"]
        return f'''<section class="slide s-compare ctx" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <p class="context">{s["context"]}</p>
  <div class="compare-grid">
    <figure><img src="{l["src"]}" alt=""><figcaption>{l["label"]}</figcaption></figure>
    <figure><img src="{r["src"]}" alt=""><figcaption>{r["label"]}</figcaption></figure>
  </div>
  {notes_html}
</section>'''

    if k == "number-grid":
        cards = "".join(
            f'<div class="ncard"><div class="ncard-num">{c["num"]}</div><div class="ncard-label">{c["label"]}</div><div class="ncard-body">{c["body"]}</div></div>'
            for c in s["cards"]
        )
        return f'''<section class="slide s-numgrid" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <div class="ncards">{cards}</div>
  {notes_html}
</section>'''

    if k == "image-with-bullet":
        b = s["bullet"]
        return f'''<section class="slide s-img-bullet" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <div class="img-bullet">
    <figure><img src="{s["src"]}" alt=""><figcaption>{s.get("caption","")}</figcaption></figure>
    <aside><div class="aside-label">{b["label"]}</div><p>{b["body"]}</p></aside>
  </div>
  {notes_html}
</section>'''

    if k == "image-with-lead":
        return f'''<section class="slide s-img-lead" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <p class="lead">{s.get("lead","")}</p>
  <figure><img src="{s["src"]}" alt=""></figure>
  <p class="caption">{s.get("caption","")}</p>
  {notes_html}
</section>'''

    if k == "video-with-context":
        return f'''<section class="slide s-video ctx" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <p class="context">{s["context"]}</p>
  <figure><video src="{s["src"]}" controls preload="metadata" playsinline></video></figure>
  <p class="caption">{s.get("caption","")}</p>
  {notes_html}
</section>'''

    if k == "image-big-question":
        return f'''<section class="slide s-bigq" data-idx="{idx}">
  <figure class="bg"><img src="{s["src"]}" alt=""></figure>
  <div class="overlay">
    <h2>{s["title"]}</h2>
    <p class="caption">{s.get("caption","")}</p>
  </div>
  {notes_html}
</section>'''

    if k == "tags":
        groups_html = ""
        for label, tags in s["groups"]:
            tags_html = "".join(f'<span class="tag-chip">{t}</span>' for t in tags)
            groups_html += f'<div class="tag-group"><div class="tag-label">{label}</div><div class="tag-chips">{tags_html}</div></div>'
        return f'''<section class="slide s-tags" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <div class="tag-groups">{groups_html}</div>
  {notes_html}
</section>'''

    return f'<section class="slide">?? {k}</section>'


slides_html = "\n".join(render_slide(i, s) for i, s in enumerate(SLIDES))
total = len(SLIDES)

HTML = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>AI 時代的新聞工作 · 2026 海外特派員營</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #0a0a0a; --bg-elev: #141414;
    --fg: #f5f5f5; --fg-dim: #aaa;
    --accent: #F4CC2F; --cna: #1B5FAA;
    --divider-bg: linear-gradient(135deg, #0b2543 0%, #1B5FAA 100%);
  }}
  html, body {{ margin:0; padding:0; height:100%; overflow:hidden; background:var(--bg); color:var(--fg);
    font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif; -webkit-font-smoothing: antialiased; }}
  #deck {{ position:relative; height:100vh; width:100vw; }}
  .slide {{ position:absolute; inset:0; display:flex; flex-direction:column;
    justify-content:center; align-items:center; padding:7vh 6vw 10vh; box-sizing:border-box;
    opacity:0; pointer-events:none; transition:opacity 380ms, transform 380ms; transform:translateX(30px); overflow:hidden; }}
  .slide.active {{ opacity:1; pointer-events:auto; transform:translateX(0); }}
  .speaker-notes {{ display:none; }}
  body.show-notes .speaker-notes {{ display:block; position:fixed; bottom:90px; left:24px; right:24px;
    background:rgba(0,0,0,0.92); color:#e5e5e5; padding:16px 22px; border-radius:10px;
    font-size:1rem; line-height:1.6; border-left:4px solid var(--accent); z-index:200; }}

  /* brand + theme toggle */
  .brand {{ position:fixed; top:22px; left:26px; z-index:100; display:flex; align-items:center; gap:10px;
    padding:6px 10px; border-radius:8px; background:rgba(255,255,255,0.04); backdrop-filter:blur(6px); }}
  .brand img {{ height:36px; width:auto; display:block; filter:brightness(8) saturate(0); }}
  .brand span {{ font-size:0.78rem; letter-spacing:0.08em; color:var(--fg-dim); }}
  .theme-toggle {{ position:fixed; top:22px; right:26px; z-index:100; width:40px; height:40px;
    border-radius:50%; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.04);
    color:var(--fg); cursor:pointer; display:flex; align-items:center; justify-content:center;
    transition:background 200ms; }}
  .theme-toggle:hover {{ background:rgba(255,255,255,0.1); }}
  .theme-toggle svg {{ width:18px; height:18px; stroke:currentColor; fill:none; stroke-width:2; }}

  /* navigation */
  .ctrl {{ position:fixed; top:0; height:100%; width:14vw; z-index:50; display:flex;
    align-items:center; justify-content:center; cursor:pointer; opacity:0; transition:opacity 200ms; color:var(--fg); }}
  .ctrl:hover {{ opacity:0.5; }}
  .ctrl.prev {{ left:0; }} .ctrl.next {{ right:0; }}
  .ctrl svg {{ width:44px; height:44px; stroke:currentColor; fill:none; stroke-width:2; }}

  .indicator {{ position:fixed; bottom:20px; right:28px; z-index:100; font-size:0.88rem;
    color:var(--fg-dim); font-variant-numeric: tabular-nums; }}
  .indicator b {{ color:var(--fg); font-weight:600; }}
  .progress {{ position:fixed; left:0; top:0; height:3px; z-index:200; background:var(--accent); transition:width 300ms; }}

  .thumbs-zone {{ position:fixed; left:0; right:0; bottom:0; height:100px; z-index:80; }}
  .thumbs {{ position:absolute; left:0; right:0; bottom:0; display:flex; gap:6px; padding:8px 12px;
    overflow-x:auto; overflow-y:hidden; background:rgba(0,0,0,0.85); backdrop-filter:blur(8px);
    opacity:0; transform:translateY(20px); pointer-events:none; transition:opacity 250ms, transform 250ms; }}
  .thumbs-zone:hover .thumbs {{ opacity:1; transform:translateY(0); pointer-events:auto; }}
  .thumb {{ flex:0 0 auto; width:78px; height:48px; border-radius:4px; background:#222; color:#ccc;
    font-size:0.7rem; display:flex; align-items:center; justify-content:center; cursor:pointer;
    border:2px solid transparent; line-height:1.1; text-align:center; padding:4px; }}
  .thumb:hover {{ background:#333; }}
  .thumb.active {{ border-color:var(--accent); background:#444; color:#fff; }}

  /* slide typography */
  .slide h1 {{ font-size:clamp(2.4rem, 6vw, 5rem); font-weight:900; line-height:1.1;
    margin:0 0 18px; letter-spacing:-0.02em; }}
  .slide h2 {{ font-size:clamp(1.5rem, 2.8vw, 2.4rem); font-weight:800; line-height:1.2;
    margin:0 0 18px; letter-spacing:-0.01em; }}
  .slide h2 small {{ font-size:0.55em; font-weight:500; color:var(--fg-dim); display:block; margin-top:6px; }}
  .slide .hl {{ color:var(--accent); }}
  .slide .subtitle {{ font-size:clamp(1.1rem, 1.6vw, 1.4rem); color:var(--fg-dim);
    max-width:32ch; line-height:1.55; }}
  .slide .tag {{ margin-top:40px; font-size:0.85rem; letter-spacing:0.1em;
    color:var(--accent); text-transform:uppercase; opacity:0.8; }}
  .slide .eyebrow {{ font-size:0.8rem; letter-spacing:0.2em; color:var(--accent);
    text-transform:uppercase; margin-bottom:18px; }}
  .slide .body {{ font-size:clamp(1.15rem, 1.8vw, 1.6rem); line-height:1.6;
    max-width:28ch; margin-top:12px; }}
  .slide .caption {{ font-size:clamp(0.95rem, 1.3vw, 1.15rem); color:var(--fg-dim);
    margin-top:18px; max-width:60ch; text-align:center; }}
  .slide .context {{ font-size:clamp(0.95rem, 1.25vw, 1.1rem); color:var(--fg-dim);
    line-height:1.65; max-width:62ch; margin:0 0 18px; }}
  .slide .lead {{ font-size:clamp(1.05rem, 1.4vw, 1.3rem); color:var(--fg); line-height:1.55;
    max-width:40ch; margin:0 0 18px; font-weight:500; }}

  /* title */
  .s-title {{ background:radial-gradient(ellipse at top, #17253c 0%, #060b14 60%, #000 100%); text-align:center; }}
  .s-title .brand-mark img {{ height:56px; filter:brightness(8); margin-bottom:28px; }}
  .s-title h1 {{ max-width:16ch; }}

  /* divider */
  .s-divider {{ background:var(--divider-bg); color:#fff; justify-content:flex-start; align-items:flex-start; padding:14vh 8vw; }}
  .s-divider .divider-num {{ font-size:clamp(1.2rem, 2vw, 1.8rem); font-weight:700; letter-spacing:0.3em;
    color:var(--accent); text-transform:uppercase; }}
  .s-divider .divider-title {{ font-size:clamp(2.5rem, 6vw, 4.4rem); font-weight:900; margin-top:20px; line-height:1.1; }}

  /* text kind */
  .s-text {{ align-items:flex-start; padding-left:10vw; padding-right:10vw; }}
  .s-text.big {{ text-align:center; align-items:center; justify-content:center; }}
  .s-text.big h2 {{ font-size:clamp(2.2rem, 6vw, 4.8rem); line-height:1.15; max-width:18ch; }}

  /* image */
  .s-image {{ justify-content:flex-start; padding-top:6vh; }}
  .s-image h2 {{ align-self:flex-start; margin-bottom:14px; }}
  .s-image figure {{ flex:1 1 auto; margin:0; display:flex; align-items:center; justify-content:center; width:100%; min-height:0; }}
  .s-image figure img {{ max-width:100%; max-height:70vh; object-fit:contain;
    box-shadow:0 20px 60px rgba(0,0,0,0.5); border-radius:6px; }}

  /* video */
  .s-video {{ justify-content:flex-start; padding-top:6vh; }}
  .s-video.ctx {{ padding-top:5vh; }}
  .s-video h2 {{ align-self:flex-start; margin-bottom:14px; }}
  .s-video .context {{ align-self:flex-start; }}
  .s-video figure {{ flex:1 1 auto; margin:0; display:flex; align-items:center; justify-content:center; width:100%; min-height:0; }}
  .s-video video {{ max-width:100%; max-height:66vh; width:auto; height:auto; border-radius:8px;
    background:#000; box-shadow:0 20px 60px rgba(0,0,0,0.6); }}

  .s-video-hero {{ justify-content:center; align-items:center; padding:5vh 8vw; }}
  .s-video-hero h2 {{ font-size:clamp(2rem, 4vw, 3.4rem); margin-bottom:28px; text-align:center; }}
  .s-video-hero figure {{ margin:0; width:100%; display:flex; justify-content:center; }}
  .s-video-hero video {{ max-width:80vw; max-height:66vh; border-radius:10px;
    box-shadow:0 20px 60px rgba(0,0,0,0.6); }}

  /* compare */
  .s-compare {{ justify-content:flex-start; padding-top:6vh; }}
  .s-compare h2 {{ align-self:flex-start; }}
  .s-compare.ctx {{ padding-top:5vh; }}
  .s-compare.ctx .context {{ align-self:flex-start; }}
  .compare-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; width:100%; flex:1 1 auto; min-height:0; }}
  .compare-grid figure {{ margin:0; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
  .compare-grid img {{ max-width:100%; max-height:60vh; object-fit:contain; border-radius:6px;
    box-shadow:0 16px 40px rgba(0,0,0,0.5); }}
  .compare-grid figcaption {{ margin-top:14px; color:var(--accent); font-weight:700;
    letter-spacing:0.1em; font-size:1.05rem; }}

  /* number grid */
  .s-numgrid {{ justify-content:flex-start; padding-top:6vh; }}
  .s-numgrid h2 {{ align-self:flex-start; }}
  .ncards {{ display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:18px;
    width:100%; flex:1 1 auto; min-height:0; }}
  .ncard {{ background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1);
    border-radius:12px; padding:24px 28px; display:flex; flex-direction:column; justify-content:center; }}
  .ncard-num {{ font-size:clamp(2.2rem, 5.5vw, 4rem); font-weight:900; color:var(--accent);
    line-height:1; letter-spacing:-0.02em; }}
  .ncard-label {{ font-size:0.85rem; letter-spacing:0.15em; text-transform:uppercase;
    color:var(--fg-dim); margin-top:8px; }}
  .ncard-body {{ font-size:clamp(0.95rem, 1.2vw, 1.1rem); line-height:1.55; margin-top:12px; color:var(--fg); }}

  /* image-with-bullet */
  .s-img-bullet {{ justify-content:flex-start; padding-top:6vh; }}
  .s-img-bullet h2 {{ align-self:flex-start; }}
  .img-bullet {{ display:grid; grid-template-columns:2fr 1fr; gap:28px; width:100%;
    flex:1 1 auto; min-height:0; align-items:center; }}
  .img-bullet figure {{ margin:0; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
  .img-bullet figure img {{ max-width:100%; max-height:58vh; object-fit:contain; border-radius:6px;
    box-shadow:0 16px 40px rgba(0,0,0,0.5); }}
  .img-bullet figcaption {{ margin-top:12px; color:var(--fg-dim); text-align:center; }}
  .img-bullet aside {{ padding-left:18px; border-left:3px solid var(--accent); }}
  .img-bullet .aside-label {{ font-size:0.85rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--accent); margin-bottom:10px; }}
  .img-bullet aside p {{ font-size:clamp(1rem, 1.3vw, 1.2rem); line-height:1.65; margin:0; }}

  /* image-with-lead */
  .s-img-lead {{ justify-content:flex-start; padding-top:6vh; align-items:center; }}
  .s-img-lead h2 {{ align-self:flex-start; }}
  .s-img-lead .lead {{ align-self:flex-start; }}
  .s-img-lead figure {{ flex:1 1 auto; margin:0; display:flex; align-items:center; justify-content:center;
    width:100%; min-height:0; }}
  .s-img-lead figure img {{ max-width:100%; max-height:54vh; object-fit:contain; border-radius:6px;
    box-shadow:0 16px 40px rgba(0,0,0,0.5); }}

  /* big question overlay */
  .s-bigq {{ padding:0; }}
  .s-bigq figure.bg {{ position:absolute; inset:0; margin:0; z-index:1; }}
  .s-bigq figure.bg img {{ width:100%; height:100%; object-fit:cover; filter:brightness(0.42) blur(1px); }}
  .s-bigq .overlay {{ position:relative; z-index:2; padding:8vh 10vw; text-align:center;
    display:flex; flex-direction:column; align-items:center; justify-content:center; }}
  .s-bigq h2 {{ font-size:clamp(2.4rem, 6vw, 5rem); line-height:1.15; max-width:20ch; text-shadow:0 4px 24px rgba(0,0,0,0.6); }}

  /* tags */
  .s-tags {{ justify-content:flex-start; padding-top:8vh; }}
  .s-tags h2 {{ align-self:flex-start; }}
  .tag-groups {{ display:flex; flex-direction:column; gap:22px; width:100%; max-width:1100px; }}
  .tag-group {{ display:grid; grid-template-columns:130px 1fr; gap:20px; align-items:baseline; }}
  .tag-label {{ color:var(--accent); font-size:0.9rem; letter-spacing:0.15em; text-transform:uppercase; font-weight:700; }}
  .tag-chips {{ display:flex; flex-wrap:wrap; gap:10px; }}
  .tag-chip {{ background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12);
    padding:8px 16px; border-radius:999px; font-size:clamp(0.9rem, 1.3vw, 1.1rem); font-weight:500; }}

  /* light mode */
  body.light {{ --bg:#f7f5ef; --bg-elev:#fff; --fg:#111; --fg-dim:#555; }}
  body.light .s-title {{ background:radial-gradient(ellipse at top, #e8f0fe 0%, #fff 60%, #fff 100%); color:#0b2543; }}
  body.light .s-title .brand-mark img {{ filter:none; }}
  body.light .brand img {{ filter:none; }}
  body.light .brand {{ background:rgba(0,0,0,0.04); }}
  body.light .brand span {{ color:#555; }}
  body.light .s-divider {{ background:linear-gradient(135deg, #1B5FAA 0%, #0b2543 100%); color:#fff; }}
  body.light .tag-chip {{ background:rgba(0,0,0,0.04); border-color:rgba(0,0,0,0.12); }}
  body.light .ncard {{ background:#fff; border-color:rgba(0,0,0,0.08); box-shadow:0 4px 16px rgba(0,0,0,0.04); }}
  body.light .thumbs {{ background:rgba(255,255,255,0.95); }}
  body.light .thumb {{ background:#eee; color:#333; }}
  body.light .thumb.active {{ background:#fff; }}

  /* mobile */
  @media (max-width: 768px) {{
    .slide {{ padding:12vh 6vw 14vh; }}
    .compare-grid, .ncards, .img-bullet {{ grid-template-columns:1fr; grid-template-rows:auto; }}
    .tag-group {{ grid-template-columns:1fr; gap:6px; }}
    .brand span {{ display:none; }}
    .ctrl {{ width:22vw; }}
  }}
</style>
</head>
<body>

<div class="brand">
  <img src="data:image/png;base64,{logo_b64}" alt="CNA">
  <span>Media Lab · 2026 海外特派員營</span>
</div>

<button class="theme-toggle" id="themeToggle" title="切換深/淺色模式">
  <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
</button>

<div class="progress" id="progress" style="width:0;"></div>

<main id="deck">
{slides_html}
</main>

<div class="ctrl prev" id="prevBtn"><svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg></div>
<div class="ctrl next" id="nextBtn"><svg viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg></div>

<div class="indicator"><b id="curPage">1</b> / {total}</div>

<div class="thumbs-zone"><div class="thumbs" id="thumbs"></div></div>

<script>
(function() {{
  const slides = document.querySelectorAll('.slide');
  const total = slides.length;
  let cur = 0;
  const curPage = document.getElementById('curPage');
  const progress = document.getElementById('progress');
  const thumbs = document.getElementById('thumbs');

  slides.forEach((sl, i) => {{
    const t = document.createElement('div');
    t.className = 'thumb';
    t.dataset.idx = i;
    const h = sl.querySelector('h1, h2, .divider-title');
    const label = h ? h.textContent.replace(/\\n/g, ' ').slice(0, 14) : '#' + (i+1);
    t.textContent = (i+1) + ' · ' + label;
    t.addEventListener('click', () => go(i));
    thumbs.appendChild(t);
  }});
  const thumbEls = thumbs.querySelectorAll('.thumb');

  function render() {{
    slides.forEach((sl, i) => {{
      sl.classList.toggle('active', i === cur);
      const v = sl.querySelector('video');
      if (v && i !== cur) v.pause();
    }});
    thumbEls.forEach((t, i) => t.classList.toggle('active', i === cur));
    curPage.textContent = cur + 1;
    progress.style.width = ((cur + 1) / total * 100) + '%';
    const active = thumbEls[cur];
    if (active) active.scrollIntoView({{ block:'nearest', inline:'center', behavior:'smooth' }});
  }}
  function go(i) {{ cur = Math.max(0, Math.min(total - 1, i)); render(); }}
  const next = () => go(cur + 1);
  const prev = () => go(cur - 1);

  document.getElementById('nextBtn').addEventListener('click', next);
  document.getElementById('prevBtn').addEventListener('click', prev);
  document.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'VIDEO') return;
    if (['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)) {{ next(); e.preventDefault(); }}
    else if (['ArrowLeft','ArrowUp','PageUp'].includes(e.key)) {{ prev(); e.preventDefault(); }}
    else if (e.key === 'Home') go(0);
    else if (e.key === 'End') go(total - 1);
    else if (e.key.toLowerCase() === 'f') {{
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    }}
    else if (e.key.toLowerCase() === 'p') document.body.classList.toggle('show-notes');
  }});

  let tx = null;
  document.addEventListener('touchstart', (e) => {{ tx = e.touches[0].clientX; }});
  document.addEventListener('touchend', (e) => {{
    if (tx == null) return;
    const dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 50) (dx < 0 ? next : prev)();
    tx = null;
  }});

  const btn = document.getElementById('themeToggle');
  if (localStorage.getItem('pres-theme') === 'light') document.body.classList.add('light');
  btn.addEventListener('click', () => {{
    document.body.classList.toggle('light');
    localStorage.setItem('pres-theme', document.body.classList.contains('light') ? 'light' : 'dark');
  }});
  render();
}})();
</script>
</body>
</html>
'''

out = OUT / "presentation.html"
out.write_text(HTML, encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size:,} bytes, {total} slides)")
