from factory import session_db

session = session_db()

query = ("""CREATE TABLE cliente(
                   cd_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                   nm_cliente VARCHAR(50),
                   nr_cpf INTEGER,
                   dt_nasc DATE
)""")
# session.execute(query)

# Transaction

cliente = ("INSERT INTO cliente (nm_cliente, nr_cpf, dt_nasc)"
           "VALUES ('Cicrano', '1235', '1992-14-21')")
session.execute(cliente)
session.commit()
