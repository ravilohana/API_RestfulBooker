import json

import requests

from src.constants.api_constants import url_create_booking
from src.helpers.api_wrapper import create_booking_ddt
from src.helpers.common_verification import verify_http_code, verify_key
from src.helpers.utils import common_headers
import pprint


class Test_Create_Booking_DDT(object):

    # restful-booker --- Create booking (POST)
    # Data Driven testing using JSON file
    #  path : src/resources/data_create_booking_ddt.json
    # "../../src/resources/data_create_booking_ddt.json"
    def test_create_booking_ddt(self):
        with open("../../src/resources/data_create_booking_ddt.json", 'r') as create_booking_payload:
            data = json.load(create_booking_payload)
            print("Total number of objects: ", len(data))
            for i in range(len(data)):
                data_new = json.dumps(data[i])
                response = requests.post(url_create_booking(), headers=common_headers(), data=data_new)
                print("Item#", i, "added", " -> ", data_new)
                verify_http_code(response, 200)
                booking_id = response.json()["bookingid"]
                verify_key(booking_id)
                pprint.pprint(response.status_code)
                pprint.pprint(response.json())

