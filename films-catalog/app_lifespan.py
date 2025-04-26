import logging
from contextlib import asynccontextmanager

from api.v1.films.crud import film_storage
from core import config
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
    await film_storage.init_storage_from_state()
    yield  # Здесь приложение работает
