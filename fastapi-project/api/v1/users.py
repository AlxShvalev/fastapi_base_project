from fastapi import APIRouter
from api.dependencies.authentication.fastapi_users_dependencies import fastapi_users
from api.schemas.user import UserRead, UserUpdate


router = APIRouter(prefix="/users", tags=["Users"])


router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
