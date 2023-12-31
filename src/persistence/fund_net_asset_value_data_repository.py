from typing import Sequence

from sqlalchemy import select

from domain.entities import FundNetAssetValueData
from domain.interfaces import FundNetAssetValueDataRepositoryInterface

from .core import BaseRepository, CRUDRepositoryMixin


class FundNetAssetValueDataRepository(
    CRUDRepositoryMixin[FundNetAssetValueData],
    BaseRepository,
    FundNetAssetValueDataRepositoryInterface,
):
    # def get_all(self) -> list[FundNetAssetValueData]:
    #     return self._get_all(entity=FundNetAssetValueData)
    def get_all(self) -> Sequence[FundNetAssetValueData]:
        return self._get_all(entity=FundNetAssetValueData)

    def get_by_id(self, id: int) -> FundNetAssetValueData | None:
        return self._get_by_id(entity=FundNetAssetValueData, id=id)

    def create(self, data: dict) -> FundNetAssetValueData:
        return self._create(entity=FundNetAssetValueData, data=data)

    def update(self, id: int, data: dict) -> FundNetAssetValueData | None:
        return self._update(entity=FundNetAssetValueData, id=id, data=data)

    def delete(self, id: int) -> bool:
        return self._delete(entity=FundNetAssetValueData, id=id)

    # additional method
    def get_by_fund_id(self, fund_id: int) -> Sequence[FundNetAssetValueData]:
        statement = select(FundNetAssetValueData).where(
            FundNetAssetValueData.fund_id == fund_id
        )
        return self.session.scalars(statement=statement).all()
