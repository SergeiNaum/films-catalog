from os import getenv

import pytest
import pytest_asyncio
from _pytest.fixtures import SubRequest
from schemas.film import FilmSchema

from testing.helpers import build_film_create

if getenv("TESTING") != "1":
    pytest.exit(
        "Environment is not ready for testing",
    )


@pytest_asyncio.fixture(
    params=[
        "slug",
        "test-slug",
        pytest.param("a" * 3, id="minimal-slug"),
        pytest.param("a" * 12, id="max-slug"),
    ]
)
async def film(request: SubRequest) -> FilmSchema:
    return await build_film_create(request.param)
