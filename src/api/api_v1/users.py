zfrom fastapi import APIRouter

from api.api_v1.fastapi_users_routers_helper import fastapi_users
from api.dependencies.authentication.backend import authentication_backend
from core.config import settings
from core.schemas.users import UserRead, UserCreate, UserUpdate

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    )
)
