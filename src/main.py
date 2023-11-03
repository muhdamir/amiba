from fastapi import FastAPI
from presentation import api
from application.events import StartupEvent


app = FastAPI(
    title="AHAM CAPITAL FUND REST API (Assessment)",
    description="This Open API is created solely for the purpose of the assessment prepared by AHAM Capital for backend development position.",
    summary="REST API for Fund Management System (Assessment)",
    on_startup=[StartupEvent()],
    # exception_handlers=
)

app.include_router(api)
