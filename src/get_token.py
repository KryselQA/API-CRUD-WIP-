import requests
from . import BASE_URL


def get_token():
    url = f"{BASE_URL}/auth"

    data = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(url, json=data)
    return response