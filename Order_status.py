response = requests.get(f"{BASE_URL}/orders")
orders = response.json()


for order in orders:
    track = order["track"]
    if order.get("finished"):
        status = 2
    elif order.get("cancelled"):
        status = -1
    elif order.get("inDelivery"):
        status = 1
    else:
        status = 0
    
    print(f"Трек {track}: статус {status}")