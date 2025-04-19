from fastapi import APIRouter, status
from schemas.film import FilmSchema, FilmSchemaCreate

from api.v1.films.crud import film_storage

router = APIRouter(
    prefix="/films",
    tags=["Films"],
)


@router.get("/all/")
async def get_films() -> list[FilmSchema]:
    return film_storage.get()


@router.post(
    "/",
    response_model=FilmSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_film(film_create: FilmSchemaCreate) -> FilmSchema:
    obj = film_storage.create(film_create)
    return obj
