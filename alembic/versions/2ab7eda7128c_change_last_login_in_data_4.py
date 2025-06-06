"""change last_login in data_4

Revision ID: 2ab7eda7128c
Revises: 5e832fe36980
Create Date: 2025-05-05 15:44:40.621659

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2ab7eda7128c'
down_revision: Union[str, None] = '5e832fe36980'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=postgresql.ENUM('admin', 'user', name='userrole'),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.String(),
               type_=postgresql.ENUM('admin', 'user', name='userrole'),
               existing_nullable=True)
    # ### end Alembic commands ###
