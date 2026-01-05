# Daily automation script for SouthgateAI
# Runs: validate-all, sync-and-build
# Schedule: Daily at 2 AM via Windows Task Scheduler

param(
    [switch]$DryRun,
    [string]$Task = "validate-all"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = "c:\Users\andy\Documents\sai\southgateai-main"
$LogFile = "$ProjectRoot\obsidian\project\automation-log.txt"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Change to project directory
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

Write-Log "Starting daily automation: $Task"

if ($DryRun) {
    Write-Log "DRY RUN - No changes will be made"
    Write-Host "Would run: claude -p `"/$Task`" --output-format json --max-turns 10"
    exit 0
}

try {
    # Run the task
    $startTime = Get-Date
    $result = claude -p "/$Task" --output-format json --max-turns 10 2>&1
    $endTime = Get-Date
    $duration = $endTime - $startTime

    # Try to parse JSON result
    try {
        $jsonResult = $result | ConvertFrom-Json
        $cost = Get-Cost $jsonResult
        Write-Log "Task completed - Duration: $($duration.TotalSeconds)s, Cost: $cost"
    }
    catch {
        Write-Log "Task completed - Duration: $($duration.TotalSeconds)s (could not parse cost)"
    }

    # Stage any changes
    git add -A

    # Check if there are changes to commit
    $hasChanges = git diff --staged --quiet; $LASTEXITCODE -ne 0

    if ($hasChanges) {
        $commitMsg = "chore(auto): Daily $Task - $(Get-Date -Format 'yyyy-MM-dd')"
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

Write-Log "Daily automation complete"
