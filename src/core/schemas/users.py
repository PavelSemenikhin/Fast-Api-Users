from fastapi_users import schemas

from core.types import USER_ID_TYPE


class UserRead(schemas.BaseUser[USER_ID_TYPE]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
