from fastapi import APIRouter, status
from schemas.film import FilmSchema, FilmSchemaCreate, FilmSchemaRead

from api.v1.films.crud import film_storage

router = APIRouter(
    prefix="/films",
    tags=["Films"],
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
async def create_film(film_create: FilmSchemaCreate) -> FilmSchema:
    return await film_storage.create(film_create)
