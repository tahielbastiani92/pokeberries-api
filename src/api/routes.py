import json
from fastapi import APIRouter, Response
from src.services.pokeapi import get_all_berries_data
from src.schemas.berries_stats import BerryStatsResponse
from src.utils.statistics import calculate_statistics

router = APIRouter(prefix="/api/v1")


@router.get("/")
def intial():
    return {"message": "Working.. Pokeberries statistics is coming.."}


@router.get("/allBerryStats", response_model=BerryStatsResponse)
def all_berry_statstics(response: Response):
    """
    Returns berries' statistics
    """
    try:
        berries_data = get_all_berries_data()
        stats = calculate_statistics(berries_data)
        return Response(content=json.dumps(stats, indent=2), media_type="application/json")
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Unexpected error occurred."}