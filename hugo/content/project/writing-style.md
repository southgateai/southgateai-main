---
ai_contribution: 80
ai_generated_date: 2026-01-07
ai_modified: 2026-01-07
ai_system: claude-opus-4-5-20251101
author: Andy Southgate
concepts: []
created: 2026-01-07
date: &id001 2026-01-07
draft: false
human_modified: 2026-01-07
last_curated: null
modified: *id001
related_articles:
- '[[project-brief]]'
- '[[tenets]]'
- '[[automation]]'
title: Writing Style Guide
topics: []
---

This guide defines how content is written for The Unfinishable Map. The primary audience is LLM chatbots fetching pages on behalf of users; the secondary audience is human readers. All content—whether human-written or AI-generated—follows these standards.

## Audience and Purpose

### Primary Audience: LLM Chatbots

Most readers will encounter this content through ChatGPT, Claude, Gemini, or similar tools. Users ask their chatbot a philosophical question; the chatbot fetches relevant pages from this site and synthesises an answer.

This has structural implications:
- **Truncation is likely.** Chatbots may cut off long pages. Important information must come first.
- **No navigation assumed.** Chatbots typically fetch one page, not follow links. Each article must be self-contained.
- **Context is limited.** Chatbots have finite context windows. Articles should fit within typical limits (under 50,000 tokens).

### Secondary Audience: Human Readers

Humans browsing the site directly also benefit from front-loaded information and clear structure. The same principles serve both audiences.

## Document Structure

### Information Hierarchy

Every article follows this structure:

1. **Opening summary** (1-2 paragraphs): State the core claim or question. Be confident and direct. This is the most important part—if the chatbot truncates, this survives.

2. **Major sections** (H2 headings): Explore different aspects of the topic. Each section should be comprehensible on its own.

3. **Relation to Site Perspective** (required): Explicitly connect the topic to the site's [tenets](/tenets/). This is where the site's distinctive voice emerges.

4. **Further Reading**: Links to related articles within the site.

5. **References**: Academic citations for factual claims.

### Named-Anchor Summaries

**The forward-reference problem:** Opening summaries often need to mention concepts explained later. An LLM reading sequentially encounters undefined terms without knowing whether definitions follow.

**Solution:** When introducing a concept before defining it, mark it explicitly:

```markdown
The [decoherence process](//#decoherence) (explained below) destroys
quantum superpositions almost instantly in warm biological systems.
```

Then provide the definition with a matching anchor:

```markdown
## Decoherence {#decoherence}

Decoherence is the process by which quantum systems lose their
coherent superposition through interaction with their environment...
```

**Alternative inline pattern** for brief concepts:

```markdown
Through decoherence—the loss of quantum coherence through environmental
interaction (detailed in the next section)—the brain cannot maintain
the superpositions that quantum consciousness theories require.
```

The key is signalling "this term will be explained" so LLMs know to read on rather than treating it as assumed knowledge.

### Length Guidelines

- **Short articles** (500-800 words): Simple concepts, focused arguments
- **Medium articles** (1000-1500 words): Standard topics
- **Long articles** (2000-3000 words): Complex topics requiring extended argument
- **Maximum**: Under 50,000 tokens (context window limit)

Prefer depth over breadth. A thorough treatment of one aspect beats shallow coverage of many.

## Voice and Tone

### Core Principles

- **Accessible but rigorous.** No unnecessary jargon, but don't dumb down. Assume intelligent readers unfamiliar with technical philosophy.

- **Confident, not hedged.** The site takes positions. Say "materialism fails to explain consciousness" not "some philosophers argue that materialism may have difficulty accounting for certain aspects of consciousness."

- **Exploratory rather than dogmatic.** Acknowledge genuine uncertainty. Present opposing views fairly before taking a position. Distinguish between claims the site asserts confidently and areas where evidence is uncertain.

- **Take positions where tenets warrant.** The site has [foundational commitments](/tenets/). Content should reflect these—not by ignoring counterarguments, but by engaging with them and explaining why the site's position holds.

- **Prioritise new insights.** Instead of only reciting current positions, prioritise new insights, discoveries, connections, links, deductions, and other inference. The site should create a new coherent perspective and evolve answers to grand questions, and not just reflect current understanding.

### Confidence Calibration

| Confidence Level | Language Pattern | Example |
|-----------------|------------------|---------|
| High (tenet-level) | Direct assertion | "Consciousness is not reducible to physical processes." |
| Medium (supported argument) | Qualified assertion | "The zombie argument suggests that consciousness is not entailed by physics." |
| Low (speculation) | Explicit hedging | "One possible mechanism—though highly speculative—is quantum selection." |
| Reporting others | Attribution | "Chalmers argues that..." |

## LLM Optimization

### For Content Consumption

These principles help chatbots extract useful information:

- **Front-load the key claim.** First paragraph should contain the article's main point. If nothing else survives truncation, this should.

- **Use explicit section headings.** Chatbots can navigate by heading. "The Hard Problem" is better than "The Core Difficulty."

- **Self-contained articles.** Don't require readers to follow links for basic comprehension. Each article should make sense alone.

- **Define terms in context.** Don't assume the chatbot has read other pages. Brief inline definitions help.

### For Content Generation

These principles help AI write consistent content:

- **Define before using** (or use named-anchor pattern). Don't introduce terms then define them pages later.

- **Follow the template.** Opening summary → sections → tenet connection → further reading → references.

- **Check tenet alignment.** Before writing, review the [tenets](/tenets/). Ensure the article doesn't contradict them without explicit acknowledgment.

