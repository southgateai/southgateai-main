# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SouthgateAI is a philosophical content platform built with Hugo and Pico CSS.

**Data flow:** Obsidian vault → Python sync tools → Hugo content → Static site (Netlify)

## Commands

```bash
# Install dependencies
uv sync

# Full build pipeline (sync + validate + build Hugo)
uv run python scripts/build.py

# Sync Obsidian → Hugo only
uv run python scripts/sync.py

# Hugo dev server
cd hugo && hugo server

# Validate frontmatter
uv run python scripts/curate.py validate hugo/content/

# AI content review
uv run python scripts/curate.py review hugo/content/topics/meaning-of-life.md

# Generate article with LLM
uv run python scripts/generate.py article "Topic Name" --style exploratory

# Generate crosslinks between content
uv run python scripts/curate.py crosslink hugo/content/ --apply

# Commit obsidian changes with human/AI attribution
uv run python scripts/commit_obsidian.py --dry-run
uv run python scripts/commit_obsidian.py
```

## Architecture

```
obsidian/           # Primary content source (Obsidian vault)
├── topics/         # Philosophical topics
├── concepts/       # Core concepts
├── templates/      # Obsidian templates
└── project/        # Project documentation

hugo/               # Static site generator
├── content/        # Synced from Obsidian
├── layouts/        # HTML templates
└── data/           # YAML data files

tools/              # Python library modules
├── sync/           # Obsidian → Hugo conversion
├── llm/            # LiteLLM client wrapper
├── generate/       # AI content generation
└── curate/         # Validation, review, crosslinks

scripts/            # CLI entry points (thin wrappers calling tools/)
```

## Authorship Tracking

When editing files in `obsidian/`, update the `ai_modified` frontmatter field with the current ISO timestamp:

```yaml
ai_modified: 2026-01-02T15:30:00+03:00
```

The `human_modified` field is updated automatically by the Obsidian Frontmatter Modified Date plugin when the user edits.

The `commit_obsidian.py` script compares these timestamps to determine git commit authorship:
- Human edits: Uses configured git user
- AI edits: Uses "southgate.ai Agent <agent@southgate.ai>"

## Frontmatter Schema

All markdown content uses a flat schema (no nesting):

```yaml
---
title: "Article Title"
created: YYYY-MM-DD
modified: YYYY-MM-DD
human_modified: YYYY-MM-DD or ISO timestamp
ai_modified: null or ISO timestamp
draft: true/false
topics: []
concepts: []
related_articles: []

ai_contribution: 0-100   # 0=human, 100=ai, 1-99=mixed
author: "Name"           # human author
ai_system: null          # or model name like "claude-sonnet-4-20250514"
ai_generated_date: null  # when AI generated content
last_curated: null       # last human review date
---
```

Authorship type is derived from `ai_contribution`:
- `0` = human (purely human-created)
- `100` = ai (purely AI-generated)
- `1-99` = mixed (human-AI collaboration)

## Code Conventions

- **Python:** Ruff linting (E, F, I, N, W), line length 100, mypy type hints required
- **Module pattern:** `scripts/` contains thin CLI wrappers, `tools/` contains business logic
- **LLM calls:** Use `tools/llm/client.py` which wraps LiteLLM for multi-provider support
- **Content links:** Obsidian uses `[[wikilinks]]`, auto-converted to Hugo markdown links during sync
- **Section index files:** Files named the same as their folder (e.g., `obsidian/project/project.md`) become `_index.md` in Hugo (e.g., `hugo/content/project/_index.md`) and serve as the section landing page
- **Site index:** `obsidian/index.md` becomes `hugo/content/_index.md` (the site landing page)

## AI Automation System

The project includes scheduled AI automation for content development. All AI-generated content is created as drafts requiring human review.

### Skills (Slash Commands)

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/validate-all` | Daily health check: frontmatter, links, orphans | No (reports only) |
| `/check-tenets` | Verify content aligns with 5 foundational tenets | No (reports only) |
| `/pessimistic-review` | Find logical gaps, unsupported claims, counterarguments | No (reports only) |
| `/optimistic-review` | Find strengths, expansion opportunities | No (reports only) |
| `/research-topic [topic]` | Web research, outputs notes to `project/research/` | No (research notes only) |
| `/expand-topic [topic]` | Generate new article (always `draft: true`) | Yes (creates drafts) |
| `/refine-draft [file]` | Improve existing draft content | Yes (keeps as draft) |
| `/work-todo` | Execute highest priority task from queue | Depends on task |

### Task Queue

Tasks are managed in `obsidian/project/todo.md`:
- P0 (urgent) → P3 (nice to have)
- Human prioritizes; AI executes
- All content changes create drafts

### Changelog

AI activity is logged to `obsidian/project/changelog.md` with:
- Timestamp, task name, status
- Duration, cost estimate
- Output files, commit hash

### Scheduled Runs

**Daily (2 AM):** `/validate-all`

**Weekly:**
- Mon/Thu: `/work-todo`
- Tue: `/refine-draft`
- Wed: crosslink generation
- Fri: `/pessimistic-review`
- Sat: `/optimistic-review`

**Monthly:**
- 1st: Progress report, research gaps
- 15th: `/check-tenets`

### Running Automation

**Local (Windows):**
```powershell
# Daily validation
.\scripts\scheduled\daily.ps1

# Weekly work
.\scripts\scheduled\weekly.ps1 -Task work-todo

# Dry run
.\scripts\scheduled\daily.ps1 -DryRun
```

**GitHub Actions:**
- Runs automatically on schedule
- Manual trigger via Actions tab with task selection
- Requires `ANTHROPIC_API_KEY` secret

### The Five Tenets

All content must align with these foundational commitments (see `obsidian/tenets/tenets.md`):

1. **Dualism** - Consciousness is not reducible to physical processes
2. **Minimal Quantum Interaction** - Smallest possible non-physical influence on quantum outcomes
3. **Bidirectional Interaction** - Consciousness causally influences the physical world
4. **No Many Worlds** - Reject MWI; indexical identity matters
5. **Occam's Razor Has Limits** - Simplicity is unreliable with incomplete knowledge
