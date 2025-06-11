from core import config
from redis import Redis

from api.v1.auth.services.users_helper import BaseUsersHelper


class RedisUsersHelper(BaseUsersHelper):
    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        users_set_name: str,
        decode_responses: bool = True,
    ) -> None:
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=decode_responses,
        )
        self.users_set_name = users_set_name

    def get_user_password(
        self,
        username: str,
    ) -> str | None:
        """
        По переданному юзернейму находит пароль.

        Возвращает пароль если есть.

        :param username: - имя пользователя
        :return: пароль по пользователю, если найден
        """
        return self.redis.hget(self.users_set_name, username)

    def add_user(self, username: str, password: str) -> None:
        self.redis.hset(self.users_set_name, username, password)


redis_users = RedisUsersHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_USERS,
    users_set_name=config.REDIS_USERS_SET_NAME,
)
