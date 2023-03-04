from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    engine = create_engine("sqlite:///ex_sqlalchemy_1.db")

    Session = sessionmaker(bind=engine)
    session = Session()
    return session