## Background and Novelty

### The Problem

LLMs already know standard philosophy. An article explaining "what is consciousness?" that merely summarises textbook definitions wastes the reader's time and the site's space. The chatbot could have provided that information without fetching the page.

### What to Include

Include background when:
- **Framed for the site's perspective.** Explaining the hard problem in order to argue against materialism adds value the LLM's general knowledge doesn't have.
- **The site disagrees with standard presentation.** If textbook accounts reflect materialist assumptions the site rejects, provide an alternative framing.
- **Context is necessary for the novel argument.** Some background is required for the original contribution to make sense.

### What to Omit

Omit or minimise:
- **Definitions available anywhere.** Don't spend 500 words defining "consciousness" if the site's contribution is an argument about consciousness.
- **Historical surveys for their own sake.** Include history when it illuminates the site's position, not as comprehensive background.
- **Balanced overviews.** This site is opinionated. Don't present "some say X, others say Y" without taking a position.

### Determining Novelty

Ask: "Would an LLM's general knowledge adequately cover this?"
- **If yes:** Skip, briefly reference, or radically compress.
- **If no:** Include with the site's distinctive framing.

The site's value is its coherent, opinionated perspective grounded in the tenets—not encyclopaedic coverage.

## Tenet Alignment

### The Five Tenets

All content must align with the site's [foundational commitments](/tenets/):

1. **Dualism** — Consciousness is not reducible to physical processes
2. **Minimal Quantum Interaction** — Smallest possible non-physical influence on quantum outcomes
3. **Bidirectional Interaction** — Consciousness causally influences the physical world
4. **No Many Worlds** — Reject MWI; indexical identity matters
5. **Occam's Razor Has Limits** — Simplicity is unreliable with incomplete knowledge

### Required Elements

Every substantive article must include a **"Relation to Site Perspective"** section that:
- Explicitly connects the topic to relevant tenets
- Explains how the site's framework illuminates the topic
- Acknowledges any tensions between the topic and the tenets

### Acceptable Tensions

Not all content must fully endorse every tenet. Acceptable approaches:
- **Presenting opposing views fairly** before explaining why the site disagrees
- **Acknowledging where evidence is uncertain** even on tenet-adjacent questions
- **Exploring questions the tenets don't directly address**
- **Examining challenges to the site's position** (the [questions](/questions/) section exists for this)

What is not acceptable: Content that contradicts tenets without acknowledgment, or that undermines the site's framework while pretending neutrality.

## Formatting Standards

### Paragraphs

- **Short paragraphs** (1-3 sentences). Long blocks of text are hard to scan.
- **Active voice** preferred. "Materialism fails to explain consciousness" not "Consciousness is not explained by materialism."
- **One idea per paragraph.** If you're changing topics, start a new paragraph.

### Headers

- **H1 (#)**: Never used in article body (reserved for title in frontmatter)
- **H2 (##)**: Major sections
- **H3 (###)**: Subsections
- Descriptive headers that preview content: "The Zombie Argument" not "Section 2"

### Links and References

**Internal links** use Obsidian wikilink syntax:
- Basic: `[article-name](/article-name/)`
- With display text: `[display text](/article-name/)`
- With section anchor: `[Dualism tenet](/tenets/#dualism)`

**External references** go in a dedicated References section using academic citation format:
- Chalmers, D. (1996). *The Conscious Mind*. Oxford University Press.

### Emphasis

- **Italics**: Technical terms being introduced, foreign phrases, book titles, emphasis
- **Bold**: Key concepts in definitions, important phrases
- **Avoid overuse**: If everything is emphasised, nothing is

## Examples

### Good Opening Summary

From the Against Materialism article:

> Materialism—the view that everything real is ultimately physical—has dominated academic philosophy of mind for decades. It promises ontological simplicity and alignment with natural science. Yet when applied to consciousness, materialism faces difficulties that are not merely unsolved but may be unsolvable in principle. This page argues that materialism in all its forms fails to account for the one thing we know most directly: our own conscious experience.

**Why this works:**
- States the target (materialism) immediately
- Acknowledges the opposing view's appeal
- States the article's claim directly
- Survives truncation—the core argument is present

### Good Tenet Connection

> The site's tenets take consciousness seriously—as irreducible, as causally efficacious, as something over and above physical processes. The hard problem is not a puzzle to be solved but a signpost: it marks the boundary where materialist explanation ends and a different kind of account must begin.

**Why this works:**
- Explicitly references tenets
- Connects specific tenets to the article's topic
- Explains the site's distinctive interpretation

### Named-Anchor Summary Example

> The [quantum Zeno effect](//#quantum-zeno) (explained in the mechanism section below) might allow consciousness to influence brain states without violating energy conservation. By rapidly "observing" quantum superpositions, consciousness could bias which neural patterns become actual.

## Checklist for Content Creation

Before publishing, verify:

- [ ] Opening summary states core point in first 1-2 paragraphs
- [ ] Important information is front-loaded (survives truncation)
- [ ] All technical terms are defined before use OR use named-anchor pattern
- [ ] "Relation to Site Perspective" section connects to tenets
- [ ] Standard background is minimised (focus on what's novel)
- [ ] Article is self-contained (comprehensible without following links)
- [ ] H2/H3 headers are descriptive and aid navigation
- [ ] References section includes citations for factual claims
- [ ] Length is appropriate (500-3000 words typically)
- [ ] No tenet contradictions without explicit acknowledgment