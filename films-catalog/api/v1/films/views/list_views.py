from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from schemas.film import FilmSchema, FilmSchemaCreate, FilmSchemaRead

from api.v1.films.crud import MovieAlreadyExistsError, film_storage
from api.v1.films.dependencies.utils import (
    api_token_or_user_basic_auth_required_for_unsafe_methods,
)

router = APIRouter(
    prefix="/films",
    tags=["Films"],
    dependencies=[Depends(api_token_or_user_basic_auth_required_for_unsafe_methods)],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthenticated. Only for unsafe methods.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid API token",
                    },
                },
            },
        },
    },
)


@router.get(
    "/all/",
    response_model=list[FilmSchemaRead],
)
async def get_films() -> list[FilmSchema] | Any:
    return film_storage.get()


@router.post(
    "/",
    response_model=FilmSchemaRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "A film with such slug already exists.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "film with slug='name' already exists.",
                    },
                },
            },
        },
    },
)
async def create_film(
    film_create: FilmSchemaCreate,
) -> FilmSchema:
    try:
        return await film_storage.create_or_raise_if_not_exists(film_create)
    except MovieAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"film with this slug: {film_create.slug} already exist",
        ) from None
