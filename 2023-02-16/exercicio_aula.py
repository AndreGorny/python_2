# Exercicio:
""" Empresa tem:
Funcionários
    Cargo
    salario
    nome
Departamentos
    nome
    setor
    funcionarios
Plano de carreira
    cargo
    proximo cargo
    faixa salarial
    nivel

    Utilizar herança e/ou composição

"""

from decimal import Decimal


class Funcionario:

    def __init__(self, cargo: str, salario: Decimal, nome: str) -> None:
        self.cargo = cargo
        self.salario = salario
        self.nome = nome


class Departamento:

    def __init__(self, nome: str, setor: str, funcionarios: str) -> None:
        self.nome = nome
        self.setor = setor
        self.funcionarios = funcionarios


class PlanoCarreira:

    def __init__(self, cargo: str, prox_cargo: str,
                 salario: Decimal, nivel: str) -> None:
        self.cargo = cargo
        self.prox_cargo = prox_cargo
        self.salario = salario
        self.nivel = nivel
