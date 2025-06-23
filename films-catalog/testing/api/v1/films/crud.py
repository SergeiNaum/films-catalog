import string
import random
from collections.abc import Generator, AsyncGenerator

import pytest
import pytest_asyncio

from api.v1.films.crud import film_storage, MovieAlreadyExistsError
from schemas.film import FilmSchema, FilmSchemaCreate


async def create_film() -> FilmSchema:
    short_url_in = FilmSchemaCreate(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            ),
        ),
        title="some Title",
        description="A short url",
        budget=500_000,
        box_office=600_000,
    )
    return await film_storage.create(short_url_in)


@pytest_asyncio.fixture
async def film() -> AsyncGenerator[FilmSchema]:
    film = await create_film()
    yield film
    await film_storage.delete(film.slug)


@pytest.mark.asyncio
async def test_create_or_rise_if_exists(film: FilmSchema) -> None:
    film_schema_create = FilmSchemaCreate(**film.model_dump())
    with pytest.raises(
        MovieAlreadyExistsError, match=film_schema_create.slug
    ) as exc_info:
        await film_storage.create_or_raise_if_not_exists(film_schema_create)
    assert exc_info.value.args[0] == film_schema_create.slug
