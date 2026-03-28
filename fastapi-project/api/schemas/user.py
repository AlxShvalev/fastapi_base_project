from fastapi_users import schemas

from core.types.user_id_type import UserIdType


class UserCreate(schemas.BaseUserCreate):
    first_name: str | None
    last_name: str | None


class UserRead(schemas.BaseUser[UserIdType]):
    first_name: str | None
    last_name: str | None


class UserUpdate(UserCreate, schemas.BaseUserUpdate):
    pass
