from fastapi_users import FastAPIUsers

from fastapi import APIRouter
from api.dependencies.backend import authentication_backend
from api.dependencies.user_manager import get_user_manager
from api.schemas.user import UserRead, UserCreate
from core.database.models import User
from core.types.user_id_type import UserIdType


fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)


router = APIRouter(prefix="/auth", tags=["auth"])

router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    prefix="/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="",
    tags=["auth"],
)
