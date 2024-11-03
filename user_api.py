import requests
import random
import string
from data import Links


class UserAPI:
    BASE_URL = Links.URL

    @staticmethod
    def generate_random_email():
        return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"

    @staticmethod
    def generate_random_password():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    @staticmethod
    def register_new_user(email, password, name="Test User"):
        url = f"{UserAPI.BASE_URL}/api/auth/register"
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(url, json=payload)

        if response.status_code == 403:
            raise ValueError(f"Failed to create user: {response.json()['message']}")
        response.raise_for_status()

        return response.json()

    @staticmethod
    def delete_user(token):
        url = f"{UserAPI.BASE_URL}/api/auth/user"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(url, headers=headers)

        if response.status_code not in [200, 202]:
            raise ValueError(f"Failed to delete user: {response.status_code}, {response.text}")
