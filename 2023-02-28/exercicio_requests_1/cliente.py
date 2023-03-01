from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    cpf: str
    endereco: str
    renda: float
