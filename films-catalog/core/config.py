import logging
from pathlib import Path

# /home/naum/PycharmProjects/films-catalog/films-catalog/core/config.py
BASE_DIR = Path(__file__).resolve().parents[2]
FILM_STORAGE_FILEPATH = BASE_DIR / "json_db.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


# Never store real tokens here!
# Only fake values

# Only for demo!
# no real users in code!!
# USERS_DB: dict[str, str] = {
#     # username: password
#     "sam": "password",
#     "bob": "qwerty",
# }


REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_DB_TOKENS = 1
REDIS_DB_USERS = 2
REDIS_TOKENS_SET_NAME = "tokens"
REDIS_USERS_SET_NAME = "users"
