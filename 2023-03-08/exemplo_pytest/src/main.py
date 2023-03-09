import requests


def main():

    response = requests.get("https://httpbin.org/status/200")
    return {
        "status_code": response.status_code
    }


def batman():
    pass
