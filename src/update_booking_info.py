import requests
from . import BOOKING_URL


def update_booking(booking_id,token):
    booking_url = f"{BOOKING_URL}/{booking_id}"

    headers = {
        "Cookie": f"token={token}",
        "Content-Type": "application/json"
    }

    update_booking_info = {
        "firstname": "Alisa",
        "lastname": "Kadilenko",
    }

    response = requests.patch(booking_url, json=update_booking_info, headers=headers)
    return response