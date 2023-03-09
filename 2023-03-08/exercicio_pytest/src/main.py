import requests

params = {"Nome": "Andre",
          "Endereço": "Rua A, 32"}


def main():
    response = requests.get(url="https://httpbin.org/get", params=params)

    if response.status_code == 200:
        payload = response.json()

        return {
            "status_code": response.status_code,
            "args": payload["args"]
        }


print(main())
