---
name: work-todo
description: Pick and execute the highest priority task from the todo queue. Creates content as drafts for human review.
---

# Work Todo

Orchestrator skill that picks the highest priority task from the queue and executes it.

## When to Use

- Scheduled automated runs (Mon/Thu)
- When `/work-todo` is invoked
- When looking for the next task to work on

## Instructions

### 1. Read the Todo Queue

Read `obsidian/project/todo.md` and parse the active tasks.

### 2. Select Task

Choose the highest priority non-blocked task:

1. **Priority order**: P0 > P1 > P2 > P3
2. **Within same priority**: Oldest first (by position in file)
3. **Skip if blocked**: Check `Blocked-by` field

### 3. Execute Based on Type

#### Type: `expand-topic`
Run the `/expand-topic` skill with the topic from the task.

#### Type: `research-topic`
Run the `/research-topic` skill with the topic from the task.

#### Type: `refine-draft`
Run the `/refine-draft` skill with the file from the task.

#### Type: `validate-all`
Run the `/validate-all` skill.

#### Type: `check-tenets`
Run the `/check-tenets` skill.

#### Type: `pessimistic-review`
Run the `/pessimistic-review` skill.

#### Type: `optimistic-review`
Run the `/optimistic-review` skill.

#### Type: Other
Execute the task directly based on its description.

### 4. Update Todo Queue

After task completion, update `obsidian/project/todo.md`:

Move the task from "Active Tasks" to "Completed Tasks":

```markdown
## Completed Tasks

### ✓ YYYY-MM-DD: [Task title]
- **Type**: [type]
- **Result**: [brief result]
- **Output**: [file created/modified, if any]
```

### 5. Handle Subtasks

If the task revealed additional work needed:

Add new tasks to the Active Tasks section with appropriate priority:
```markdown
### P2: [New subtask]
- **Type**: [type]
- **Status**: pending
- **Notes**: Discovered while working on [parent task]
```

### 6. Log to Changelog

Append to `obsidian/project/changelog.md`:
```markdown
### HH:MM - work-todo
- **Status**: Success/Partial/Failed
- **Task**: "[task title]"
- **Type**: [task type]
- **Duration**: Xm Ys
- **Output**: [what was produced]
- **Subtasks added**: [count or "None"]
```

### 7. Commit

Create a git commit with message describing what was done:
```
feat(content): [Description based on task type]

Task: [task title]
Type: [type]
[Additional context]
```

## Task Selection Rules

### Never Select
- Tasks with `Status: in-progress` (already being worked)
- Tasks with `Status: blocked`
- Tasks with unmet `Blocked-by` dependencies

### Prefer
- P0 tasks (urgent)
- Tasks that unblock other tasks
- Tasks aligned with current content gaps

### Limit
- Only execute ONE task per invocation
- If task is very large, complete a reasonable chunk and note remaining work

## Error Handling

If a task fails:
1. Do NOT mark it complete
2. Update its status to note the failure
3. Add notes about what went wrong
4. Log the failure to changelog
5. Create a subtask if a specific fix is needed

```markdown
### P1: [Original task]
- **Type**: [type]
- **Status**: failed
- **Notes**: Failed on YYYY-MM-DD: [error description]
```

## Important

- Execute only ONE task per invocation
- All content changes create drafts
- Always update todo.md after completion
- Always log to changelog.md
- Create commits for all changes
- Don't skip tasks without reason
