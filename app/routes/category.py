from fastapi import APIRouter
from app.endpoints import category

router = APIRouter()
router.include_router(prefix='/create/category', )
