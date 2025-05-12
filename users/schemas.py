from pydantic import BaseModel, EmailStr,Field
from typing import Annotated
from annotated_types import MinLen,MaxLen


class CreateUser(BaseModel):
    #username: str = Field(...,min_length=13,max_length=30) - старый метод
    username: Annotated[str, MinLen(5), MaxLen(30)] # - новый метод
    email: EmailStr