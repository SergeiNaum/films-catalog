import uvicorn
from fastapi import (
    FastAPI,
    Request,
)

from constants import FILMS
from schemas.film import FilmSchema

app = FastAPI(
    title="Films App",
)


@app.get("/")
async def hello_world(request: Request):
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "docs": str(docs_url),
    }


@app.get("/films/")
async def get_films() -> list[FilmSchema]:
    return FILMS


def get_film_by_id(movie_id: int, films: list[FilmSchema]) -> FilmSchema:
    return next((film for film in films if movie_id == film.id), None)


@app.get("/films/{movie_id}")
async def get_film_detail(
    movie_id: int,
) -> FilmSchema | None:
    return get_film_by_id(movie_id, FILMS)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
