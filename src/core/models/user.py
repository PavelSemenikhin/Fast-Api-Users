from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class User(Base, SQLAlchemyBaseUserTable[int]):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)