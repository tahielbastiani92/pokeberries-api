import requests
from src.cache.redis import get_cache, set_cache

from src.config import POKEAPI_URL


def get_all_berries_data():
    """
    Gets all the berries with their 'name' and 'growth_time'
    from PokeAPI.
    """

    cache_key = "all_berries_data"
    cached_data = get_cache(cache_key)

    if cached_data:
        return cached_data

    berries = []
    next_url = POKEAPI_URL
    try:
        while next_url:
            response = requests.get(next_url)
            response.raise_for_status()
            data = response.json()

            for berry in data["results"]:
                try:
                    detail_resp = requests.get(berry["url"])
                    detail_resp.raise_for_status()
                    detail_data = detail_resp.json()

                    berries.append({
                        "name": detail_data["name"],
                        "growth_time": detail_data["growth_time"]
                    })
                except Exception as e:
                    print(f"Error getting berry details for {berry.get('name')}: {e}")
                    return {"error": "Unexpected error occurred while fetching berry details."}

            next_url = data["next"]
        set_cache(cache_key, berries)
        return berries
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error: {e}")
        return {"error": "Unexpected error occurred while fetching data."}

