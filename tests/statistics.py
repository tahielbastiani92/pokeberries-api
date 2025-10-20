import pytest
from statistics import mean, median, variance
from collections import Counter
from src.utils.statistics import calculate_statistics


@pytest.mark.parametrize(
    "berries_data, expected_min,expected_max, expected_median, expected_mean, expected_variance",
    [
        (
            # N > 1 items
            [
                {"name": "rawst", "growth_time": 3},
                {"name": "sitrus", "growth_time": 6},
                {"name": "cheri", "growth_time": 3},
                {"name": "pecha", "growth_time": 9},
            ],
            3, 9, median([3, 6, 3, 9]), mean([3, 6, 3, 9]), variance([3, 6, 3, 9])
        ),
        (
            # Same items
            [
                {"name": "rawst", "growth_time": 5},
                {"name": "pecha", "growth_time": 5},
                {"name": "sitrus", "growth_time": 5},
            ],
            5, 5, median([5, 5, 5]), mean([5, 5, 5]), 0
        ),
        (
            # Single item
            [
                {"name": "cheri", "growth_time": 5},
            ],
            5, 5, median([5]), mean([5]), 0,
        ),
        (
            # No items
            [],
            None, None, None, None, None
        ),

    ],
)
def test_calculate_statistics_various_cases(
    berries_data, expected_min, expected_max, expected_median, expected_mean, expected_variance
):
    result = calculate_statistics(berries_data)
    if not berries_data:
        assert result == {}
        return

    growth_times = [b["growth_time"] for b in berries_data]

    assert result["berries_names"] == sorted([b["name"] for b in berries_data])
    assert result["min_growth_time"] == expected_min
    assert result["max_growth_time"] == expected_max
    assert result["median_growth_time"] == expected_median
    assert result["mean_growth_time"] == expected_mean
    assert result["variance_growth_time"] == expected_variance
    assert result["frequency_growth_time"] == dict(Counter(sorted(growth_times)))


def test_calculate_statistics_invalid_data():
    berries_data = [{"name": "cheri"}, {"name": "pecha", "growth_time": 7}]
    result = calculate_statistics(berries_data)
    assert "error" in result


def test_calculate_statistics_non_numeric_growth_time():
    berries_data = [
        {"name": "oran", "growth_time": "a"},
        {"name": "pecha", "growth_time": 5},
    ]
    result = calculate_statistics(berries_data)
    assert "error" in result

