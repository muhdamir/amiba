from fastapi import Depends

from persistence.fund_repository import FundRepository

from ..models import FundPatchModel, FundPostModel
from .fund_service_interface import FundServiceInterface


class FundService(
    FundServiceInterface,
):
    def __init__(
        self,
        repository: FundRepository = Depends(),
    ) -> None:
        self.repository = repository

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id=id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: FundPostModel):
        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundPatchModel):
        dict_data = data.model_dump(exclude_unset=True)
        return self.repository.update(id=id, data=dict_data)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id=id)
