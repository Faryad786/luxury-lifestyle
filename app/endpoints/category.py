from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryInDB
from app.services.category_service import (
    create_category,
    get_category,
    update_category,
    delete_category,
    list_categories
)

router = APIRouter()

@router.post("/", response_model=CategoryInDB, status_code=status.HTTP_201_CREATED)
async def create(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await create_category(db, category)

@router.get("/{category_id}", response_model=CategoryInDB)
async def read(category_id: int, db: AsyncSession = Depends(get_db)):  # ✅ FIXED
    return await get_category(db, category_id)

@router.put("/{category_id}", response_model=CategoryInDB)
def update(category_id: int, update_data: CategoryUpdate, db: AsyncSession = Depends(get_db)):
    return update_category(db, category_id, update_data)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(category_id: int, db: AsyncSession = Depends(get_db)):
    delete_category(db, category_id)
    return

@router.get("/", response_model=List[CategoryInDB])
def list_all(db: AsyncSession = Depends(get_db)):
    return list_categories(db)
