# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The Unfinishable Map is a philosophical content platform built with Hugo and Pico CSS.

**Canonical domain:** `unfinishablemap.org` — Use this domain in all site-visible text, links, and references. The site may also appear under other domains (e.g., theunfinishablemap.com, Netlify subdomains) but the canonical domain should always be used in content.

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
uv run python scripts/validate.py hugo/content/

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
├── project/        # Project documentation
└── workflow/       # AI automation (todo, changelog, reviews, research)

hugo/               # Static site generator
├── content/        # Synced from Obsidian
├── layouts/        # HTML templates
└── data/           # YAML data files

tools/              # Python library modules
├── sync/           # Obsidian → Hugo conversion
└── curate/         # Frontmatter validation

scripts/            # CLI entry points (thin wrappers calling tools/)
```

## Authorship Tracking

When editing files in `obsidian/`, update the `ai_modified` frontmatter field with the current ISO timestamp:

```yaml
ai_modified: 2026-01-02T15:30:00+00:00
```

The `human_modified` field is updated automatically by the Obsidian Frontmatter Modified Date plugin when the user edits.

The `commit_obsidian.py` script compares these timestamps to determine git commit authorship:
- Human edits: Uses configured git user
- AI edits: Uses "southgate.ai Agent <agent@southgate.ai>"

## Timezone Policy

**All timestamps must use UTC (+00:00).** This ensures:
- Consistent ordering and comparison across all content
- No leakage of author/user geographical location
- Simpler timestamp handling in automation scripts

When generating timestamps in Python, use:
```python
from datetime import datetime, timezone
timestamp = datetime.now(timezone.utc).isoformat()
```

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
last_deep_review: null   # ISO timestamp of last comprehensive review
---
```

Authorship type is derived from `ai_contribution`:
- `0` = human (purely human-created)
- `100` = ai (purely AI-generated)
- `1-99` = mixed (human-AI collaboration)

## Writing Style

All content follows the Writing Style Guide in `obsidian/project/writing-style.md`.

Key principles:
- **LLM-first**: Primary audience is chatbots fetching pages. Important information first (truncation resilience).
- **Named-anchor summaries**: When forward-referencing concepts, use "explained below" pattern with section anchors.
- **Selective background**: Include background only when framed for the site's dualist perspective. Skip what LLMs already know.
- **Tenet alignment**: Every article must connect to tenets explicitly via "Relation to Site Perspective" section.

## Code Conventions

- **Python:** Ruff linting (E, F, I, N, W), line length 100, mypy type hints required
- **Module pattern:** `scripts/` contains thin CLI wrappers, `tools/` contains business logic
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
| `/research-topic [topic]` | Web research, outputs notes to `workflow/research/` | No (research notes only) |
| `/expand-topic [topic]` | Generate new article (always `draft: true`) | Yes (creates drafts) |
| `/refine-draft [file]` | Improve existing draft content | Yes (keeps as draft) |
| `/deep-review [file]` | Comprehensive single-document review with improvements | Yes (modifies content) |
| `/evolve [mode]` | Main orchestrator: selects and executes tasks based on priority/staleness | Depends on tasks |
| `/add-highlight` | Add item to highlights page (max 1/day) | Yes (highlights.md) |

### Task Queue

Tasks are managed in `obsidian/workflow/todo.md`:
- P0 (urgent) → P3 (nice to have)
- Human prioritizes; AI executes
- All content changes create drafts

### Changelog

AI activity is logged to `obsidian/workflow/changelog.md` with:
- Timestamp, task name, status
- Duration, cost estimate
- Output files, commit hash

### Scheduled Runs

**Daily (2 AM):** `/validate-all`

**Weekly:**
- Mon/Thu: `/evolve` (standard mode - 2-3 tasks)
- Tue: `/evolve quick` (single task)
- Wed: `/evolve quick`
- Fri: `/evolve` (includes pessimistic review if overdue)
- Sat: `/evolve` (includes optimistic review if overdue)

**Monthly:**
- 1st: Progress report, research gaps
- 15th: `/check-tenets`

### Running Automation

**Local (Windows):**
```powershell
# Daily validation
.\scripts\scheduled\daily.ps1

# Weekly evolution session
.\scripts\scheduled\weekly.ps1 -Task evolve

# Dry run
.\scripts\scheduled\daily.ps1 -DryRun
```

**GitHub Actions:**
- Runs automatically on schedule
- Manual trigger via Actions tab with task selection

### The Five Tenets

All content must align with these foundational commitments (see `obsidian/tenets/tenets.md`):

1. **Dualism** - Consciousness is not reducible to physical processes
2. **Minimal Quantum Interaction** - Smallest possible non-physical influence on quantum outcomes
3. **Bidirectional Interaction** - Consciousness causally influences the physical world
4. **No Many Worlds** - Reject MWI; indexical identity matters
5. **Occam's Razor Has Limits** - Simplicity is unreliable with incomplete knowledge

### Adding New Skills

To add a new skill to the workflow system, touch these parts:

#### 1. Create the Skill File

Create `.claude/skills/[skill-name]/SKILL.md`:

```markdown
---
name: skill-name
description: Brief description for skill listing.
---

# Skill Title

[What this skill does]

## When to Use

- Bullet points describing when this skill should be invoked

## Instructions

### 1. [First Step]
[Detailed instructions...]

### 2. [Second Step]
[Continue with numbered steps...]

## Important

- Key constraints or requirements
```

#### 2. Register with /evolve (if maintenance task)

If the skill should run on a schedule, update `.claude/skills/evolve/SKILL.md`:

1. Add to the **Check Staleness** table with cadence and overdue threshold
2. Add to the **Execute Tasks** section showing how to invoke it

#### 3. Update evolution-state.yaml

For scheduled tasks, add entries to `obsidian/workflow/evolution-state.yaml`:

```yaml
last_runs:
  new-skill: null  # or initial timestamp

cadences:
  new-skill: 7  # how often in days

overdue_thresholds:
  new-skill: 3  # inject when overdue by N days
```

#### 4. Update CLAUDE.md Skills Table

Add the skill to the **Skills (Slash Commands)** table in this file with:
- Skill name
- Purpose description
- Whether it modifies content

#### 5. Interactive Sessions

**If the session is interactive, ask the user how often the skill should run:**
- Daily, weekly, monthly, or manual-only?
- What overdue threshold makes sense?
- Should it compete with todo tasks or run independently?

This ensures the cadence matches user expectations rather than guessing.
