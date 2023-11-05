from datetime import datetime

from .core import BasePatchModel, BasePostModel, BaseResponseModel


class FundNetAssetValueDataResponseModel(
    BaseResponseModel,
):
    fund_nav_data_id: int
    fund_id: int
    fund_nav_data: float
    fund_nav_data_date_of_creation: datetime
    fund_nav_data_date_of_update: datetime


class FundNetAssetValueDataPostModel(
    BasePostModel,
):
    fund_id: int
    fund_nav_data: float


class FundNetAssetValueDataPatchModel(
    BasePatchModel,
):
    fund_id: int | None = None
    fund_nav_data: float | None = None
