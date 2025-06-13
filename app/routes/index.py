# app/routes/index.py

from fastapi import APIRouter
from app.endpoints import category 

api_router = APIRouter()

# Include your category router
api_router.include_router(
    category.router,
    prefix="/api/v1/category",
    tags=["Category"]
)

# Add other routers similarly:
# from app.endpoints import user
# api_router.include_router(user.router, prefix="/api/v1/user", tags=["User"])
