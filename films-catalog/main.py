import uvicorn
from fastapi import (
    FastAPI,
    Request,
)

app = FastAPI(
    title="Films App",
)


@app.get("/")
async def hello_world(request: Request):
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "docs": str(docs_url),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
