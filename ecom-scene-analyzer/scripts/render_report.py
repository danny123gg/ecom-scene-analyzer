#!/usr/bin/env python3
"""场景图分析报告渲染脚本 v6 - 多图支持 + combo_strategy Tab + HTML转义 + 输入校验"""

import json, base64, sys, re, mimetypes, html as html_mod
from pathlib import Path

REQUIRED_KEYS = ["meta", "overview", "dimensions", "insights", "style_params", "prompts"]

DIM_META = {
    "angle": {"label": "拍摄角度"}, "light": {"label": "光线与影调"},
    "color": {"label": "色调与质感"}, "comp": {"label": "构图与视觉动线"},
    "model": {"label": "儿童模特与成长叙事"},
}
DIM_ORDER = ["angle", "light", "color", "comp", "model"]
PARAM_ORDER = [
    ("camera","机位"),("lighting","光线"),("color_tone","色调"),
    ("human_chair_space","人椅空间"),("character","人物"),
    ("growth_narrative","成长叙事"),("props","场景道具"),("composition","构图"),
    ("key_constraints","关键约束"),
]

# ── HTML 转义工具 ──

def esc(text):
    """纯文本转义，不保留任何 HTML 标签"""
    return html_mod.escape(str(text))

def esc_rich(text):
    """富文本转义：保留 <strong></strong>，转义其余所有 HTML"""
    text = html_mod.escape(str(text))
    text = text.replace("&lt;strong&gt;", "<strong>").replace("&lt;/strong&gt;", "</strong>")
    return text

# ── 基础渲染工具 ──

def img_b64(path):
    p = Path(path); mime,_ = mimetypes.guess_type(str(p))
    if not mime: mime="image/jpeg"
    with open(p,"rb") as f: return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"

def rp(text):
    """渲染单段（富文本，保留 <strong>）"""
    text=esc_rich(text.strip())
    m=re.match(r'^【([^】]+)】\s*(.*)',text,re.DOTALL)
    if m: return f'<p><span class="st">{m.group(1)}：</span>{m.group(2).strip()}</p>'
    return f'<p>{text}</p>'

def segs(text):
    """渲染多段（富文本）"""
    parts=[p.strip() for p in text.strip().split('\n') if p.strip()]
    if len(parts)<=1: return rp(text.strip())
    return ''.join(rp(p) for p in parts)

# ── 输入校验 ──

def validate(data):
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        print(f"错误：JSON 缺少必需字段：{', '.join(missing)}", file=sys.stderr)
        print(f"必需的顶层字段：{', '.join(REQUIRED_KEYS)}", file=sys.stderr)
        sys.exit(1)

# ── 各模块渲染 ──

def r_imgs(uris):
    if not uris: return ""
    if len(uris) == 1:
        return f'<img id="heroImg" class="hero-single" src="{uris[0]}" alt="">'
    items = ''.join(f'<img class="hero-multi-item" src="{uri}" alt="">' for uri in uris)
    return f'<div class="hero-multi">{items}</div>'

def r_thumbs(uris):
    if not uris: return ""
    if len(uris) == 1:
        return '<div class="float-thumb"><img id="thumbImg" src="" alt=""></div>'
    items = ''.join(f'<img class="thumb-item" src="{uri}" alt="">' for uri in uris)
    return f'<div class="float-thumb float-thumb-multi">{items}</div>'

def r_overview(ov):
    return f'''<div class="ov-grid">
  <div class="ov-card"><div class="ov-label">图片类型</div><div class="ov-value">{esc(ov.get("type",""))}</div></div>
  <div class="ov-card"><div class="ov-label">品类共识定位</div><div class="ov-value">{esc(ov.get("consensus",""))}</div></div>
  <div class="ov-card"><div class="ov-label">核心视觉策略</div><div class="ov-value">{esc(ov.get("strategy",""))}</div></div>
</div>'''

