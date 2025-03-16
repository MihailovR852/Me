import requests
from configuration.config import CREATE_ORDER_URL, GET_ORDER_URL

def create_order(order_data):
    response = requests.post(CREATE_ORDER_URL, json=order_data)
    return response

def get_order_by_track(track_number):
    response = requests.get(f"{GET_ORDER_URL}{track_number}")
    return response