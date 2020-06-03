import requests


def generate_URL(path, arguments):
    return path + arguments


def get_response(url):
    response = requests.get(url)
    if error_handle(response):
        return long_lat(response)
    else:
        return f'Error occurred when retrieving postcode (error message {response.status_code})'


def error_handle(response):
    if str(response.status_code).startswith('2') or str(response.status_code).startswith('3'):
        return True
    else:
        return False


def long_lat(response):
    response_dict = response.json()['result']
    long = response_dict['longitude']
    lat = response_dict['latitude']
    pm_con = response_dict['parliamentary_constituency']
    nuts = response_dict['nuts']

    return f'Your Longitude is {long}, your latitude is {lat}, your parliamentary constituency is {pm_con} and your NUTS value is: {nuts}'

