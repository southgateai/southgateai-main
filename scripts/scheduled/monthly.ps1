# Monthly automation script for SouthgateAI
# Runs: check-tenets, progress-report, research-gaps
# Schedule: 1st and 15th of month via Windows Task Scheduler

param(
    [switch]$DryRun,
    [ValidateSet("check-tenets", "progress-report", "research-gaps")]
    [string]$Task = "check-tenets",
    [int]$MaxTurns = 15
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

Write-Log "Starting monthly automation: $Task"

if ($DryRun) {
    Write-Log "DRY RUN - No changes will be made"
    Write-Host "Would run: claude -p `"/$Task`" --output-format json --max-turns $MaxTurns"
    exit 0
}

try {
    # Determine allowed tools based on task
    $allowedTools = "Bash,Read,Glob,Grep,Edit,Write"
    if ($Task -eq "research-gaps") {
        $allowedTools += ",WebSearch"
    }

    # Build the prompt based on task
    $prompt = "/$Task"
    if ($Task -eq "progress-report") {
        # Progress report is a special prompt, not a skill
        $prompt = @"
Generate a progress report for the SouthgateAI compendium.

Analyze:
1. Content coverage - what topics/concepts exist vs what's needed
2. Draft status - how many drafts await review
3. Quality - recent review findings
4. Tenet alignment - any concerns
5. Next priorities - what should be worked on

Output to obsidian/project/reviews/progress-report-$(Get-Date -Format 'yyyy-MM-dd').md
"@
    }

    # Run the task
    $startTime = Get-Date
    $result = claude -p $prompt --output-format json --max-turns $MaxTurns --allowedTools $allowedTools 2>&1
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
        $commitMsg = "chore(auto): Monthly $Task - $(Get-Date -Format 'yyyy-MM-dd')"
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

Write-Log "Monthly automation complete"
