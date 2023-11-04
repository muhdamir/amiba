from infrastructure.database.config import engine
from domain.entities import Base
from sqlalchemy import Engine


class StartupEvent:
    """
    This class is the collection of all startup event
    """

    def __init__(
        self,
        base=Base,
        engine: Engine = engine,
    ) -> None:
        # db
        self._engine = engine
        self._base = base

    def __call__(self) -> None:
        print("AHAM CAPITAL SERVICE STARTED")

    def _create_table(self) -> None:
        self._base.metadata.create_all(bind=self._engine)
