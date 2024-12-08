import requests
from config import BASE_URL


class OrderMethods:
    @staticmethod
    def create_order(ingredients, access_token=None):
        payload = {"ingredients": ingredients}
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        response = requests.post(f"{BASE_URL}/api/orders", headers=headers, json=payload)
        return response.status_code, response.json()

    @staticmethod
    def get_orders(access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        response = requests.get(f"{BASE_URL}/api/orders", headers=headers)
        return response.status_code, response.json()