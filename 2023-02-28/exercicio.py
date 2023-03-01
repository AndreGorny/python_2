from dataclasses import dataclass
import requests


@dataclass
class Cliente:
    nome: str
    cpf: str
    endereco: str
    telefone: str


params = Cliente(
    "Andre",
    "1234",
    "Rua A, 12",
    "999550022"
)

response = requests.get("https://httpbin.org/get", params=params)
