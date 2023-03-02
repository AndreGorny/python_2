from sqlalchemy import create_engine

engine = create_engine(url="mysql+pymysql://root:361617@127.0.0.1:3306/aula")

conn = engine.connect()

conn.close()
