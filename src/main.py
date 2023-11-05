from fastapi import FastAPI

from application.events import StartupEvent
from application.exceptions import exception_handlers
from presentation import api

app = FastAPI(
    title="AHAM CAPITAL FUND REST API (Assessment)",
    description="This Open API is created solely for the purpose of the assessment prepared by AHAM Capital for backend development position.",
    summary="REST API for Fund Management System (Assessment)",
    exception_handlers=exception_handlers,  # type: ignore
)

app.include_router(api)
