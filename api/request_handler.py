import requests

# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
verify_ssl = True


# general GET request
# - assumes GET requests will not have a body
def get(base_url, request_root, request_path, request_name, headers):
    return requests.get(
        f'{base_url}{request_root}{request_path}',
        headers = headers,
        verify = verify_ssl
    )

# general POST request
def post(base_url, request_root, request_path, request_name, headers, payload):
    return requests.post(
        f'{base_url}{request_root}{request_path}',
        headers = headers,
        json = payload,
        verify = verify_ssl
    )

# general PUT request
def put(base_url, request_root, request_path, request_name, headers, payload):
    return requests.put(
        f'{base_url}{request_root}{request_path}',
        headers = headers,
        json = payload,
        verify = verify_ssl
    )

# general DELETE request
# - assumes DELETE requests will not have a body
def delete(base_url, request_root, request_path, request_name, headers):
    return requests.delete(
        f'{base_url}{request_root}{request_path}',
        headers = headers,
        verify = verify_ssl
    )