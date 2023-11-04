from datetime import date

from .core import BasePatchModel, BasePostModel, BaseResponseModel
from .fund_manager_model import FundManagerResponseModel


class FundResponseModel(
    BaseResponseModel,
):
    fund_id: int
    fund_name: str
    fund_manager_id: int
    fund_description: str
    fund_net_asset_value: float
    fund_date_of_creation: date
    fund_date_of_update: date
    fund_performance: float
    fund_manager: FundManagerResponseModel


class FundPostModel(
    BasePostModel,
):
    fund_name: str
    fund_manager_id: int
    fund_description: str
    fund_net_asset_value: float
    fund_performance: float


class FundPatchModel(
    BasePatchModel,
):
    fund_name: str | None = None
    fund_manager_id: int | None = None
    fund_description: str | None = None
    fund_net_asset_value: float | None = None
    fund_performance: float | None = None
