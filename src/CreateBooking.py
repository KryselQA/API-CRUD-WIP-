import requests
def create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking"


    person = {
        "firstname" : "Denis",
        "lastname" : "Erofeev",
        "totalprice" : 1234,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-11-12",
            "checkout" : "2026-11-18"
        },
        "additionalneeds" : "Breakfast"
    }

    response = requests.post(booking_url, json=person)
    booking_id = (response.json())["bookingid"]

    return booking_id, response.status_code, booking_url