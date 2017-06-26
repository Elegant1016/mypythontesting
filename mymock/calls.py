import requests


def get_data():
    response = requests.get("http://www.google.com")
    return response.status_code
