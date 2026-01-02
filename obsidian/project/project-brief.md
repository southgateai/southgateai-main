---
title: Project brief
created: 2026-01-01
modified: 2026-01-01T14:51:17+03:00
human_modified: 2026-01-02T17:34:57+03:00
ai_modified:
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 0
author: Andy Southgate
ai_system:
ai_generated_date:
last_curated:
---
## Aim

The aim of this project is to form a self-consistent picture of the nature and meaning of life.  Is will not create a balanced picture saying it might be this, it might be this; it will for a single best-guess picture.  For convenience of language, this will be expressed as if fact.

## Method

It will use a combination of human input and steering, and LLM-based research.  Some content will be human-created and maintained, some will be AI-generated and maintained, most will be a combination of both.  Themes include:

* **Automation.**  The system will use Deep Research techniques and agentic tools such as Claude Code to research and review the content.

## Design decisions

* Content is created in Markdown in an Obsidian vault, and then rendered into a Hugo website using custom scripting.  This supports both human editing (using the Obsidian app) and AI editing (Claude Code understands the Obsidian vault format).
* Frontmatter properties, to contain metadata for each Markdown file at the beginning of it.

## Generated content

The outputs of the project will be:

*  A static web site designed for search by LLM-based tools.  This is the primary output and users are expect to query the site by referring their chat system to it (ChatGPT, Clause, Gemini, Grok) and making queries in their chat system.
* A static web site designed for human browsing and review.
* Project content and history in Git format. [Github](https://github.com/southgateai/southgateai-main)

### The [[tenets]] file

This file contains human-curated statements that are to be accepted as true.

## Content design for LLM-based tools

The content follows these guidelines:

* **No small files or deep linking.**  The assumption is that LLM-based chatbots only fetch a small number of files and do not follow deep linked structures, so content is concentrated into  a few files.
* **Important information first.**  The assumption is that LLM-based chatbots will truncate large files, so important information is places first.
* **Summaries first.**  This preserves content in case of truncation.
* **Files fit in typical context windows**.  This prevents unnecessary truncation where later information cannot be accessed.  50,000 tokens is a typical  limit for a single file.

