from factory import get_session
from cliente import Cliente

session = get_session()

sql = """CREATE TABLE cliente(
    cd_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nm_cliente VARCHAR(50),
    nr_cpf VARCHAR(20),
    ds_endereco VARCHAR(100),
    vl_renda DECIMAL(10,2)
)"""

session.execute(sql)

c = Cliente(
    nm_cliente="Fulano",
    nr_cpf="12",
    ds_endereco="Rua Sei Lá, 12",
    vl_renda=1350
)
d = Cliente(
    nm_cliente="Beltrano",
    nr_cpf="17",
    ds_endereco="Rua Sei Lá, 27",
    vl_renda=1435
)
e = Cliente(
    nm_cliente="Cicrano",
    nr_cpf="15",
    ds_endereco="Rua Delta, 111",
    vl_renda=1650
)
f = Cliente(
    nm_cliente="Batman",
    nr_cpf="10",
    ds_endereco="Rua Sei Lá, 12",
    vl_renda=1100
)

session.add(c)
session.add(d)
session.add(e)
session.add(f)

session.commit()

session.close()
