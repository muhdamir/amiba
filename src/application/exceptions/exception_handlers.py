from fastapi import Request, status
from fastapi.responses import JSONResponse

from .exceptions import EntryNotFoundError


async def entry_not_found_error(
    request: Request,
    exc: EntryNotFoundError,
):
    return JSONResponse(
        content={"detail": str(exc)},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


exception_handlers = {
    EntryNotFoundError: entry_not_found_error,
}
