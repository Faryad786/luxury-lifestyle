from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryInDB
from app.exceptions.category_excepton import (
    CategoryAlreadyExistsException,
    CategoryNotFoundException
)


async def create_category(db: AsyncSession, category: CategoryCreate):
    result = await db.execute(select(Category).where(Category.name == category.name))
    existing_category = result.scalars().first()

    if existing_category:
        raise CategoryAlreadyExistsException()

    new_category = Category(**category.dict())
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category

async def get_category(db: AsyncSession, category_id: int) -> CategoryInDB:
    # Correct SQLAlchemy 2.0 async query syntax
    stmt = select(Category).where(
        Category.id == category_id,
        Category.is_deleted == False
    )
    result = await db.execute(stmt)
    category = result.scalars().first()
    
    if not category:
        raise CategoryNotFoundException()
    return category

def update_category(db: AsyncSession, category_id: int, update_data: CategoryUpdate) -> CategoryInDB:
    category = db.query(Category).filter(Category.id == category_id, Category.is_deleted == False).first()
    if not category:
        raise CategoryNotFoundException()
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: AsyncSession, category_id: int) -> None:
    category = db.query(Category).filter(Category.id == category_id, Category.is_deleted == False).first()
    if not category:
        raise CategoryNotFoundException()
    category.is_deleted = True
    db.commit()

def list_categories(db: AsyncSession) -> list[CategoryInDB]:
    return db.query(Category).filter(Category.is_deleted == False).all()
