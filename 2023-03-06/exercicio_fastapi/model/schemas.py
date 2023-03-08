from pydantic import BaseModel


class ClienteBase(BaseModel):
    nm_cliente: str
    nr_cpf: str
    ds_endereco: str


class ClienteInsert(ClienteBase):
    pass


class ClienteSelect(ClienteBase):
    cd_cliente: int


class Cliente(ClienteBase):
    cd_clidente: int

    class Config:
        orm_mode = True