def r_dims(dims):
    cards=[]
    for key in DIM_ORDER:
        if key not in dims: continue
        d=dims[key]; label=DIM_META[key]["label"]
        cards.append(f'''<div class="dim-card">
  <h3><span class="dim-dot"></span>{label}</h3>
  <div class="db obs-b"><span class="bt obs-bt">观察</span>{segs(d.get("observation",""))}</div>
  <div class="db attr-b"><span class="bt attr-bt">归因</span>{segs(d.get("attribution",""))}</div>
</div>''')
    return '\n'.join(cards)

def r_insights(insights):
    cards=[]
    for ins in insights:
        cards.append(f'''<div class="ins-card">
  <h3>{esc(ins.get("title",""))}</h3>
  <div class="ins-row"><span class="it it-a">归因</span>{segs(ins.get("attribution",""))}</div>
  <div class="ins-row"><span class="it it-m">元思考</span>{segs(ins.get("meta_thinking",""))}</div>
  <div class="ins-row"><span class="it it-r">复用</span>{segs(ins.get("reuse",""))}</div>
</div>''')
    return '\n'.join(cards)

def r_params(sp):
    rows=[]
    for key,label in PARAM_ORDER:
        if key=="character":
            s,e=sp.get("character_surface",""),sp.get("character_essence","")
            val=f'<div class="ps"><span class="psl">表象</span>{esc(s)}</div><div class="ps"><span class="psl">本质</span>{esc(e)}</div>'
        else: val=esc(sp.get(key,""))
        rows.append(f'<tr><td>{label}</td><td>{val}</td></tr>')
    return f'''<div class="pm-label">场景模板：<span class="pm-name">{esc(sp.get("template_name",""))}</span></div>
<table><thead><tr><th>维度</th><th>参数</th></tr></thead><tbody>
{''.join(rows)}
</tbody></table>'''

def r_prompt_item(p, i):
    if isinstance(p, dict):
        label = esc(p.get("label", f"Prompt {i}"))
        content = esc(p.get("content", ""))
        return f'<div class="pr-item"><div class="pr-tag">{label}</div>{content}</div>'
    return f'<div class="pr-item"><div class="pr-label">Prompt {i}</div>{esc(p)}</div>'

def r_prompts(prompts):
    mi=[r_prompt_item(p, i) for i,p in enumerate(prompts.get("model",[]),1)]
    si=[r_prompt_item(p, i) for i,p in enumerate(prompts.get("scene",[]),1)]
    ci=[r_prompt_item(p, i) for i,p in enumerate(prompts.get("combined",[]),1)]
    tabs = ['<button class="sub-tab active" data-subtab="st-model">模特塑造</button>',
            '<button class="sub-tab" data-subtab="st-scene">场景塑造</button>']
    panes = [f'<div id="st-model" class="sub-pane active">{chr(10).join(mi)}</div>',
             f'<div id="st-scene" class="sub-pane">{chr(10).join(si)}</div>']
    if ci:
        tabs.append('<button class="sub-tab" data-subtab="st-combined">完整画面</button>')
        panes.append(f'<div id="st-combined" class="sub-pane">{chr(10).join(ci)}</div>')
    return f'''<div class="sub-tab-bar">{''.join(tabs)}</div>
{''.join(panes)}'''

def r_combo(combo):
    if not combo: return ""
    return f'<div class="combo-card">{segs(combo)}</div>'

