import logging

import uvicorn
from api import router as api_router
from app_lifespan import lifespan
from fastapi import (
    FastAPI,
    Request,
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Films App",
    lifespan=lifespan,
)
app.include_router(api_router)


@app.get("/")
async def hello_world(request: Request):
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "docs": str(docs_url),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
