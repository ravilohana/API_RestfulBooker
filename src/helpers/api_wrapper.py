import json

import requests

from src.constants.api_constants import url_create_token, url_create_booking
from src.helpers.payload_manager import payload_create_token
from src.helpers.utils import common_headers


def get_request(url, auth, headers, in_json):
    get_response_data = requests.get(url=url, headers=headers, auth=auth)
    if in_json is True:
        return get_response_data.json()
    return get_response_data


def post_request(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


# def post_request_create_token(url, auth, headers, payload, in_json):
#     post_response_create_token = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
#     if in_json is True:
#         return post_response_create_token.json()
#     return post_response_create_token

def update_data(url, auth, headers, payload, in_json):
    update_response_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return update_response_data.json()
    return update_response_data


def patch_data(url, auth, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_data(url, auth, headers, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data


def create_token_response():
    create_token_res = post_request(url=url_create_token(), headers=common_headers(), auth=None,
                                    payload=payload_create_token(), in_json=False)
    token_val = create_token_res.json()["token"]
    return token_val

# Not working
# def create_booking_ddt(json_file_path):
#     with open(json_file_path, 'r') as create_booking_payload:
#         data = json.load(create_booking_payload)
#         print("Total number of objects: ", len(data))
#         for i in range(len(data)):
#             data_new = json.dumps(data[i])
#             response = requests.post(url_create_booking(), headers=common_headers(), data=data_new)
#             print("Item#", i, "added", " -> ", data_new)
#             return response
