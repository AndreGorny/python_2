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
    url="https://httpbin.org/gzip",
    params=params
)

print(response.headers)
print(response.text)
