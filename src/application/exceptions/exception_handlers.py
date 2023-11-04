from fastapi import Request
from fastapi.responses import JSONResponse

from .exceptions import EntryNotFoundError


async def entry_not_found_error(
    request: Request,
    exc: EntryNotFoundError,
):
    print(request)
    return JSONResponse(content=str(exc))


exception_handlers = {
    EntryNotFoundError: entry_not_found_error,
}
