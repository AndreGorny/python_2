from datetime import date
from decimal import Decimal

class Pessoa:

    def __init__(self, nome: str, cpf: int,
                 nascimento: date, sexo: str,
                 fone: str, endereco: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.sexo = sexo
        self.fone = fone
        self.endereco = endereco
    

class Cliente(Pessoa):

    def __init__(self, nome: str, cpf: int,
                 nascimento: date, sexo: str,
                 fone: str, endereco: str) -> None:
        super().__init__(nome, cpf, nascimento, sexo)


class Funcionario(Pessoa):

    def __init__(self, nome: str, cpf: int,
                 nascimento: date, sexo: str,
                 fone: str, endereco: str,
                 salario: Decimal, cargo: str) -> None:
        super().__init__(nome, cpf, nascimento, sexo)
        self.salario = salario
        self.cargo = cargo

class Produto:

    def __init__(self, cod: int, marca: str,
                 nome: str, tipo: str,
                 valor: Decimal) -> None:
        self.cod = cod
        self.marca = marca
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
