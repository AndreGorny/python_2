from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Departamento:
    nome: str
    setor: str


@dataclass
class Funcionario:
    nome: str
    cargo: str
    salario: Decimal
    dpto: Departamento  # Composição. Um funcionário TEM
                        # um departamento


@dataclass
class Cargo:
    nome: str
    faixa_salario: str
    nivel: str


@dataclass
class PlanoCarreira:
    cargo: Cargo
    prox_cargo: str
