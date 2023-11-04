from fastapi import Depends

from persistence import FundRepository, FundManagerRepository

from ..exceptions import EntryNotFoundError
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
        # additional repository
        self.fund_manager_repository = FundManagerRepository(
            session=self.repository.session
        )

    def get_by_id(self, id: int):
        if entry := self.repository.get_by_id(id=id):
            return entry
        raise EntryNotFoundError(id=id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: FundPostModel):
        # check fund manager id exists
        if self.fund_manager_repository.get_by_id(id=data.fund_manager_id):
            dict_data = data.model_dump()
            return self.repository.create(data=dict_data)
        raise EntryNotFoundError(id=data.fund_manager_id)

    def update(self, id: int, data: FundPatchModel):
        # check if id exists
        self.get_by_id(id=id)
        dict_data = data.model_dump(exclude_unset=True)
        return self.repository.update(id=id, data=dict_data)

    def delete(self, id: int) -> bool:
        # check if id exists
        self.get_by_id(id=id)
        return self.repository.delete(id=id)
