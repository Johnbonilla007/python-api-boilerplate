"""Adding email to user table

Revision ID: 7126f7d9ccbe
Revises: 1402f3402408
Create Date: 2025-02-24 12:00:44.864980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7126f7d9ccbe'
down_revision: Union[str, None] = '1402f3402408'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_index('ix_users_password', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__users__3213E83FD62FC6BF')
    )
    op.create_index('ix_users_password', 'users', ['password'], unique=False)
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
