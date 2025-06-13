from fastapi import HTTPException, status
from typing import Optional
from app.utils.error_message import get_error_message  

class FileNotFoundError(HTTPException):
    def __init__(self, detail: Optional[str] = "File not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "FileNotFoundError"}
        )

class BadRequestException(HTTPException):
    def __init__(self, detail: Optional[str] = "Bad request"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "BadRequest"}
        )


class UnauthorizedException(HTTPException):
    def __init__(self, detail: Optional[str] = "Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "Unauthorized"}
        )


class ForbiddenException(HTTPException):
    def __init__(self, detail: Optional[str] = "Forbidden"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "Forbidden"}
        )


class ConflictException(HTTPException):
    def __init__(self, detail: Optional[str] = "Conflict"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "Conflict"}
        )

class NotFoundException(HTTPException):
    def __init__(self, detail: Optional[str] = "Resource not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "NotFound"}
        )

class ServerErrorException(HTTPException):
    def __init__(self, detail: Optional[str] = "Internal server error"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_error_message(detail) if callable(get_error_message) else detail,
            headers={"X-Error": "ServerError"}
        )
        
