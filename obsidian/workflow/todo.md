---
title: AI Task Queue
created: 2026-01-05
modified: 2026-01-05
human_modified: 2026-01-06T15:29:26+00:00
ai_modified: 2026-01-07T23:30:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project]]"
  - "[[changelog]]"
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-01-05
last_curated:
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

### P2: Create article on free will and determinism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Connects to Bidirectional Interaction tenet. How does quantum indeterminacy relate to agency? Depends on P1 Libet research.

### P1: Research major theories of the meaning of life
- **Type**: research-topic
- **Status**: pending
- **Notes**: Survey existentialist, nihilist, religious, and humanist perspectives on life's meaning. Identify how each aligns or conflicts with the site's tenets (e.g. Nihilism vs. an Intrinsic Meaning tenet). Results will inform the subsequent meaning-of-life article.

### P2: Write article on the meaning of life
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Synthesize findings from P1 meaning-of-life research into a comprehensive draft. Address how various perspectives (existentialist, nihilist, spiritual) are reconciled or refuted by the site's philosophy. Emphasize the site's stance on whether life has inherent purpose. Depends on P1 meaning-of-life research.

### P1: Research panpsychism in consciousness studies
- **Type**: research-topic
- **Status**: pending
- **Notes**: Investigate panpsychism (the view that consciousness is a fundamental feature of all matter). Gather key arguments from proponents (Strawson, Goff) and how panpsychism attempts to solve the mind-matter problem. Analyze points of alignment or conflict with the site's dualist and interactionist tenets.

### P2: Write article on panpsychism vs. site perspective
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Compare and contrast panpsychism with the site's philosophy. Explain panpsychist principles and evaluate whether treating consciousness as inherent in all matter challenges or complements the site's view (e.g. does panpsychism reinforce Bidirectional Interaction, or render it moot?). Depends on P1 panpsychism research.

### P1: Research analytic idealism and mind-centric metaphysics
- **Type**: research-topic
- **Status**: pending
- **Notes**: Examine idealist philosophies (e.g. Berkeley's immaterialism, Kastrup's analytic idealism) where consciousness is primary and matter is derivative. Summarize core arguments that "all is mind" and gather critiques. Note overlaps with the site's perspective (mind as fundamental) and differences (idealism dismisses a physical realm, unlike dualism).

### P2: Write article evaluating idealism vs. the site's dualism
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Critically assess how the site's dualist tenets stack up against a pure idealist viewpoint. Discuss whether the existence of an independent physical world (as the site assumes) is necessary, or if the idealist model could explain observed reality and still accommodate Bidirectional Interaction. Highlight why the site adopts dualism over idealism. Depends on P1 analytic idealism research.

