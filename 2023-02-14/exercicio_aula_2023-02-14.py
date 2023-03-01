#Cliente:
#   nome
#   cpf
#   data nascimento
#   endereco
#   renda

#Funcionario:
#   nome
#   cpf
#   data nascimento
#   endereco
#   cargo
#   salario

#metodos: validar cpf
#         verificar cpf
#         marcar ponto

from datetime import date
import decimal

class Pessoa:

    def __init__(self, nome: str,
                 cpf: int, nascimento: date,
                 endereco: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
    
    def validar_cpf(self):
        pass


class Cliente(Pessoa):

    def __init__(self, nome: str, cpf: int,
                 nascimento: date, endereco: str,
                 renda: decimal) -> None:
        super().__init__(nome, cpf, nascimento, endereco)
        self.renda = renda
    
    def verificar_cpf(self):
        pass


class Funcionario(Pessoa):

    def __init__(self, nome: str, cpf: int,
                 nascimento: date, endereco: str,
                 cargo: str, salario: decimal) -> None:
        super().__init__(nome, cpf, nascimento, endereco)
        self.cargo = cargo
        self.salario = salario

    def marca_ponto(self):
        pass

