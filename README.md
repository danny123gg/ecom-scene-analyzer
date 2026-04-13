[中文版](README_zh.md) | English

# ecom-scene-analyzer

A Claude Code Skill for analyzing e-commerce scene photography (currently specialized in children's learning furniture), producing multi-dimensional visual analysis reports and AI image generation prompts.

One thing became increasingly clear while building this Skill: **the model's capability ceiling is far higher than most people assume, but that ceiling doesn't surface on its own.** It needs to be awakened — and the way you awaken it isn't a more clever prompt, it's how you see the world.

Your disciplinary range, your aesthetic sensitivity, your ability to distinguish phenomena from principles, your intuition that "there might be another layer here" — these determine how deep you can take AI.

In this sense, **a Skill is not just an automation tool — it's a model potential activation system**. Through carefully designed knowledge injection, analytical perspectives, and cognitive pathways, it guides the model from its default state of surface-level description to a depth that touches the essence of things.

This document explores how that understanding took shape.

<a href="https://github.com/user-attachments/assets/8173a4ed-6cd2-4396-9298-2b73aa130647" target="_blank"><img width="800" alt="Report Overview" src="https://github.com/user-attachments/assets/8173a4ed-6cd2-4396-9298-2b73aa130647" /></a>

---

## Skills Start from Dialogue with the Model

The methodology behind this Skill wasn't designed upfront. It emerged gradually through dialogue with the model.

The process went roughly like this: start with a few images, dialogue with the model from different dimensions, explore and probe. In the conversation, stimulate, align, calibrate — see under which perspectives the model produces analysis that makes you think "yes, that's the depth I'm looking for." Collect those good results along with the thinking process that produced them, then reverse-engineer them into methodology. That methodology becomes the Skill's foundation.

Then polish with different Cases.

This polishing process is critical. What it's essentially doing is **testing which cognitive paths are surface-level and which are essence-level.** An analytical angle that works on a few specific images might fail on a different one — then it's surface. Cognitive paths that survive different Cases are genuine essence, and those are what deserve to stay in the Skill.

---

There's an easily overlooked byproduct of this process: **building a Skill is itself a cognitive upgrade path for the designer.**

When you force yourself to articulate "why this image works" clearly enough to encode in a Skill for the model to execute — your own understanding deepens in the process. Many judgments you previously made by intuition get forced into explicit form, and that explicit articulation exposes fuzzy areas you hadn't noticed before.

A Skill isn't just a tool for others. **Building it is the process of turning tacit knowledge into explicit methodology, a process of increasing the designer's own cognitive density.**

The final Skill is frozen dialogue wisdom — letting others stand directly on this cognitive path without having to find their way from scratch.

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

## From Surface to Essence

The discussion above — "perspectives determine depth" — addresses how to make the model see deeper. But there's an equally important question: **once it sees deeper, what should the Skill retain?**

During iteration, a recurring tendency emerged: the model would extract specific visual features from a few images and solidify them as rules. For example, seeing that good scene photos used soft lighting, it would encode "must use soft lighting."

But soft lighting isn't the rule — it's one expression of the rule. The actual rule is: lighting in children's categories should serve a sense of safety — hard shadows on children trigger subconscious "unsafe" associations. Understanding this rule, soft lighting is just one means among others.

**Encoding the surface actually constrains the model** — you lock it into specific visual choices, and it can only imitate. **Encoding the essence activates the model** — you tell it "why," and it has room to flexibly apply that principle in new scenarios, producing solutions you didn't anticipate yourself.

A good Skill gives the model understanding, not instructions.

---

This "from surface to essence" principle applies not just to what the Skill encodes, but also to what it asks the model to produce.

"Key light enters from the right at 45°, soft light, low contrast" — that's **identification**, staying at "what."

"Soft light was chosen because hard shadows trigger 'unsafe' associations, and the core emotional need of the mother-and-baby category is safety" — that's **attribution**, reaching "why."

**Identification tells you "what." Attribution tells you "why."** The gap between these isn't a matter of detail — it's a difference in kind.

Identification isn't reusable — "this image uses soft light" helps nothing for the next image. But "soft light in children's categories fundamentally serves a safety need" transfers to packaging design, retail lighting, children's app interfaces — any context where safety is a core concern.

More importantly, attribution is what creates **resonance**. Identification makes people think "yes, correct." Attribution makes people think "ah, so that's why."

---

Above attribution sits another layer called **meta-thinking** — abstracting transferable principles from specific cases.

For example, from "the side view is the best angle for showing sitting posture" attributed to "because it's like a posture X-ray," jumping to "all products whose core selling point is body-state improvement should prioritize state readability over product appearance."

The latter is meta-thinking — a cognitive framework transferable to lumbar pillows, ergonomic keyboards, and entirely different categories.

**Analysis is valid within a specific Case. Insight is valid across Cases.** A Skill that only requires attribution produces analysis; requiring meta-thinking is what makes insight possible.

Looking back at these layers — Skill encoding essence rather than surface, output progressing from identification to attribution to meta-thinking — they're all doing the same thing: **pushing the model from "describing the surface" toward "grasping the essence."** The model doesn't lack the ability to reach the essence; it lacks a signal telling it "don't stop at the surface, keep going deeper." **Every layer of the Skill's design is that signal.**

---

## From Analysis to Generation

No matter how deep the analysis goes, if it can't be converted into executable generation instructions, it stays at the "understanding" stage. The other half of this Skill is prompt generation — turning all the analytical insights into prompts that can be directly fed to AI image generation tools.

The complexity of this step far exceeded expectations.

Analysis is "understanding why a good image works." Prompts are "instructing the generation of an equally good new image." This looks like a simple transfer from understanding to execution, but there's a massive gap in between: **the language of analysis is attributional ("why use soft lighting"), while prompt language must be descriptive ("natural light filtered through sheer curtains from the right").** You need to re-encode "why" back into "what" — but every detail of that "what" must have been forged through "why."

> **Prompts are not translations of style parameters — they are crystallizations of the entire analysis.** When the prompt says "cream-colored knit top," that's not a random color pick — it's the product of understanding that "the upper body overlaps with the chair back and should implement a stealth strategy, not competing for visual weight." When it says "a quiet afternoon," that's not atmospheric decoration — it's anchoring the exact usage scenario that triggers parental identification. It looks like describing a scene. It's actually encoding insight.

Two design choices in this "from essence to expression" conversion are worth mentioning.

**The first is "Step Zero"** — before filling in any parameters, describe a complete life scene in one sentence. For example: "A quiet afternoon, a well-behaved girl doing homework at her desk, sunlight streaming through sheer curtains." With this holistic image, clothing colors, props, and lighting are no longer isolated parameters requiring individual decisions — they grow naturally from the scene. This counters the model's tendency to "assemble from parameter tables," which produces technically correct but lifeless images.

**The second is the separation of content and design_notes** — content is pure execution instruction for AI generation tools, design_notes are decision explanations for designers. The model tends to unconsciously mix "why this color was chosen" into "what colors are in the scene." Separating the two is a structural countermeasure designed around an observed cognitive tendency.

> **On generation model choice**: The generated prompts are recommended for use with Google's Gemini model family. Tested with good results on Nano Banana 2 (Gemini 3.1 Flash Image). Prompt effectiveness correlates directly with the generation model's intelligence level — stronger models interpret visual semantics, spatial relationships, and character descriptions more accurately, producing noticeably better output.

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

This Skill's structure can be copied. Three separated knowledge files, five-dimension framework, six attribution perspectives, cognitive ladder — switch categories, replace domain knowledge, and the framework still holds.

But structure is just the skeleton. What determines a Skill's true depth are the judgments made while building it — "which perspectives to include," "how deep to push," "what to keep and what to discard." These judgments don't come from prompt techniques. They come from the understanding of human motivation you gained from psychology, the beyond-language perceptual ability you cultivated in art museums, the habit of questioning premises you formed through philosophical training — from the sensitivity to things that all your reading, experience, and thinking have deposited.

**AI is the sum of all known knowledge. A person with deep humanistic literacy is the conductor of that sum.** Doesn't need to play every instrument, but knows what section should sound at what moment.

---

This Skill is one attempt — freezing a cognitive pathway that emerged from dialogue, making it reusable for more people. But using it is itself a practice in activating model potential: category knowledge fills the model's domain blind spots, the attribution toolbox pushes it from phenomena to essence, the cognitive ladder guides it from analysis to insight. **This logic isn't limited to e-commerce photo analysis — it's a Skill design paradigm transferable to any domain.**

And at a larger scale, there's a question worth serious consideration by everyone working with AI:

Model intelligence is advancing rapidly, but human cognitive bandwidth and knowledge reserves have inherent limits. Today you can activate the model's depth by providing six analytical perspectives. But when the model's capability ceiling far exceeds the number of perspectives you can think of, the bottleneck is no longer the model — **the bottleneck is the human.**

**How to more effectively activate model potential may be the most central and urgent question in human-AI collaboration.** It's not just a technical question — it's a question about human growth itself. This Skill is one small-scale experiment toward that question, but far from an answer. The answer needs more people exploring together.

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
└── scripts/
    └── render_report.py           # JSON → interactive HTML
```

## License

[CC BY-NC-SA 4.0](LICENSE)
