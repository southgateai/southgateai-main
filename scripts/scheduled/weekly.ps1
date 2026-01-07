# Weekly automation script for The Unfinishable Map
# Runs: evolve, refine-draft, pessimistic-review, optimistic-review, crosslink
# Schedule: Various days via Windows Task Scheduler

param(
    [switch]$DryRun,
    [ValidateSet("evolve", "refine-draft", "pessimistic-review", "optimistic-review", "crosslink")]
    [string]$Task = "evolve",
    [int]$MaxTurns = 25
)

$ErrorActionPreference = "Stop"
$ProjectRoot = "c:\Users\andy\Documents\sai\theunfinishablemap"
$UvPath = "C:\Users\andy\.local\bin\uv.exe"
$LogFile = "$ProjectRoot\obsidian\workflow\automation-log.txt"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Set-Location $ProjectRoot

function Write-Log {
    param([string]$Message)
    $LogEntry = "$Timestamp - $Message"
    Write-Host $LogEntry
    Add-Content -Path $LogFile -Value $LogEntry
}

Write-Log "Starting weekly automation: $Task"

if ($DryRun) {
    Write-Log "DRY RUN - No changes will be made"
    & $UvPath run python scripts/run_workflow.py $Task --dry-run
    exit 0
}

try {
    # Crosslink is a special case - run Python directly
    if ($Task -eq "crosslink") {
        & $UvPath run python scripts/curate.py crosslink hugo/content/ --apply
        $exitCode = $LASTEXITCODE

        # Commit if changes
        git add -A
        git diff --staged --quiet
        if ($LASTEXITCODE -ne 0) {
            $dayOfWeek = (Get-Date).DayOfWeek
            $commitMsg = "chore(auto): Weekly crosslink ($dayOfWeek) - $(Get-Date -Format 'yyyy-MM-dd')"
            git commit -m $commitMsg --author="southgate.ai Agent <agent@southgate.ai>"
            Write-Log "Changes committed: $commitMsg"
        }
    }
    else {
        # Run the workflow executor
        & $UvPath run python scripts/run_workflow.py $Task --commit --max-turns $MaxTurns
        $exitCode = $LASTEXITCODE
    }

    if ($exitCode -eq 0) {
        Write-Log "Task completed successfully"
    }
    elseif ($exitCode -eq 2) {
        Write-Log "Task hit max turns limit"
    }
    else {
        Write-Log "Task failed with exit code $exitCode"
        exit $exitCode
    }
}
catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    exit 1
}

Write-Log "Weekly automation complete"
