from sqlalchemy import create_engine

user = "root"
password = "361617"
host = "127.0.0.1"
port = 3306
db = "aula"


def server_connection():
    return create_engine(
        url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    )


if __name__ == '__main__':
    try:
        engine = server_connection()
        print(f"Conetado com sucesso no servidor {host}, database {db}")
    except Exception:
        print("Não foi possível conectar no servidor.")