CSS = r"""
:root {
  --bg:#EBEEF2;--sf:#F5F7FA;--sa:#EDF0F4;--bd:#C8D1DC;--dv:#D8DEE6;
  --tp:#2D3741;--ts:#566575;--tm:#8D9BAA;
  --ac:#6889A8;--al:rgba(104,137,168,0.08);--am:rgba(104,137,168,0.18);
  --co:#5E8A9E;--ca:#7E7FA6;
  --ta:#7A8FA5;--tmt:#8B8EAF;--tr:#7EA89A;
  --r:10px;--sh:0 1px 4px rgba(45,55,65,0.05);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei",-apple-system,sans-serif;background:var(--bg);color:var(--tp);font-size:14px;line-height:1.8;-webkit-font-smoothing:antialiased}
.wrap{max-width:900px;margin:0 auto;padding:0 24px}

/* ── Header ── */
.hero{display:flex;gap:20px;align-items:flex-start;padding:32px 0 24px}
.hero-img{flex:0 0 320px}
.hero-img img.hero-single{width:100%;border-radius:var(--r);border:1px solid var(--bd)}
.hero-multi{display:flex;gap:8px}
.hero-multi-item{flex:1 1 0;min-width:0;border-radius:var(--r);border:1px solid var(--bd);object-fit:cover;max-height:360px}
.hero-info{flex:1;min-width:0}
.hero-info h1{font-size:19px;font-weight:600;margin-bottom:4px}
.hero-info .meta{font-size:12px;color:var(--tm);margin-bottom:16px}
.ov-grid{display:flex;flex-direction:column;gap:10px}
.ov-card{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:12px 14px;box-shadow:var(--sh)}
.ov-label{font-size:10.5px;color:var(--tm);font-weight:600;margin-bottom:3px;letter-spacing:0.04em}
.ov-value{font-size:12.5px;color:var(--tp);line-height:1.55}

/* ── Floating thumbnail ── */
.float-thumb{position:fixed;top:60px;left:max(16px,calc((100vw - 900px)/2 - 160px));width:140px;z-index:90;opacity:0;pointer-events:none;transition:opacity 0.25s}
.float-thumb.show{opacity:1;pointer-events:auto}
.float-thumb img{width:100%;border-radius:8px;border:1px solid var(--bd);box-shadow:0 2px 12px rgba(0,0,0,0.1)}
.float-thumb-multi{display:flex;flex-direction:column;gap:6px}
.float-thumb-multi .thumb-item{width:100%;border-radius:8px;border:1px solid var(--bd);box-shadow:0 2px 12px rgba(0,0,0,0.1)}

/* ── Tab bar ── */
.tab-bar{display:flex;gap:0;background:var(--sf);border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;margin-bottom:20px;box-shadow:var(--sh);position:sticky;top:0;z-index:100}
.tab-bar.stuck{border-radius:0;margin-left:-24px;margin-right:-24px;border-left:none;border-right:none;box-shadow:0 2px 8px rgba(0,0,0,0.08)}
.tab-btn{flex:1;padding:12px 6px;font-size:12px;font-weight:600;color:var(--tm);background:transparent;border:none;cursor:pointer;transition:all 0.2s;border-bottom:2px solid transparent;letter-spacing:0.02em;white-space:nowrap}
.tab-btn:hover{color:var(--ts);background:var(--al)}
.tab-btn.active{color:var(--ac);border-bottom-color:var(--ac);background:var(--al)}

/* ── Tab content ── */
.tab-pane{display:none}
.tab-pane.active{display:block}

/* ── Dim cards ── */
.dim-card{background:var(--sf);border:1px solid var(--bd);border-radius:var(--r);box-shadow:var(--sh);margin-bottom:14px;overflow:hidden;border-left:3px solid var(--ac)}
.dim-card h3{font-size:13.5px;font-weight:600;padding:13px 18px;margin:0;display:flex;align-items:center;gap:8px;background:var(--al);border-bottom:1px solid var(--dv)}
.dim-dot{width:6px;height:6px;border-radius:50%;background:var(--ac);flex-shrink:0}
.db{padding:14px 18px}
.attr-b{background:rgba(104,137,168,0.03);border-top:1px dashed var(--dv)}
.bt{display:inline-block;font-size:10.5px;font-weight:600;letter-spacing:0.05em;padding:2px 9px;border-radius:4px;margin-bottom:10px}
.obs-bt{background:rgba(94,138,158,0.12);color:var(--co)}
.attr-bt{background:rgba(126,127,166,0.12);color:var(--ca)}
.db p{color:var(--ts);font-size:13px;line-height:1.85;margin:0 0 7px}
.db p:last-child{margin-bottom:0}

/* inline subtitle */
.st{font-weight:600;color:var(--ac);font-size:13px}
strong{font-weight:600;color:var(--tp)}

/* ── Insights ── */
.ins-card{background:var(--sf);border:1px solid var(--bd);border-radius:var(--r);box-shadow:var(--sh);margin-bottom:14px;overflow:hidden}
.ins-card h3{font-size:13.5px;font-weight:600;padding:14px 18px 12px;margin:0;border-bottom:1px solid var(--dv);background:var(--al)}
.ins-row{padding:12px 18px;border-bottom:1px solid rgba(0,0,0,0.04)}
.ins-row:last-child{border-bottom:none}
.it{display:inline-block;font-size:10px;font-weight:600;letter-spacing:0.05em;color:#fff;border-radius:4px;padding:2px 8px;margin-bottom:8px}
.it-a{background:var(--ta)}.it-m{background:var(--tmt)}.it-r{background:var(--tr)}
.ins-row p{font-size:13px;color:var(--ts);line-height:1.85;margin:0 0 7px}
.ins-row p:last-child{margin-bottom:0}

/* ── Params ── */
.pm-label{font-size:12.5px;color:var(--tm);margin-bottom:12px}
.pm-name{font-size:12.5px;font-weight:600;color:var(--ts);padding:4px 12px;background:var(--sf);border:1px solid var(--bd);border-radius:6px;display:inline-block}
table{width:100%;border-collapse:collapse;font-size:12.5px;background:var(--sf);border-radius:var(--r);overflow:hidden;border:1px solid var(--bd);box-shadow:var(--sh)}
thead th{background:var(--sa);color:var(--ts);font-weight:600;text-align:left;padding:9px 14px;font-size:11.5px}
tbody td{padding:10px 14px;vertical-align:top;border-top:1px solid var(--dv);color:var(--ts);line-height:1.7}
tbody td:first-child{color:var(--tp);font-weight:600;width:90px;white-space:nowrap}
tbody tr:nth-child(even) td{background:var(--sa)}
.ps{margin-bottom:5px}.ps:last-child{margin-bottom:0}
.psl{display:inline-block;font-size:10px;font-weight:600;color:#fff;background:var(--ca);border-radius:3px;padding:1px 5px;margin-right:5px}

/* ── Prompts ── */
.sub-tab-bar{display:inline-flex;gap:2px;background:var(--dv);border-radius:6px;padding:2px;margin-bottom:14px}
.sub-tab{padding:5px 14px;font-size:11px;font-weight:600;color:var(--tm);background:transparent;border:none;border-radius:4px;cursor:pointer;transition:all 0.15s;white-space:nowrap;letter-spacing:0.02em}
.sub-tab:hover{color:var(--ts)}
.sub-tab.active{color:var(--tp);background:var(--sf);box-shadow:0 1px 3px rgba(0,0,0,0.08)}
.sub-pane{display:none}
.sub-pane.active{display:block}
.pr-item{background:var(--sa);border-radius:8px;padding:12px 14px;margin-bottom:8px;font-size:12.5px;line-height:1.7;color:var(--ts);white-space:pre-wrap}
.pr-item:last-child{margin-bottom:0}
.pr-label{font-size:10.5px;font-weight:600;color:var(--tm);margin-bottom:3px}
.pr-tag{font-size:10.5px;font-weight:600;color:var(--ca);background:rgba(126,127,166,0.1);display:inline-block;padding:2px 8px;border-radius:4px;margin-bottom:6px}

/* ── Combo strategy ── */
.combo-card{background:var(--sf);border:1px solid var(--bd);border-radius:var(--r);box-shadow:var(--sh);padding:16px 18px;border-left:3px solid var(--tr)}
.combo-card p{font-size:13px;color:var(--ts);line-height:1.85;margin:0 0 7px}
.combo-card p:last-child{margin-bottom:0}

.footer-pad{height:60px}
"""

