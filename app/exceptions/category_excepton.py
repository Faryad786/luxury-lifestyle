from typing import Optional
from app.exceptions.exceptions_file import ConflictException, NotFoundException

class CategoryAlreadyExistsException(ConflictException):
    def __init__(self, detail: Optional[str] = "Category already exists"):
        super().__init__(detail)

class CategoryNotFoundException(NotFoundException):
    def __init__(self, detail: Optional[str] = "Category not found"):
        super().__init__(detail)
