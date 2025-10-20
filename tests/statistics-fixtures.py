""" Just a note - it could be a bit redundant, but i'd prefer to include fixture tests"""
import pytest
from faker import Faker
from statistics import mean, median, variance
from collections import Counter
from src.utils.statistics import calculate_statistics 


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def fake_berries(fake):
    def _generate(num_items=10, min_growth=1, max_growth=20):
        return [
            {
                "name": fake.unique.word(),
                "growth_time": fake.random_int(min_growth, max_growth)
            }
            for _ in range(num_items)
        ]
    return _generate


@pytest.mark.parametrize("num_items", [0, 1, 5, 10, 25])
def test_calculate_statistics_with_faker(fake_berries, num_items):
    berries_data = fake_berries(num_items)
    result = calculate_statistics(berries_data)

    if not berries_data:
        assert result == {}
        return

    growth_times = [b["growth_time"] for b in berries_data]

    expected = {
        "berries_names": sorted([b["name"] for b in berries_data]),
        "min_growth_time": min(growth_times),
        "max_growth_time": max(growth_times),
        "median_growth_time": median(growth_times),
        "mean_growth_time": mean(growth_times),
        "variance_growth_time": variance(growth_times) if len(growth_times) > 1 else 0,
        "frequency_growth_time": dict(Counter(sorted(growth_times))),
    }

    for key, value in expected.items():
        assert result[key] == value
