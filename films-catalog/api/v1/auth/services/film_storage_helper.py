from abc import ABC, abstractmethod
from typing import Any

from schemas.film import FilmSchema


class BaseBookStorageHelper(ABC):
    """
    Что мне нужно от обёртки?
    - Добавлять книгу в хранилище
    - Удалять книгу из хранилища
    - возвращать список всех книг из хранилища
    """

    @abstractmethod
    def add_film(
        self,
        film_schema: FilmSchema,
    ) -> None: ...

    @abstractmethod
    def delete_film(
        self,
        slug: str,
    ) -> None: ...

    @abstractmethod
    def get_all_films(self) -> list[Any]: ...
