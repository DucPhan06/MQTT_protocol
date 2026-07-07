"""remove categories column from articles

Revision ID: 5a7bf0b102b2
Revises: c07aa2193a02
Create Date: 2026-07-07 18:37:01.310667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '5a7bf0b102b2'
down_revision: Union[str, Sequence[str], None] = 'c07aa2193a02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("articles", "categories")


def downgrade() -> None:
    op.add_column(
        "articles",
        sa.Column("categories", postgresql.ARRAY(sa.String(length=50)), nullable=True)
    )
