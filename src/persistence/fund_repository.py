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

    # additional method
    def get_by_name(self, fund_name: str, exclude_id: int | None = None):
        query = self.session.query(Fund).filter_by(fund_name=fund_name)
        if not exclude_id:
            return query.all()
        return query.filter(Fund.fund_id != exclude_id).all()
