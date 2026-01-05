---
title: AI Automation System
created: 2026-01-05
modified: 2026-01-05
human_modified: 2026-01-05
ai_modified: 2026-01-05T17:30:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project]]"
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-01-05
last_curated:
---

This site uses scheduled AI automation to develop content over time. The system is designed to converge toward a comprehensive philosophical compendium while maintaining human oversight and alignment with the site's [[tenets]].

## How It Works

```mermaid
flowchart TD
    subgraph Human
        H1[Prioritize tasks in todo.md]
        H2[Review drafts]
        H3[Publish or refine]
    end

    subgraph AI Scheduled Tasks
        A1[Daily: Validate content]
        A2[Weekly: Execute todo items]
        A3[Weekly: Review for weaknesses]
        A4[Weekly: Find opportunities]
        A5[Monthly: Check tenet alignment]
    end

    subgraph Output
        O1[Draft articles]
        O2[Research notes]
        O3[Review reports]
        O4[Changelog entries]
    end

    H1 --> A2
    A1 --> O4
    A2 --> O1
    A2 --> O2
    A3 --> O3
    A4 --> O3
    A5 --> O3
    O1 --> H2
    O3 --> H1
    H2 --> H3
```

**Key principle:** All AI-generated content is created as drafts (`draft: true`). A human must review and approve before publishing.

## Skills (Slash Commands)

The AI has access to these specialized skills:

| Skill | Purpose | Output |
|-------|---------|--------|
| `/validate-all` | Check frontmatter, links, find orphans | Changelog entry |
| `/check-tenets` | Verify content aligns with 5 tenets | Review report |
| `/pessimistic-review` | Find weaknesses from critic perspectives | Review report |
| `/optimistic-review` | Find strengths from supporter perspectives | Review report |
| `/research-topic` | Web research on a topic | Research notes |
| `/expand-topic` | Generate new article | Draft article |
| `/refine-draft` | Improve existing draft | Updated draft |
| `/work-todo` | Execute highest priority task | Depends on task |

## Multi-Perspective Reviews

The review skills use philosophical personas to generate diverse critiques:

### Pessimistic Review Critics

| Persona | Worldview | Attack Vector |
|---------|-----------|---------------|
| Patricia Churchland | Eliminative Materialism | Consciousness talk is folk psychology |
| Daniel Dennett | Hard Physicalism | You're inflating intuitions into metaphysics |
| Max Tegmark | Quantum Skepticism | Decoherence kills quantum mind theories |
| David Deutsch | Many-Worlds Defense | Intuition shouldn't override mathematical elegance |
| Karl Popper | Empiricism | What experiment could prove you wrong? |
| Nagarjuna | Buddhist Philosophy | You're clinging to an illusory self |

### Optimistic Review Supporters

| Persona | Worldview | Praise Focus |
|---------|-----------|--------------|
| David Chalmers | Property Dualism | Taking the hard problem seriously |
| Henry Stapp | Quantum Mind | Engaging physics-consciousness interface |
| Thomas Nagel | Phenomenology | Centering first-person experience |
| Alfred N. Whitehead | Process Philosophy | Avoiding crude substance dualism |
| Robert Kane | Libertarian Free Will | Taking agency seriously |
| Colin McGinn | Mysterianism | Epistemic humility |

## Task Queue

Tasks are managed in [[todo]]:

- **P0**: Urgent - execute immediately
- **P1**: High - execute this week
- **P2**: Medium - execute when time permits
- **P3**: Low - nice to have, needs human approval

The AI picks the highest priority non-blocked task and executes it. All activity is logged to [[changelog]].

## Schedule

| Frequency | Task | Purpose |
|-----------|------|---------|
| Daily 2AM | `/validate-all` | Health check |
| Mon/Thu 3AM | `/work-todo` | Content development |
| Tue 3AM | `/refine-draft` | Quality improvement |
| Wed 3AM | Crosslink generation | Content relationships |
| Fri 3AM | `/pessimistic-review` | Find weaknesses |
| Sat 3AM | `/optimistic-review` | Find opportunities |
| 1st of month | Progress report | Strategic assessment |
| 15th of month | `/check-tenets` | Alignment verification |

## Safety Mechanisms

1. **Draft-first policy**: All AI content has `draft: true`
2. **Tenet alignment**: Monthly checks against foundational commitments
3. **Human prioritization**: Humans control the todo queue
4. **Full logging**: Every action recorded in changelog
5. **Authorship tracking**: AI edits marked with `ai_modified` timestamp

## Running Locally

```powershell
# Daily validation
.\scripts\scheduled\daily.ps1

# Execute a todo item
.\scripts\scheduled\weekly.ps1 -Task work-todo

# Dry run (no changes)
.\scripts\scheduled\daily.ps1 -DryRun
```

## Technical Details

The automation is built on:

- **Claude Code** (`claude -p` command) for AI execution
- **Skills** defined in `.claude/skills/*/SKILL.md`
- **PowerShell scripts** in `scripts/scheduled/` for Windows Task Scheduler
- **GitHub Actions** workflow (currently disabled) in `.github/workflows/`

For implementation details, see the [GitHub repository](https://github.com/southgateai/southgateai).

## Convergence Goal

The system aims to build a complete "meaning of life" compendium by:

1. Replacing all placeholder content with substantive articles
2. Covering major philosophical positions on meaning
3. Building a coherent cross-linked web of ideas
4. Passing pessimistic reviews with no major gaps
5. Maintaining alignment with site tenets
6. Human review and approval of all content

Progress is tracked in monthly progress reports.
