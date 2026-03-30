from fastapi import APIRouter
from api.dependencies.authentication import fastapi_users
from api.schemas.user import UserRead, UserUpdate


router = APIRouter(prefix="/users", tags=["Users"])


router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)

router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
