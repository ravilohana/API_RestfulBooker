import requests.auth

from src.constants.api_constants import url_create_booking, url_get_update_delete_booking
from src.helpers.api_wrapper import post_request, get_request, update_data, delete_data
from src.helpers.common_verification import verify_http_code, verify_key
from src.helpers.payload_manager import payload_create_booking, payload_update_booking, payload_patch_booking
from src.helpers.utils import common_headers, headers_put_patch_delete_req


class TestIntegrationTC1(object):

    def test_verify_creating_booking_updating_deleting(self):
        # create the booking and get the firstname and lastname keys value
        # verify the status code 200
        # verify the booking id not equal to zero and greater than 0

        post_response = post_request(url=url_create_booking(), headers=common_headers(), auth=None,
                                     payload=payload_create_booking(), in_json=False)
        verify_http_code(post_response, 200)
        booking_id = post_response.json()["bookingid"]
        post_request_firstname_key = post_response.json()['booking']['firstname']
        post_request_lastname_key = post_response.json()['booking']['lastname']
        print(post_request_firstname_key)
        print(post_request_lastname_key)
        verify_key(booking_id)
        print(booking_id)
        # print(payload_create_booking().get('firstname'))
        # print(payload_create_booking().get('lastname'))

        # get the booking record by booking
        # verify the firstname key with post request
        # verify the lastname key with post request
        # verify the status code 200

        get_response = get_request(url=url_get_update_delete_booking(booking_id), auth=None, headers=common_headers(),
                                   in_json=False)
        verify_http_code(post_response, 200)
        print(get_response.json())
        print(get_response.json()["firstname"])
        print(get_response.json()["lastname"])
        assert post_request_firstname_key == get_response.json()["firstname"]
        assert post_request_lastname_key == get_response.json()["lastname"]

        print("Code Working.................")

        # update booking
        # Here I am passing username and password for bearer token for authorization
        update_response = update_data(url=url_get_update_delete_booking(booking_id),
                                      headers=headers_put_patch_delete_req(),
                                      auth=('admin', 'password123'),
                                      # auth={'Authorization': 'Basic '+token_val},
                                      payload=payload_update_booking(), in_json=False)

        verify_http_code(update_response, 200)
        update_response_firstname_key = update_response.json()['firstname']
        update_response_lastname_key = update_response.json()['lastname']
        print("********************************************")
        print("update response payload")
        print(update_response.json()['firstname'])
        print(update_response.json()['lastname'])
        print("********************************************")
        print("Update request payload")
        print(payload_update_booking().get('firstname'))
        print(payload_update_booking().get('lastname'))
        assert update_response_firstname_key == "Stone Cole"
        assert update_response_lastname_key == "Steve Austin"

        # patch booking
        # Here I am passing username and password for bearer token for authorization
        patch_response = update_data(url=url_get_update_delete_booking(booking_id),
                                     headers=headers_put_patch_delete_req(),
                                     auth=('admin', 'password123'),
                                     payload=payload_patch_booking(), in_json=False)

        verify_http_code(update_response, 200)
        patch_response_firstname_key = patch_response.json()['firstname']
        patch_response_lastname_key = patch_response.json()['lastname']
        print("********************************************")
        print("update response payload")
        print(patch_response.json()['firstname'])
        print(patch_response.json()['lastname'])
        print("********************************************")
        print("Update request payload")
        print(payload_patch_booking().get('firstname'))
        print(payload_patch_booking().get('lastname'))
        assert patch_response_firstname_key == "Neil"
        assert patch_response_lastname_key == "Armstrong (Partial Update)"

        # Delete Request
        # # Here I am passing username and password for bearer token for authorization
        delete_response = delete_data(url=url_get_update_delete_booking(booking_id),
                                      headers=headers_put_patch_delete_req(),
                                      auth=('admin', 'password123'),
                                      in_json=False)
        # print(headers_put_patch_delete(token_val))

        verify_http_code(delete_response, 201)
        delete_response = delete_response.text
        assert delete_response == "Created"

        print("*********** ALl Http methods Done ! -----> Create token ---> POST -> GET ---> PUT --> DELETE")