def gen_js(is_multi_img):
    # 单图时需要复制 hero src 到缩略图（避免 base64 重复写入 HTML）
    copy_src_js = "" if is_multi_img else """
  var heroImg = document.getElementById('heroImg');
  var thumbImg = document.getElementById('thumbImg');
  if (heroImg && thumbImg) { thumbImg.src = heroImg.src; }"""

    return f'''<script>
document.addEventListener('DOMContentLoaded', function() {{
  var tabs = document.querySelectorAll('.tab-btn');
  var panes = document.querySelectorAll('.tab-pane');
  var bar = document.querySelector('.tab-bar');
  var hero = document.querySelector('.hero');
  var thumb = document.querySelector('.float-thumb');

  tabs.forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      tabs.forEach(function(b){{ b.classList.remove('active'); }});
      panes.forEach(function(p){{ p.classList.remove('active'); }});
      btn.classList.add('active');
      document.getElementById(btn.dataset.tab).classList.add('active');
    }});
  }});

  document.querySelectorAll('.sub-tab').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var bar = btn.parentElement;
      bar.querySelectorAll('.sub-tab').forEach(function(b){{ b.classList.remove('active'); }});
      bar.parentElement.querySelectorAll('.sub-pane').forEach(function(p){{ p.classList.remove('active'); }});
      btn.classList.add('active');
      document.getElementById(btn.dataset.subtab).classList.add('active');
    }});
  }});
{copy_src_js}
  window.addEventListener('scroll', function() {{
    if (!hero) return;
    var heroBottom = hero.getBoundingClientRect().bottom;
    if (heroBottom < 0) {{
      bar.classList.add('stuck');
      if (thumb) thumb.classList.add('show');
    }} else {{
      bar.classList.remove('stuck');
      if (thumb) thumb.classList.remove('show');
    }}
  }});
}});
</script>'''

