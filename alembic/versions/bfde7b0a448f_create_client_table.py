"""create client table

Revision ID: bfde7b0a448f
Revises: 84be61b4efa5
Create Date: 2026-07-08 17:39:40.298399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = 'bfde7b0a448f'
down_revision: Union[str, Sequence[str], None] = '84be61b4efa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "clients",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("client_id", sa.String(length=255), nullable=False),
        sa.Column("subscribed_topic", postgresql.ARRAY(sa.String(length=50)), nullable=False),
        sa.Column("qos", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("last_seen_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("is_active", sa.Boolean(),  server_default=sa.text("true"), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table("clients")
    pass
