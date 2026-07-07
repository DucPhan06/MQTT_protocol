#app.models.article.py

#python describes table

from datetime import datetime

from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY

class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    article_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)

    title: Mapped[str] = mapped_column(Text, nullable=False)

    link: Mapped[str] = mapped_column(Text, nullable=False)

    source_name: Mapped[str] = mapped_column(String(255), nullable=False)

    source_id: Mapped[str] = mapped_column(String(255), nullable=True)

    #TODO: create tables according to categories
    categories: Mapped[list[str]] = mapped_column(ARRAY(String(50)), nullable=False, default=list)

    language: Mapped[list[str]] = mapped_column(ARRAY(String(50)), nullable=False, default=list)

    country: Mapped[list[str]] = mapped_column(ARRAY(String(50)), nullable=False, default=list)

    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    fetched_at: Mapped[datetime] = mapped_column( DateTime(timezone=True), server_default=func.now(), nullable=False)
