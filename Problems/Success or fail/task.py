import requests


def check_success(url):
    if requests.get(url).ok:
        return 'Success'
    return 'Fail'
