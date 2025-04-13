from decimal import Decimal

from pydantic import BaseModel


class BaseFilmSchema(BaseModel):
    id: int
    title: str
    description: str


class FilmSchema(BaseFilmSchema):
    budget: int
    box_office: int
