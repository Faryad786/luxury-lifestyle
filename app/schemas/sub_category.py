from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SubcategoryBase(BaseModel):
    name: str
    parent_id: int

class SubcategoryCreate(SubcategoryBase):
    pass

class SubcategoryUpdate(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[int] = None
    is_active: Optional[bool] = None

class SubcategoryInDB(SubcategoryBase):
    id: int
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

class Config:
        from_attributes = True  # for Pydantic v2
