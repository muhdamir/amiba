from fastapi import APIRouter

ping_router = APIRouter(prefix="/ping", tags=["Ping"])


@ping_router.get("/")
async def ping():
    """
    ping network test
    """
    return "pong"
