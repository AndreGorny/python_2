from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = "aula.db"


def engine_db():
    engine = create_engine("sqlite:///aula.db")
    return engine


def session_db():
    engine = engine_db()
    Session = sessionmaker(bind=engine)
    return Session()
