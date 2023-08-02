import json
import sys
from pathlib import Path


def payload_create_booking():
    payload = {
        "firstname": "Sammy",
        "lastname": "Shaw",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-12-12"
        },
        "additionalneeds": "Dinner"
    }
    return payload


# payload is taken from json file
# data driven testing

def payload_create_booking_ddt():

    file_path = "../../src/resources/data_create_booking_ddt.json"
    print(file_path)
    with open(file_path, "r") as read_file:
        # print("Converting JSON encoded data into Python dictionary")
        data = json.load(read_file)
        for x in range(0, len(data)):
            payload = {
                "firstname": data[x]['firstname'],
                "lastname": data[x]['lastname'],
                "totalprice": data[x]['totalprice'],
                "depositpaid": data[x]['depositpaid'],
                "bookingdates": {
                    "checkin": data[x]['bookingdates']['checkin'],
                    "checkout": data[x]['bookingdates']['checkout']
                },
                "additionalneeds": data[x]['additionalneeds']
            }
            return payload


def payload_update_booking():
    update_payload = {
        "firstname": "Stone Cole",
        "lastname": "Steve Austin",
        "totalprice": 7978898,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-28",
            "checkout": "2024-10-30"
        },
        "additionalneeds": "Breakfast,Lunch,Dinner"
    }
    return update_payload


def payload_patch_booking():
    update_payload = {
        "firstname": "Neil",
        "lastname": "Armstrong (Partial Update)",
        "totalprice": 7978898,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-28",
            "checkout": "2024-10-30"
        },
        "additionalneeds": "Breakfast,Lunch,Dinner"
    }
    return update_payload


def payload_create_token():
    payload_token = {
        "username": "admin",
        "password": "password123"
    }
    return payload_token
