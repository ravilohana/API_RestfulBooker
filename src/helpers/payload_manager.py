
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
