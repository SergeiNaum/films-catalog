import random
from typing import Annotated

from annotated_types import Len
from fastapi import APIRouter, status, Depends

from api.v1.films.dependencies.utils import get_film_by_slug
from api.v1.films.crud import film_storage
from schemas.film import FilmSchema, FilmSchemaCreate

router = APIRouter(
    prefix="/films",
    tags=["Films"],
)


@router.get("/all/")
async def get_films() -> list[FilmSchema]:
    return film_storage.get()


@router.get("/{movie_slug}")
async def get_film_details(
    movie: Annotated[
        get_film_by_slug,
        Depends(get_film_by_slug),
    ],
) -> FilmSchema | None:
    return movie


@router.post(
    "/",
    response_model=FilmSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_film(film_create: FilmSchemaCreate) -> FilmSchema:
    obj = film_storage.create(film_create)
    return obj