def gen(data):
    validate(data)
    meta=data.get("meta",{})
    ml=f'{esc(meta.get("category",""))} · {esc(meta.get("description",""))} · {esc(meta.get("usage",""))}'
    imgs=data.get("images",[])
    uris=[img_b64(p) for p in imgs] if imgs else []
    img_html=r_imgs(uris)
    thumb_html=r_thumbs(uris)

    is_multi = len(uris) > 1
    combo = data.get("combo_strategy")
    has_combo = combo is not None and combo != ""

    tab_buttons = '''  <button class="tab-btn active" data-tab="t1">五维分析</button>
  <button class="tab-btn" data-tab="t2">核心洞察</button>
  <button class="tab-btn" data-tab="t3">风格参数</button>
  <button class="tab-btn" data-tab="t4">提示词</button>'''
    if has_combo:
        tab_buttons += '\n  <button class="tab-btn" data-tab="t5">组合策略</button>'

    combo_pane = ""
    if has_combo:
        combo_pane = f'''
<div id="t5" class="tab-pane">
{r_combo(combo)}
</div>'''

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>场景图分析报告</title>
<style>{CSS}</style>
</head>
<body>

{thumb_html}

<div class="wrap">

<div class="hero">
  <div class="hero-img">{img_html}</div>
  <div class="hero-info">
    <h1>场景图分析报告</h1>
    <div class="meta">{ml}</div>
    {r_overview(data.get("overview",{}))}
  </div>
</div>

<div class="tab-bar">
{tab_buttons}
</div>

<div id="t1" class="tab-pane active">
{r_dims(data.get("dimensions",{}))}
</div>

<div id="t2" class="tab-pane">
{r_insights(data.get("insights",[]))}
</div>

<div id="t3" class="tab-pane">
{r_params(data.get("style_params",{}))}
</div>

<div id="t4" class="tab-pane">
{r_prompts(data.get("prompts",{}))}
</div>
{combo_pane}

<div class="footer-pad"></div>
</div>

{gen_js(is_multi)}
</body>
</html>'''

def main():
    if len(sys.argv)<3:
        print("用法: python render_report.py <input.json> <output.html>",file=sys.stderr); sys.exit(1)
    with open(sys.argv[1],"r",encoding="utf-8") as f: data=json.load(f)
    with open(sys.argv[2],"w",encoding="utf-8") as f: f.write(gen(data))
    print(f"报告已生成: {sys.argv[2]}")

if __name__=="__main__": main()
