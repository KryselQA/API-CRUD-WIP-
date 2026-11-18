import requests
import pytest
from CreateBooking import create_booking
from DeleteBooking import delete_booking
from GetToken import get_token
from GetInfoAboutBooking import get_info_about_booking
from UpdateBookingInfo import update_booking

booking_id, status_code, booking_url = create_booking()

def test_three():
    get_token()
    assert status_code == 200

    create_booking()
    assert status_code == 200

    get_info_about_booking()
    assert status_code == 200

    update_booking()
    assert status_code == 200

    delete_booking()
    assert status_code == 200