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
        # check if email has been taken
        if self.repository.get_by_email(email=data.fund_manager_email):
            raise InputNotUnique(input=data.fund_manager_email)

        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundManagerPatchModel):
        # check if email has been taken
        email = data.fund_manager_email
        email_exist = (
            self.repository.get_by_email(
                email=email,
                exclude_id=id,
            )
            if email
            else None
        )
        if email_exist and email:
            raise InputNotUnique(input=email)

        dict_data = data.model_dump(exclude_unset=True)

        if updated_data := self.repository.update(
            id=id,
            data=dict_data,
        ):
            return updated_data

        raise EntryNotFoundError(id=id)

    def delete(self, id: int):
        if status := self.repository.delete(id=id):
            return status

        raise EntryNotFoundError(id=id)
