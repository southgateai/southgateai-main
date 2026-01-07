"""Staleness detection for maintenance tasks."""

from datetime import datetime, timezone
from typing import Optional

from .state import EvolutionState
from .scoring import ScoredTask, score_synthetic_task


def check_staleness(
    skill_name: str,
    state: EvolutionState,
    now: Optional[datetime] = None,
) -> tuple[bool, int]:
    """
    Check if a maintenance task is overdue.

    Args:
        skill_name: Name of the skill to check
        state: Current evolution state
        now: Current time (defaults to now)

    Returns:
        Tuple of (is_overdue, days_overdue)
    """
    if now is None:
        now = datetime.now(timezone.utc)

    # Get last run time
    last_run = state.last_runs.get(skill_name)
    if last_run is None:
        # Never run - consider it very overdue
        return True, 30

    # Ensure timezone awareness
    if last_run.tzinfo is None:
        last_run = last_run.replace(tzinfo=timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    # Get cadence
    cadence_days = state.cadences.get(skill_name, 7)

    # Calculate days since last run
    days_since = (now - last_run).days

    # Check against cadence
    days_overdue = days_since - cadence_days

    return days_overdue > 0, max(0, days_overdue)


def get_overdue_tasks(
    state: EvolutionState,
    now: Optional[datetime] = None,
) -> list[ScoredTask]:
    """
    Get all overdue maintenance tasks as synthetic scored tasks.

    Only returns tasks that exceed their overdue threshold (not just past cadence).

    Args:
        state: Current evolution state
        now: Current time (defaults to now)

    Returns:
        List of ScoredTask for overdue maintenance tasks
    """
    if now is None:
        now = datetime.now(timezone.utc)

    overdue_tasks: list[ScoredTask] = []

    # Check each maintenance task
    maintenance_skills = [
        "validate-all",
        "pessimistic-review",
        "optimistic-review",
        "check-tenets",
        "check-links",
        "deep-review",
    ]

    for skill_name in maintenance_skills:
        is_overdue, days_overdue = check_staleness(skill_name, state, now)

        if not is_overdue:
            continue

        # Check against overdue threshold (not just cadence)
        threshold = state.overdue_thresholds.get(skill_name, 3)
        if days_overdue < threshold:
            continue

        # Create synthetic task
        scored = score_synthetic_task(skill_name, days_overdue, state)
        overdue_tasks.append(scored)

    return overdue_tasks


def get_status_report(state: EvolutionState, now: Optional[datetime] = None) -> str:
    """
    Generate a human-readable staleness status report.

    Args:
        state: Current evolution state
        now: Current time (defaults to now)

    Returns:
        Markdown-formatted status report
    """
    if now is None:
        now = datetime.now(timezone.utc)

    lines = ["## Maintenance Status", ""]
    lines.append("| Task | Last Run | Cadence | Status |")
    lines.append("|------|----------|---------|--------|")

    maintenance_skills = [
        "validate-all",
        "pessimistic-review",
        "optimistic-review",
        "check-tenets",
        "check-links",
        "deep-review",
    ]

    for skill_name in maintenance_skills:
        last_run = state.last_runs.get(skill_name)
        cadence = state.cadences.get(skill_name, 7)

        if last_run is None:
            last_run_str = "Never"
            status = "OVERDUE"
        else:
            # Ensure timezone awareness
            if last_run.tzinfo is None:
                last_run = last_run.replace(tzinfo=timezone.utc)
            if now.tzinfo is None:
                now = now.replace(tzinfo=timezone.utc)

            days_ago = (now - last_run).days
            last_run_str = f"{days_ago}d ago"

            is_overdue, days_overdue = check_staleness(skill_name, state, now)
            threshold = state.overdue_thresholds.get(skill_name, 3)

            if days_overdue >= threshold:
                status = f"OVERDUE ({days_overdue}d)"
            elif is_overdue:
                status = f"Due ({days_overdue}d)"
            else:
                status = "OK"

        lines.append(f"| {skill_name} | {last_run_str} | {cadence}d | {status} |")

    return "\n".join(lines)
