from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.schemas.sub_category import SubcategoryCreate, SubcategoryUpdate, SubcategoryInDB
from app.services import sub_category_service

router = APIRouter()

@router.post("/", response_model=SubcategoryInDB)
async def create_subcategory(
    subcategory: SubcategoryCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await sub_category_service.create_subcategory(db, subcategory)

@router.get("/{subcategory_id}", response_model=SubcategoryInDB)
async def get_subcategory(subcategory_id: int, db: AsyncSession = Depends(get_db)):
    return await sub_category_service.get_subcategory(db, subcategory_id)

@router.get("/", response_model=List[SubcategoryInDB])
def list_subcategories(db: AsyncSession = Depends(get_db)):
    return sub_category_service.list_subcategories(db)

@router.put("/{subcategory_id}", response_model=SubcategoryInDB)
def update_subcategory(subcategory_id: int, update_data: SubcategoryUpdate, db:AsyncSession  = Depends(get_db)):
    return sub_category_service.update_subcategory(db, subcategory_id, update_data)

@router.delete("/{subcategory_id}")
def delete_subcategory(subcategory_id: int, db: AsyncSession = Depends(get_db)):
    return sub_category_service.delete_subcategory(db, subcategory_id)
