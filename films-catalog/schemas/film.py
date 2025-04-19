from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel


class FilmSchemaBase(BaseModel):
    title: str
    description: Annotated[str, MaxLen(200)] = ""
    budget: int
    box_office: int


class FilmSchemaCreate(FilmSchemaBase):
    slug: Annotated[str, Len(3, 100)]


class FilmSchemaUpdate(FilmSchemaBase):
    description: Annotated[str, MaxLen(200)]


class FilmSchema(FilmSchemaBase):
    slug: str
