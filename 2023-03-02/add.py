from factory import session_db

session = session_db


cliente = ("INSERT INTO cliente (nm_cliente, dt_nasc)"
           "VALUES ('Fulano', '1990-01-01')")
session.execute()
session.commit
