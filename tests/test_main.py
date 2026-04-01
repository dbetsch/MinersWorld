import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.roblox_sync import fetch_inventory_by_username

client = TestClient(app)


def test_dashboard_returns_200():
    response = client.get("/dashboard")
    assert response.status_code == 200


def test_ores_returns_200():
    response = client.get("/ores")
    assert response.status_code == 200


def test_inventory_returns_200():
    response = client.get("/inventory")
    assert response.status_code == 200


def test_imports_returns_200():
    response = client.get("/imports")
    assert response.status_code == 200


def test_settings_returns_200():
    response = client.get("/settings")
    assert response.status_code == 200


def test_roblox_sync_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        fetch_inventory_by_username("TestUser")
