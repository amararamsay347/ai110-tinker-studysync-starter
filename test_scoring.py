"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

import pytest

from scoring import session_rating
from scoring_helpers import apply_streak_bonus


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).

def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"

def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


# --- Edge cases / bad input handling ---

def test_session_rating_rejects_out_of_range_high():
    with pytest.raises(ValueError):
        session_rating(1000)


def test_session_rating_rejects_negative():
    with pytest.raises(ValueError):
        session_rating(-46)


def test_session_rating_rejects_float():
    with pytest.raises(TypeError):
        session_rating(69.5)


def test_session_rating_rejects_bool():
    with pytest.raises(TypeError):
        session_rating(True)


def test_apply_streak_bonus_caps_at_100():
    assert apply_streak_bonus(95, 3) == 100


def test_apply_streak_bonus_rejects_out_of_range_score():
    with pytest.raises(ValueError):
        apply_streak_bonus(1000, 3)


def test_apply_streak_bonus_rejects_negative_score():
    with pytest.raises(ValueError):
        apply_streak_bonus(-46, 3)


def test_apply_streak_bonus_rejects_float_score():
    with pytest.raises(TypeError):
        apply_streak_bonus(69.5, 3)


def test_apply_streak_bonus_rejects_negative_streak():
    with pytest.raises(ValueError):
        apply_streak_bonus(80, -1)


def test_apply_streak_bonus_rejects_float_streak():
    with pytest.raises(TypeError):
        apply_streak_bonus(80, 2.5)