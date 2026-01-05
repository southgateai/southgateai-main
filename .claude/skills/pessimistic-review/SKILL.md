---
name: pessimistic-review
description: Critically analyze content for logical gaps, unsupported claims, and potential counterarguments. Does not modify content.
---

# Pessimistic Review

Adversarial analysis to find weaknesses in site content. Acts as a critical reviewer looking for flaws.

## When to Use

- Weekly quality review
- Before publishing important content
- When `/pessimistic-review` is invoked
- Optionally with a specific file: `/pessimistic-review obsidian/topics/meaning-of-life.md`

## Instructions

### 1. Select Content to Review

If a specific file is provided, review that file.

Otherwise, select content using this priority:
1. Files with `draft: true` (drafts need review before publishing)
2. Files not yet reviewed (check `obsidian/project/reviews/` for existing reviews)
3. Oldest content by `modified` date

### 2. Critical Analysis

For each piece of content, analyze for:

#### Logical Gaps
- Are there non-sequiturs in the argument?
- Do conclusions follow from premises?
- Are there missing steps in reasoning?

#### Unsupported Claims
- Are assertions made without evidence or argument?
- Are sources cited for factual claims?
- Are philosophical positions attributed correctly?

#### Counterarguments Not Addressed
- What would a critic say?
- Are obvious objections ignored?
- Are alternative interpretations dismissed too quickly?

#### Internal Contradictions
- Does the content contradict itself?
- Does it conflict with other site content?
- Does it conflict with the site's tenets?

#### Language Issues
- Is language overly strong without justification? ("clearly," "obviously," "must be")
- Are there weasel words hiding weak arguments?
- Is the tone appropriately uncertain where warranted?

### 3. Generate Report

Create a report at `obsidian/project/reviews/pessimistic-YYYY-MM-DD.md`:

```markdown
---
title: Pessimistic Review - YYYY-MM-DD
created: YYYY-MM-DD
draft: false
ai_contribution: 100
ai_system: [current model]
---

# Pessimistic Review

**Date**: YYYY-MM-DD
**Content reviewed**: [filename or list]

## Executive Summary

[2-3 sentence summary of main findings]

## Critical Issues

### Issue 1: [Title]
- **File**: [filename]
- **Location**: [section or quote]
- **Problem**: [description]
- **Severity**: High/Medium/Low
- **Recommendation**: [how to address]

## Counterarguments to Address

### [Topic/Claim]
- **Current content says**: [summary]
- **A critic would argue**: [counterargument]
- **Suggested response**: [how to address]

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| [claim] | [file:section] | [what's needed] |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "clearly shows" | Too strong | "suggests" |

## Strengths (Brief)

Despite criticisms, note what works well to preserve during revisions.
```

### 4. Add Actionable Items

If significant issues are found, add tasks to `obsidian/project/todo.md`:

```markdown
### P2: Address gaps in [filename]
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found [brief description]. See pessimistic-YYYY-MM-DD.md
```

### 5. Log to Changelog

Append summary to `obsidian/project/changelog.md`.

## Important

- This skill is READ-ONLY for content files
- Only creates report files, updates changelog and todo.md
- Does NOT modify the content itself
- Be genuinely critical - the goal is to find real weaknesses
- But be constructive - always suggest how to improve
