from .core import CRUDServiceInterfaceMixin
from ..models import FundManagerPatchModel, FundPostModel


class FundManagerServiceInterface(
    CRUDServiceInterfaceMixin[FundPostModel, FundManagerPatchModel],
):
    pass
