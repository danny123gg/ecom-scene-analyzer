---
name: ecom-scene-analyzer
description: 分析儿童学习家居（学习桌、学习椅）电商场景图，输出多维度视觉分析报告，并基于分析结果生成模特塑造和场景塑造的 AI 提示词。当用户上传相关产品的场景图、主图或竞品参考图时触发，包括"帮我看看这张图""分析一下这几张竞品图"等表述。
---

# 儿童学习家居电商场景图分析与提示词生成 Skill

## 这个 Skill 做什么

从电商场景图中提取视觉策略，通过多维度归因解释"为什么这样做是有效的"，并基于分析结果生成可直接用于 AI 生成工具的模特塑造和场景塑造提示词。

好的分析不只是告诉设计师"这张图做了什么"，更要让设计师理解"为什么这样做"——只有理解了背后的原因，才能在新场景中灵活复用而非机械模仿。提示词则将这些理解转化为可执行的生成指令。

核心理念：**用场景替代说明书，用视觉心理替代文字说服。** 电商场景图的本质不是"拍产品"，而是构建一个消费者愿意走进去的生活切片。

## 适用范围

- **产品品类**：学习桌、学习椅、儿童人体工学椅
- **图片类型**：场景图（详情页用）、主图（搜索列表用）

## 品类认知

儿童学习家居有经过市场验证的视觉共识，详见 `references/category-knowledge.md`。分析前先读取该文件，分析时作为背景知识参考，帮助判断一张图是"遵循共识"还是"有意突破"，归因时帮助解释视觉选择背后的品类逻辑。

---

## 操作流程（必须遵守）

按以下步骤依次执行，不要跳步：

1. **读取品类知识**：`view` 读取 `references/category-knowledge.md`
2. **读取分析指引并分析图片**：`view` 读取 `references/analysis-guide.md`，按其中的分析方法论和字段定义逐维度分析图片，将结果写入 `/home/claude/analysis.json`。JSON 结构严格遵循下方骨架。注意：
   - `images` 字段填写原始文件路径（如 `/mnt/user-data/uploads/xxx.png`），脚本会自动转 base64
   - `style_params` 中 `character_surface`（表象）和 `character_essence`（本质）分开填写
   - 文本字段严格遵循分析指引中的排版规范
3. **读取提示词指引并生成提示词**：`view` 读取 `references/prompt-guide.md`，在思考中完成前置决策，然后补充 JSON 的 `prompts` 部分。注意：
   - `prompts` 全部使用中文，`scene` 不包含产品本身
   - 每条提示词为 `{ "label": "标签", "content": "提示词正文" }` 格式，`model` 层额外包含 `design_notes` 字段

   **⚑ 提示词自检**（JSON 落盘前，在思考中完成，不需要输出检查过程）：
   - **content 是否纯净？** 扫描每条 content，搜索「而非原版」「替代」「选X而非Y」「比X更」「因为」「目的是」等比较性/解释性语言。如发现，将其移至 design_notes。唯一允许的对比是气质锁定句式（"是A而非B"描述目标状态）
   - **每条 content 是否包含画幅比例和主体占比参数？** 缺失则补充
   - 两条提示词之间是否有真实差异——变体是否只是基准的措辞改写？如果是，重新设计可变元素的替换方案
   - 如有遗漏，补充后再写入 JSON。如自检发现遗漏，直接在 JSON 中补充修正后再落盘。

4. **运行渲染脚本**：`bash` 执行 `python /mnt/skills/user/ecom-scene-analyzer/scripts/render_report.py /home/claude/analysis.json /mnt/user-data/outputs/场景图分析-[简短标识].html`，其中 `[简短标识]` 取自 `meta.description` 的关键词（如 `场景图分析-背面坐姿场景图.html`）。如果脚本报错，根据 stderr 中的错误信息定位并修正 `analysis.json` 中的问题字段，然后重新执行脚本，不要重新生成整份分析。
5. **交付**：用 `present_files` 展示生成的 HTML 文件。对话中只说一句简短引导语，如"分析报告已生成，请查看"

**禁止**：不要手动编写任何 HTML/CSS。不要在对话中直接输出分析文字。所有视觉渲染由脚本完成。

**异常处理**：如果上传的图片不属于适用范围（非儿童学习家居产品）、图片模糊无法辨认、或缺少关键信息（如没有人物的纯产品图），直接告知用户并说明原因，不要强行套用分析框架。

**渲染说明**：最终报告是 Tab 交互式布局——图片与总体印象在顶部并排展示，「五维分析」「核心洞察」「风格参数提取」「提示词生成」分为四个 Tab 切换查看，Tab 栏在滚动时会置顶，图片会缩小悬浮在左上角供随时对照。

---

## JSON 结构总览

完整的 JSON 骨架如下。分析相关字段（meta ~ style_params）的详细定义在 `references/analysis-guide.md`，提示词字段（prompts）的定义在 `references/prompt-guide.md`。

```json
{
  "meta": { "category": "", "description": "", "usage": "" },
  "images": [],
  "overview": { "type": "", "consensus": "", "strategy": "" },
  "dimensions": {
    "angle": { "observation": "", "attribution": "" },
    "light": { "observation": "", "attribution": "" },
    "color": { "observation": "", "attribution": "" },
    "comp":  { "observation": "", "attribution": "" },
    "model": { "observation": "", "attribution": "" }
  },
  "insights": [
    { "title": "", "attribution": "", "meta_thinking": "", "reuse": "" }
  ],
  "style_params": {
    "template_name": "",
    "camera": "", "lighting": "", "color_tone": "",
    "human_chair_space": "",
    "character_surface": "", "character_essence": "",
    "growth_narrative": "", "props": "", "composition": "",
    "key_constraints": ""
  },
  "prompts": {
    "model": [{ "label": "", "design_notes": "", "content": "" }],
    "scene": [{ "label": "", "content": "" }],
    "combined": [{ "label": "", "content": "" }]
  }
}
```
