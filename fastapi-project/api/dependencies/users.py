from typing import TYPE_CHECKING, Annotated, AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from core.database import db_handler
from core.database.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated["AsyncSession", Depends(db_handler.get_session)],
) -> AsyncGenerator[SQLAlchemyUserDatabase]:
    yield User.get_db(session=session)
