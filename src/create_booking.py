import requests
from faker import Faker
from datetime import timedelta
from . import BOOKING_URL

fake = Faker()


def create_booking(first_name):
    booking_url = BOOKING_URL

    checkin = fake.date_between(
        start_date="-1y", # минус год от текущего дня
        end_date="+1y" # плюс год от текущего дня
    )

    checkout = fake.date_between(
        start_date=checkin + timedelta(days=1),
        end_date=checkin + timedelta(days=30)
    )

    person = {
        "firstname" : first_name,
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(100, 5000),
        "depositpaid" : fake.boolean(),
        "bookingdates" : {
            "checkin" : checkin.isoformat(), # Пришлось так сделать, т.к. JSON не умеет напрямую работать с объектами даты
            "checkout" : checkout.isoformat()
        },
        "additionalneeds": fake.random_element(elements=(
            "Breakfast",
            "Late Checkout",
            "Extra pillows",
            "Extra towels",
            "Airport transfer",
            "Sea view",
            "Non-smoking room"
        ))
    }

    response = requests.post(booking_url, json=person)

    return response