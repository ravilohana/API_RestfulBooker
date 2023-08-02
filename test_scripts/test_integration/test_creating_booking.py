"""

Author: Ravi Lohana
Objective: Create and verify by POST Request
TC#1 - Verify the status code
TC#2 - verify the Body --> booking ID
TC#3 -- verify the JSON Schemas is valid

"""

import pytest

# payload
# base url
# verify

from src.constants.api_constants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import *


class Test_Integration(object):

    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)
        print(response.status_code)
        print(response.json())


