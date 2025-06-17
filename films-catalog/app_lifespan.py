import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from core import config
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any]:
    logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
    yield  # Здесь приложение работает
