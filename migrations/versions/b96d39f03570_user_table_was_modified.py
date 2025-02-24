"""User table was modified

Revision ID: b96d39f03570
Revises: a2329b0f5595
Create Date: 2025-02-24 12:23:33.097920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b96d39f03570'
down_revision: Union[str, None] = 'a2329b0f5595'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=True),
    sa.Column('Password', sa.String(length=255), nullable=True),
    sa.Column('Email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_index(op.f('ix_User_Email'), 'User', ['Email'], unique=True)
    op.create_index(op.f('ix_User_Id'), 'User', ['Id'], unique=False)
    op.create_index(op.f('ix_User_Name'), 'User', ['Name'], unique=False)
    op.create_index(op.f('ix_User_Password'), 'User', ['Password'], unique=False)
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
    sa.Column('email', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__users__3213E83F99FB696F')
    )
    op.create_index('ix_users_password', 'users', ['password'], unique=False)
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.drop_index(op.f('ix_User_Password'), table_name='User')
    op.drop_index(op.f('ix_User_Name'), table_name='User')
    op.drop_index(op.f('ix_User_Id'), table_name='User')
    op.drop_index(op.f('ix_User_Email'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###
