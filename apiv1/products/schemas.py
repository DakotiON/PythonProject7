from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: str
    date: datetime


class ProductCreate(BaseModel):
    pass


class Product(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )  # указываем что нужно брать свойства из атрибутов через - configdict
    id: int
