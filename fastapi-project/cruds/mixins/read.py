from typing import Any, Generic, Optional, Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from constants.crud_types import ModelType


class ReadAsync(Generic[ModelType]):
    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        return await db.get(self.model, id)

    async def get_by_uid(self, db: AsyncSession, *, uid: str) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.uid == uid)
        if hasattr(self.model, "is_deleted"):
            statement = statement.where(self.model.is_deleted.is_(False))
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 1000
    ) -> Sequence[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        if hasattr(self.model, "is_deleted"):
            statement = statement.where(self.model.is_deleted.is_(False))
        result = await db.execute(statement)
        return result.scalars().all()

    async def get_multi_by_uids(
        self, db: AsyncSession, *, uids: [UUID]
    ) -> Sequence[ModelType]:
        if not uids:
            return []
        statement = select(self.model).where(self.model.uid.in_(uids))
        if hasattr(self.model, "is_deleted"):
            statement = statement.where(self.model.is_deleted.is_(False))
        result = await db.execute(statement)
        return result.scalars().all()
