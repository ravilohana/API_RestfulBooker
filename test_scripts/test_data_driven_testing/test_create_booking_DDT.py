
from src.constants.api_constants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verification import verify_http_code, verify_key
from src.helpers.payload_manager import payload_create_booking, payload_create_booking_ddt
from src.helpers.utils import common_headers
import pprint


class Test_Create_Booking_DDT(object):

    # restful-booker --- Create booking (POST)
    # Data Driven testing using JSON file
    #  path : src/resources/data_create_booking_ddt.json
    
    def test_create_booking_ddt(self):
        response = post_request(url=url_create_booking(),
                                headers=common_headers(),
                                auth=None,
                                payload=payload_create_booking_ddt(),
                                in_json=False)
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        pprint.pprint(response.status_code)
        pprint.pprint(response.json())
        print(response.status_code)
        print(response.json())
