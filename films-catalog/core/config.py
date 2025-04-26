import logging
from pathlib import Path

# /home/naum/PycharmProjects/films-catalog/films-catalog/core/config.py
BASE_DIR = Path(__file__).resolve().parents[2]
FILM_STORAGE_FILEPATH = BASE_DIR / "json_db.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
