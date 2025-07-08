import random
import string

from api.v1.films.crud import film_storage
from schemas.film import FilmSchema, FilmSchemaCreate


def build_film_create(slug: str) -> FilmSchemaCreate:
    return FilmSchemaCreate(
        slug=slug,
        title="some Title",
        description="A short url",
        budget=500_000,
        box_office=600_000,
    )


async def film_create(slug: str) -> FilmSchema:
    film_in = build_film_create(slug=slug)

    return await film_storage.create(film_in)


def build_film_create_random_slug() -> FilmSchemaCreate:
    return build_film_create(
        slug="".join(
            random.choices(  # noqa S311
                string.ascii_letters,
                k=8,
            ),
        ),
    )


async def film_create_random_slug() -> FilmSchema:
    film_in = build_film_create_random_slug()
    return await film_storage.create(film_in)
