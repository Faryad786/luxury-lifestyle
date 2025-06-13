# app/utils/error_messages.py

ERROR_MESSAGES = {
    "FileNotFound": "The requested file was not found.",
    "BadRequest": "The request could not be understood or was missing required parameters.",
    "Unauthorized": "Authentication credentials were missing or incorrect.",
    "Forbidden": "You do not have permission to access this resource.",
    "Conflict": "A conflict occurred with the current state of the resource.",
    "NotFound": "The specified resource was not found.",
    "ServerError": "An internal server error occurred. Please try again later.",
    "ValidationError": "Input validation failed.",
    # Add more custom messages or codes as needed
}

def get_error_message(key: str) -> str:
    """
    Retrieves a human-readable error message for a given key.
    If the key is not found, it returns the key itself.
    """
    return ERROR_MESSAGES.get(key, key)
