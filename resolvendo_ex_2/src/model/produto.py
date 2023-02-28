from dataclasses import dataclass
from datetime import date


@dataclass
class Produto:
    nm_produto: str
    tp_produto: str
    dt_validade: date
    lote: str
