from schemas.film import FilmSchema


def get_film_by_id(movie_id: int, films: list[FilmSchema]) -> FilmSchema | None:
    return next((film for film in films if movie_id == film.id), None)
