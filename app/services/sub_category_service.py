from sqlalchemy import select

from app.models.sub_category import Subcategory
from app.schemas.sub_category import SubcategoryCreate, SubcategoryUpdate
from app.exceptions.exceptions_file import NotFoundException, ConflictException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category

async def create_subcategory(db: AsyncSession, subcategory_data: SubcategoryCreate):
    # Check for existing subcategory
    stmt = select(Subcategory).where(Subcategory.name == subcategory_data.name)
    result = await db.execute(stmt)
    existing = result.scalars().first()
    
    if existing:
        raise ConflictException("Subcategory already exists")
    parent_stmt = select(Category).where(Category.id == subcategory_data.parent_id)
    parent_result = await db.execute(parent_stmt)
    if not parent_result.scalars().first():
        raise ConflictException("Parent category does not exist")

    # Create new subcategory
    subcategory = Subcategory(**subcategory_data.dict())
    db.add(subcategory)
    await db.commit()
    await db.refresh(subcategory)
    return subcategory


async def get_subcategory(db: AsyncSession, subcategory_id: int):
    result = await db.execute(
        select(Subcategory).where(
            Subcategory.id == subcategory_id,
            Subcategory.is_deleted == False
        )
    )
    subcategory = result.scalar_one_or_none()
    if not subcategory:
        raise NotFoundException("Subcategory not found")
    return subcategory

def list_subcategories(db:AsyncSession):
    return db.query(Subcategory).filter(Subcategory.is_deleted == False).all()

def update_subcategory(db: AsyncSession, subcategory_id: int, update_data: SubcategoryUpdate):
    subcategory = get_subcategory(db, subcategory_id)
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(subcategory, field, value)
    db.commit()
    db.refresh(subcategory)
    return subcategory

def delete_subcategory(db: AsyncSession, subcategory_id: int):
    subcategory = get_subcategory(db, subcategory_id)
    subcategory.is_deleted = True
    db.commit()
    return {"message": "Subcategory deleted"}
