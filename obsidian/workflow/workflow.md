---
title: Workflow System
created: 2026-01-05
modified: 2026-01-10
human_modified: 2026-01-05
ai_modified: 2026-01-10T17:00:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[automation]]"
  - "[[todo]]"
  - "[[changelog]]"
  - "[[highlights]]"
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-01-05
last_curated:
---

The workflow system executes AI skills programmatically and tracks their execution history.

## Overview

Skills are invoked via the Claude CLI using stream-json format, which allows proper skill expansion and tool access. The workflow executor:

1. Invokes a skill by name
2. Captures execution metrics (duration, cost, turns)
3. Logs results to this file
4. Optionally commits changes with AI authorship

## Available Skills

### Orchestration

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/evolve [mode]` | Main orchestrator—selects and executes tasks based on priority and staleness | Yes (runs other skills) |
| `/replenish-queue [mode]` | Auto-generate tasks when queue is empty or near-empty | Yes (todo.md only) |
| `/tune-system` | Monthly meta-review—analyze system operation, adjust cadences/thresholds | Yes (state, minor) |

### Content Creation

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/expand-topic [topic]` | Generate new article on a topic | Yes (creates draft) |
| `/refine-draft [file]` | Improve existing draft content | Yes (edits content) |
| `/research-topic [topic]` | Web research, outputs notes to [[research]] | Research notes only |
| `/research-voids` | Daily research on cognitive gaps and unchartable territories | Research notes only |

### Review & Validation

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/validate-all` | Check frontmatter, links, orphans | No (reports only) |
| `/check-tenets` | Verify alignment with 5 foundational tenets | No (reports only) |
| `/check-links` | Verify all internal links work | No (reports only) |
| `/pessimistic-review` | Find logical gaps, unsupported claims, counterarguments | No (reports only) |
| `/optimistic-review` | Find strengths and expansion opportunities | No (reports only) |
| `/deep-review [file]` | Comprehensive single-document review with improvements | Yes (modifies content) |

### Publishing

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/add-highlight [topic]` | Add item to [[highlights\|What's New]] page (max 1/day) | Yes (highlights.md) |

## Queue Replenishment

The task queue in [[todo]] auto-replenishes when active tasks (P0-P2) drop below 3. `/evolve` triggers `/replenish-queue` automatically as its first step.

### Task Types and Chains

Tasks generate follow-up tasks automatically:

| Type | Description | Generates |
|------|-------------|-----------|
| `research-topic` | Web research producing notes | → `expand-topic` |
| `expand-topic` | Write new article | → `cross-review` |
| `cross-review` | Review article in light of new content | (terminal) |
| `refine-draft` | Improve existing draft | (terminal) |
| `deep-review` | Comprehensive single-doc review | (terminal) |

### Task Generation Sources

`/replenish-queue` generates tasks from four sources:

1. **Task chains**: Recent `research-topic` completions that need articles written; recent `expand-topic` completions that need cross-review integration
2. **Unconsumed research**: Research notes in `research/` without corresponding articles
3. **Gap analysis**: Content gaps based on tenet support, undefined concepts, coverage targets
4. **Staleness**: AI-generated content not reviewed in 30+ days

### Replenishment Modes

- `conservative`: 3-5 high-confidence tasks only
- (default): 5-8 tasks with good diversity
- `aggressive`: 8-12 tasks including speculative ones

### Cross-Review Tasks

When a new article is written, `/replenish-queue` generates `cross-review` tasks for related existing articles. These reviews:

- Add wikilinks to the new content
- Check for arguments that the new content supports or challenges
- Ensure consistent terminology
- Identify missing cross-references

## System Tuning

The `/tune-system` skill provides meta-level self-improvement for the automation system. It runs monthly (30-day cadence, injected when 45 days overdue).

### What It Analyzes

1. **Cadence adherence**: Are maintenance tasks running on schedule or frequently overdue?
2. **Failure patterns**: What's causing systematic task failures?
3. **Queue health**: Is replenishment producing tasks that actually get executed?
4. **Review findings**: Are identified issues being addressed?
5. **Convergence progress**: Is the system making progress toward goals?

### Change Tiers

| Tier | Scope | Approval |
|------|-------|----------|
| **Tier 1** | Cadence ±2 days, threshold ±2 days | Automatic (max 3/session) |
| **Tier 2** | New P3 tasks, larger changes | Recommendation only |
| **Tier 3** | Skill changes, tenet-related | Report only |

### Safeguards

- **Evidence threshold**: Requires 5+ data points before making changes
- **Change cooldown**: Settings can't change twice within 60 days
- **Locked settings**: Human can lock any setting via `locked_settings` in state
- **Abort conditions**: Stops if >50% failure rate or convergence regresses

### Output

Creates report at `workflow/reviews/system-tune-YYYY-MM-DD.md` documenting findings, changes applied, and recommendations.

## Running Workflows

### From Command Line

```bash
# Run a skill
uv run python scripts/run_workflow.py validate-all

# Dry run (see what would happen)
uv run python scripts/run_workflow.py evolve --dry-run

# Run with more turns for complex tasks
uv run python scripts/run_workflow.py expand-topic --max-turns 30

# Run and commit changes
uv run python scripts/run_workflow.py evolve --commit
```

### From PowerShell Scripts

The scheduled scripts in `scripts/scheduled/` call the workflow executor:

```powershell
# Daily validation
.\scripts\scheduled\daily.ps1

# Weekly tasks
.\scripts\scheduled\weekly.ps1 -Task evolve
```

## Execution Format

Each workflow execution logs:

- **Status**: Success, Error, MaxTurns, or PermissionDenied
- **Duration**: How long the execution took
- **Cost**: API cost in USD
- **Turns**: Conversation turns used vs maximum
- **Output**: Brief summary or error message
- **Session**: Session ID for debugging

## Recent Executions

