from fastapi import FastAPI
from factory import get_session
from cliente import Cliente

app = FastAPI()

session = get_session()


@app.get("/clientes")
def clientes() -> list:
    """Retorna uma lista com todos os clientes"""

    response = session.query(Cliente).all()

    return response


@app.get("/clientes/{cd_cliente}")
def cliente(cd_cliente: int) -> dict:

    response = session.query(Cliente).filterby(cd_cliente=cd_cliente)
    for r in response:
        return r.__dict__
