from factory import get_session
from cliente import Cliente

session = get_session()

sql = """CREATE TABLE cliente(
    cd_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nm_cliente VARCHAR(50),
    nr_cpf VARCHAR(20),
    ds_endereco VARCHAR(100)
)"""

session.execute(sql)

a = Cliente(
    nm_cliente="Fulano",
    nr_cpf="12345",
    ds_endereco="Rua A, 10"
)

b = Cliente(
    nm_cliente="Cicrano",
    nr_cpf="32146",
    ds_endereco="Rua B, 100"
)

c = Cliente(
    nm_cliente="Beltrano",
    nr_cpf="35465",
    ds_endereco="Rua B, 27"
)

session.add(a)
session.add(b)
session.add(c)
session.commit()

results = session.query(Cliente).all()
for result in results:
    print(result)
