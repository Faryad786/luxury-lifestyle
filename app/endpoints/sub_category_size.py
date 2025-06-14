from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.sub_category_size import SizeCreate, SizeUpdate, SizeResponse
from app.services import sub_category_size_service as size_service

router = APIRouter()

@router.post("/", response_model=SizeResponse)
async def create_size(size: SizeCreate, db: AsyncSession = Depends(get_db)):
    return await size_service.create_size(db, size)

@router.get("/{size_id}", response_model=SizeResponse)
async def get_size(size_id: int, db: AsyncSession = Depends(get_db)):
    return await size_service.get_size_by_id(db, size_id)

@router.get("/", response_model=list[SizeResponse])
async def list_sizes(db: AsyncSession = Depends(get_db)):
    return await size_service.get_all_sizes(db)

@router.put("/{size_id}", response_model=SizeResponse)
async def update_size(size_id: int, size: SizeUpdate, db: AsyncSession = Depends(get_db)):
    return await size_service.update_size(db, size_id, size)

@router.delete("/{size_id}")
async def delete_size(size_id: int, db: AsyncSession = Depends(get_db)):
    return await size_service.delete_size(db, size_id)
