import random
import string
from typing import Any

import pytest
import pytest_asyncio
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient
from main import app
from schemas.film import FilmSchemaCreate

from testing.helpers import build_film_create_random_slug


def test_create_film(auth_client: TestClient) -> None:
    url = app.url_path_for("create_film")
    data = FilmSchemaCreate(
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
    ).model_dump(mode="json")
    response = auth_client.post(url, json=data)

    assert response.status_code == status.HTTP_201_CREATED, data


class TestCreateInvalid:
    @pytest.fixture(
        params=[
            pytest.param(("a", "string_too_short"), id="too-short-slug"),
            pytest.param(("a" * 13, "string_too_long"), id="to-long-slug"),
        ]
    )
    def movie_create_values(self, request: SubRequest) -> tuple[dict[str, Any], str]:
        build = build_film_create_random_slug()
        data = build.model_dump(mode="json")
        slug, err_type = request.param
        data["slug"] = slug
        return data, err_type

    def test_invalid_slug(
        self, movie_create_values: FilmSchemaCreate, auth_client: TestClient
    ) -> None:
        url = app.url_path_for("create_film")
        create_data, expected_error_type = movie_create_values
        response = auth_client.post(url, json=create_data)

        assert (
            response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        ), response.text
        error_detail = response.json()["detail"][0]
        assert error_detail["type"] == expected_error_type

    def test_create_movie_already_exists(self, auth_client: TestClient) -> None:
        url = app.url_path_for("create_film")
        data = FilmSchemaCreate(
            slug="Aliens2",
            title="Aliens2",
            description="0",
            budget=0,
            box_office=0,
        ).model_dump()

        response = auth_client.post(url, json=data)

        assert response.status_code == status.HTTP_409_CONFLICT, data
        response_data = response.json()
        expected_error_detail = f"film with this slug: {data.get('slug')} already exist"
        assert response_data["detail"] == expected_error_detail, response_data
