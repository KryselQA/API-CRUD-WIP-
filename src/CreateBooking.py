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

    # Я не придумал как искать по полученному id в отдельной функции пока, поэтому оставил в одной
    url_for_find_book = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    response_by_id = requests.get(url_for_find_book)

    return booking_id, response.status_code, response_by_id, booking_url