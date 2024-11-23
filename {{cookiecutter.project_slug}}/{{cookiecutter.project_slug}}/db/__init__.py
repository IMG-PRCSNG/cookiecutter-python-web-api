from sqlmodel import SQLModel, create_engine
from .models import Dummy


def create_db_and_tables(db_url: str):
    engine = create_engine(db_url)
    SQLModel.metadata.create_all(engine)

    return engine
