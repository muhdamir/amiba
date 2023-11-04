from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .fund import Fund


class FundNetAssetValue(Base):
    __tablename__ = "FUND_NET_ASSET_VALUE"

    # fields
    fund_nav_id: Mapped[int] = mapped_column(primary_key=True)
    fund_id: Mapped[int] = mapped_column(
        ForeignKey("FUND.fund_id", ondelete="CASCADE"),
        nullable=False,
    )
    fund_nav: Mapped[float] = mapped_column(nullable=False)
    fund_nav_date_of_creation: Mapped[datetime] = mapped_column(
        nullable=False,
        default=func.now(),
    )
    fund_nav_date_of_update: Mapped[datetime] = mapped_column(
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    # relationships
    fund: Mapped["Fund"] = relationship()
