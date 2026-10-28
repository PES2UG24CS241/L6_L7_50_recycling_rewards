import pytest
from recycling_rewards import (
    reward_points,
    collection_accepted,
    slot_status,
)


# Tests for reward_points()

def test_unknown_material():
    with pytest.raises(ValueError, match="unknown material"):
        reward_points("glass", 10, False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        reward_points("paper", -1, False)


def test_weight_at_minimum_returns_zero():
    assert reward_points("paper", 5, False) == 0


def test_weight_below_minimum_with_bonus():
    assert reward_points("paper", 4, True) == 0


def test_paper_reward_without_bonus():
    assert reward_points("paper", 6, False) == 6


def test_paper_reward_with_bonus():
    assert reward_points("paper", 6, True) == 12


def test_plastic_reward():
    assert reward_points("plastic", 4, False) == 6


def test_metal_reward():
    assert reward_points("metal", 3, False) == 12


def test_metal_large_extra_weight():
    assert reward_points("metal", 23, False) == 378


def test_nonmetal_large_extra_weight():
    assert reward_points("plastic", 24, False) == 210


def test_metal_bonus_does_not_reduce_minimum():
    assert reward_points("metal", 2, True) == 0


# Tests for collection_accepted()

def test_hazardous_collection_within_limit():
    assert collection_accepted(5, 2, True) is True


def test_hazardous_collection_over_limit():
    assert collection_accepted(6, 2, True) is False


def test_collection_over_50_kg():
    assert collection_accepted(51, 1, False) is False


def test_collection_with_three_bags():
    assert collection_accepted(20, 3, False) is True


def test_collection_with_more_than_three_bags():
    assert collection_accepted(20, 4, False) is False


# Tests for slot_status()

def test_morning_slot_open_at_cutoff():
    assert slot_status(20, True, False) == "open"


def test_morning_slot_late():
    assert slot_status(19, True, False) == "late"


def test_morning_slot_missed():
    assert slot_status(4, True, False) == "missed"


def test_evening_slot_open_at_cutoff():
    assert slot_status(10, False, False) == "open"


def test_evening_slot_late():
    assert slot_status(9, False, False) == "late"


def test_evening_slot_missed():
    assert slot_status(-6, False, False) == "missed"


def test_holiday_morning_cutoff():
    assert slot_status(35, True, True) == "open"


def test_holiday_evening_cutoff():
    assert slot_status(25, False, True) == "open"
