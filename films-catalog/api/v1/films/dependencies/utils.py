from fastapi import HTTPException, status

from schemas.film import FilmSchema


def get_film_by_id(movie_id: int, films: list[FilmSchema]) -> FilmSchema | None:
    film = next((film for film in films if movie_id == film.id), None)
    if film:
        return film
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")
