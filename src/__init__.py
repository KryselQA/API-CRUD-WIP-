BASE_URL = "https://restful-booker.herokuapp.com"
BOOKING_URL = f"{BASE_URL}/booking"

from .create_booking import create_booking
from .delete_booking import delete_booking
from .get_token import get_token
from .get_info_about_booking import get_info_about_booking
from .update_booking_info import update_booking