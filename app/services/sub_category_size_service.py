from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.category_size import Size
from app.schemas.sub_category_size import SizeCreate, SizeUpdate
from app.exceptions.exceptions_file import NotFoundException

async def create_size(db: AsyncSession, size_data: SizeCreate):
    new_size = Size(**size_data.dict())
    db.add(new_size)
    await db.commit()
    await db.refresh(new_size)
    return new_size

async def get_size_by_id(db: AsyncSession, size_id: int):
    result = await db.execute(select(Size).where(Size.id == size_id, Size.is_deleted == False))
    size = result.scalar_one_or_none()
    if not size:
        raise NotFoundException("Size not found")
    return size

async def get_all_sizes(db: AsyncSession):
    result = await db.execute(select(Size).where(Size.is_deleted == False))
    return result.scalars().all()

async def update_size(db: AsyncSession, size_id: int, size_data: SizeUpdate):
    size = await get_size_by_id(db, size_id)
    for key, value in size_data.dict(exclude_unset=True).items():
        setattr(size, key, value)
    await db.commit()
    await db.refresh(size)
    return size

async def delete_size(db: AsyncSession, size_id: int):
    size = await get_size_by_id(db, size_id)
    size.is_deleted = True
    await db.commit()
    return {"detail": "Size soft-deleted successfully"}
