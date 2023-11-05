from datetime import datetime

from .core import BasePatchModel, BasePostModel, BaseResponseModel


class FundNetAssetValueDataResponseModel(
    BaseResponseModel,
):
    fund_nav_id: int
    fund_id: int
    fund_nav: float
    fund_nav_date_of_creation: datetime
    fund_nav_date_of_update: datetime


class FundNetAssetValueDataPostModel(
    BasePostModel,
):
    fund_id: int
    fund_nav: float


class FundNetAssetValueDataPatchModel(
    BasePatchModel,
):
    fund_id: int | None = None
    fund_nav: float | None = None
