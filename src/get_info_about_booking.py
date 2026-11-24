import requests
from . import BOOKING_URL


def get_info_about_booking(booking_id):
    url = f"{BOOKING_URL}/{booking_id}"
    response = requests.get(url)
    return response