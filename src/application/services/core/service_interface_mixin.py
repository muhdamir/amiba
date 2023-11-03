from abc import ABC, abstractmethod
from typing import Generic, TypeVar

PostData = TypeVar("PostData")
PatchData = TypeVar("PatchData")


class ReadServiceInterfaceMixin(
    ABC,
):
    """
    If `Read` service needed, include this mixin in the interface class such that:
    >>> class AServiceInterface(
    ...     ReadServiceInterfaceMixin
    ... ):
    ...     pass
    """

    @abstractmethod
    def get_by_id(self, id: int):
        ...

    @abstractmethod
    def get_all(self):
        ...


class CreateServiceInterfaceMixin(
    ABC,
    Generic[PostData],
):
    """
    If `Create` service needed, include this mixin in the interface class such that:
    >>> class AServiceInterface(
    ...     CreateServiceInterfaceMixin[APostData],
    ... ):
    ...     pass
    """

    @abstractmethod
    def create(self, data: PostData):
        ...


class UpdateServiceInterfaceMixin(
    ABC,
    Generic[PatchData],
):
    """
    If `Update` service needed, include this mixin in the interface class such that:
    >>> class AServiceInterface(
    ...     UpdateServiceInterfaceMixin[APatchData],
    ... ):
    ...     pass
    """

    @abstractmethod
    def update(self, id: int, data: PatchData):
        ...


class DeleteServiceInterfaceMixin(
    ABC,
):
    """
    If `Delete` service needed, include this mixin in the interface class such that:
    >>> class AServiceInterface(
    ...     DeleteServiceInterfaceMixin,
    ... ):
    ...     pass
    """

    @abstractmethod
    def delete(self, id: int):
        ...


class CRUDServiceInterfaceMixin(
    DeleteServiceInterfaceMixin,
    UpdateServiceInterfaceMixin[PatchData],
    ReadServiceInterfaceMixin,
    CreateServiceInterfaceMixin[PostData],
    Generic[PostData, PatchData],
):
    """
    If `CRUD` service needed, include this mixin in the interface class such that:
    >>> class AServiceInterface(
    ...     CRUDServiceInterfaceMixin[APostData, APatchData],
    ... ):
    ...     pass
    """

    pass
