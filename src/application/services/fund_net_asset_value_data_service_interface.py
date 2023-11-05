from ..models import FundNetAssetValueDataPatchModel, FundNetAssetValueDataPostModel
from .core import CRUDServiceInterfaceMixin


class FundNetAssetValueDataServiceInterface(
    CRUDServiceInterfaceMixin[
        FundNetAssetValueDataPostModel,
        FundNetAssetValueDataPatchModel,
    ]
):
    pass
