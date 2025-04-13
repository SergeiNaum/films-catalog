from fastapi import APIRouter

from api.v1.films.dependencies.utils import get_film_by_id
from api.v1.films.crud import FILMS
from schemas.film import FilmSchema


router = APIRouter(
    prefix="/films",
    tags=["Films"],
)


@router.get("/all/")
async def get_films() -> list[FilmSchema]:
    return FILMS


@router.get("/{movie_id}")
async def get_film_detail(
    movie_id: int,
) -> FilmSchema | None:
    return get_film_by_id(movie_id, FILMS)
