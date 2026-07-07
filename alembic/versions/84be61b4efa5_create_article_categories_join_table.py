"""create article categories join table

Revision ID: 84be61b4efa5
Revises: 5a7bf0b102b2
Create Date: 2026-07-07 19:00:46.690076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84be61b4efa5'
down_revision: Union[str, Sequence[str], None] = '5a7bf0b102b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("topic", sa.String(length=255), nullable=False, unique=True),
    )

    op.create_table(
        "article_categories",
        sa.Column("article_id", sa.Integer(), sa.ForeignKey("articles.id"), primary_key=True),
        sa.Column("category_id", sa.Integer(), sa.ForeignKey("categories.id"), primary_key=True),
    )


def downgrade() -> None:
    op.drop_table("article_categories")
    op.drop_table("categories")
