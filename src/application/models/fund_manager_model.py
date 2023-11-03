from datetime import date

from pydantic import EmailStr

from .core import BasePatchModel, BasePostModel, BaseResponseModel


class FundManagerResponseModel(BaseResponseModel):
    fund_manager_id: int
    fund_manager_name: str
    fund_manager_email: str
    date_created_on: date
    date_updated_on: date


class FundManagerPostModel(BasePostModel):
    fund_manager_name: str
    fund_manager_email: EmailStr


class FundManagerPatchModel(BasePatchModel):
    fund_manager_name: str | None
    fund_manager_email: EmailStr | None
