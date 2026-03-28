from typing import TYPE_CHECKING
from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.types.user_id_type import UserIdType
from .base import BaseModel
from .mixins.pks import IntIdMixin
from .mixins.timestamps import UpdatedAtMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(BaseModel, IntIdMixin, UpdatedAtMixin, SQLAlchemyBaseUserTable[UserIdType]):
    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True)

    @classmethod
    async def get_db(cls, session: "AsyncSession"):
        yield SQLAlchemyUserDatabase(session, cls)
