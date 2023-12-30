import requests

def get(URL: str):
    request = requests.get(URL)

    if request.status_code != 200:
        raise Exception(f'Status code returned {request.status_code}!')

    return request.json()


def post(URL: str, content: dict):
    request = requests.post(URL, json = content)

    if request.status_code != 200:
        raise Exception(f'Status code returned {request.status_code}!')

    return request.json()
