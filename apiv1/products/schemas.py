from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: str
    date: datetime


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    name: str | None = None
    description: str | None = None
    date: datetime | None = None


class Product(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )  # указываем что нужно брать свойства из атрибутов через - configdict
    id: int
