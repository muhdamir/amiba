from typing import Generic, Protocol, TypeVar
from typing import Union
from sqlalchemy.orm import Session

from application.models.core import BasePatchModel, BasePostModel
from domain.entities import Base
from domain.interfaces.core import CRUDRepositoryInterfaceMixin
from persistence import FundManagerRepository
from persistence.core import CRUDRepositoryMixin

Entity = TypeVar("Entity", bound=Base, covariant=True)


class BaseRepository(Protocol):
    session: Session


class ReadRepository(
    BaseRepository,
    Protocol,
    Generic[Entity],
):
    session: Session

    def get_all(self):
        ...

    def get_by_id(self, id: int):
        ...


class CreateRepository(
    BaseRepository,
    Protocol,
    Generic[Entity],
):
    session: Session

    def create(self, data: dict):
        ...


class DeleteRepository(
    BaseRepository,
    Protocol,
    Generic[Entity],
):
    session: Session

    def delete(self, id: int):
        ...


class UpdateRepository(
    BaseRepository,
    Protocol,
    Generic[Entity],
):
    def update(self, id: int, data: dict):
        ...


class CRUDRepository(
    DeleteRepository[Entity],
    UpdateRepository[Entity],
    ReadRepository[Entity],
    CreateRepository[Entity],
    Protocol,
    Generic[Entity],
):
    pass


T = TypeVar("T", bound=Base)


class Service(Protocol, Generic[T]):
    repository: Union[
        CreateRepository[T],
        ReadRepository[T],
        UpdateRepository[T],
        DeleteRepository[T],
        CRUDRepository[T],
    ]


class ReadServiceMixin:
    def _get_all(self: Service):
        if isinstance(self, ReadRepository):
            self.repository.get_all()


# ################################################
# def ha(l: ReadRepository):
#     l.get_all()


# # type function pun akan ada error
# ha(l=FundManagerRepository())
