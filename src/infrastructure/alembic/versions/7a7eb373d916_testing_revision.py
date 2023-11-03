"""testing revision

Revision ID: 7a7eb373d916
Revises: 
Create Date: 2023-11-02 01:13:41.201240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a7eb373d916'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FUND_MANAGER',
    sa.Column('fund_manager_id', sa.Integer(), nullable=False),
    sa.Column('fund_manager_name', sa.String(), nullable=False),
    sa.Column('fund_manager_email', sa.String(), nullable=False),
    sa.Column('date_created_on', sa.Date(), nullable=False),
    sa.Column('date_updated_on', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('fund_manager_id')
    )
    op.create_table('FUND',
    sa.Column('fund_id', sa.Integer(), nullable=False),
    sa.Column('fund_name', sa.String(), nullable=False),
    sa.Column('fund_manager_id', sa.Integer(), nullable=False),
    sa.Column('fund_description', sa.String(), nullable=False),
    sa.Column('fund_net_asset_value', sa.Float(), nullable=False),
    sa.Column('fund_date_of_creation', sa.Date(), nullable=False),
    sa.Column('fund_date_of_update', sa.Date(), nullable=False),
    sa.Column('fund_performance', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['fund_manager_id'], ['FUND_MANAGER.fund_manager_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('fund_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FUND')
    op.drop_table('FUND_MANAGER')
    # ### end Alembic commands ###
