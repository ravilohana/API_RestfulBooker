# Help you to read the json files and provide you the json data
import json


def get_payload_auth():
    # Read from the auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.load(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json",
    }

    return headers


# def headers_put_patch_delete(token):
#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Cookie": "token=" + str(token)
#     }
#     return headers

def headers_put_patch_delete(token):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token=" + str(token)
    }
    return headers


def headers_put_patch_delete_req():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return headers
