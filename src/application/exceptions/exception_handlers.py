from fastapi import Request, status
from fastapi.responses import JSONResponse

from .exceptions import EntryNotFoundError, InputNotUnique

# from sqlalchemy.exc import IntegrityError


async def entry_not_found_error(
    request: Request,
    exc: EntryNotFoundError,
):
    return JSONResponse(
        content={"detail": str(exc)},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


async def input_not_unique(
    request: Request,
    exc: InputNotUnique,
):
    return JSONResponse(
        content={"detail": str(exc)},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


# async def foreign_key_violation_error(
#     request: Request,
#     exec: IntegrityError,
# ):
#     print("here")
#     print(exec.orig)
#     print(exec.statement)
#     return JSONResponse(content={"detail": str(exec)})


exception_handlers = {
    EntryNotFoundError: entry_not_found_error,
    InputNotUnique: input_not_unique,
    # IntegrityError: foreign_key_violation_error,
}
