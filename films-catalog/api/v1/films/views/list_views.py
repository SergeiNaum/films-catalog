from fastapi import APIRouter, Depends, status
from schemas.film import FilmSchema, FilmSchemaCreate, FilmSchemaRead

from api.v1.films.crud import film_storage
from api.v1.films.dependencies.utils import api_token_or_user_basic_auth_required_for_unsafe_methods

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
async def get_films() -> list[FilmSchema]:
    return film_storage.get()


@router.post(
    "/",
    response_model=FilmSchemaRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_film(
    film_create: FilmSchemaCreate,
) -> FilmSchema:
    return await film_storage.create(film_create)
