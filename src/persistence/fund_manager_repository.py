from domain.entities import FundManager
from domain.interfaces import FundManagerRepositoryInteface

from .core import BaseRepository, CRUDRepositoryMixin


class FundManagerRepository(
    CRUDRepositoryMixin[FundManager],
    BaseRepository,
    FundManagerRepositoryInteface,
):
    def get_all(self) -> list[FundManager]:
        return self._get_all(entity=FundManager)

    def get_by_id(self, id: int) -> FundManager | None:
        return self._get_by_id(entity=FundManager, id=id)

    def create(self, data: dict) -> FundManager:
        return self._create(entity=FundManager, data=data)

    def update(self, id: int, data: dict) -> FundManager:
        return self._update(entity=FundManager, id=id, data=data)

    def delete(self, id: int) -> bool:
        return self._delete(entity=FundManager, id=id)
