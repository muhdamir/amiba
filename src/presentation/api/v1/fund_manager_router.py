from application.services import FundManagerService
from fastapi import APIRouter, Depends
from fastapi import status
from application.models import (
    FundManagerPatchModel,
    FundManagerPostModel,
    FundManagerResponseModel,
)

fund_manager_router = APIRouter(
    prefix="/fund_manager",
    tags=["Fund Manager - Fund Manager Endpoints"],
)


@fund_manager_router.get(
    path="/",
    response_model=list[FundManagerResponseModel],
)
async def get_all_fund_manager(
    service: FundManagerService = Depends(),
):
    """
    Get list of available fund managers
    """
    return service.get_all()


@fund_manager_router.get(
    path="/{fund_manager_id}",
    response_model=FundManagerResponseModel,
)
async def get_fund_manager_by_id(
    fund_manager_id: int,
    service: FundManagerService = Depends(),
):
    """
    Get fund manager details by fund manager id
    """
    return service.get_by_id(id=fund_manager_id)


@fund_manager_router.post(
    path="/",
    response_model=FundManagerResponseModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_fund_manager(
    data: FundManagerPostModel,
    service: FundManagerService = Depends(),
):
    """
    Register a new fund manager
    """
    return service.create(data=data)


@fund_manager_router.patch(
    path="/{fund_manager_id}",
    response_model=FundManagerResponseModel,
)
async def update(
    fund_manager_id: int,
    data: FundManagerPatchModel,
    service: FundManagerService = Depends(),
):
    """
    Update detail of a fund manager
    """
    return service.update(id=fund_manager_id, data=data)


@fund_manager_router.delete(
    path="/{fund_manager_id}",
    response_model=bool,
)
async def delete(
    fund_manager_id: int,
    service: FundManagerService = Depends(),
):
    """
    Delete a fund manager
    """
    return service.delete(id=fund_manager_id)
