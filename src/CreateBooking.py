import requests
import pprint
def createBooking():
    url = "https://restful-booker.herokuapp.com/booking"

    person = {
        "firstname" : "Denis",
        "lastname" : "Erofeev",
        "totalprice" : 1234,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-11-12",
            "checkout" : "2019-11-18"
        },
        "additionalneeds" : "Breakfast"
    }

    response = requests.post(url, json=person)

    print(response.json())
    print(response.status_code)