"""
Target file for Tinker 1B, Part 2.

Move `apply_streak_bonus(combined_score, streak_days)` here from scoring.py,
then update the import at the top of scoring.py so `run_demo()` and the
Session Scorer tab still work exactly as before.
"""

def apply_streak_bonus(combined_score: int, streak_days: int) -> int:
    """Add a bonus for consecutive study days, capped at 100."""
    if isinstance(combined_score, bool) or not isinstance(combined_score, int):
        raise TypeError(f"combined_score must be an int, got {combined_score!r}")
    if isinstance(streak_days, bool) or not isinstance(streak_days, int):
        raise TypeError(f"streak_days must be an int, got {streak_days!r}")
    if not 0 <= combined_score <= 120:
        raise ValueError(f"combined_score must be between 0 and 120, got {combined_score}")
    if streak_days < 0:
        raise ValueError(f"streak_days must be non-negative, got {streak_days}")

    boosted = combined_score + streak_days * 2
    return min(boosted, 100)