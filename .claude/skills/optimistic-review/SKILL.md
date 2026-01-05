---
name: optimistic-review
description: Identify content strengths and opportunities for expansion. Suggests new topics and connections.
---

# Optimistic Review

Find strengths in existing content and identify opportunities for expansion and improvement.

## When to Use

- Weekly opportunity assessment
- When planning content roadmap
- When `/optimistic-review` is invoked
- Optionally with a specific file: `/optimistic-review obsidian/concepts/existentialism.md`

## Instructions

### 1. Select Content to Review

If a specific file is provided, review that file.

Otherwise, review all non-draft content in:
- `obsidian/topics/`
- `obsidian/concepts/`
- `obsidian/tenets/`

### 2. Strength Analysis

For each piece of content, identify:

#### Strong Arguments
- Which arguments are particularly compelling?
- What evidence is well-presented?
- Where is the reasoning especially clear?

#### Unique Insights
- What perspectives are original or underrepresented elsewhere?
- What connections are made that others miss?
- What framings are particularly effective?

#### Effective Communication
- Where is complex content made accessible?
- What analogies or examples work well?
- Where does the writing flow naturally?

### 3. Opportunity Analysis

Identify opportunities for:

#### Natural Expansion Points
- What topics naturally follow from existing content?
- What questions does the content raise but not answer?
- What depth could be added to surface-level treatments?

#### Missing Perspectives
- What philosophical traditions are underrepresented?
- What historical context would enrich the discussion?
- What scientific developments are relevant but not covered?

#### Cross-Linking Opportunities
- What existing content could link to this?
- What new content would strengthen the web?
- Are there concepts that need their own pages?

### 4. Generate Report

Create a report at `obsidian/project/reviews/optimistic-YYYY-MM-DD.md`:

```markdown
---
title: Optimistic Review - YYYY-MM-DD
created: YYYY-MM-DD
draft: false
ai_contribution: 100
ai_system: [current model]
---

# Optimistic Review

**Date**: YYYY-MM-DD
**Content reviewed**: [list of files]

## Executive Summary

[2-3 sentence summary of strengths and opportunities]

## Content Strengths

### [filename]
- **Strongest point**: [description]
- **Notable quote**: "[quote]"
- **Why it works**: [analysis]

## Expansion Opportunities

### High Priority

#### [Topic Name]
- **Builds on**: [existing content]
- **Would address**: [gap or question]
- **Estimated scope**: Short/Medium/Long article
- **Tenet alignment**: [how it fits with tenets]

### Medium Priority

[Similar format]

### Ideas for Later

[Brief list of lower-priority topics]

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| [file1] | [file2] | [why they should link] |

## New Concept Pages Needed

- **[Concept]**: [why it deserves its own page]
```

### 5. Add Suggested Tasks

Add expansion opportunities to `obsidian/project/todo.md` as P3 (low priority, needs human approval):

```markdown
### P3: Write article on [suggested topic]
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. See optimistic-YYYY-MM-DD.md
```

### 6. Log to Changelog

Append summary to `obsidian/project/changelog.md`.

## Important

- This skill is READ-ONLY for content files
- Only creates report files, updates changelog and todo.md
- Does NOT modify content
- Be genuinely enthusiastic about strengths
- But be realistic about opportunities - quality over quantity
- New topics should align with site tenets
