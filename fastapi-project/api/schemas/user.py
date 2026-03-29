from fastapi_users import schemas
from pydantic import BaseModel

from core.types.user_id_type import UserIdType


class UserExtraFields(BaseModel):
    first_name: str | None
    last_name: str | None


class UserCreate(UserExtraFields, schemas.BaseUserCreate):
    pass


class UserRead(UserExtraFields, schemas.BaseUser[UserIdType]):
    pass


class UserUpdate(UserExtraFields, schemas.BaseUserUpdate):
    pass
