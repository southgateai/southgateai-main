---
ai_contribution: 100
ai_generated_date: 2026-01-03
ai_modified: 2026-01-03 00:00:00+00:00
ai_system: claude-opus-4-5-20251101
author: Andy Southgate
concepts: []
created: 2026-01-03
date: &id001 2026-01-03
draft: false
human_modified: 2026-01-03 16:05:09+03:00
last_curated: null
modified: *id001
related_articles:
- '[[project-brief]]'
title: SouthgateAI Project
topics: []
---

SouthgateAI is a philosophical content platform exploring the nature and meaning of life. The project combines human insight with AI-assisted research to build a coherent worldview expressed through structured content.

## Architecture

The data flows through these components:
- **Obsidian vault** - Primary content source (Markdown files with frontmatter)
- **Python sync tools** - Converts Obsidian wikilinks to Hugo markdown links
- **Hugo** - Static site generator that builds HTML from content
- **Netlify** - Hosts the static site

```mermaid
flowchart LR
    A[Obsidian Vault] --> B[Python Sync]
    B --> C[Hugo Content]
    C --> D[Hugo Build]
    D --> E[Static Site]
    E --> F[Netlify]
```

## Project Structure

| Directory | Purpose |
|-----------|---------|
| `obsidian/` | Primary content source (Obsidian vault) |
| `hugo/` | Static site generator and templates |
| `tools/` | Python library modules for sync, LLM, generation |
| `scripts/` | CLI entry points |

## Related Documents

- [project-brief](/project/project-brief/) - Project aims, methods, and design decisions
- [tenets](/tenets/) - Human-curated foundational statements

## Contributing

Content contributions follow the authorship tracking system documented in the project brief. Human edits and AI edits are tracked separately through frontmatter timestamps.