from typing import Annotated

from fastapi import APIRouter, Depends, status
from schemas.film import FilmSchema, FilmSchemaUpdate

from api.v1.films.crud import film_storage
from api.v1.films.dependencies.utils import get_film_by_slug

FILM_BY_SLUG = Annotated[FilmSchema, Depends(get_film_by_slug)]


router = APIRouter(
    prefix="/{movie_slug}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Film not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Film 'slug' not found",
                    },
                },
            },
        },
    },
)


@router.get("/")
async def get_film_details(film: FILM_BY_SLUG) -> FilmSchema | None:
    return film


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_film(film: FILM_BY_SLUG) -> None:
    film_storage.delete(film)


@router.put("/")
async def update_film(film: FILM_BY_SLUG, film_in: FilmSchemaUpdate) -> FilmSchema:
    return film_storage.update(film_schema=film, film_schema_in=film_in)
