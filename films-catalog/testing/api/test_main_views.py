from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_view() -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["docs"] == "http://testserver/docs", response_data
