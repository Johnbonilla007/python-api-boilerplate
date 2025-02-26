"""Merge heads

Revision ID: dc4d16b27aa6
Revises: 67a6feedd3e3, 6da2425e0f6a
Create Date: 2025-02-26 12:03:37.620707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc4d16b27aa6'
down_revision: Union[str, None] = ('67a6feedd3e3', '6da2425e0f6a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
