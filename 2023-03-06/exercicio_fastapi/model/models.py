from sqlalchemy import Column, Integer, String
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


class Pontuacao(Base):
    __tablename__ = "pontuacao"

    cd_pontuacao = Column("cd_pontuacao", int, primary_key=True)
    cd_cliente = Column("cd_cliente", int)
    vl_pontos = Column("vl_pontos", float)


@dataclass
class Cliente(ClienteTable):
    cd_cliente: int
    nm_cliente: str
    nr_cpf: str
    ds_endereco: str


def pontuar(cliente, valor):
    pass


def pagamento():

    # O pagamento aconteceu

    cliente = {"cd_cliente": 1}
    valor = 1200
    pontuar(cliente, valor)
