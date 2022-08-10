from urllib import response
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_only_positive_numbers():
    response = client.post(
        "/utilities/atoi",
        json={"input_str": "42"}
    )
    assert response.status_code == 200
    assert response.json()["data"]["result"] == "42"


def test_only_negative_numbers():
    response = client.post(
        "/utilities/atoi",
        json={"input_str": "-42"}
    )
    assert response.status_code == 200
    assert response.json()["data"]["result"] == "-42"


def test_whitespace():
    response = client.post(
        "/utilities/atoi",
        json={"input_str": " -42"}
    )
    assert response.status_code == 200
    assert response.json()["data"]["result"] == "-42"


def test_with_numbers_and_characters():
    response = client.post(
        "/utilities/atoi",
        json={"input_str": "4193 with words"}
    )
    assert response.status_code == 200
    assert response.json()["data"]["result"] == "4193"


def test_with_characters_and_numbers():
    response = client.post(
        "/utilities/atoi",
        json={"input_str": "words with 41"}
    )
    assert response.status_code == 200
    assert response.json()["data"]["result"] == "0"
