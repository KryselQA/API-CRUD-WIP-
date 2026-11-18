import requests
from CreateBooking import create_booking
from GetToken import get_token

booking_id, status_code, booking_url = create_booking()
auth_status_code, auth_response, token = get_token()

def update_booking():
    booking_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

    headers = {
        "Cookie": f"token={token}",
        "Content-Type": "application/json"
    }

    update_booking_info = {
        "firstname": "Alisa",
        "lastname": "Kadilenko",
    }

    response = requests.patch(booking_url, json=update_booking_info, headers=headers)
    return response.status_code