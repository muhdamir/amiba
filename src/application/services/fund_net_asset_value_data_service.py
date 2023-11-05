from fastapi import Depends

from application.models.fund_net_asset_value_data_model import (
    FundNetAssetValueDataPatchModel,
    FundNetAssetValueDataPostModel,
)
from persistence import FundNetAssetValueDataRepository

from .fund_net_asset_value_data_service_interface import (
    FundNetAssetValueDataServiceInterface,
)


class FundNetAssetValueDataService(
    FundNetAssetValueDataServiceInterface,
):
    def __init__(
        self,
        repository: FundNetAssetValueDataRepository = Depends(),
    ) -> None:
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id=id)

    def create(self, data: FundNetAssetValueDataPostModel):
        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def update(self, id: int, data: FundNetAssetValueDataPatchModel):
        dict_data = data.model_dump(exclude_unset=True)
        return self.repository.update(id=id, data=dict_data)

    def delete(self, id: int):
        return self.repository.delete(id=id)
