# perform API testing
from config.settings import settings
import requests
import pytest

@pytest.mark.parametrize("mode", [False, True])
def test_simulate_purchase(mode):
    payload = {
            "email": settings.AMAZON_EMAIL,
            "password": settings.AMAZON_PASSWORD,
            "headless": mode
        }

    response = requests.post(settings.API_URL, json=payload)
    
    # Verify status response code
    assert response.status_code == 200, f"Error HTTP: {response.status_code}"
    
    # Verify checkout
    data = response.json()
    assert data["status"] == "success"
    assert "Finalizar la compra de manera segura" in data["details"]