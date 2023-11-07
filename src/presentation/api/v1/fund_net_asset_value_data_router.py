from fastapi import APIRouter, Depends

from application.models import (
    FundNetAssetValueDataPatchModel,
    FundNetAssetValueDataPostModel,
    FundNetAssetValueDataResponseModel,
)
from application.services import FundNetAssetValueDataService

fund_net_asset_value_data_router = APIRouter(
    prefix="/fund_nav_data",
    tags=["Fund Net Asset Value Data - fund net asset value related endpoints"],
)


@fund_net_asset_value_data_router.get(
    path="/",
    response_model=list[FundNetAssetValueDataResponseModel],
)
async def get_all_row_fund_nav_data(
    fund_id: int | None = None,
    service: FundNetAssetValueDataService = Depends(),
):
    """
    Get all row fund NAV data, sorted by its name by default.
    """
    return service.get_by_fund_id(fund_id=fund_id)


@fund_net_asset_value_data_router.get(
    path="/{fund_nav_data_id}",
    response_model=FundNetAssetValueDataResponseModel,
)
async def get_specific_row_fund_nav_data(
    fund_nav_data_id: int,
    service: FundNetAssetValueDataService = Depends(),
):
    """
    Get speficific row of fund NAV data
    """
    return service.get_by_id(id=fund_nav_data_id)


@fund_net_asset_value_data_router.post(
    path="/",
    response_model=FundNetAssetValueDataResponseModel,
)
async def create_a_new_entry_for_fund_nav_data(
    data: FundNetAssetValueDataPostModel,
    service: FundNetAssetValueDataService = Depends(),
):
    """
    Insert a new nav data for a specific fund
    """
    return service.create(data=data)


@fund_net_asset_value_data_router.patch(
    path="/{fund_nav_data_id}",
    response_model=FundNetAssetValueDataResponseModel,
)
async def update_entry_for_fund_nav_data(
    fund_nav_data_id: int,
    data: FundNetAssetValueDataPatchModel,
    service: FundNetAssetValueDataService = Depends(),
):
    """
    Update/fix specific fund nav data row
    """
    return service.update(id=fund_nav_data_id, data=data)


@fund_net_asset_value_data_router.delete(
    path="/{fund_nav_data_id}",
    response_model=bool,
)
async def delete_entry_for_fund_nav_data(
    fund_nav_data_id: int,
    service: FundNetAssetValueDataService = Depends(),
):
    """
    Delete specific fund nav data row
    """
    return service.delete(id=fund_nav_data_id)
