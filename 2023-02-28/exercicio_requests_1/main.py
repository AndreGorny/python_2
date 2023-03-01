from cliente import Cliente
import requests

c = Cliente(
    nome="Fulano",
    cpf="12",
    endereco="Rua Seila, 12",
    renda=1200
)

params = c.__dict__

response = requests.get(
    url="https://httpbin.org/get",
    params=params
)

if response.status_code == 200:
    payload = response.json()

    print("HTTP Status ->", response.status_code)
    print("Parâmetros ->", payload["args"])
    print("IP ->", payload["origin"])
    print("URL ->", payload["url"])
