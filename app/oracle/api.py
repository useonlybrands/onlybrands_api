import requests

session = requests.Session()


def check_ig_request(url: str):
    response = session.get(url)
    return response.status_code
