
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from dataclasses import dataclass

Base = declarative_base()


class ClienteTable(Base):
    __tablename__ = "cliente"

    cd_cliente = Column("cd_cliente", Integer, primary_key=True,
                        autoincrement=True)
    nm_cliente = Column("nm_cliente", String(50), nullable=False)
    nr_cpf = Column("nr_cpf", String(20))
    ds_endereco = Column("ds_endereco", String(100))
    vl_renda = Column("vl_renda", Float)


@dataclass
class Cliente(ClienteTable):
    cd_cliente: int
    nm_cliente: str
    nr_cpf: str
    ds_endereco: str
    vl_renda: float
