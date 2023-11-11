from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar

Entity = TypeVar("Entity")


class ReadRepositoryInterfaceMixin(
    ABC,
    Generic[Entity],
):
    """
    If `Read` operation needed, include this mixin in the interface class such that:
    >>> class ARepositoryInterface(
    ...     ReadRepositoryInterfaceMixin[AnEntity]
    ... ):
    ...     pass
    """

    @abstractmethod
    def get_by_id(self, id: int) -> Entity | None:
        ...

    @abstractmethod
    def get_all(self) -> Sequence[Entity]:
        ...


class CreateRepositoryInterfaceMixin(
    ABC,
    Generic[Entity],
):
    """
    If `Create` operation needed, include this mixin in the interface class such that:
    >>> class ARepositoryInterface(
    ...     CreateRepositoryInterfaceMixin[AnEntity]
    ... ):
    ...     pass
    """

    @abstractmethod
    def create(self, data: dict) -> Entity:
        ...


class UpdateRepositoryInterfaceMixin(
    ABC,
    Generic[Entity],
):
    """
    If `Update` operation needed, include this mixin in the interface class such that:
    >>> class ARepositoryInterface(
    ...     UpdateRepositoryInterfaceMixin[AnEntity]
    ... ):
    ...     pass
    """

    @abstractmethod
    def update(self, id: int, data: dict) -> Entity | None:
        ...


class DeleteRepositoryInterfaceMixin(
    ABC,
    Generic[Entity],
):
    """
    If `Delete` operation needed, include this mixin in the interface class such that:
    >>> class ARepositoryInterface(
    ...     DeleteRepositoryInterfaceMixin[AnEntity]
    ... ):
    ...     pass
    """

    @abstractmethod
    def delete(self, id: int) -> bool:
        ...


class CRUDRepositoryInterfaceMixin(
    CreateRepositoryInterfaceMixin[Entity],
    ReadRepositoryInterfaceMixin[Entity],
    UpdateRepositoryInterfaceMixin[Entity],
    DeleteRepositoryInterfaceMixin[Entity],
    Generic[Entity],
):
    """
    If all `CRUD` operation needed, include this mixin in the interface class such that:
    >>> class ARepositoryInterface(
    ...     GenericCRUDRepositoryInterface[AnEntity]
    ... ):
    ...     pass
    """

    pass
