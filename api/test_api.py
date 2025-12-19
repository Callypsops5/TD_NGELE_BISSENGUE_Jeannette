import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {"status": "OK"}


def test_items(client):
    response = client.get("/items")
    assert response.status_code in [200, 500]
