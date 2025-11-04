from fastapi_users import FastAPIUsers

from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.user_manager import get_user_manager
from core.models import User
from core.types import USER_ID_TYPE

fastapi_users = FastAPIUsers[User, USER_ID_TYPE](
    get_user_manager,
    [authentication_backend],
)
