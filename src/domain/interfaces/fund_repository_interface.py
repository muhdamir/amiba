from ..entities import Fund
from .core import CRUDRepositoryInterfaceMixin


class FundRepositoryInterface(
    CRUDRepositoryInterfaceMixin[Fund],
):
    pass
