from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, SQLAlchemyBaseUserTable[int]):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @classmethod
    def get_user_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
