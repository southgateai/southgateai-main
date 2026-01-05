# Weekly automation script for SouthgateAI
# Runs: work-todo, refine-draft, pessimistic-review, optimistic-review
# Schedule: Various days via Windows Task Scheduler

param(
    [switch]$DryRun,
    [ValidateSet("work-todo", "refine-draft", "pessimistic-review", "optimistic-review", "crosslink")]
    [string]$Task = "work-todo",
    [int]$MaxTurns = 20
)

$ErrorActionPreference = "Stop"
$ProjectRoot = "c:\Users\andy\Documents\sai\southgateai-main"
$LogFile = "$ProjectRoot\obsidian\project\automation-log.txt"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Set-Location $ProjectRoot

function Write-Log {
    param([string]$Message)
    $LogEntry = "$Timestamp - $Message"
    Write-Host $LogEntry
    Add-Content -Path $LogFile -Value $LogEntry
}

function Get-Cost {
    param($JsonResult)
    if ($JsonResult.cost_usd) {
        return $JsonResult.cost_usd
    }
    return "unknown"
}

Write-Log "Starting weekly automation: $Task"

if ($DryRun) {
    Write-Log "DRY RUN - No changes will be made"
    Write-Host "Would run: claude -p `"/$Task`" --output-format json --max-turns $MaxTurns"
    exit 0
}

try {
    # Determine allowed tools based on task
    $allowedTools = "Bash,Read,Glob,Grep,Edit,Write"
    if ($Task -eq "work-todo" -or $Task -eq "research-topic") {
        $allowedTools += ",WebSearch"
    }

    # Run the task
    $startTime = Get-Date
    $result = claude -p "/$Task" --output-format json --max-turns $MaxTurns --allowedTools $allowedTools 2>&1
    $endTime = Get-Date
    $duration = $endTime - $startTime

    # Try to parse JSON result
    try {
        $jsonResult = $result | ConvertFrom-Json
        $cost = Get-Cost $jsonResult
        Write-Log "Task completed - Duration: $($duration.TotalMinutes)m, Cost: $cost"
    }
    catch {
        Write-Log "Task completed - Duration: $($duration.TotalMinutes)m (could not parse cost)"
    }

    # Stage any changes
    git add -A

    # Check if there are changes to commit
    $hasChanges = git diff --staged --quiet; $LASTEXITCODE -ne 0

    if ($hasChanges) {
        $dayOfWeek = (Get-Date).DayOfWeek
        $commitMsg = "chore(auto): Weekly $Task ($dayOfWeek) - $(Get-Date -Format 'yyyy-MM-dd')"
        git commit -m $commitMsg --author="southgate.ai Agent <agent@southgate.ai>"
        Write-Log "Changes committed: $commitMsg"
    }
    else {
        Write-Log "No changes to commit"
    }
}
catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    exit 1
}

Write-Log "Weekly automation complete"
