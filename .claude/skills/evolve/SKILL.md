# Evolve

The main orchestrator for autonomous site evolution. Intelligently selects and executes tasks based on priority, staleness, and site goals. Automatically replenishes the task queue when empty.

## Usage

```
/evolve [mode]
```

Modes:
- `quick` - Execute 1 task (highest scored)
- (default) - Standard session, execute 2-3 tasks
- `deep` - Execute 3-5 tasks including maintenance

## Session Workflow

### 0. Check Queue Health (Pre-flight)

Before doing anything else, check if the queue needs replenishment:

```python
state = load_state('obsidian/workflow/evolution-state.yaml')
todo = parse_todo('obsidian/workflow/todo.md')

active_tasks = count_active_tasks(todo)  # P0-P2 only, P3 doesn't count
needs_replenishment = active_tasks < 3

if needs_replenishment:
    # Run replenishment before proceeding
    invoke('/replenish-queue')
    # Reload todo after replenishment
    todo = parse_todo('obsidian/workflow/todo.md')
```

**Threshold**: Replenish when fewer than 3 active tasks (P0-P2) remain. P3 tasks don't count toward this threshold since they require human promotion.

**Note**: Replenishment runs FIRST, before staleness checks or task selection, to ensure there's always meaningful work available.

### 1. Load State

Read `obsidian/workflow/evolution-state.yaml` to get:
- Last run timestamps for maintenance tasks
- Failed task retry counts
- Content statistics

### 2. Check Staleness

For each maintenance task, check if overdue:

| Task | Cadence | Inject when overdue by |
|------|---------|------------------------|
| validate-all | 1 day | 2 days |
| pessimistic-review | 7 days | 3 days |
| optimistic-review | 7 days | 3 days |
| check-tenets | 30 days | 5 days |
| check-links | 7 days | 3 days |
| deep-review | 1 day | 2 days |
| tune-system | 30 days | 45 days |
| research-voids | 1 day | 2 days |

Create synthetic tasks for overdue maintenance.

### 3. Load and Score Tasks

Read `obsidian/workflow/todo.md` and score all tasks:

```
SCORE = PRIORITY_BASE + STALENESS_BONUS + URGENCY_MOD - FAILURE_PENALTY

PRIORITY_BASE: P0=400, P1=300, P2=200, P3=100
STALENESS_BONUS: days_overdue * 20 (max 150) - for synthetic maintenance tasks
URGENCY_MOD: +50 critical issue, +30 medium issue, +20 has research
FAILURE_PENALTY: -100 per failure, -500 at 3+ failures
```

### 4. Select Tasks

Based on mode:
- **Quick**: Top 1 task
- **Standard**: Top 2-3 tasks (at least 1 content + 1 maintenance if overdue)
- **Deep**: Top 3-5 tasks

Never select:
- Tasks with 3+ failures (these are blocked)
- P3 tasks (require human promotion)
- Tasks with unmet dependencies

### 5. Execute Tasks

For each selected task:

1. If synthetic (maintenance): invoke the skill directly
   - `/validate-all`
   - `/pessimistic-review`
   - `/optimistic-review`
   - `/check-tenets`
   - `/check-links`
   - `/deep-review`
   - `/tune-system`
   - `/research-voids`

2. If queue task: invoke based on type
   - `expand-topic` → `/expand-topic [topic]`
   - `research-topic` → `/research-topic [topic]`
   - `refine-draft` → `/refine-draft [file]`
   - `cross-review` → `/deep-review [target-file]` with cross-reference context

3. After each task:
   - Record outcome (success/failed/partial)
   - If failed: increment retry count in state
   - If 3+ failures: move to Blocked section in todo.md
   - If success: mark completed in todo.md (see Completed Task Format below)
   - **If success AND task type generates chains**: update `task_chains` in state (see Task Chain Recording below)

