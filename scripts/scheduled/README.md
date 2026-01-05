# Scheduled Automation Scripts

These PowerShell scripts are designed to run via Windows Task Scheduler for automated content maintenance.

## Scripts

### daily.ps1
**Frequency**: Daily at 2 AM
**Tasks**: `validate-all` (default)

```powershell
# Run validation
.\scripts\scheduled\daily.ps1

# Dry run (no changes)
.\scripts\scheduled\daily.ps1 -DryRun

# Run specific task
.\scripts\scheduled\daily.ps1 -Task validate-all
```

### weekly.ps1
**Frequency**: Various days
**Tasks**: `work-todo`, `refine-draft`, `pessimistic-review`, `optimistic-review`, `crosslink`

```powershell
# Work on highest priority todo
.\scripts\scheduled\weekly.ps1 -Task work-todo

# Run pessimistic review
.\scripts\scheduled\weekly.ps1 -Task pessimistic-review

# With custom max turns
.\scripts\scheduled\weekly.ps1 -Task work-todo -MaxTurns 30
```

**Suggested Schedule**:
- Monday 3AM: `work-todo`
- Tuesday 3AM: `refine-draft`
- Wednesday 3AM: `crosslink`
- Thursday 3AM: `work-todo`
- Friday 3AM: `pessimistic-review`
- Saturday 3AM: `optimistic-review`

### monthly.ps1
**Frequency**: 1st and 15th of month
**Tasks**: `check-tenets`, `progress-report`, `research-gaps`

```powershell
# Check tenet alignment
.\scripts\scheduled\monthly.ps1 -Task check-tenets

# Generate progress report
.\scripts\scheduled\monthly.ps1 -Task progress-report
```

**Suggested Schedule**:
- 1st of month: `progress-report`, `research-gaps`
- 15th of month: `check-tenets`

## Setting Up Windows Task Scheduler

1. Open Task Scheduler (`taskschd.msc`)
2. Create a new task:
   - **General**: Run whether user is logged in or not
   - **Triggers**: Daily at 2:00 AM (or your preferred time)
   - **Actions**: Start a program
     - Program: `powershell.exe`
     - Arguments: `-ExecutionPolicy Bypass -File "c:\Users\andy\Documents\sai\southgateai-main\scripts\scheduled\daily.ps1"`
     - Start in: `c:\Users\andy\Documents\sai\southgateai-main`
   - **Conditions**: Start only if AC power (recommended)
   - **Settings**: If task fails, restart every 1 hour

## Logs

All scripts log to `obsidian/project/automation-log.txt`.

## Cost Tracking

Scripts attempt to parse cost from Claude's JSON output and log it. Review `automation-log.txt` to monitor usage.

## Troubleshooting

1. **Claude not found**: Ensure `claude` is in PATH
2. **Permission errors**: Run as administrator or adjust execution policy
3. **Git errors**: Ensure git credentials are configured for automated commits
