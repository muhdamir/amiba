from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .fund import Fund


class FundManager(Base):
    __tablename__ = "FUND_MANAGER"

    # fields
    fund_manager_id: Mapped[int] = mapped_column(primary_key=True)
    fund_manager_name: Mapped[str] = mapped_column(nullable=False)
    fund_manager_email: Mapped[str] = mapped_column(nullable=False)
    date_created_on: Mapped[date] = mapped_column(default=func.current_date())
    date_updated_on: Mapped[date] = mapped_column(
        default=func.current_date(),
        onupdate=func.current_date(),
    )

    # relationships
    # when fund_manager is deleted, all child will be deleted
    # all, delete-orphan will deleted all child that is orphan (deassociated from its parent)
    funds: Mapped[list["Fund"]] = relationship(cascade="all, delete")
