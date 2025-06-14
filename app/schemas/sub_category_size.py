from pydantic import BaseModel
from datetime import datetime

class SizeBase(BaseModel):
    dimension: str
    image: str
    category_id: int
    subcategory_id: int

class SizeCreate(SizeBase):
    pass

class SizeUpdate(BaseModel):
    dimension: str | None = None
    image: str | None = None
    category_id: int | None = None
    subcategory_id: int | None = None

class SizeResponse(SizeBase):
    id: int
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
