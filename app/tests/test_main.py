import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    Base.metadata.drop_all(bind=engine)
    db.close()

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_create_category(client):
    payload = {"name": "Electronics", "description": "Devices and gadgets"}
    response = client.post("/api/categories/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Electronics"

def test_get_categories(client):
    response = client.get("/api/categories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)