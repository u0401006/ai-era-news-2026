#!/usr/bin/env python3
"""Build AI時代的新聞工作 deck — v3, strict MD-driven.

Rule: only use text the user wrote in the MD — no editorial additions.
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


SLIDES = [
    # Title
    {
        "kind": "title",
        "title": "AI 時代的新聞工作",
        "footer": "中央社媒體實驗室 · 2026 海外特派員營",
    },
    # Opening
    {
        "kind": "video-hero",
        "src": media("jiming_opening.mp4"),
        "title": "特別來賓",
    },

    # ─── Part 1 ───
    {"kind": "divider", "num": "Part 1", "title": "AI 大浪來了，媒體受衝擊"},

    {
        "kind": "long-list",
        "title": "2026 年，不好的開局",
        "items": [
            "華郵裁員300位編採人員，關閉體育版、圖書版，裁撤中東、印度與澳洲等地駐外記者，資源集中在政治、商業、科技、健康和氣候，報導重點轉到全國受眾；AI整合到新聞產製流程當中，包含管理讀者評論、製作Podcast，建立自有AI搜尋工具或資料庫服務。",
            "BBC 4月宣布裁1,800~2,000個職位，每10人就有1人需離職，以減輕「龐大財務壓力」、達成未來2年樽節新台幣214億元目標。",
            "根據就業諮詢公司，2025年，美國媒體業裁撤17,163個崗位，洛杉磯時報、NBC新聞、CBS新聞等，都因廣告收入下降、債台高築、受眾轉向社群平台與AI，持續成本清算轉型。",
            "關鍵評論網、TVBS裁員",
        ],
    },

    {
        "kind": "image-with-text",
        "title": "完蛋了，這些職業都要失業啦",
        "src": media("AI_job_replace.png"),
        "img_caption": "翻譯蹲完記者蹲，記者蹲，記者蹲完工程師蹲",
        "body": "迪士尼宣布裁員1,000人，波及影視、行銷、ESPN和公司總部等部門。漫威約8%人力遭到解僱。Snapchat母公司宣布裁員1,000人，占整體人力16%。公司將裁員歸咎於「AI的快速發展」，稱AI進步有助員工減少重複性工作。",
    },

    {
        "kind": "image",
        "title": "其實，我更忙了",
        "src": media("DW_ai.png"),
        "caption": "德國之聲AI發展主管的分享",
    },

    {
        "kind": "tags-plain",
        "title": "AI 熱詞你聽過幾個？",
        "rows": [
            ["ChatGPT", "Claude", "Gemini", "Grok", "Perplexity"],
            ["Midjourney", "Nano Banana", "Seedance"],
            ["Copilot", "Vibe Coding", "ClaudeCode", "Agentic Coding", "Harness Coding"],
            ["OpenClaw", "Hermes Agent"],
        ],
    },

    # ─── Part 2 ───
    {"kind": "divider", "num": "Part 2", "title": "你的識讀能力幾級？"},

    {
        "kind": "paragraph",
        "title": "literacy",
        "body": "談談古老的這個字 literacy。本來是在講國家的人識不識「字」，因為識字，整體素質、國力才能提升。<br><br>現代已擴展為獲取、理解、創造與傳達資訊的綜合能力，包含電腦素養、金融知識、媒體識讀等專業技能。它是個人賦權、終身學習及融入社會的關鍵基礎。",
    },

    {
        "kind": "image",
        "title": "這張照片哪裡怪 1？",
        "src": media("a_younger_president_in_the_white_house_oval_office_2024.png"),
        "caption": "這張照片哪裡怪 1",
    },

    {
        "kind": "image",
        "title": "這張照片哪裡怪 2026？",
        "src": media("a_younger_president_in_the_white_house_oval_office_2026.png"),
        "caption": "這張照片哪裡怪 2",
    },

    {
        "kind": "image-with-context",
        "title": "這張照片哪裡怪 2？",
        "context": "凱特王妃術後首張官方照疑遭修改 美聯路透法新等多家媒體撤稿。<br>意在平息公眾對凱特健康情形臆測的照片卻引來更多傳言和紛擾......美聯社、路透社、法新社等國際通訊社，以及Getty、Shutterstock等圖庫公司陸續撤回照片，並通知客戶停止使用。撤圖的主要原因是照片修改幅度過大、有經數位技術改造的痕跡。未有跡象顯示照片為偽造。",
        "src": media("kate1.png"),
        "caption": "這張照片哪裡怪 3",
    },

    {
        "kind": "image",
        "title": "這張照片哪裡怪 2？",
        "src": media("kate2.jpg"),
        "caption": "你不說我真不知道",
    },

    # ─── Part 3 ───
    {"kind": "divider", "num": "Part 3", "title": "新聞倫理的新課題：這樣可以嗎？"},

    {
        "kind": "image",
        "title": "這樣可以嗎之一？",
        "src": media("TVBS.jpg"),
        "caption": "做得出來的請舉手",
    },

    {
        "kind": "image",
        "title": "這樣可以嗎之二？",
        "src": media("sakura.png"),
        "caption": "有一個小 mark",
    },

    {
        "kind": "image",
        "title": "這樣可以嗎之二？",
        "src": media("sakura-gen.png"),
        "caption": "我...只是想要...對焦",
    },

    {
        "kind": "video",
        "title": "這樣可以嗎之三？",
        "src": media("realtime-photo.mov"),
        "caption": "仔細看，它長高了",
    },

    {
        "kind": "image",
        "title": "理解 LLM 的原理",
        "src": media("WhatsLLM.png"),
        "caption": "你一定要知道它是接龍引擎",
    },

    {
        "kind": "image",
        "title": "它哪天說不定幫你個大忙",
        "src": media("dirty-data.png"),
        "caption": "Garbage In Garbage Out",
    },

    # ─── Part 4 ───
    {"kind": "divider", "num": "Part 4", "title": "中央社媒體實驗室的 AI 應用"},

    {
        "kind": "paragraph",
        "body": "比賽就是這樣的 好像跑步游泳一樣 還不是你做什麼他就做什麼<br><br>但全球華文媒體有用過飛鴿傳書又有用過AI的，只有中央社",
    },

    {
        "kind": "video-with-context",
        "title": "志明編輯助手",
        "context": "以往不同新聞領域、不同語種的新聞，需要不同職務的人來處理，但是有了助手？",
        "src": media("jiming_combine.mp4"),
        "caption": "綜合外電報導？交給志明",
    },

    {
        "kind": "video",
        "title": "Agents 時代來臨",
        "src": media("agent-line.mp4"),
        "caption": "組一張圖，你先開 photoshop？",
    },

    {
        "kind": "video",
        "title": "零點擊時代的新聞會是怎麼樣 1",
        "src": media("fake.mov"),
        "caption": "零點擊？示範給你看",
    },

    {
        "kind": "video",
        "title": "零點擊時代的新聞會是怎麼樣 2",
        "src": media("AskCNA.mov"),
        "caption": "Ask CNA",
    },

    {
        "kind": "image",
        "title": "零點擊時代的新聞會是怎麼樣 3",
        "src": media("cna-mcp.png"),
        "caption": "在 Claude、ChatGPT 就能問中央社",
    },

    # ─── 結語 ───（合併 divider + 大哉問為單頁）
    {
        "kind": "image-big-question",
        "eyebrow": "結 語",
        "title": "民主社會可以沒有新聞嗎？",
        "src": media("AI_combo.png"),
        "caption": "記者在現場",
    },

    {
        "kind": "image-with-lead",
        "title": "學習在 AI 時代，你的準備是什麼？",
        "lead": "好像不用再問要不要學程式？<br>至少，你要會問 AI。那...問哪個？",
        "src": media("mav_council_3.png"),
        "caption": "小孩子才做選擇，我全都問",
    },

    {
        "kind": "image-with-lead",
        "title": "要不要學程式？",
        "lead": "Prompt: 仿照間諜家家酒的三大角色，把臉改成中年男子",
        "src": media("mav_council-ojisan.png"),
        "caption": "世界萬物皆有名字，有名字才能開始",
    },

    {
        "kind": "image",
        "title": "大叔說教時間",
        "src": media("ending.png"),
        "caption": "參加我是海外特派員，增廣見聞",
    },
]


# ============================================================
# Renderer
# ============================================================
def render_slide(idx: int, s: dict) -> str:
    k = s["kind"]

    if k == "title":
        return f'''<section class="slide s-title" data-idx="{idx}">
  <div class="brand-mark"><img src="data:image/png;base64,{logo_b64}" alt="CNA"></div>
  <h1>{s["title"]}</h1>
  <div class="tag">{s.get("footer","")}</div>
</section>'''

    if k == "divider":
        return f'''<section class="slide s-divider" data-idx="{idx}">
  <div class="divider-num">{s["num"]}</div>
  <h2 class="divider-title">{s["title"]}</h2>
</section>'''

    if k == "text":
        body = f'<p class="body">{s["body"]}</p>' if s.get("body") else ""
        return f'''<section class="slide s-text" data-idx="{idx}">
  <h2>{s["title"]}</h2>{body}
</section>'''

    if k == "paragraph":
        title = f'<h2>{s["title"]}</h2>' if s.get("title") else ""
        return f'''<section class="slide s-paragraph" data-idx="{idx}">
  {title}
  <p class="para">{s["body"]}</p>
</section>'''

    if k == "long-list":
        items = "".join(
            f'<li><span class="ln">{i+1:02d}</span><span class="lt">{t}</span></li>'
            for i, t in enumerate(s["items"])
        )
        return f'''<section class="slide s-longlist" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <ol class="longlist">{items}</ol>
</section>'''

    if k == "image":
        cap = f'<p class="caption">{s["caption"]}</p>' if s.get("caption") else ""
        title = f'<h2>{s["title"]}</h2>' if s.get("title") else ""
        return f'''<section class="slide s-image" data-idx="{idx}">
  {title}
  <figure><img src="{s["src"]}" alt=""></figure>
  {cap}
</section>'''

    if k == "image-with-text":
        return f'''<section class="slide s-img-text" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <figure><img src="{s["src"]}" alt=""><figcaption>{s.get("img_caption","")}</figcaption></figure>
  <p class="body">{s["body"]}</p>
</section>'''

    if k == "image-with-context":
        return f'''<section class="slide s-img-ctx" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <p class="context">{s["context"]}</p>
  <figure><img src="{s["src"]}" alt=""></figure>
  <p class="caption">{s.get("caption","")}</p>
</section>'''

    if k == "image-with-lead":
        return f'''<section class="slide s-img-lead" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <p class="lead">{s.get("lead","")}</p>
  <figure><img src="{s["src"]}" alt=""></figure>
  <p class="caption">{s.get("caption","")}</p>
</section>'''

    if k == "image-big-question":
        eyebrow = f'<div class="eyebrow">{s["eyebrow"]}</div>' if s.get("eyebrow") else ""
        return f'''<section class="slide s-bigq" data-idx="{idx}">
  <figure class="bg"><img src="{s["src"]}" alt=""></figure>
  <div class="overlay">
    {eyebrow}
    <h2>{s["title"]}</h2>
    <p class="caption">{s.get("caption","")}</p>
  </div>
</section>'''

    if k == "video":
        cap = f'<p class="caption">{s["caption"]}</p>' if s.get("caption") else ""
        title = f'<h2>{s["title"]}</h2>' if s.get("title") else ""
        return f'''<section class="slide s-video" data-idx="{idx}">
  {title}
  <figure><video src="{s["src"]}" controls preload="metadata" playsinline></video></figure>
  {cap}
</section>'''

    if k == "video-hero":
        return f'''<section class="slide s-video-hero" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <figure><video src="{s["src"]}" controls preload="metadata" playsinline></video></figure>
</section>'''

    if k == "video-with-context":
        return f'''<section class="slide s-video ctx" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <p class="context">{s["context"]}</p>
  <figure><video src="{s["src"]}" controls preload="metadata" playsinline></video></figure>
  <p class="caption">{s.get("caption","")}</p>
</section>'''

    if k == "tags-plain":
        rows = "".join(
            '<div class="tag-row">' + "".join(f'<span class="tag-chip">{t}</span>' for t in row) + "</div>"
            for row in s["rows"]
        )
        return f'''<section class="slide s-tags" data-idx="{idx}">
  <h2>{s["title"]}</h2>
  <div class="tag-rows">{rows}</div>
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
    opacity:0; pointer-events:none; transition:opacity 380ms, transform 380ms; transform:translateX(30px);
    overflow-y:auto; overflow-x:hidden; scrollbar-width:thin; scrollbar-color:rgba(255,255,255,0.2) transparent; }}
  .slide.active {{ opacity:1; pointer-events:auto; transform:translateX(0); }}
  .slide::-webkit-scrollbar {{ width:8px; }}
  .slide::-webkit-scrollbar-thumb {{ background:rgba(255,255,255,0.2); border-radius:4px; }}
  .slide::-webkit-scrollbar-thumb:hover {{ background:rgba(255,255,255,0.4); }}
  .slide .scroll-hint {{ position:absolute; bottom:16px; left:50%; transform:translateX(-50%);
    color:var(--accent); font-size:0.78rem; letter-spacing:0.1em; opacity:0.7;
    pointer-events:none; animation:bob 1.8s ease-in-out infinite; }}
  @keyframes bob {{ 0%,100% {{ transform:translate(-50%, 0); }} 50% {{ transform:translate(-50%, 5px); }} }}

  /* brand + theme toggle */
  .brand {{ position:fixed; bottom:16px; right:24px; z-index:100; display:flex; align-items:center; gap:10px;
    padding:6px 12px; border-radius:8px; background:rgba(255,255,255,0.04); backdrop-filter:blur(6px); }}
  .brand img {{ height:28px; width:auto; display:block; filter:brightness(8) saturate(0); }}
  .brand span {{ font-size:0.72rem; letter-spacing:0.08em; color:var(--fg-dim); }}
  .theme-toggle {{ position:fixed; top:22px; right:26px; z-index:100; width:40px; height:40px;
    border-radius:50%; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.04);
    color:var(--fg); cursor:pointer; display:flex; align-items:center; justify-content:center; transition:background 200ms; }}
  .theme-toggle:hover {{ background:rgba(255,255,255,0.1); }}
  .theme-toggle svg {{ width:18px; height:18px; stroke:currentColor; fill:none; stroke-width:2; }}

  /* navigation */
  .ctrl {{ position:fixed; top:0; height:100%; width:14vw; z-index:50; display:flex;
    align-items:center; justify-content:center; cursor:pointer; opacity:0; transition:opacity 200ms; color:var(--fg); }}
  .ctrl:hover {{ opacity:0.5; }}
  .ctrl.prev {{ left:0; }} .ctrl.next {{ right:0; }}
  .ctrl svg {{ width:44px; height:44px; stroke:currentColor; fill:none; stroke-width:2; }}

  .indicator {{ position:fixed; bottom:20px; left:28px; z-index:100; font-size:0.88rem;
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

  /* typography */
  .slide h1 {{ font-size:clamp(2.4rem, 6vw, 5rem); font-weight:900; line-height:1.1;
    margin:0 0 18px; letter-spacing:-0.02em; }}
  .slide h2 {{ font-size:clamp(1.5rem, 2.8vw, 2.4rem); font-weight:800; line-height:1.2;
    margin:0 0 18px; letter-spacing:-0.01em; }}
  .slide .tag {{ margin-top:40px; font-size:0.85rem; letter-spacing:0.1em;
    color:var(--accent); text-transform:uppercase; opacity:0.8; }}
  .slide .body {{ font-size:clamp(1rem, 1.4vw, 1.2rem); line-height:1.7;
    max-width:60ch; margin-top:12px; color:var(--fg); }}
  .slide .caption {{ font-size:clamp(0.95rem, 1.3vw, 1.15rem); color:var(--fg-dim);
    margin-top:18px; max-width:60ch; text-align:center; }}
  .slide .context {{ font-size:clamp(0.95rem, 1.2vw, 1.1rem); color:var(--fg-dim);
    line-height:1.7; max-width:64ch; margin:0 0 18px; }}
  .slide .lead {{ font-size:clamp(1.05rem, 1.4vw, 1.3rem); color:var(--fg); line-height:1.6;
    max-width:44ch; margin:0 0 18px; font-weight:500; }}

  /* title */
  .s-title {{ background:radial-gradient(ellipse at top, #17253c 0%, #060b14 60%, #000 100%); text-align:center; }}
  .s-title .brand-mark img {{ height:56px; filter:brightness(8); margin-bottom:28px; }}

  /* divider */
  .s-divider {{ background:var(--divider-bg); color:#fff; justify-content:flex-start; align-items:flex-start; padding:14vh 8vw; }}
  .s-divider .divider-num {{ font-size:clamp(1.2rem, 2vw, 1.8rem); font-weight:700; letter-spacing:0.3em;
    color:var(--accent); text-transform:uppercase; }}
  .s-divider .divider-title {{ font-size:clamp(2.5rem, 6vw, 4.4rem); font-weight:900; margin-top:20px; line-height:1.1; }}

  /* text hook */
  .s-text {{ text-align:center; }}
  .s-text h2 {{ font-size:clamp(2rem, 5vw, 4rem); max-width:18ch; }}

  /* paragraph */
  .s-paragraph {{ justify-content:center; align-items:flex-start; padding:8vh 12vw; }}
  .s-paragraph h2 {{ margin-bottom:22px; }}
  .para {{ font-size:clamp(1.05rem, 1.5vw, 1.4rem); line-height:1.8; max-width:60ch; color:var(--fg); margin:0; }}

  /* long numbered list */
  .s-longlist {{ justify-content:flex-start; padding-top:6vh; padding-left:8vw; padding-right:8vw; }}
  .s-longlist h2 {{ align-self:flex-start; color:var(--accent); }}
  .longlist {{ list-style:none; padding:0; margin:0; width:100%; max-width:95ch; counter-reset:none; }}
  .longlist li {{ display:grid; grid-template-columns:60px 1fr; gap:16px; align-items:flex-start;
    padding:14px 0; border-bottom:1px solid rgba(255,255,255,0.08); }}
  .longlist li:last-child {{ border-bottom:none; }}
  .longlist .ln {{ color:var(--accent); font-weight:800; font-size:1.4rem; line-height:1.6;
    font-variant-numeric:tabular-nums; }}
  .longlist .lt {{ font-size:clamp(0.95rem, 1.2vw, 1.12rem); line-height:1.75; color:var(--fg); }}

  /* image */
  .s-image {{ justify-content:flex-start; padding-top:6vh; }}
  .s-image h2 {{ align-self:flex-start; margin-bottom:14px; }}
  .s-image figure {{ flex:1 1 auto; margin:0; display:flex; align-items:center; justify-content:center; width:100%; min-height:0; }}
  .s-image figure img {{ max-width:100%; max-height:70vh; object-fit:contain;
    box-shadow:0 20px 60px rgba(0,0,0,0.5); border-radius:6px; }}

  /* image + text */
  .s-img-text {{ justify-content:flex-start; padding-top:6vh; }}
  .s-img-text h2 {{ align-self:flex-start; margin-bottom:14px; }}
  .s-img-text figure {{ margin:0; display:flex; flex-direction:column; align-items:center; width:100%; }}
  .s-img-text figure img {{ max-width:100%; max-height:48vh; object-fit:contain; border-radius:6px;
    box-shadow:0 16px 40px rgba(0,0,0,0.5); }}
  .s-img-text figcaption {{ margin-top:12px; color:var(--fg-dim); font-size:0.95rem; }}
  .s-img-text .body {{ margin-top:20px; max-width:70ch; }}

  /* image + context */
  .s-img-ctx {{ justify-content:flex-start; padding-top:6vh; }}
  .s-img-ctx h2 {{ align-self:flex-start; }}
  .s-img-ctx .context {{ align-self:flex-start; }}
  .s-img-ctx figure {{ margin:0; display:flex; justify-content:center; width:100%; }}
  .s-img-ctx figure img {{ max-width:100%; max-height:50vh; object-fit:contain; border-radius:6px;
    box-shadow:0 16px 40px rgba(0,0,0,0.5); }}

  /* image + lead */
  .s-img-lead {{ justify-content:flex-start; padding-top:6vh; align-items:center; }}
  .s-img-lead h2 {{ align-self:flex-start; }}
  .s-img-lead .lead {{ align-self:flex-start; }}
  .s-img-lead figure {{ flex:1 1 auto; margin:0; display:flex; align-items:center; justify-content:center; width:100%; min-height:0; }}
  .s-img-lead figure img {{ max-width:100%; max-height:54vh; object-fit:contain; border-radius:6px;
    box-shadow:0 16px 40px rgba(0,0,0,0.5); }}

  /* big question overlay */
  .s-bigq {{ padding:0; }}
  .s-bigq figure.bg {{ position:absolute; inset:0; margin:0; z-index:1; }}
  .s-bigq figure.bg img {{ width:100%; height:100%; object-fit:cover; filter:brightness(0.42) blur(1px); }}
  .s-bigq .overlay {{ position:relative; z-index:2; padding:8vh 10vw; text-align:center;
    display:flex; flex-direction:column; align-items:center; justify-content:center; }}
  .s-bigq .eyebrow {{ font-size:0.9rem; letter-spacing:0.3em; color:var(--accent);
    text-transform:uppercase; margin-bottom:18px; font-weight:700; text-shadow:0 2px 12px rgba(0,0,0,0.6); }}
  .s-bigq h2 {{ font-size:clamp(2.4rem, 6vw, 5rem); line-height:1.15; max-width:20ch; text-shadow:0 4px 24px rgba(0,0,0,0.6); }}

  /* video */
  .s-video {{ justify-content:flex-start; padding-top:6vh; }}
  .s-video.ctx {{ padding-top:5vh; }}
  .s-video h2 {{ align-self:flex-start; margin-bottom:14px; }}
  .s-video .context {{ align-self:flex-start; }}
  .s-video figure {{ flex:1 1 auto; margin:0; display:flex; align-items:center; justify-content:center; width:100%; min-height:0; }}
  .s-video video {{ max-width:100%; max-height:66vh; border-radius:8px; background:#000;
    box-shadow:0 20px 60px rgba(0,0,0,0.6); }}

  .s-video-hero {{ justify-content:center; align-items:center; padding:5vh 8vw; }}
  .s-video-hero h2 {{ font-size:clamp(2rem, 4vw, 3.4rem); margin-bottom:28px; text-align:center; }}
  .s-video-hero figure {{ margin:0; width:100%; display:flex; justify-content:center; }}
  .s-video-hero video {{ max-width:80vw; max-height:66vh; border-radius:10px;
    box-shadow:0 20px 60px rgba(0,0,0,0.6); }}

  /* tags */
  .s-tags {{ justify-content:flex-start; padding-top:8vh; }}
  .s-tags h2 {{ align-self:flex-start; }}
  .tag-rows {{ display:flex; flex-direction:column; gap:14px; width:100%; max-width:1100px; }}
  .tag-row {{ display:flex; flex-wrap:wrap; gap:10px; }}
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
  body.light .longlist li {{ border-bottom-color:rgba(0,0,0,0.08); }}
  body.light .thumbs {{ background:rgba(255,255,255,0.95); }}
  body.light .thumb {{ background:#eee; color:#333; }}
  body.light .thumb.active {{ background:#fff; }}

  /* mobile */
  @media (max-width: 768px) {{
    .slide {{ padding:12vh 6vw 14vh; }}
    .brand span {{ display:none; }}
    .ctrl {{ width:22vw; }}
    .longlist li {{ grid-template-columns:40px 1fr; }}
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
    const h = sl.querySelector('h1, h2, .divider-title');
    const label = h ? h.textContent.replace(/\\n/g, ' ').slice(0, 14) : '#' + (i+1);
    t.textContent = (i+1) + ' · ' + label;
    t.addEventListener('click', () => go(i));
    thumbs.appendChild(t);
  }});
  const thumbEls = thumbs.querySelectorAll('.thumb');

  function addScrollHint(sl) {{
    let existing = sl.querySelector('.scroll-hint');
    const overflows = sl.scrollHeight > sl.clientHeight + 4;
    if (overflows && !existing) {{
      const hint = document.createElement('div');
      hint.className = 'scroll-hint';
      hint.innerHTML = '▼ 往下捲動';
      sl.appendChild(hint);
      sl.addEventListener('scroll', () => {{
        hint.style.opacity = sl.scrollTop > 40 ? '0' : '0.7';
      }}, {{ passive: true }});
    }} else if (!overflows && existing) {{
      existing.remove();
    }}
  }}

  function render() {{
    slides.forEach((sl, i) => {{
      sl.classList.toggle('active', i === cur);
      const v = sl.querySelector('video');
      if (v && i !== cur) v.pause();
      if (i === cur) {{
        sl.scrollTop = 0;
        requestAnimationFrame(() => addScrollHint(sl));
      }}
    }});
    thumbEls.forEach((t, i) => t.classList.toggle('active', i === cur));
    curPage.textContent = cur + 1;
    progress.style.width = ((cur + 1) / total * 100) + '%';
    const active = thumbEls[cur];
    if (active) active.scrollIntoView({{ block:'nearest', inline:'center', behavior:'smooth' }});
  }}

  window.addEventListener('resize', () => {{ const s = slides[cur]; if (s) addScrollHint(s); }});
  document.querySelectorAll('.slide img').forEach(img => {{
    img.addEventListener('load', () => {{ const s = slides[cur]; if (s) addScrollHint(s); }});
  }});

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
