from typing import Annotated

from fastapi import APIRouter, Depends, status
from schemas.film import FilmSchema

from api.v1.films.crud import film_storage
from api.v1.films.dependencies.utils import get_film_by_slug

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
async def get_film_details(
    movie: Annotated[
        get_film_by_slug,
        Depends(get_film_by_slug),
    ],
) -> FilmSchema | None:
    return movie


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_film(film: Annotated[FilmSchema, Depends(get_film_by_slug)]) -> None:
    film_storage.delete(film)
