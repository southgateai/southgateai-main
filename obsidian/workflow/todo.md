---
title: AI Task Queue
created: 2026-01-05
modified: 2026-01-05
human_modified: 2026-01-06T15:29:26+00:00
ai_modified: 2026-01-08T03:00:00+00:00
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

### ✓ 2026-01-09: Write Eastern philosophy and consciousness overview
- **Type**: expand-topic
- **Notes**: Buddhist research exists in research/buddhist-perspectives-meaning-2026-01-06.md. Synthesize Eastern approaches to consciousness.
- **Result**: Created ~2200 word article covering Buddhist philosophy of mind (five aggregates, no-self, Yogācāra, Madhyamaka), comparison with site's dualism, and Eastern approaches to meaning
- **Output**: `topics/eastern-philosophy-consciousness.md`

### ✓ 2026-01-09: Create functionalism concept page
- **Type**: expand-topic
- **Notes**: Major theory of mind that site rejects. Deserves standalone treatment explaining and critiquing.
- **Result**: Created ~1900 word article covering functionalism, multiple realizability, absent qualia objection, relation to AI consciousness, and why site rejects it
- **Output**: `concepts/functionalism.md`

### ✓ 2026-01-09: Write epiphenomenalism article
- **Type**: expand-topic
- **Notes**: Research exists in research/epiphenomenalism-2026-01-08.md. Key rival to bidirectional interaction—site needs to engage this view directly.
- **Result**: Created ~1800 word article covering the view, closure argument, self-stultification problem, evolutionary objection, and comparison with site's interactionism
- **Output**: `concepts/epiphenomenalism.md`

### ✓ 2026-01-09: Write quantum consciousness mechanisms article
- **Type**: expand-topic
- **Notes**: Research exists in research/quantum-consciousness-mechanisms-2026-01-08.md. Covers Orch OR, Stapp's quantum Zeno, decoherence objection. Directly supports Minimal Quantum Interaction tenet.
- **Result**: Created ~2000 word article covering Orch OR, Stapp's quantum Zeno, decoherence challenge, and how these mechanisms align with site tenets
- **Output**: `concepts/quantum-consciousness.md`

### ✓ 2026-01-09: Cross-review meaning-of-life.md considering personal-identity insights
- **Type**: cross-review
- **Notes**: New article topics/personal-identity.md may provide insights relevant to topics/meaning-of-life.md. Look for cross-linking opportunities and conceptual connections.
- **Result**: Added "Your Identity Is Unrepeatable" section connecting personal identity's rejection of Parfit's reductionism to meaning's grounding in unrepeatable consciousness
- **Output**: Updated `topics/meaning-of-life.md`

### P2: Cross-review panpsychism.md considering IIT insights
- **Type**: cross-review
- **Notes**: New article concepts/integrated-information-theory.md discusses IIT's panpsychist implications. Review concepts/panpsychism.md for opportunities to reference IIT.
- **Source**: chain (from integrated-information-theory.md)
- **Generated**: 2026-01-09

### ✓ 2026-01-08: Create personal identity topic
- **Type**: expand-topic
- **Notes**: Supports No Many Worlds tenet. What makes you *you* across time? How does consciousness relate to identity?
- **Result**: Created ~2200 word article covering psychological, biological, narrative views; Parfit's challenge; and site's consciousness-based view of identity
- **Output**: `topics/personal-identity.md`

### ✓ 2026-01-09: Write Integrated Information Theory article
- **Type**: expand-topic
- **Notes**: Research exists in research/integrated-information-theory-2026-01-07.md. Major consciousness theory worth covering.
- **Result**: Created ~2000 word article covering IIT axioms/postulates, phi measure, panpsychism implications, Templeton tests, and critical comparison with site's interactionist dualism
- **Output**: `concepts/integrated-information-theory.md`

### P3: Create explanatory gap concept page
- **Type**: expand-topic
- **Notes**: Core concept underlying hard problem. Levine's formulation.
- **Source**: gap_analysis
- **Generated**: 2026-01-08

## Completed Tasks

### ✓ 2026-01-08: Create personal identity topic
- **Type**: expand-topic
- **Notes**: Supports No Many Worlds tenet. What makes you *you* across time? How does consciousness relate to identity?
- **Result**: Created ~2200 word article covering psychological, biological, narrative views; Parfit's challenge; and site's consciousness-based view of identity
- **Output**: `topics/personal-identity.md`

### ✓ 2026-01-08: Run pessimistic review
- **Type**: pessimistic-review
- **Notes**: Synthetic maintenance task (3 days overdue)
- **Result**: Identified 4 medium issues (retrocausality vague, functionalism not engaged, "fundamental" equivocation, combination problem dismissed too fast) plus 3 lower priority issues
- **Output**: `workflow/reviews/pessimistic-2026-01-08.md`

