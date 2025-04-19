from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel

DescriptionStr = Annotated[str, MaxLen(200)]


class FilmSchemaBase(BaseModel):
    title: str
    description: DescriptionStr = ""
    budget: int
    box_office: int


class FilmSchemaCreate(FilmSchemaBase):
    """
    Модель для создания фильма
    """

    slug: Annotated[str, Len(3, 100)]


class FilmSchemaUpdate(FilmSchemaBase):
    """
    Модель для обновления информации о фильме
    """

    description: DescriptionStr


class FilmSchemaPartialUpdate(FilmSchemaBase):
    """
    Модель для частичного обновления информации
    о фильме
    """

    budget: int | None = None
    box_office: int | None = None
    title: str | None = None
    description: DescriptionStr | None = None


class FilmSchema(FilmSchemaBase):
    """Модель фильма"""

    slug: str
