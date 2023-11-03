from .fund_manager_service_interface import FundManagerServiceInterface
from .core.service_mixin import ReadServiceMixin
from persistence import FundManagerRepository
from fastapi import Depends


class FundManagerService(
    ReadServiceMixin[FundManagerRepository],
    FundManagerServiceInterface,
):
    def __init__(
        self,
        repository: FundManagerRepository = Depends(),
    ) -> None:
        self.repository = repository

    def get_all(self):
        return self._get_all()
