from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class FilmSchemaBase(BaseModel):
    slug: str
    title: str
    description: str
    budget: int
    box_office: int


class FilmSchemaCreate(FilmSchemaBase):
    slug: Annotated[str, Len(3, 100)]


class FilmSchema(FilmSchemaBase): ...
