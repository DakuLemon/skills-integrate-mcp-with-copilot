import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app, activities


def setup_function():
    activities["GitHub Skills"]["participants"] = []


def test_github_skills_activity_is_available():
    client = TestClient(app)

    response = client.get("/activities")

    assert response.status_code == 200
    assert "GitHub Skills" in response.json()


def test_sign_up_for_github_skills_activity():
    client = TestClient(app)

    response = client.post(
        "/activities/GitHub%20Skills/signup?email=student@mergington.edu"
    )

    assert response.status_code == 200
    assert "student@mergington.edu" in activities["GitHub Skills"]["participants"]
