from typing import Any, Generic, TypeVar

from faker import Faker
from sqlalchemy.orm import Session

from domain.entities import Base, Fund, FundManager, FundNetAssetValueData

fake = Faker()

Entity = TypeVar("Entity", bound=Base)


class BaseFactory(Generic[Entity]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_entry(self, entry: Entity) -> Entity:
        self.session.add(entry)
        self.session.commit()
        self.session.refresh(entry)
        return entry


class FactoryFundManager(
    BaseFactory[FundManager],
):
    def __init__(self, session: Session) -> None:
        self.fund_manager = FundManager()
        self.fund_manager.fund_manager_email = fake.name()
        self.fund_manager.fund_manager_name = fake.name()
        super().__init__(session=session)

    def __call__(self) -> FundManager:
        return self.create_entry(entry=self.fund_manager)


class FactoryFund(
    BaseFactory[Fund],
):
    def __init__(
        self,
        fund_manager_id: int,
        session: Session,
    ) -> None:
        self.fund = Fund()
        self.fund.fund_description = fake.text()
        self.fund.fund_manager_id = fund_manager_id
        self.fund.fund_name = fake.name()
        self.fund.fund_performance = fake.pyfloat()
        self.session = session

    def __call__(self) -> Fund:
        return self.create_entry(entry=self.fund)
