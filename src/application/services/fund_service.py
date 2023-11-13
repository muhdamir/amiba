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
        # check if fund manager id exists
        if not self.fund_manager_repository.get_by_id(id=data.fund_manager_id):
            raise EntryNotFoundError(id=data.fund_manager_id)

        # check if fund name is taken
        if self.repository.get_by_name(fund_name=data.fund_name):
            raise InputNotUnique(input=data.fund_name)

        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundPatchModel):
        # check fund name is taken
        fund_name = data.fund_name
        fund_name_exist = (
            self.repository.get_by_name(
                fund_name=fund_name,
                exclude_id=id,
            )
            if fund_name
            else None
        )
        if fund_name_exist and fund_name:
            raise InputNotUnique(input=fund_name)

        dict_data = data.model_dump(exclude_unset=True)
        if updated_data := self.repository.update(
            id=id,
            data=dict_data,
        ):
            return updated_data

        raise EntryNotFoundError(id=id)

    def delete(self, id: int) -> bool:
        if status := self.repository.delete(id=id):
            return status

        raise EntryNotFoundError(id=id)
