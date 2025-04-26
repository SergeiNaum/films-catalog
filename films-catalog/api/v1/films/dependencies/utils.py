import logging

from fastapi import HTTPException, status, BackgroundTasks
from schemas.film import FilmSchema

from api.v1.films.crud import film_storage

logger = logging.getLogger(__name__)


async def get_film_by_slug(slug: str) -> FilmSchema | None:
    film: FilmSchema | None = film_storage.get_by_slug(slug)
    if film:
        return film
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")


async def add_background_task(background_task: BackgroundTasks):
    yield
    logger.info("adding background task")
    background_task.add_task(film_storage.save_state_to_json)
