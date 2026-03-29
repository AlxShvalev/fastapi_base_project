from fastapi import APIRouter
from api.dependencies.authentication.backend import authentication_backend
from api.schemas.user import UserRead, UserCreate
from api.dependencies.authentication.fastapi_users_dependencies import fastapi_users


router = APIRouter(prefix="/auth", tags=["Auth"])

router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    prefix="/jwt",
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="",
)
