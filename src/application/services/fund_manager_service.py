from fastapi import Depends

from application.models.fund_manager_model import (
    FundManagerPatchModel,
    FundManagerPostModel,
)
from persistence import FundManagerRepository

from ..exceptions import EntryNotFoundError, InputNotUnique
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
        # check email has been taken
        if self.repository.get_by_email(email=data.fund_manager_email):
            raise InputNotUnique(input=data.fund_manager_email)

        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundManagerPatchModel):
        # check id exist
        current_data = self.get_by_id(id=id)
        # check email has been taken
        if data.fund_manager_email:
            if self.repository.get_by_email(
                email=data.fund_manager_email,
                exclude_id=current_data.fund_manager_id,
            ):
                raise InputNotUnique(input=data.fund_manager_email)

        dict_data = data.model_dump(exclude_unset=True)
        return self.repository.update(id=id, data=dict_data)

    def delete(self, id: int):
        # check id exist
        self.get_by_id(id=id)
        return self.repository.delete(id=id)
