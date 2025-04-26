import json
import logging

import aiofiles
from core.config import FILM_STORAGE_FILEPATH
from pydantic import BaseModel, Field, ValidationError
from schemas.film import (
    FilmSchema,
    FilmSchemaCreate,
    FilmSchemaPartialUpdate,
    FilmSchemaUpdate,
)

logger = logging.getLogger(__name__)


class FilmStorage(BaseModel):
    slug_to_film: dict[str, FilmSchema] = Field(default_factory=dict)

    def get(self) -> list[FilmSchema]:
        return list(self.slug_to_film.values())

    def get_by_slug(self, slug: str) -> FilmSchema | None:
        return self.slug_to_film.get(slug)

    async def create(self, film_schema_create: FilmSchemaCreate):
        film = FilmSchema(**film_schema_create.model_dump())
        self.slug_to_film[film.slug] = film
        logger.info("Created film %s", film.title)
        return film

    async def delete_by_slug(self, slug: str) -> FilmSchema | None:
        self.slug_to_film.pop(slug, None)

    async def delete(self, film_schema: FilmSchema):
        await self.delete_by_slug(slug=film_schema.slug)
        logger.info("Deleted film %s", film_schema.title)

    async def update(
        self,
        film_schema: FilmSchema,
        film_schema_in: FilmSchemaUpdate,
    ) -> FilmSchema:
        for field_name, value in film_schema_in:
            setattr(film_schema, field_name, value)
        logger.info("updated film %s", film_schema.title)
        return film_schema

    async def partial_update(
        self,
        film_schema: FilmSchema,
        film_schema_in: FilmSchemaPartialUpdate,
    ) -> FilmSchema:
        for field_name, value in film_schema_in.model_dump(exclude_unset=True).items():
            setattr(film_schema, field_name, value)

        logger.info("partial update film %s", film_schema.title)
        return film_schema

    @classmethod
    async def load_from_json(cls) -> "FilmStorage":
        file_path = FILM_STORAGE_FILEPATH
        if not file_path.exists():
            logger.info("json_db_file doesn't exist")
            return FilmStorage()

        async with aiofiles.open(file_path) as file:
            json_data = await file.read()
            if not json_data.strip():  # Проверка на пустой файл
                return FilmStorage()

            raw_data = json.loads(json_data)
            logger.info("loaded films from json_db_file")
            return cls.model_validate(raw_data)

    async def save_state_to_json(self) -> None:
        async with aiofiles.open(FILM_STORAGE_FILEPATH, "w") as file:
            logger.info("saved films from json_db_file")
            await file.write(self.model_dump_json(indent=2))

    async def init_storage_from_state(self) -> None:
        try:
            data = await FilmStorage.load_from_json()
        except ValidationError:
            logger.warning("Rewritten storage file due to validation error.")
            return

        self.slug_to_film.update(data.slug_to_film)
        logger.warning("Recovered data from storage file.")


film_storage = FilmStorage()
