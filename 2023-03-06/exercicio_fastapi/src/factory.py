from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = "root"
password = "361617"
host = "127.0.0.1"
port = 3306
db = "ex_fastapi"


def get_engine():
    return create_engine(
        url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    )


def get_session():
    engine = get_engine()

    Session = sessionmaker(bind=engine)
    session = Session()
    return session
