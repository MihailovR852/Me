import requests

BASE_URL = "https://1bc101d1-c1b3-4f46-bc26-601fb1ccb4f1.serverhub.praktikum-services.ru"

def test_order_creation():
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metroStation": 5,
        "phone": "+79991234567",
        "rentTime": 5,
        "deliveryDate": "2025-03-10",
        "comment": "Привезите вовремя!",
        "color": ["BLACK"]
    }
    
    response = requests.post(f"{BASE_URL}/orders", json=order_data)
    assert response.status_code == 201, "Ошибка при создании заказа"
    
    track_number = response.json().get("track")
    assert track_number, "Трек-номер не получен"

    response = requests.get(f"{BASE_URL}/orders/track?t={track_number}")
    assert response.status_code == 200, "Ошибка при получении заказа"

    print(f"✅ Тест пройден! Заказ {track_number} успешно создан и найден.")

test_order_creation()