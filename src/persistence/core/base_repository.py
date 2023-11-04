from fastapi import Depends
from sqlalchemy.orm import Session

from infrastructure.database import get_session

from .repository_mixin import Repository


class BaseRepository:
    """
    All Repository class should inherit from BaseRepository
    """

    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        self.session = session

    @classmethod
    def from_existing_repository(cls, repository: Repository):
        """
        Use this class method when we need
        to instiate a repository class using
        other repository object's session

        eg:
        >>> class AService:
        ...     def __init__(
        ...         self,
        ...         repository: ARepository = Depends(),
        ...     ) -> None:
        ...         self.repository = repository
        ...         self.other_repository = AnotherRepository.from_existing_repository(repository)
        """
        return cls(repository.session)
