from fastapi import FastAPI
from factory import get_session
from model.schemas import Cliente, PontoBase, ResponseBase
from model.models import Pontuacao
app = FastAPI()

session = get_session()


@app.get("/clientes")
def clientes() -> list:
    """Retorna uma lista com todos os clientes"""

    response = session.query(Cliente).all()

    return response


@app.get("/cliente/{cd_cliente}")
def cliente(cd_cliente):

    response = session.query(Cliente).filter_by(cd_cliente=cd_cliente)
    return list(response)


@app.post("/cliente/")
def test_cliente(cliente: Cliente):
    print(cliente)

    c = Cliente(
        nm_cliente=cliente.nm_cliente,
        nr_cpf=cliente.nr_cpf,
        ds_endereco=cliente.ds_endereco
    )

    session.add(c)
    session.commit()

    return {
        "status": "Sucesso",
        "mensagem": "Cliente cadastrado com sucesso!"
    }


@app.post("/pontos/", response_model=ResponseBase)
def cadastra_pontos(pontos: PontoBase):

    p = Pontuacao(
        cd_cliente=pontos.cd_cliente,
        vl_pontos=pontos.vl_pontos
    )

    session.add(p)
    session.commit()

    return ResponseBase(
        status="Sucesso",
        mensagem="Pontuacao cadastrada com sucesso!"
    )


@app.get("/pontos/cliente/{cd_cliente}")
def consulta_pontos(cd_cliente: int):

    response = session.query(Cliente).filter_by(cd_cliente=cd_cliente)
    return list(response)
