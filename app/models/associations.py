
from sqlalchemy import Column, ForeignKey, Table

from app.db.base import Base


article_categories = Table(
    "article_categories",
    Base.metadata,
    Column("article_id", ForeignKey("articles.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)