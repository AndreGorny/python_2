from fastapi import FastAPI

app = FastAPI()


@app.get("/clientes")
def clientes() -> list:
    """Retorna uma lista com todos os clientes"""

    cliente = [
        {
            "nome": "Fulano",
            "cpf": 12345,
            "dt_nasc": "1990-02-14"
        }
    ]

    return cliente


@app.get("/cliente/{cd_cliente}")
def cliente(cd_cliente) -> dict:

    cliente = {
        "nome": "Fulano",
        "cpf": 12345,
        "dt_nasc": "1990-02-14"
        }

    return cliente

# get -> "/cliente/{cd_cliente}/endereco" -> busca o endereço do cliente
# post -> "/cliente/{cd_cliente}/endereco" -> cadastra o endereço do cliente
