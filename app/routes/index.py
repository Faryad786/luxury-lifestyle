# app/routes/index.py

from fastapi import APIRouter
from app.endpoints import category ,sub_category , sub_category_size

api_router = APIRouter()

# Include your category router
api_router.include_router(
    category.router,
    prefix="/api/v1/category",
    tags=["Category"]
)

api_router.include_router(
    sub_category.router,
    prefix="/api/v1/subcategory",
    tags=["SubCategory"]
)

api_router.include_router(
    sub_category_size.router,
    prefix="/api/v1/subcategory_size",
    tags=["SubCategory Size"]
)

# Add other routers similarly:
# from app.endpoints import user
# api_router.include_router(user.router, prefix="/api/v1/user", tags=["User"])