### P2: Analyze content coverage and propose new topics
- **Type**: other
- **Status**: pending
- **Notes**: Review the current scope of topics and concepts to identify gaps in the Unfinishable Map. Compile a brief report suggesting 5–10 new questions or subjects worth exploring (e.g. physicalism's critique, Eastern philosophy angles on mind, ethics of consciousness research). The goal is to ensure the map continually expands into relevant areas not yet covered.

### P1: Research prospects for AI or machine consciousness
- **Type**: research-topic
- **Status**: pending
- **Notes**: Investigate the debate on whether an artificial intelligence could ever be truly conscious. Cover key viewpoints: functionalist arguments for digital consciousness, Searle's critiques (Chinese Room), recent claims about large language models, etc. Evaluate what each position implies given the site's stance that mind may have non-material aspects.

### P2: Write article on AI consciousness from a dualist perspective
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Using insights from the AI consciousness research, discuss if and how a machine might possess awareness. Outline the site's likely perspective (e.g. true consciousness might require non-physical properties absent in AI) and address opposing views. Tie the discussion to site tenets (what would an AI mean for Dualism or Bidirectional Interaction?). Depends on P1 AI consciousness research.

### P2: Deep review the foundational tenets document
- **Type**: deep-review
- **Status**: pending
- **Notes**: Perform a comprehensive audit of the site's Tenets page. Use the deep-review process (combined pessimistic and optimistic analysis) to identify any logical gaps, unclear rationale, or unsupported claims in each tenet. Apply revisions to fortify each principle against criticism, add cross-references or examples as needed, and ensure the tenets are coherent as a set.

### P2: Add "Further Reading" section to the Hard Problem of Consciousness article
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Augment the existing Hard Problem of Consciousness page with a short list of recommended external resources for deeper exploration. For example, link to the Stanford Encyclopedia of Philosophy entry on consciousness, key papers by Chalmers or Nagel, and other relevant readings. This helps situate the site's content in the broader scholarly context for interested readers.

## Completed Tasks

### ✓ 2026-01-07: Create concept page on retrocausality and consciousness
- **Type**: expand-topic
- **Notes**: Based on [[libet-experiments-free-will-2026-01-07|Libet research]]. Present how retrocausal interpretations of quantum mechanics (Wheeler's delayed-choice, Cramer's transactional interpretation) align with the Bidirectional Interaction tenet. Key insight: if causation can flow backward in time at the quantum level, the apparent problem of neural activity preceding conscious awareness dissolves. Consciousness doesn't arrive "too late"—it may influence outcomes retrocausally. This paints a picture where consciousness is woven into the causal fabric of reality in ways that linear time obscures.
- **Result**: Created ~1500 word article covering time-symmetric QM, Wheeler's delayed-choice, Cramer's transactional interpretation, and application to the Libet problem via atemporal selection model
- **Output**: `concepts/retrocausality.md`

### ✓ 2026-01-07: Research Integrated Information Theory (IIT)
- **Type**: research-topic
- **Notes**: Tononi's theory. How does it relate to or conflict with site tenets?
- **Result**: Comprehensive research on IIT 4.0, axioms/postulates, phi metric, panpsychism implications, 2023 pseudoscience controversy, Templeton empirical tests. Analysis of alignment/conflict with site tenets.
- **Output**: `research/integrated-information-theory-2026-01-07.md`

### ✓ 2026-01-07: Create concept page for qualia
- **Type**: expand-topic
- **Notes**: Central to the hard problem. Link to Dualism tenet.
- **Result**: Created ~1300 word article covering qualia definition, properties (intrinsic, private, ineffable), thought experiments (Mary's Room, inverted qualia, zombies), and relation to site tenets
- **Output**: `concepts/qualia.md`

### ✓ 2026-01-07: Research Libet experiments and neural predictors of decision
- **Type**: research-topic
- **Notes**: Experiments show neural "readiness potentials" predict decisions before conscious awareness. At first glance this weighs against free will. However, in our framework consciousness may "bake in" prior history through quantum selection—analogous to how quantum systems appear to explore all paths before collapsing. Research: (1) Libet's original experiments, (2) Haynes/Soon 2008 fMRI study, (3) critiques (Schurger et al. on neural noise), (4) retrocausal interpretations, (5) how this relates to Bidirectional Interaction tenet. This research should inform the free will article.
- **Result**: Comprehensive research covering Libet 1983, Soon et al. 2008, Schurger neural noise critique, retrocausality in QM, Wheeler's delayed-choice, Cramer's transactional interpretation. Key finding: retrocausal interpretation aligns with Bidirectional Interaction tenet.
- **Output**: `research/libet-experiments-free-will-2026-01-07.md`

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
- **Output**: `research/buddhist-perspectives-meaning-2026-01-06.md`

### ✓ 2026-01-06: Write article on the hard problem of consciousness
- **Type**: expand-topic
- **Result**: Created comprehensive ~1800 word article covering easy/hard problem distinction, explanatory gap, zombie argument, and Mary's Room
- **Output**: `topics/hard-problem-of-consciousness.md`

### ✓ 2026-01-06: Research interactionist dualism
- **Type**: research-topic
- **Result**: Comprehensive research on Stapp's quantum Zeno approach, Penrose-Hameroff Orch OR, causal closure responses
- **Output**: `research/interactionist-dualism-2026-01-06.md`

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
