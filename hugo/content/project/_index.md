---
ai_contribution: 100
ai_generated_date: 2026-01-03
ai_modified: 2026-01-04 00:00:00+00:00
ai_system: claude-opus-4-5-20251101
author: Andy Southgate
concepts: []
created: 2026-01-03
date: &id001 2026-01-03
draft: false
human_modified: 2026-01-05 14:16:56+03:00
last_curated: null
modified: *id001
related_articles:
- '[[project-brief]]'
- '[[automation]]'
- '[[todo]]'
- '[[changelog]]'
title: The Unfinishable Map Project
topics: []
---

The Unfinishable Map is a philosophical content platform exploring the nature and meaning of life. The project combines human insight with AI-assisted research to build a coherent worldview expressed through structured content.

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

**Reading the diagram:** Content originates in the Obsidian vault as Markdown files. Python sync tools convert Obsidian-style wikilinks to standard Markdown links and copy files to Hugo's content directory. Hugo then builds HTML pages from this content. The resulting static site is deployed to Netlify for hosting.

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
- [automation](/project/automation/) - AI automation system for content development
- [todo](/project/todo/) - Task queue for AI and human work
- [changelog](/project/changelog/) - Log of all AI activity

## Contributing

Content contributions follow the authorship tracking system documented in the project brief. Human edits and AI edits are tracked separately through frontmatter timestamps.