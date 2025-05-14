from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, DateTime
from datetime import datetime
from typing import Optional

from .base import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text())
    date: Mapped[Optional[datetime]] = mapped_column(DateTime(), nullable=True)
