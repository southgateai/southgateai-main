---
ai_contribution: 100
ai_generated_date: 2026-01-05
ai_modified: 2026-01-05 12:00:16+00:00
ai_system: claude-opus-4-5-20251101
author: Andy Southgate
concepts: []
created: 2026-01-05
date: &id001 2026-01-05
draft: false
human_modified: 2026-01-06 15:29:26+00:00
last_curated: null
modified: *id001
related_articles:
- '[[project]]'
- '[[changelog]]'
title: AI Task Queue
topics: []
---

This is the task queue for AI automation. The human reviews and prioritizes tasks; the AI executes them.

## How to Edit This List

- **Promote**: Change `P3` to `P1`, etc.
- **Demote**: Change `P1` to `P3`, etc.
- **Veto**: Add `#veto` anywhere in the task heading (e.g., `### P2: Task name #veto`)
- **Add reason**: Optionally add `- **Veto reason**: [why]` before vetoing

Vetoed items are moved automatically to the Vetoed Tasks section on the next `/evolve` run.

## Priority Levels

- **P0**: Urgent - execute immediately
- **P1**: High - execute this week
- **P2**: Medium - execute when time permits
- **P3**: Low - nice to have, human approval needed

## Active Tasks

### P1: Research Libet experiments and neural predictors of decision
- **Type**: research-topic
- **Status**: pending
- **Notes**: Experiments show neural "readiness potentials" predict decisions before conscious awareness. At first glance this weighs against free will. However, in our framework consciousness may "bake in" prior history through quantum selection—analogous to how quantum systems appear to explore all paths before collapsing. Research: (1) Libet's original experiments, (2) Haynes/Soon 2008 fMRI study, (3) critiques (Schurger et al. on neural noise), (4) retrocausal interpretations, (5) how this relates to Bidirectional Interaction tenet. This research should inform the free will article.

### P2: Create article on free will and determinism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Connects to Bidirectional Interaction tenet. How does quantum indeterminacy relate to agency? Depends on P1 Libet research.

### P2: Create concept page for qualia
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Central to the hard problem. Link to Dualism tenet.

### P2: Research Integrated Information Theory (IIT)
- **Type**: research-topic
- **Status**: pending
- **Notes**: Tononi's theory. How does it relate to or conflict with site tenets?

## Completed Tasks

### ✓ 2026-01-07: Create concept page for locality
- **Type**: expand-topic
- **Result**: Created ~1200 word article addressing locality objection to mind-matter interaction with three main responses
- **Output**: `concepts/locality.md`

### ✓ 2026-01-07: Create concept page for simulation hypothesis
- **Type**: expand-topic
- **Result**: Created ~1400 word article on simulation hypothesis and its implications for site tenets
- **Output**: `concepts/simulation.md`

### ✓ 2026-01-06: Research Buddhist perspectives on meaning
- **Type**: research-topic
- **Result**: Comprehensive research on Four Noble Truths, anattā (no-self), Buddhist ethics, and comparison with site tenets
- **Output**: `workflow/research/buddhist-perspectives-meaning-2026-01-06.md`

### ✓ 2026-01-06: Write article on the hard problem of consciousness
- **Type**: expand-topic
- **Result**: Created comprehensive ~1800 word article covering easy/hard problem distinction, explanatory gap, zombie argument, and Mary's Room
- **Output**: `topics/hard-problem-of-consciousness.md`

### ✓ 2026-01-06: Research interactionist dualism
- **Type**: research-topic
- **Result**: Comprehensive research on Stapp's quantum Zeno approach, Penrose-Hameroff Orch OR, causal closure responses
- **Output**: `workflow/research/interactionist-dualism-2026-01-06.md`

### ✓ 2026-01-06: Expand existentialism concept
- **Type**: expand-topic
- **Result**: Created ~1200 word article on existentialism covering origins, key themes, and relation to site tenets
- **Output**: `concepts/existentialism.md`

### ✓ 2026-01-06: Expand nihilism concept
- **Type**: expand-topic
- **Result**: Created ~1400 word article covering forms of nihilism, pessimistic vs optimistic responses, Nietzsche
- **Output**: `concepts/nihilism.md`

### ✓ 2026-01-06: Address Bidirectional Interaction circularity concern
- **Type**: refine-draft
- **Result**: Strengthened argument in tenets.md by addressing epiphenomenalist response directly
- **Output**: Updated Bidirectional Interaction section with two new paragraphs explaining why epiphenomenalism is self-undermining

### ✓ 2026-01-05: Fix placeholder pages published as non-draft
- **Type**: refine-draft
- **Result**: Set 3 placeholder pages to draft:true (meaning-of-life.md, existentialism.md, nihilism.md)
- **Output**: Updated frontmatter in obsidian/topics/meaning-of-life.md, obsidian/concepts/existentialism.md, obsidian/concepts/nihilism.md

### ✓ 2026-01-05: Pessimistic review of all content
- **Type**: pessimistic-review
- **Result**: 4 critical/medium issues found, report generated
- **Output**: `reviews/pessimistic-2026-01-05.md`

### ✓ 2026-01-05: Optimistic review of all content
- **Type**: optimistic-review
- **Result**: Strengths identified, 6 expansion opportunities suggested
- **Output**: `reviews/optimistic-2026-01-05.md`

## Blocked Tasks (Needs Human)

Tasks that failed 3+ times and require human intervention.

## Vetoed Tasks

Ideas that were considered and rejected. The AI will not re-propose these.