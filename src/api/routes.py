import io
import base64
import json
from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates
from matplotlib import pyplot as plt
from src.services.pokeapi import get_all_berries_data
from src.schemas.berries_stats import BerryStatsResponse
from src.utils.statistics import calculate_statistics


router = APIRouter(prefix="/api/v1")
template = Jinja2Templates(directory="src/templates")


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


@router.get("/allBerryStats/view")
def all_berry_statstics_view(request: Request):
    """
    Berries' statistics graphics and tables
    """
    try:
        berries_data = get_all_berries_data()
        stats = calculate_statistics(berries_data)
        try:

            x = list(map(int, stats["frequency_growth_time"].keys()))
            y = list(stats["frequency_growth_time"].values())

            # Histogram
            plt.figure(figsize=(6, 4))
            plt.bar(x, y, color="skyblue", edgecolor="black")
            plt.title("Berry Growth Time Distribution")
            plt.xlabel("Growth Time")
            plt.ylabel("Frequency")
            plt.grid(axis="y", linestyle="--", alpha=0.7)
            buffer = io.BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            histogram = base64.b64encode(buffer.getvalue()).decode("utf-8")
            plt.close()

            # Pie
            plt.figure(figsize=(6, 4))
            plt.pie(
                y,
                labels=x,
                autopct="%1.1f%%",
                startangle=90,
                colors=plt.cm.Paired.colors,
            )
            plt.title("Growth Time Proportion")
            plt.tight_layout()
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            pie = base64.b64encode(buffer.getvalue()).decode("utf-8")
            plt.close()
        except Exception as e:
            print(f"Error: {e}")
            return {"error": "Error occurred making graphics."}
        return template.TemplateResponse("berries.html", {"request": request, "berries": stats, "histogram": histogram, "pie": pie})
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Unexpected error occurred."}
