from ..models import FundManagerPatchModel, FundManagerPostModel
from .core import CRUDServiceInterfaceMixin


class FundManagerServiceInterface(
    CRUDServiceInterfaceMixin[
        FundManagerPostModel,
        FundManagerPatchModel,
    ],
):
    pass
