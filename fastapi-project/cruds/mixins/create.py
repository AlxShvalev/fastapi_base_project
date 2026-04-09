from typing import Generic

from sqlalchemy.ext.asyncio import AsyncSession

from constants.crud_types import CreateSchemaType, ModelType


class CreateAsync(Generic[CreateSchemaType, ModelType]):
    async def create(
        self, db: AsyncSession, *, obj_in: CreateSchemaType, commit: bool = True
    ) -> ModelType:
        obj_in_data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        if commit:
            await db.commit()
            await db.refresh(db_obj)
        return db_obj
