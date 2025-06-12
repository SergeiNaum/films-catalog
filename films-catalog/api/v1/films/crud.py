import logging

from pydantic import BaseModel, Field
from schemas.film import (
    FilmSchema,
    FilmSchemaCreate,
    FilmSchemaPartialUpdate,
    FilmSchemaUpdate,
)

from api.v1.auth.services.redis_film_storage_helper import redis_films_storage

logger = logging.getLogger(__name__)


class MovieBaseError(Exception):
    """Base exception for film-catalog CRUD"""


class MovieAlreadyExistsError(MovieBaseError):
    """Raised on FILM created if such slugalredy exists"""


class FilmStorage(BaseModel):
    slug_to_film: dict[str, FilmSchema] = Field(default_factory=dict)

    def get(self) -> list[FilmSchema]:
        return [FilmSchema.model_validate_json(data) for data in redis_films_storage.get_all_films()]

    def get_by_slug(self, slug: str) -> FilmSchema | None:
        if data := redis_films_storage.get_film_details(slug):
            return FilmSchema.model_validate_json(data)

    def exists(self, slug: str) -> bool:
        return redis_films_storage.film_exists(slug)

    async def create_or_raise_if_not_exists(self, film_schema_create: FilmSchemaCreate):
        if not self.exists(film_schema_create.slug):
            return await film_storage.create(film_schema_create)
        raise MovieAlreadyExistsError(film_schema_create.slug)

    async def create(self, film_schema_create: FilmSchemaCreate):
        film = FilmSchema(**film_schema_create.model_dump())
        redis_films_storage.add_film(film)
        logger.info("Created film %s", film.title)
        return film

    async def delete_by_slug(self, slug: str) -> FilmSchema | None:
        redis_films_storage.delete_film(slug)

    async def delete(self, slug: str):
        await self.delete_by_slug(slug=slug)
        logger.info("Deleted film with slug %s", slug)

    async def update(
        self,
        film_schema: FilmSchema,
        film_schema_in: FilmSchemaUpdate,
    ) -> FilmSchema:
        for field_name, value in film_schema_in:
            setattr(film_schema, field_name, value)
        redis_films_storage.add_film(film_schema)
        logger.info("updated film %s", film_schema.title)
        return film_schema

    async def partial_update(
        self,
        film_schema: FilmSchema,
        film_schema_in: FilmSchemaPartialUpdate,
    ) -> FilmSchema:
        for field_name, value in film_schema_in.model_dump(exclude_unset=True).items():
            setattr(film_schema, field_name, value)
        redis_films_storage.add_film(film_schema)
        logger.info("partial update film %s", film_schema.title)
        return film_schema


film_storage = FilmStorage()
