from fastapi import HTTPException, status

from api.v1.films.crud import film_storage
from schemas.film import FilmSchema


def get_film_by_slug(slug: str) -> FilmSchema | None:
    film: FilmSchema | None = film_storage.get_by_slug(slug)
    if film:
        return film
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")
