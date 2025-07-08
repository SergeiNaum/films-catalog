import pytest
from api.v1.films.crud import film_storage
from fastapi import status
from fastapi.testclient import TestClient
from main import app
from schemas.film import FilmSchema


@pytest.mark.asyncio
async def test_delete(film: FilmSchema, auth_client: TestClient) -> None:
    url = app.url_path_for("delete_film", movie_slug=film.slug)

    response = auth_client.delete(url, params={"film": film.slug})
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text
    assert not film_storage.exists(film.slug)
