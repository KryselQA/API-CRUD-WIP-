import requests
from . import BOOKING_URL


def delete_booking(booking_id, token):
    delete_url = f"{BOOKING_URL}/{booking_id}"

    headers = {
        "Cookie": f"token={token}",
        "Content-Type": "application/json"
    }

    response = requests.delete(delete_url, headers=headers)
    return response