4. **Commit after each task** (for easy reversion):
   - If task modified files, commit immediately
   - Use task-specific commit message:
     ```
     feat(auto): [task-type] - [brief description]

     Task: [task title]
     Session: [session number]
     ```
   - Examples:
     - `feat(auto): expand-topic - retrocausality concept page`
     - `feat(auto): research-topic - Libet experiments`
     - `chore(auto): validate-all - daily health check`
   - Use AI authorship for commit

### 6. Update State

Update `obsidian/workflow/evolution-state.yaml`:
- `last_updated` timestamp
- `session_count` increment
- `last_runs` for any maintenance tasks executed
- `failed_tasks` counts
- `recent_tasks` history
- `content_stats` (recount files)
- `progress` metrics

### 7. Calculate Convergence

Compute convergence score (0-100%):
- 50% weight: Content breadth (topics, concepts, arguments written)
- 30% weight: Quality (critical/medium issues from reviews)
- 20% weight: Completeness (no placeholders)

### 8. Generate Report

Output session summary:

```markdown
## Evolution Session Complete

**Mode**: standard
**Tasks executed**: 3
**Duration**: ~15 minutes

### Tasks
1. ✓ Run pessimistic-review (overdue by 5 days) - Score: 350
2. ✓ Write article on hard problem - Score: 300
3. ✗ Research quantum decoherence - Failed (attempt 2/3)

### Metrics
- Convergence: 28% → 32%
- Content: 11 files (+1)
- Quality: 0 critical, 2 medium issues

### Next Session
Recommended tasks:
1. P1: Address circularity concern (Score: 300)
2. validate-all (due tomorrow)
```

### 9. Add Highlight (if warranted)

If the session produced highlight-worthy work, add an item to the highlights page:

**Highlight-worthy:**
- New article written → highlight with link to article
- Significant insight from review → highlight the finding
- Research completed → highlight key discovery
- Major refinement → highlight what improved

**Not highlight-worthy (skip):**
- Routine maintenance (validate-all, check-links, check-tenets)
- Failed tasks
- Minor refinements

Use the CLI:
```bash
uv run python scripts/highlights.py add "Title" "Description (max 280 chars)" --type new-article --link "[[article]]"
```

The manager enforces max 1 highlight per day—if already added, it will silently skip.

### 10. Sync and Validate Site

Before the final commit, sync content to Hugo and verify no broken links:

```bash
# Sync Obsidian → Hugo
uv run python scripts/sync.py

# Build site (validates templates and content)
cd hugo && hugo --gc --minify

# Start server and check links
hugo server &
sleep 3
python .claude/skills/check-links/scripts/check_links.py
```

**If broken links are found:**
1. Log them to the session report
2. For each broken link, check if:
   - The target file exists but has `draft: true` → Fix by setting `draft: false`
   - The wikilink is malformed → Fix the source file
   - The target doesn't exist → Note as issue in report
3. Re-sync after fixes
4. If links still broken after reasonable attempts, note in session report

This step catches issues like:
- Articles marked as drafts that are linked from published content
- Wikilink conversion errors
- Missing pages

### 11. Final Session Commit

After all tasks complete and site validation passes, commit session-level updates (state file, changelog, todo updates):

```
chore(auto): Evolution session [N] complete

Tasks executed: [count]
Convergence: [old]% → [new]%
```

Use AI authorship for the commit.

**Note:** Individual task outputs are committed in step 5.4. This final commit captures only the session bookkeeping (state, changelog, todo). This separation allows easy reversion of specific tasks without affecting session metadata.

## Handling Failures

When a task fails:
1. Increment retry count in `failed_tasks`
2. Log the failure reason
3. If retry count reaches 3:
   - Move task to "## Blocked Tasks (Needs Human)" section in todo.md
   - Add explanation of failure pattern
   - Do not retry until human intervenes

## Completed Task Format

When marking a task as completed, preserve all original information and add execution details:

```markdown
### ✓ YYYY-MM-DD: [Task title from original]
- **Type**: [original type]
- **Notes**: [ORIGINAL NOTES VERBATIM - do not modify or summarise]
- **Result**: [What was actually done]
- **Output**: [Files created/modified]
```

