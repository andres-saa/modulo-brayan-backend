"""Añadiendo campos a la tabla de productos

Revision ID: 9bf4e5180263
Revises: 6191bcd08438
Create Date: 2023-11-16 22:29:44.772354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bf4e5180263'
down_revision: Union[str, None] = '6191bcd08438'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
