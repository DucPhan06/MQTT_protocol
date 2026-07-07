#app.models.category

from sqlalchemy import ARRAY, String

from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name : Mapped[str] = mapped_column(String(255), nullable=False)

    topic : Mapped[str] = mapped_column(String(255), nullable=False)

    articles = relationship(
        "Article",
        secondary="article_categories",
        back_populates="categories",
    )

