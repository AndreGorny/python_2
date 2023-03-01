from dataclasses import dataclass
from datetime import date


@dataclass
class Produto:
    nm_produto: str = None
    tp_produto: str = None
    dt_validade: date = None
    lote: str = None
