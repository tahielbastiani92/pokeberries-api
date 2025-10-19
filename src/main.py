from fastapi import FastAPI, Response
from src.services.pokeapi import get_all_berries_data
from src.utils.statistics import calculate_statistics
from typing import List, Dict

app = FastAPI(title="Pokeberries API")


@app.get("/")
def intial():
    return {"message": "Working.. Pokeberries statistics is coming.."}

@app.get("/allBerryStats", response_model=dict)
def all_berry_statstics(response: Response):
    """
    Returns berries' statistics
    """
    try:
        berries_data = get_all_berries_data()
        stats = calculate_statistics(berries_data)
        response.headers["Content-Type"] = "application/json"
        return stats
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Unexpected error occurred."}
