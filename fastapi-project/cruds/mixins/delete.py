from typing import Generic

from sqlalchemy.ext.asyncio import AsyncSession

from constants.crud_types import ModelType


class DeleteAsync(Generic[ModelType]):
    async def delete(self, db: AsyncSession, *, id: int, commit: bool = True) -> None:
        obj = await db.get(self.model, id)
        if obj:
            await db.delete(obj)
            if commit:
                await db.commit()
                await db.flush()
