import src
from faker import Faker
fake = Faker()


# def test_get_token():
#     response = src.get_token()
#
#     assert response.status_code == 200
#
#     token = response.json()["token"]
#     assert token is not None
#
#
# def test_create_booking():
#     response = src.create_booking()
#
#     assert response.status_code == 200
#
#     booking_id = response.json()["bookingid"]
#     assert booking_id is not None
#
#
# def test_get_info_booking():
#     response = src.get_info_about_booking(booking_id)
#
#     assert response.status_code == 200
#
#
# def test_update_booking():
#     booking_response = src.create_booking()
#     booking_id = booking_response.json()["bookingid"]
#
#     token_response = src.get_token()
#     token = token_response.json()["token"]
#
#     response = src.update_booking(booking_id, token)
#
#     assert response.status_code == 200
#
#
# def test_delete_booking():
#     booking_response = src.create_booking()
#     booking_id = booking_response.json()["bookingid"]
#
#     token_response = src.get_token()
#     token = token_response.json()["token"]
#
#     response = src.delete_booking(booking_id, token)
#
#     assert response.status_code == 201


def test_crud_full_cycle():

    get_token = src.get_token()
    token = get_token.json()["token"]
    assert get_token.status_code == 200

    first_name = fake.first_name()

    create_book = src.create_booking(first_name)
    booking_id = create_book.json()["bookingid"]
    assert first_name == create_book.json()["booking"]["firstname"]
    assert create_book.status_code == 200

    get_info = src.get_info_about_booking(booking_id)
    assert get_info.status_code == 200

    update_booking = src.update_booking(booking_id, token)
    assert update_booking.status_code == 200

    delete_booking = src.delete_booking(booking_id, token)
    assert delete_booking.status_code == 201
    assert delete_booking.url.endswith(f"/booking/{booking_id}")

    check_after_delete = src.get_info_about_booking(booking_id)
    assert check_after_delete.status_code == 404