from statistics import mean, median, variance
from collections import Counter


def calculate_statistics(berries_data):

    if not berries_data:
        return {}
    try:
        growth_times = [b['growth_time'] for b in berries_data]
        berry_names = [b['name'] for b in berries_data]

        variance_growth = variance(growth_times) if len(growth_times) > 1 else 0
        freq = Counter(growth_times)
        return {
            "berries_names": berry_names,
            "min_growth_time": min(growth_times),
            "median_growth_time": median(growth_times),
            "max_growth_time": max(growth_times),
            "variance_growth_time": variance_growth,
            "mean_growth_time": mean(growth_times),
            "frequency_growth_time": dict(freq)
        }
    except Exception as e:
        print(f"An unexpected error: {e}")
        return {"error": "Unexpected error occurred while calculating statistics."}
