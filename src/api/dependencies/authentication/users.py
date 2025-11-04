from typing import TYPE_CHECKING

from fastapi import Depends

from core.models import User, async_get_db

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(session: "AsyncSession" = Depends(async_get_db)):
    yield User.get_db(session=session)
