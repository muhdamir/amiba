from fastapi import Depends

from application.models.fund_manager_model import (
    FundManagerPatchModel,
    FundManagerPostModel,
)
from persistence import FundManagerRepository

from ..exceptions import EntryNotFoundError
from .fund_manager_service_interface import FundManagerServiceInterface


class FundManagerService(
    FundManagerServiceInterface,
):
    def __init__(
        self,
        repository: FundManagerRepository = Depends(),
    ) -> None:
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        if entry := self.repository.get_by_id(id=id):
            return entry
        raise EntryNotFoundError(id=id)

    def create(self, data: FundManagerPostModel):
        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundManagerPatchModel):
        # check id exist
        self.get_by_id(id=id)
        dict_data = data.model_dump()
        return self.repository.update(id=id, data=dict_data)

    def delete(self, id: int):
        # check id exist
        self.get_by_id(id=id)
        return self.repository.delete(id=id)
