from typing import Protocol, TypeVar, runtime_checkable
from typing import Union
from sqlalchemy.orm import Session

from application.models.core import BasePatchModel, BasePostModel
from domain.entities import Base

Entity = TypeVar("Entity", bound=Base, covariant=True)


@runtime_checkable
class BaseRepository(Protocol):
    session: Session


@runtime_checkable
class ReadRepository(
    BaseRepository,
    Protocol[Entity],
):
    session: Session

    def get_all(self):
        ...

    def get_by_id(self, id: int):
        ...


@runtime_checkable
class CreateRepository(
    BaseRepository,
    Protocol[Entity],
):
    session: Session

    def create(self, data: dict):
        ...


@runtime_checkable
class DeleteRepository(
    BaseRepository,
    Protocol[Entity],
):
    session: Session

    def delete(self, id: int):
        ...


@runtime_checkable
class UpdateRepository(
    BaseRepository,
    Protocol[Entity],
):
    def update(self, id: int, data: dict):
        ...


@runtime_checkable
class CRUDRepository(
    DeleteRepository[Entity],
    UpdateRepository[Entity],
    ReadRepository[Entity],
    CreateRepository[Entity],
    Protocol[Entity],
):
    pass


T = TypeVar("T", bound=Base)


class Service(Protocol[T]):
    repository: Union[
        CreateRepository[T],
        ReadRepository[T],
        UpdateRepository[T],
        DeleteRepository[T],
        CRUDRepository[T],
    ]


class ReadServiceMixin:
    def _get_all(self: Service):
        if isinstance(
            self.repository,
            (ReadRepository, CRUDRepository),
        ):
            return self.repository.get_all()
        raise Exception("Repository does not have Read operation functionality")

    def _get_by_id(self: Service, id: int):
        if isinstance(self.repository, (ReadRepository, CRUDRepository)):
            return self.repository.get_by_id(id=id)
        raise Exception("Repository does not have Read operation functionality")


class CreateServiceMixin:
    def _create(self: Service, data: dict):
        if isinstance(
            self.repository,
            (CreateRepository, CRUDRepository),
        ):
            return self.repository.create(data=data)
        raise Exception("Repository does not have Create operation functionality")


class UpdateServiceMixin:
    def _update(self: Service, id: int, data: dict):
        if isinstance(
            self.repository,
            UpdateRepository,
        ):
            return self.repository.update(id=id, data=data)
        raise Exception("Repository does not have Update operation functionality")


class DeleteServiceMixin:
    def _delete(self: Service, id: int):
        if isinstance(
            self.repository,
            DeleteRepository,
        ):
            return self.repository.delete(id=id)
        raise Exception("Repository does not have Delete operation functionality")


# ################################################
# def ha(l: ReadRepository):
#     l.get_all()


# # type function pun akan ada error
# ha(l=FundManagerRepository())
