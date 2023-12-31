"""User model fields updated

Revision ID: cd9114f00135
Revises: 4f5543d6e484
Create Date: 2023-08-11 16:46:01.806954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd9114f00135'
down_revision: Union[str, None] = '4f5543d6e484'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
