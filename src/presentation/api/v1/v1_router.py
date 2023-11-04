from fastapi import APIRouter

from .fund_manager_router import fund_manager_router
from .fund_router import fund_router
from .ping_router import ping_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(ping_router)
v1_router.include_router(fund_router)
v1_router.include_router(fund_manager_router)
