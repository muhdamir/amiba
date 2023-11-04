from ..models import FundPatchModel, FundPostModel
from .core import CRUDServiceInterfaceMixin


class FundServiceInterface(
    CRUDServiceInterfaceMixin[
        FundPostModel,
        FundPatchModel,
    ]
):
    pass
