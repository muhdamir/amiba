from typing import Generic, TypeVar, Protocol, ClassVar
from domain.interfaces.core import (
    CRUDRepositoryInterfaceMixin,
    CreateRepositoryInterfaceMixin,
    DeleteRepositoryInterfaceMixin,
    ReadRepositoryInterfaceMixin,
    UpdateRepositoryInterfaceMixin,
)
from application.models.core import BasePatchModel, BasePostModel

Entity = TypeVar("Entity")
PostData = TypeVar("PostData", bound=BasePostModel)
PatchData = TypeVar("PatchData", bound=BasePatchModel)

# Repository[Entity] = TypeVar(
#     "Repository[Entity]",
#     CRUDRepositoryInterfaceMixin[Entity],
#     ReadRepositoryInterfaceMixin[Entity],
#     # covariant=True
# )
Repository = CRUDRepositoryInterfaceMixin[Entity] | ReadRepositoryInterfaceMixin[Entity]


class Service(Protocol, Generic[Entity]):
    repository: Repository[Entity]


class ReadService(Generic[Entity]):
    def _get_by_id(self: Service[Entity], id: int):
        return self.repository.get_by_id(id=id)

    def _get_all(self: Service[Entity]):
        return self.repository.get_all()

    def _create(self: Service[Entity], data: PostData):
        dict_data = data.model_dump()
        return self.repository.create(data=dict_data)

    def _update(self: Service[Entity], id: int, data: PatchData):
        dict_data = data.model_dump(exclude_unset=True)
        return self.repository.update(id=id, data=dict_data)

    def _delete(self: Service[Entity], id: int):
        return self.repository.delete(id=id)
