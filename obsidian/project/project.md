---
title: SouthgateAI Project
created: 2026-01-03
modified: 2026-01-03
human_modified: 2026-01-03T16:05:09+03:00
ai_modified: 2026-01-03T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project-brief]]"
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-01-03
last_curated:
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

- [[project-brief]] - Project aims, methods, and design decisions
- [[tenets]] - Human-curated foundational statements

## Contributing

Content contributions follow the authorship tracking system documented in the project brief. Human edits and AI edits are tracked separately through frontmatter timestamps.
