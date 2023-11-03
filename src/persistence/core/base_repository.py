from fastapi import Depends
from infrastructure.database import get_session
from sqlalchemy.orm import Session


class BaseRepository:
    """
    All Repository class should inherit from BaseRepository
    """

    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        self.session = session