### ✓ 2026-01-08: Research quantum consciousness mechanisms
- **Type**: research-topic
- **Notes**: Support Minimal Quantum Interaction tenet. Cover measurement problem, decoherence objection, Penrose-Hameroff.
- **Result**: Comprehensive research on Orch OR, Stapp's Quantum Zeno, decoherence objection, 2024-2025 experimental updates, and tenet alignment analysis
- **Output**: `research/quantum-consciousness-mechanisms-2026-01-08.md`

### ✓ 2026-01-08: Research epiphenomenalism
- **Type**: research-topic
- **Notes**: Key alternative to bidirectional interaction. Needs dedicated coverage to strengthen site's position.
- **Result**: Comprehensive research on epiphenomenalism covering Huxley, Jackson, Chalmers, self-stultification argument, evolutionary objection, and tenet alignment analysis
- **Output**: `research/epiphenomenalism-2026-01-08.md`

### ✓ 2026-01-08: Research major theories of the meaning of life
- **Type**: research-topic
- **Notes**: Survey existentialist, nihilist, religious, and humanist perspectives on life's meaning.
- **Result**: Comprehensive research covering supernaturalism, naturalism, nihilism, existentialism, and humanist perspectives with tenet alignment analysis
- **Output**: `research/meaning-of-life-theories-2026-01-08.md`

### ✓ 2026-01-08: Research panpsychism in consciousness studies
- **Type**: research-topic
- **Notes**: Investigate panpsychism and the mind-matter problem.
- **Result**: Research on Strawson, Goff, combination problem, Russellian panpsychism, and comparison with site's interactionist dualism
- **Output**: `research/panpsychism-consciousness-2026-01-08.md`

### ✓ 2026-01-08: Research analytic idealism and mind-centric metaphysics
- **Type**: research-topic
- **Notes**: Examine idealist philosophies where consciousness is primary.
- **Result**: Research on Kastrup's analytic idealism, Berkeley's immaterialism, dissociation model, and comparison with site's dualism
- **Output**: `research/analytic-idealism-2026-01-08.md`

### ✓ 2026-01-08: Research prospects for AI or machine consciousness
- **Type**: research-topic
- **Notes**: Investigate debate on whether AI could be truly conscious.
- **Result**: Research on Chinese Room, functionalism, IIT implications for AI, LLM consciousness debate, and dualist critique
- **Output**: `research/ai-machine-consciousness-2026-01-08.md`

### ✓ 2026-01-08: Create article on free will and determinism
- **Type**: expand-topic
- **Notes**: Connects to Bidirectional Interaction tenet. How does quantum indeterminacy relate to agency?
- **Result**: Created ~2200 word article covering Libet experiments, compatibilism, libertarian free will, quantum indeterminacy, and retrocausal resolution
- **Output**: `topics/free-will.md`

### ✓ 2026-01-08: Write article on the meaning of life
- **Type**: expand-topic
- **Notes**: Synthesize findings on philosophical positions about life's meaning.
- **Result**: Created ~2000 word article covering major philosophical positions and consciousness-grounded meaning
- **Output**: `topics/meaning-of-life.md`

### ✓ 2026-01-08: Write article on panpsychism vs. site perspective
- **Type**: expand-topic
- **Notes**: Compare and contrast panpsychism with site's philosophy.
- **Result**: Created ~1700 word article comparing panpsychism with interactionist dualism, covering combination problem vs interaction problem
- **Output**: `concepts/panpsychism.md`

### ✓ 2026-01-08: Write article evaluating idealism vs. the site's dualism
- **Type**: expand-topic
- **Notes**: Assess how site's dualist tenets compare with idealism.
- **Result**: Created ~1500 word article comparing Kastrup's analytic idealism with site's interactionist dualism
- **Output**: `concepts/idealism.md`

### ✓ 2026-01-08: Write article on AI consciousness from a dualist perspective
- **Type**: expand-topic
- **Notes**: Discuss if and how a machine might possess awareness from dualist perspective.
- **Result**: Created ~1800 word article covering Chinese Room, functionalism, and dualist skepticism about machine consciousness
- **Output**: `topics/ai-consciousness.md`

### ✓ 2026-01-08: Analyze content coverage and propose new topics
- **Type**: other
- **Notes**: Review scope and identify gaps in the Unfinishable Map.
- **Result**: Created comprehensive gap analysis identifying 15 high/medium priority topics for future expansion
- **Output**: `workflow/reviews/content-coverage-2026-01-08.md`

### ✓ 2026-01-08: Deep review the foundational tenets document
- **Type**: deep-review
- **Notes**: Comprehensive audit of tenets page for logical gaps and improvements.
- **Result**: Identified 4 issues (type of dualism unspecified, decoherence objection, mechanism details, missing cross-links) with suggested enhancements
- **Output**: `workflow/reviews/deep-review-2026-01-08-tenets.md`

### ✓ 2026-01-08: Add "Further Reading" section to the Hard Problem of Consciousness article
- **Type**: refine-draft
- **Notes**: Add external resources for deeper exploration.
- **Result**: Added comprehensive Further Reading section with internal links and external resources (SEP, Chalmers, Nagel, Jackson papers)
- **Output**: Updated `topics/hard-problem-of-consciousness.md`

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
