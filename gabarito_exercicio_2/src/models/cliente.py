from dataclasses import dataclass
from datetime import date
from typing import Any


@dataclass
class Cliente:
    nm_cliente: str = None
    nr_cpf: str = None
    dt_nascimento: date = None
    endereco: str = None

    def __setattr__(self, key: str, value: Any) -> None:
        object.__setattr__(self, key, value)