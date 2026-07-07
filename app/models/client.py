#app.models.category

from datetime import datetime

from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, func, Integer
from sqlalchemy.dialects.postgresql import ARRAY

class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    client_id : Mapped[str] = mapped_column(String(255), nullable=False)

    subscribed_topic : Mapped[list[str]] = mapped_column(ARRAY(String(50)), nullable=False, default=list)

    qos : Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column( DateTime(timezone=True), server_default=func.now(), nullable=False)

    last_seen_at : Mapped[datetime] = mapped_column( DateTime(timezone=True), server_default=func.now(), nullable=False)

    is_active : Mapped[str] = mapped_column(String(255), nullable=False)