**Important:** The original `Notes` field must be preserved exactly as written. This maintains the human's original intent and reasoning. Add execution details in the separate `Result` and `Output` fields.

## Task Chain Recording

When certain task types complete successfully, record chain information for `/replenish-queue`:

### After `research-topic` completes:

Add to `task_chains.pending_articles` in evolution-state.yaml:
```yaml
pending_articles:
  - "research/panpsychism-consciousness-2026-01-08.md"
```

This signals that research exists without a corresponding article.

### After `expand-topic` completes:

1. **Remove from pending_articles** if this article was based on research
2. **Add to pending_cross_reviews** with related articles:

```yaml
pending_cross_reviews:
  - new_article: "concepts/panpsychism.md"
    review_targets:
      - "topics/hard-problem-of-consciousness.md"
      - "concepts/qualia.md"
    generated: "2026-01-08T10:00:00+00:00"
```

**Finding review targets**: Look at the new article's:
- `related_articles` frontmatter
- Wikilinks in content
- Topics/concepts that share themes

Maximum 2 review targets per article (configurable in state).

### After `cross-review` completes:

Remove the completed review from `pending_cross_reviews`:
```python
for chain in pending_cross_reviews:
    if chain['new_article'] == task.chain_parent:
        chain['review_targets'].remove(task.target_file)
        if not chain['review_targets']:
            pending_cross_reviews.remove(chain)
```

## Blocked Tasks Section

When a task is blocked, add to todo.md:

```markdown
## Blocked Tasks (Needs Human)

### P1: [Task title]
- **Failures**: 3
- **Last attempt**: 2026-01-06
- **Notes**: [ORIGINAL NOTES VERBATIM]
- **Error pattern**: [description of what went wrong]
- **Suggested action**: [how human might fix]
```

## State File Location

`obsidian/workflow/evolution-state.yaml`

## Dependencies

This skill uses:
- `tools/evolution/state.py` - State loading/saving
- `tools/evolution/scoring.py` - Task scoring
- `tools/evolution/staleness.py` - Staleness detection
- `tools/todo/processor.py` - Todo parsing

## Cross-Review Task Handling

When executing a `cross-review` task:

1. **Read the chain parent** (the new article that triggered this review)
2. **Read the target article** (the existing article to review)
3. **Analyze for**:
   - Places to add `[[new-article]]` wikilinks
   - Arguments that the new content supports or challenges
   - Terminology consistency
   - Missing cross-references
4. **Make edits** if improvements found
5. **Log findings** even if no edits made (document the review)

Example cross-review task:
```markdown
### P2: Review hard-problem-of-consciousness.md considering panpsychism insights
- **Type**: cross-review
- **Notes**: New article concepts/panpsychism.md may provide insights relevant to topics/hard-problem-of-consciousness.md.
- **Source**: chain (from panpsychism.md)
```

Execution:
1. Read `concepts/panpsychism.md` to understand what's new
2. Read `topics/hard-problem-of-consciousness.md` looking for:
   - References to panpsychism that could now link to the concept page
   - Arguments that panpsychism analysis strengthens or complicates
   - Missing context that panpsychism article provides
3. Edit hard-problem article if improvements found
4. Mark task complete with summary of changes (or "no changes needed")

## Queue Replenishment

The queue is automatically replenished when:
- Active tasks (P0-P2) drop below 3
- `needs_replenishment: true` in state file

Replenishment uses `/replenish-queue` which generates tasks from:
1. **Task chains**: Recent completions that should generate follow-ups
2. **Unconsumed research**: Research notes without corresponding articles
3. **Gap analysis**: Content areas needing expansion
4. **Staleness**: Content not reviewed recently

See `/replenish-queue` skill for full details.

## Notes

- P3 tasks are never auto-selected; human must promote to P2+
- Synthetic maintenance tasks compete fairly via scoring
- Each task is committed separately for easy reversion of individual tasks
- The skill is designed for manual triggering (2-3x per week)
- Queue replenishment happens automatically when needed (step 0)
