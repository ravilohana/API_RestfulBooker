# HTTP status code
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected HTTP Status: " + expected_data


# Any Key, should not be null, of empty

def verify_key(key):
    assert key != 0, "key is non empty: " + key
    assert key > 0, "key should be greater than zero : " + key
