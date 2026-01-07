---
title: Workflow System
created: 2026-01-05
modified: 2026-01-07
human_modified: 2026-01-05
ai_modified: 2026-01-07T23:00:00+00:00
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

### Content Creation

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/expand-topic [topic]` | Generate new article on a topic | Yes (creates draft) |
| `/refine-draft [file]` | Improve existing draft content | Yes (edits content) |
| `/research-topic [topic]` | Web research, outputs notes to [[research]] | Research notes only |

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

