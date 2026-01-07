#!/usr/bin/env python3
"""Execute a workflow skill via Claude CLI."""

import subprocess
import sys
from pathlib import Path

import click
from rich.console import Console

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.workflow import run_skill, WorkflowResult, WorkflowStatus
from tools.workflow.executor import log_execution

console = Console()

PROJECT_ROOT = Path(__file__).parent.parent
WORKFLOW_PATH = PROJECT_ROOT / "obsidian" / "workflow" / "workflow.md"


def print_result(result: WorkflowResult) -> None:
    """Print workflow result to console."""
    status_color = {
        WorkflowStatus.SUCCESS: "green",
        WorkflowStatus.ERROR: "red",
        WorkflowStatus.MAX_TURNS: "yellow",
        WorkflowStatus.PERMISSION_DENIED: "red",
    }
    color = status_color.get(result.status, "white")

    console.print(f"\n[bold]Workflow Result: {result.skill}[/bold]")
    console.print(f"  Status: [{color}]{result.status.value}[/{color}]")
    console.print(f"  Duration: {result.duration_seconds:.1f}s")
    console.print(f"  Cost: ${result.cost_usd:.4f}")
    console.print(f"  Turns: {result.turns_used}/{result.max_turns}")
    console.print(f"  Session: {result.session_id}")

    if result.output:
        console.print(f"\n[bold]Output:[/bold]")
        console.print(f"  {result.output[:500]}")

    if result.errors:
        console.print(f"\n[bold red]Errors:[/bold red]")
        for error in result.errors:
            console.print(f"  • {error}")


@click.command()
@click.argument("skill")
@click.option("--max-turns", default=20, help="Maximum conversation turns")
@click.option("--dry-run", is_flag=True, help="Show what would be executed without running")
@click.option("--no-log", is_flag=True, help="Don't log to workflow.md")
@click.option("--commit", is_flag=True, help="Commit changes after execution")
@click.option("--commit-author", default="southgate.ai Agent <agent@southgate.ai>",
              help="Git commit author")
def main(
    skill: str,
    max_turns: int,
    dry_run: bool,
    no_log: bool,
    commit: bool,
    commit_author: str,
) -> None:
    """Execute a workflow skill via Claude CLI.

    SKILL is the name of the skill to execute (e.g., 'validate-all', 'evolve').
    """
    console.print(f"[bold]Executing workflow:[/bold] {skill}")

    if dry_run:
        console.print("[yellow]DRY RUN - No changes will be made[/yellow]")

    # Run the skill
    result = run_skill(
        skill=skill,
        max_turns=max_turns,
        working_dir=PROJECT_ROOT,
        dry_run=dry_run,
    )

    print_result(result)

    # Log to workflow.md
    if not no_log and not dry_run and WORKFLOW_PATH.exists():
        log_execution(result, WORKFLOW_PATH)
        console.print(f"\n[dim]Logged to {WORKFLOW_PATH}[/dim]")

    # Commit changes if requested
    if commit and not dry_run:
        try:
            # Stage all changes
            subprocess.run(
                ["git", "add", "-A"],
                cwd=str(PROJECT_ROOT),
                check=True,
                capture_output=True,
            )

            # Check if there are changes to commit
            diff_result = subprocess.run(
                ["git", "diff", "--staged", "--quiet"],
                cwd=str(PROJECT_ROOT),
                capture_output=True,
            )

            if diff_result.returncode != 0:
                # There are changes to commit
                commit_msg = f"chore(auto): {skill} - {result.timestamp.strftime('%Y-%m-%d')}"
                subprocess.run(
                    ["git", "commit", "-m", commit_msg, f"--author={commit_author}"],
                    cwd=str(PROJECT_ROOT),
                    check=True,
                    capture_output=True,
                )
                console.print(f"\n[green]Committed:[/green] {commit_msg}")
            else:
                console.print("\n[dim]No changes to commit[/dim]")

        except subprocess.CalledProcessError as e:
            console.print(f"\n[red]Git error:[/red] {e}")

    # Exit with appropriate code
    if result.status in (WorkflowStatus.ERROR, WorkflowStatus.PERMISSION_DENIED):
        sys.exit(1)
    elif result.status == WorkflowStatus.MAX_TURNS:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
