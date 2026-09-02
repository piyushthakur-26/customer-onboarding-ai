from uuid import uuid4

from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_create_customer():
    email = f"test_{uuid4()}@example.com"

    response = client.post(
        "/customers/",
        json={
            "full_name": "Test Customer",
            "email": email,
            "phone": "9999999999",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["full_name"] == "Test Customer"
    assert data["email"] == email
    assert data["phone"] == "9999999999"
    assert "id" in data
    assert "created_at" in data


def test_create_customer_invalid_email():
    response = client.post(
        "/customers/",
        json={
            "full_name": "Invalid Email",
            "email": "not-an-email",
            "phone": "9999999999",
        },
    )

    assert response.status_code == 422


def test_get_customer_not_found():
    response = client.get("/customers/99999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found."


def test_create_customer_duplicate_email():
    email = f"duplicate_{uuid4()}@example.com"

    first_response = client.post(
        "/customers/",
        json={
            "full_name": "Duplicate Test",
            "email": email,
            "phone": "9999999999",
        },
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/customers/",
        json={
            "full_name": "Duplicate Test Again",
            "email": email,
            "phone": "8888888888",
        },
    )

    assert second_response.status_code == 409

    assert second_response.json()["detail"] == (
        "A customer with this email already exists."
    )