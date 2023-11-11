from typing import Generic, Protocol, Sequence, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.entities import Base


class Repository(Protocol):
    """
    Protocol class for repository.
    Mixin class should refer this class as type hint.
    """

    session: Session


Entity = TypeVar("Entity", bound=Base)


class ReadRepositoryMixin(Generic[Entity]):
    """
    Add ReadRepositoryMixin to have access to common `Read` operation functions.
    >>> class ARepository(
    ...     ReadRepositoryMixin[AnEntity],
    ...     ARepositoryInterface,
    ... ):
    ...     # example 1
    ...     def get_by_id(self, id:int):
    ...         return self._get_by_id(entity=AnEntity, id=id)
    """

    def _get_by_id(
        self: Repository,
        entity: type[Entity],
        id: int,
    ) -> Entity | None:
        return self.session.get(entity=entity, ident=id)

    def _get_all(
        self: Repository,
        entity: type[Entity],
    ) -> Sequence[Entity]:
        return self.session.scalars(select(entity)).all()


class CreateRepositoryMixin(Generic[Entity]):
    """
    Add ReadRepositoryMixin to have access to common `Create` operation function.
    >>> class ARepository(
    ...     CreateRepositoryMixin[AnEntity],
    ...     ARepositoryInterface,
    ... ):
    ...     # example 1
    ...     def create(self, data:dict):
    ...         return self._create(entity=AnEntity, data=data)
    """

    def _create(
        self: Repository,
        entity: type[Entity],
        data: dict,
    ) -> Entity:
        new_entry = entity(**data)
        self.session.add(new_entry)
        self.session.commit()
        self.session.refresh(new_entry)
        return new_entry


class UpdateRepositoryMixin(Generic[Entity]):
    """
    Add ReadRepositoryMixin to have access to common `Update` operation function.
    >>> class ARepository(
    ...     UpdateRepositoryMixin[AnEntity],
    ...     ARepositoryInterface,
    ... ):
    ...     # example 1
    ...     def update(self, id:int, data:dict):
    ...         return self._update(entity=AnEntity, data=data)
    """

    def _update(
        self: Repository,
        entity: type[Entity],
        id: int,
        data: dict,
    ) -> Entity | None:
        target_entry = self.session.get(entity=entity, ident=id)

        if not target_entry:
            return target_entry

        for field, value in data.items():
            setattr(target_entry, field, value)

        self.session.commit()
        self.session.refresh(target_entry)
        return target_entry


class DeleteRepositoryMixin(Generic[Entity]):
    """
    Add DeleteRepositoryMixin to have access to common `Delete` operation function.
    >>> class ARepository(
    ...     DeleteRepositoryMixin[AnEntity],
    ...     ARepositoryInterface,
    ... ):
    ...     # example 1
    ...     def delete(self, id:int):
    ...         return self._delete(entity=AnEntity, id=id)
    """

    def _delete(
        self: Repository,
        entity: type[Entity],
        id: int,
    ) -> bool:
        target_entry = self.session.get(entity=entity, ident=id)

        if not target_entry:
            return False

        self.session.delete(target_entry)
        return True


class CRUDRepositoryMixin(
    DeleteRepositoryMixin[Entity],
    UpdateRepositoryMixin[Entity],
    ReadRepositoryMixin[Entity],
    CreateRepositoryMixin[Entity],
    Generic[Entity],
):
    """
    Add CRUDRepositoryMixin to have access to common `CRUD` operation functions.
    >>> class ARepository(
    ...     CRUDRepositoryMixin[AnEntity],
    ...     ARepositoryInterface,
    ... ):
    ...     # example 1
    ...     def delete(self, id:int):
    ...         return self._delete(entity=AnEntity, id=id)
    """
