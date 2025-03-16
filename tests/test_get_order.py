import pytest
from sender_requests.api_client import create_order, get_order_by_track
from data.order_data import order_payload

def test_get_order():
    create_response = create_order(order_payload)
    track_number = create_response.json().get("track")

    response = get_order_by_track(track_number)
    
    assert response.status_code == 200, f"Ошибка: {response.text}"
    assert response.json().get("track") == track_number, "Ошибка: неверный трек-номер"