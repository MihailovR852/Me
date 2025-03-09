import requests

BASE_URL = "https://1bc101d1-c1b3-4f46-bc26-601fb1ccb4f1.serverhub.praktikum-services.ru"


response = requests.get(f"{BASE_URL}/couriers")
couriers = response.json()


response = requests.get(f"{BASE_URL}/orders")
orders = response.json()


in_delivery_orders = [order for order in orders if order.get("inDelivery")]


courier_orders = {}

for order in in_delivery_orders:
    courier_id = order.get("courierId")
    if courier_id:
        courier_orders[courier_id] = courier_orders.get(courier_id, 0) + 1


for courier in couriers:
    courier_id = courier["id"]
    login = courier["login"]
    orders_count = courier_orders.get(courier_id, 0)
    print(f"Курьер {login}: {orders_count} заказов в доставке")