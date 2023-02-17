from dataclasses import dataclass


@dataclass
class Endereco:
    logradouro: str
    cep: str


@dataclass
class Fone:
    pass


@dataclass
class Cliente:
    nome: str
    cpf: str
    endereco: Endereco
    fone: Fone
