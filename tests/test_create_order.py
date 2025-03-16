import pytest
from sender_requests.api_client import create_order
from data.order_data import order_payload

def test_create_order():
    response = create_order(order_payload)
    
    assert response.status_code == 201, f"Ошибка: {response.text}"
    
    track_number = response.json().get("track")
    assert track_number is not None, "Ошибка: трек-номер не получен"