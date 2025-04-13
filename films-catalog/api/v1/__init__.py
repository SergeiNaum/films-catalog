from fastapi import APIRouter

from api.v1.films.views import router as films_router

router = APIRouter(
    prefix="/api_v1",
)


router.include_router(films_router)
