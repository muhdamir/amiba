from domain.entities import Fund
from domain.interfaces import FundRepositoryInterface

from .core import BaseRepository, CRUDRepositoryMixin


class FundRepository(
    CRUDRepositoryMixin[Fund],
    BaseRepository,
    FundRepositoryInterface,
):
    def get_all(self) -> list[Fund]:
        return self._get_all(entity=Fund)

    def get_by_id(self, id: int) -> Fund | None:
        return self._get_by_id(entity=Fund, id=id)

    def create(self, data: dict) -> Fund:
        return self._create(entity=Fund, data=data)

    def update(self, id: int, data: dict) -> Fund:
        return self._update(entity=Fund, id=id, data=data)

    def delete(self, id: int) -> bool:
        return self._delete(entity=Fund, id=id)
