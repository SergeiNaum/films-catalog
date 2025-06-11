import logging
from contextlib import asynccontextmanager

from core import config
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
    yield  # Здесь приложение работает
