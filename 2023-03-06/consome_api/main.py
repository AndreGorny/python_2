import requests


def post_cliente():

    payload = {
        "nm_cliente": "Jacaré",
        "nr_cpf": "12345678951",
        "ds_endereco": "Rua É o Tchan",
    }

    response = requests.post(url="http://127.0.0.1:8000/cliente", json=payload)
    print(response)
    print(response.text)


post_cliente()
