from .core import CRUDServiceInterfaceMixin
from ..models import FundPatchModel, FundPostModel


class FundServiceInterface(
    CRUDServiceInterfaceMixin[
        FundPostModel,
        FundPatchModel,
    ]
):
    pass
