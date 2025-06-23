import logging

import uvicorn
from api import router as api_router
from api.main_views import router as main_router
from app_lifespan import lifespan
from fastapi import (
    FastAPI,
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Films App",
    lifespan=lifespan,
)
app.include_router(api_router)
app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
