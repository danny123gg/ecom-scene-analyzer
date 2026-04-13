[中文版](README_zh.md) | English

# ecom-scene-analyzer

A Claude Code Skill for analyzing e-commerce scene photography (currently specialized in children's learning furniture), producing multi-dimensional visual analysis reports and AI image generation prompts.

One thing became increasingly clear while building this Skill: **the model's capability ceiling is far higher than most people assume, but that ceiling doesn't surface on its own.** It needs to be awakened — and the way you awaken it isn't a more clever prompt, it's how you see the world.

Your disciplinary range, your aesthetic sensitivity, your ability to distinguish phenomena from principles, your intuition that "there might be another layer here" — these determine how deep you can take AI.

In this sense, **a Skill is not just an automation tool — it's a model potential activation system**. Through carefully designed knowledge injection, analytical perspectives, and cognitive pathways, it guides the model from its default state of surface-level description to a depth that touches the essence of things.

This document explores how that understanding took shape.

<a href="https://github.com/user-attachments/assets/8173a4ed-6cd2-4396-9298-2b73aa130647" target="_blank"><img width="800" alt="Report Overview" src="https://github.com/user-attachments/assets/8173a4ed-6cd2-4396-9298-2b73aa130647" /></a>

---

## Perspectives Determine Depth

Most people who've used AI have noticed this: the same question, asked differently, can produce dramatically different quality answers.

This is common enough, but it's easy to file under "prompt techniques" — as if mastering certain phrasing would reliably unlock better results.

Building this Skill made me think it's not that simple.

When analyzing scene photos, asking the model to "analyze composition, lighting, and subjects" produced clean, organized, basic analysis.

Then switching to a different set of lenses — psychology, marketing — the analysis jumped a level.

The model began explaining how **mirror neurons** create parental identification when the child doesn't look at the camera, how the absence of text is a **high-context communication** strategy, how two images form a complementary **consumer decision pathway**.

The model had this knowledge all along. But in the first round, all of it stayed dormant.

These capabilities need a signal to activate — and **that signal is the analytical perspective you provide**.

---

This kept proving true through subsequent iterations.

Adding **cultural semiotics**, the model could read a children's painting on the floor as a class-identity signal — "this family values artistic education."

Adding **sensory synesthesia**, it could analyze how warm light filtered through curtains triggers a temperature association, giving a flat image a sense of physical space.

Each new dimension didn't just add another paragraph — it opened an entirely invisible analytical layer.

So returning to that initial observation — "different phrasing yields different quality" — the essence isn't phrasing difference, it's **perspective difference**.

The model's analytical capability works more like a function: input is the set of perspectives you provide, output is the corresponding depth of analysis. The richer and more cross-disciplinary the perspectives, the more layered the output.

---

This understanding directly shaped the Skill's design direction.

A Skill's core job isn't constraining the model's behavior — "you must output in this format" — but **configuring a set of lenses through which it observes the world**.

The "attribution toolbox" in this Skill — six analytical perspectives: visual design principles, psychological mechanisms, marketing strategy, category-specific knowledge, cultural semiotics, sensory synesthesia — does exactly this.

But an uncomfortable question follows immediately: **who decides which lenses to include?**

Choosing "look at this through a psychology lens" requires having some sensitivity to consumer psychology yourself. Choosing "look at this through sensory synesthesia" requires that when you stand before the image, you can feel the warmth the light suggests.

Without these sensitivities, you wouldn't think to include these perspectives in the toolbox — not because you don't know these concepts exist, but because you lack the intuition to connect a cross-disciplinary concept to the specific commercial image in front of you.

This intuition is hard to describe as a "skill." It's more like a sensitivity that slowly sediments from long immersion in different disciplines and aesthetic experiences.

A nose for "there might be another layer here."

This means **the Skill designer's cognitive boundary becomes the ceiling of the Skill's output quality**. The Skill can be copied, but the judgment behind which lenses to include cannot.

---

## Observations Are Not Principles

An interesting pitfall came up during construction.

The initial dialogue rounds were based on a few specific images. The model identified visual features — hardwood floors, light-colored plush carpet, child not facing the camera, warm yellow tones — and when abstracting into a Skill, these features were directly encoded as rules.

As if every good children's chair scene photo needed hardwood floors and plush carpet.

Testing with new images exposed the problem. An excellent photo with gray tile floors, white walls, and a child smiling at the camera violated every "rule" in the Skill.

---

What went wrong?

Hardwood floors, plush carpet, not facing the camera — these are **observations**, not **principles**.

They're specific choices made in those particular images, not universal laws about what a good scene photo looks like.

The real principle lives one layer below: floor material should unify with the overall spatial style and convey the target audience's aesthetic identity. This principle manifests as entirely different floor materials in different scenarios, all valid.

This mistake is actually very common — not just AI, humans do it constantly. We naturally tend to extract patterns from limited samples and treat patterns as laws.

See warm tones in three good photos, conclude "good photos should use warm tones." But warm tones are just one expression of the principle "convey warmth and safety." Cool tones can also convey safety in another context, as long as the overall visual language is unified.

---

After recognizing this, the Skill's architecture underwent a significant restructuring.

What's encoded in the Skill was divided into three layers:

- **Hard constraints** — physical laws (human-chair proportion, perspective consistency, light-shadow direction), never violable
- **Category defaults** — industry consensus (warm tones, soft lighting, tidy environment), overridable
- **User customization** — Case-level choices (specific clothing color, room type, props), fully flexible

**A Skill should encode principles, not phenomena.**

This sounds like an obvious truism, but distinguishing the two in practice is harder than it looks.

---

## Attribution Is the Soul

After the Skill was running, another problem emerged.

The output analysis was detailed and comprehensive across dimensions, but reading it always felt like something was missing.

Eventually it became clear: it was doing identification, not attribution.

---

"Key light enters from the right at 45°, soft light, low contrast" — that's identification.

"Soft light was chosen because hard shadows on children subconsciously trigger 'unsafe' associations, and the core emotional need of the mother-and-baby category is safety" — that's attribution.

The gap between these isn't a matter of detail. It's a **difference in kind**.

**Identification tells you "what." Attribution tells you "why."**

---

Identification isn't reusable — "this image uses soft light" helps nothing for the next image.

But "soft light in children's categories is fundamentally serving a safety need" transfers to any category where safety is a core concern. Packaging design, retail lighting in mother-and-baby stores, children's app interface color schemes — the attribution holds across all of them.

More importantly, attribution is what creates **resonance** in the reader.

Identification makes people think "yes, correct." Attribution makes people think "ah, so that's why."

A report with only identification leaves you knowing facts without being sure why they matter. A report with attribution leaves you understanding the complete persuasion logic behind an image, and knowing how that logic can transfer.

---

This Skill ultimately established six attribution perspectives, not as a "more is better" checklist, but to cover the different dimensions of "why does a person get persuaded by an image."

It might work at the visual design level, the psychological level, or the cultural identity level. These dimensions aren't mutually exclusive — the same visual element often operates across multiple levels simultaneously.

Above attribution sits another layer called **meta-thinking**.

Attribution answers "why is this image effective." Meta-thinking answers "what transferable principle lies behind this that can be carried to other domains entirely."

For example, from "the side view is the best angle for showing sitting posture" attributed to "because it's like a posture X-ray," jumping to "all products whose core selling point is body-state improvement should prioritize state readability over product appearance."

The latter is meta-thinking — a cognitive framework transferable to lumbar pillows, ergonomic keyboards, and entirely different categories.

This is the dividing line between analysis and insight. Analysis is valid within a specific Case. Insight is valid across Cases.

A Skill that only requires attribution produces analysis; requiring meta-thinking is what makes insight possible.

Looking back at these design layers — perspective injection, attribution toolbox, meta-thinking requirements — they're all doing the same thing: **pushing the model from "describing the surface" toward "grasping the essence."** The model doesn't lack the ability to reach the essence; it lacks a signal telling it "don't stop at the surface, keep going deeper." **Every layer of the Skill's design is that signal.**

---

## From Analysis to Generation

The other half of this Skill is prompt generation — based on analysis results, producing prompts that can be directly used with AI image generation tools.

> **Prompts are not translations of style parameters — they are crystallizations of the entire analysis.** They read like surface-level descriptions — what color, what angle, what clothing — but every specific choice is a distillation of the deeper analysis. When the prompt says "cream-colored knit top," that's not a random color pick — it's the product of understanding that "the upper body overlaps with the chair back and should implement a stealth strategy, not competing for visual weight." When it says "a quiet afternoon," that's not atmospheric decoration — it's anchoring the exact usage scenario that triggers parental identification. It looks like describing a scene. It's actually encoding insight.

> **On generation model choice**: The generated prompts are recommended for use with Google's Gemini model family. Tested with good results on Gemini Nano and Imagen (Banana2). Prompt effectiveness correlates directly with the generation model's intelligence level — stronger models interpret visual semantics, spatial relationships, and character descriptions more accurately, producing noticeably better output.
>
> From another angle, using this Skill is itself a process of activating the model's potential — category knowledge supplements its vertical domain cognition, the attribution toolbox configures cross-disciplinary analytical perspectives, and the cognitive ladder guides it from identification to insight. A Skill isn't just an execution script; it's a carefully designed set of cognitive activation signals.

Two design choices are worth mentioning.

**The first is "Step Zero."** Before filling in any parameters, describe a complete life scene in one sentence — "A quiet afternoon, a well-behaved girl doing homework at her desk, sunlight streaming through sheer curtains."

With this image in mind, clothing colors, prop choices, and lighting direction are no longer isolated parameters requiring individual decisions — they grow naturally from the scene.

This solves the problem of models "assembling from parameter tables" which produces technically correct but lifeless images. Whole-first, then parts — not parts-first, then assembly.

**The second is the separation of content and design_notes.** The prompt body (content) is pure execution instruction for AI generation tools; design notes (design_notes) are decision explanations for designers.

The model tends to unconsciously mix "why this color was chosen" into "what colors are in the scene" — it has an inclination to explain its own choices. Separating the two is a structural countermeasure designed around an observed cognitive tendency.

There are quite a few similar small designs — requiring variants to cover different dimensions rather than just rephrase, self-checking for aspect ratio and subject proportion inclusion — each backed by a real problem encountered during iteration.

Accumulated together, they form a map of the model's cognitive tendencies.

---

## Making Thinking Visible

The presentation of results is also worth investing in.

Analysis content is rendered into an interactive HTML report: source image and overview displayed side by side, four tabs switching between five-dimension analysis, core insights, style parameters, and prompts. The tab bar sticks on scroll, the source image shrinks to a floating thumbnail for reference.

Different cognitive layers are carried by different visual hierarchies — observation and attribution presented separately, core insights' three-level progression (attribution → meta-thinking → reuse suggestions) each in their own block.

<p>
<a href="https://github.com/user-attachments/assets/3ff4f544-1aea-4cb2-bb76-893a0df48b4b" target="_blank"><img width="32%" alt="Core Insights" src="https://github.com/user-attachments/assets/3ff4f544-1aea-4cb2-bb76-893a0df48b4b" /></a>
<a href="https://github.com/user-attachments/assets/3a23a953-81ba-484f-89a3-36993bb9c6d1" target="_blank"><img width="32%" alt="Style Parameters" src="https://github.com/user-attachments/assets/3a23a953-81ba-484f-89a3-36993bb9c6d1" /></a>
<a href="https://github.com/user-attachments/assets/c04ff253-2461-44e5-b20b-a08d053eac70" target="_blank"><img width="32%" alt="Prompt Generation" src="https://github.com/user-attachments/assets/c04ff253-2461-44e5-b20b-a08d053eac70" /></a>
</p>

**Deep thinking deserves to be clearly seen.**

This aligns with the Skill's own philosophy: not a black box, but a cognitive pathway visible at every step.

---

## Returning to the Beginning

This Skill's structure — three separated knowledge files, five-dimension analysis framework, six attribution perspectives, cognitive ladder — all of this can be copied.

Switch to a different category, replace the domain knowledge file, and the framework still holds.

But the judgments made while building this framework — including sensory synesthesia in the toolbox rather than something else, requiring meta-thinking rather than stopping at attribution, distinguishing observations from principles rather than conflating them — these judgments come from the designer's own accumulation.

Not any one specific kind of accumulation, but the sensitivity to things that sediments from all reading, experience, and thinking combined.

---

The model's capability is the same for everyone. But how far each person can awaken it differs.

The difference isn't in who has mastered better prompt techniques, but in who can provide richer perspectives, more accurate judgments, deeper lines of questioning.

The source of these things is the understanding of human motivation you gained from psychology, the beyond-language perceptual ability you cultivated in art museums, the habit of questioning premises you formed through philosophical training, the sensitivity to the world that all your experiences have deposited.

AI is the sum of all known knowledge. A person with deep humanistic literacy is the conductor of that sum — doesn't need to play every instrument, but knows what section should sound at what moment.

This Skill is one attempt. It tries to freeze a cognitive pathway that emerged from dialogue, making it reusable for more people.

But it's more than a reusable tool. Using this Skill is itself a practice in activating model potential — you'll see how category knowledge fills the model's vertical domain blind spots, how the attribution toolbox pushes it from "describing phenomena" to "explaining essences," how the cognitive ladder guides it from analysis to insight. This logic of moving from surface to core isn't limited to e-commerce photo analysis — it's a Skill design methodology transferable to any domain.

And this is the final reminder: what truly determines the depth of output isn't the Skill's structure, but whether the person designing the Skill has the ability to grasp the essence of things rather than stopping at the surface — and how much they're willing to invest in their own depth.

There's also a longer-term question worth considering. Model intelligence is advancing rapidly, but human cognitive bandwidth and knowledge reserves have inherent limits. As the model's capability ceiling keeps rising while the human conductor's bandwidth doesn't scale proportionally, **how to more effectively activate model potential may become the most central question in human-AI collaboration**. This Skill is one small-scale experiment toward that question, but far from an answer. The answer needs more people exploring together.

---

## Getting Started

**Prerequisites**: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI or desktop app, or use [claude.ai](https://claude.ai) directly. Python 3.6+ (for report rendering).

**Install**: Download the `.skill` file from [Releases](../../releases) and install in Claude Code. If using claude.ai, upload the Skill file contents as project knowledge.

**Usage**: Upload an e-commerce scene photo and say "帮我分析这张场景图" or "Analyze this scene photo." The Skill triggers automatically, producing an interactive HTML analysis report.

---

## Category Adaptation

1. Replace `references/category-knowledge.md` — write your category knowledge. Key: write principles, not phenomena. Not "use soft lighting," but "soft lighting serves the safety need — hard shadows trigger unsafe associations."
2. Mostly keep `references/analysis-guide.md` — the five-dimension framework and attribution toolbox are category-agnostic.
3. Adjust `references/prompt-guide.md` and `SKILL.md` as needed.

---

## File Structure

```
ecom-scene-analyzer/
├── SKILL.md                       # Skill definition and execution flow
├── references/
│   ├── category-knowledge.md      # Domain knowledge
│   ├── analysis-guide.md          # Analytical methodology
│   └── prompt-guide.md            # Prompt generation guidelines
├── scripts/
│   └── render_report.py           # JSON → interactive HTML
└── docs/
```

## License

[CC BY-NC-SA 4.0](LICENSE)
