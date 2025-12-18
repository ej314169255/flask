import atexit
import datetime
import os

from sqlalchemy import DateTime, Integer, String, create_engine, func
from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column, sessionmaker

POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1234")
POSTGRES_DB = os.getenv("POSTGRES_DB", "netology")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):

    def id_dict(self):
        return {"id": self.id}


class User(Base):
    __tablename__ = "users"

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    name: MappedColumn[str] = mapped_column(String, unique=True)
    password: MappedColumn[str] = mapped_column(String)
    registration_time: MappedColumn[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "registration_time": int(self.registration_time.timestamp()),
        }


Base.metadata.create_all(bind=engine)

atexit.register(engine.dispose)
