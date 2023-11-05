from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .fund_manager import FundManager
    from .fund_net_asset_value_data import FundNetAssetValueData


class Fund(Base):
    __tablename__ = "FUND"

    # fields
    fund_id: Mapped[int] = mapped_column(primary_key=True)
    fund_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    fund_manager_id: Mapped[int] = mapped_column(
        ForeignKey("FUND_MANAGER.fund_manager_id", ondelete="CASCADE"),
        nullable=False,
    )
    fund_description: Mapped[str] = mapped_column(nullable=False)
    fund_date_of_creation: Mapped[date] = mapped_column(
        nullable=False,
        default=func.current_date(),
    )
    fund_date_of_update: Mapped[date] = mapped_column(
        nullable=False,
        default=func.current_date(),
        onupdate=func.current_date(),
    )
    fund_performance: Mapped[float] = mapped_column(nullable=False)

    # relationships
    fund_manager: Mapped["FundManager"] = relationship()
    fund_net_asset_value: Mapped["FundNetAssetValueData"] = relationship()
