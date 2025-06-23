from fastapi import APIRouter, Request


router = APIRouter()


@router.get("/")
async def hello_world(request: Request) -> dict[str, str]:
    docs_url = request.url.replace(path="/docs", query="")
    return {
        "docs": str(docs_url),
    }
