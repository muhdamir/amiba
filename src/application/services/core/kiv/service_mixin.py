from typing import Generic, Protocol, TypeVar, Union, runtime_checkable, Any

from sqlalchemy.orm import Session

from application.models.core import BasePatchModel, BasePostModel


@runtime_checkable
class BaseRepository(Protocol):
    session: Session


@runtime_checkable
class ReadRepository(
    BaseRepository,
    Protocol,
):
    session: Session

    def get_all(self) -> Any:
        ...

    def get_by_id(self, id: int) -> Any:
        ...


@runtime_checkable
class CreateRepository(
    BaseRepository,
    Protocol,
):
    session: Session

    def create(self, data: dict) -> Any:
        ...


@runtime_checkable
class DeleteRepository(
    BaseRepository,
    Protocol,
):
    session: Session

    def delete(self, id: int) -> Any:
        ...


@runtime_checkable
class UpdateRepository(
    BaseRepository,
    Protocol,
):
    def update(self, id: int, data: dict) -> Any:
        ...


@runtime_checkable
class CRUDRepository(
    DeleteRepository,
    UpdateRepository,
    ReadRepository,
    CreateRepository,
    Protocol,
):
    pass


T = TypeVar(
    "T", bound=CreateRepository | ReadRepository | UpdateRepository | DeleteRepository
)


class Service(Protocol[T]):
    repository: T


class ReadServiceMixin(Generic[T]):
    def _get_all(self: Service[T]):
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


class CreateServiceMixin(Generic[T]):
    def _create(self: Service[T], data: dict):
        if isinstance(
            self.repository,
            (CreateRepository, CRUDRepository),
        ):
            return self.repository.create(data=data)
        raise Exception("Repository does not have Create operation functionality")


class UpdateServiceMixin(Generic[T]):
    def _update(self: Service[T], id: int, data: dict):
        if isinstance(
            self.repository,
            UpdateRepository,
        ):
            return self.repository.update(id=id, data=data)
        raise Exception("Repository does not have Update operation functionality")


class DeleteServiceMixin(Generic[T]):
    def _delete(self: Service[T], id: int):
        if isinstance(
            self.repository,
            DeleteRepository,
        ):
            return self.repository.delete(id=id)
        raise Exception("Repository does not have Delete operation functionality")
