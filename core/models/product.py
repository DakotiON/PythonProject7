from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, DateTime, ForeignKey, String
from datetime import datetime
from typing import Optional

from .base import Base
from .mixins import UserRelationMixins

if TYPE_CHECKING:
    from .user import User


class Product(UserRelationMixins, Base):
    __tablename__ = "products"

    _user_back_populates = "products"

    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    date: Mapped[Optional[datetime]] = mapped_column(DateTime(), nullable=True)
