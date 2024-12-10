import requests
from config import BASE_URL


class UserMethods:

    @staticmethod
    def register_user(user_data):
        response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
        return response.status_code, response.json()

    @staticmethod
    def login_user(user_data):
        response = requests.post(f"{BASE_URL}/api/auth/login", json=user_data)
        return response.status_code, response.json()

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(f"{BASE_URL}/api/auth/user", headers=headers)
        return response.status_code, response.json()

    @staticmethod
    def update_user(access_token, updated_data):
        headers = {"Authorization": access_token}
        response = requests.patch(
            f"{BASE_URL}/api/auth/user", json=updated_data, headers=headers
        )
        print(f"{response.text}")
        return response.status_code, response.json()

    @staticmethod
    def get_user_data(token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{BASE_URL}/users/{user_id}",
            headers=headers
        )
        return response.json()
