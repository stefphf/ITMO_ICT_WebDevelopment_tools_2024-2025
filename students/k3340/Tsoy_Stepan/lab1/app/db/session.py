from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False, connect_args={})


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)