from ..entities import FundManager
from .core import CRUDRepositoryInterfaceMixin


class FundManagerRepositoryInteface(
    CRUDRepositoryInterfaceMixin[FundManager],
):
    pass
