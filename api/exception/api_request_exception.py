
class ApiRequestException(Exception):
    def __init__(self, message: str, status_code: int | None):
        super().__init__(message)
        self.message = message 
        self.status_code = status_code

    def __str__(self) -> str:
        return f'Failed to fetch data from api: {self.message}'
    