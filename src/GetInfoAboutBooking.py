import requests
from CreateBooking import create_booking

booking_id, status_code, booking_url = create_booking()

def get_info_about_booking():
    url_for_find_book = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    response_by_id = requests.get(url_for_find_book)
    return response_by_id.status_code