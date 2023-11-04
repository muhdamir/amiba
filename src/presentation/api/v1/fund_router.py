from fastapi import APIRouter, Depends

from application.models import FundPatchModel, FundPostModel, FundResponseModel
from application.services import FundService

fund_router = APIRouter(
    prefix="/fund",
    tags=["Fund - Fund Management Endpoints"],
)


@fund_router.get(
    "/",
    response_model=list[FundResponseModel],
)
async def get_all_fund(
    service: FundService = Depends(),
):
    """
    Get all funds available in the server
    """
    return service.get_all()


@fund_router.get(
    "/{fund_id}",
    response_model=FundResponseModel,
)
async def get_fund_by_id(
    fund_id: int,
    service: FundService = Depends(),
):
    """
    Get details of a fund by the given id
    """
    return service.get_by_id(id=fund_id)


@fund_router.post(
    "/",
    response_model=FundResponseModel,
)
async def create_new_fund(
    data: FundPostModel,
    service: FundService = Depends(),
):
    """
    Create a new fund
    """
    return service.create(data=data)


@fund_router.patch(
    "/{fund_id}",
    response_model=FundResponseModel,
)
async def update_fund(
    fund_id: int,
    data: FundPatchModel,
    service: FundService = Depends(),
):
    """
    Partially update a fund
    """
    return service.update(id=fund_id, data=data)


@fund_router.delete(
    "/{fund_id}",
    response_model=bool,
)
async def delete_fund_by_id(
    fund_id: int,
    service: FundService = Depends(),
):
    """
    Delete a fund by the given id
    """
    return service.delete(fund_id)
