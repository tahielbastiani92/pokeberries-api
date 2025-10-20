from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_all_berry_stats_endpoint():
    response = client.get("api/v1/allBerryStats")
    assert response.status_code == 200
    data = response.json()
    assert "berries_names" in data
    assert "mean_growth_time" in data
    assert isinstance(data["berries_names"], list)
