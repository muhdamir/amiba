from fastapi import Depends

from persistence import FundManagerRepository, FundRepository

from ..exceptions import EntryNotFoundError, InputNotUnique
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
        self.fund_manager_repository = FundManagerRepository.from_existing_repository(
            repository
        )

    def get_by_id(self, id: int):
        if entry := self.repository.get_by_id(id=id):
            return entry
        raise EntryNotFoundError(id=id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: FundPostModel):
        # check fund manager id exists
        if not self.fund_manager_repository.get_by_id(id=data.fund_manager_id):
            raise EntryNotFoundError(id=data.fund_manager_id)
        # check fund name is taken
        if self.repository.get_by_name(fund_name=data.fund_name):
            raise InputNotUnique(input=data.fund_name)

        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundPatchModel):
        # check if id exists
        current_data = self.get_by_id(id=id)
        # check fund name is taken
        if data.fund_name:
            if self.repository.get_by_name(
                fund_name=data.fund_name,
                exclude_id=current_data.fund_id,
            ):
                raise InputNotUnique(input=data.fund_name)
        dict_data = data.model_dump(exclude_unset=True)
        return self.repository.update(id=id, data=dict_data)

    def delete(self, id: int) -> bool:
        # check if id exists
        self.get_by_id(id=id)
        return self.repository.delete(id=id)
