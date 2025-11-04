from typing import TYPE_CHECKING

from fastapi import Depends

from core.models import async_get_db, AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
        session: "AsyncSession" = Depends(async_get_db),
):
    yield AccessToken.get_db(session=session)
