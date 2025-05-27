import secrets
from abc import ABC, abstractmethod

from core import config
from redis import Redis


class BaseTokensHelper(ABC):
    """
    Что мне нужно от обёртки?
    - Проверять на наличие токены
    - Добавлять токен в хранилище
    - Удалять токен из хранилища
    - генерировать и добавлять токены в хранилище
    """

    @abstractmethod
    def token_exist(self, token: str) -> bool: ...

    @abstractmethod
    def add_token(self, token: str) -> None:
        "Save token in storage"
        ...

    @abstractmethod
    def delete_token(self, token: str) -> None:
        "Delete token"
        ...

    @classmethod
    def generate_token(cls) -> str:
        return secrets.token_urlsafe(16)

    def generate_and_save_token(self) -> str:
        token = self.generate_token()
        self.add_token(token)
        return token


class RedisTokensHelper(BaseTokensHelper):
    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        tokens_set_name: str,
        decode_responses: bool = True,
    ) -> None:
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=decode_responses,
        )
        self.tokens_set = tokens_set_name

    def token_exist(self, token: str) -> bool:
        return bool(self.redis.sismember(self.tokens_set, token))

    def add_token(self, token: str) -> None:
        self.redis.sadd(self.tokens_set, token)

    def delete_token(self, token: str) -> None:
        self.redis.srem(self.tokens_set, token)


redis_tokens = RedisTokensHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_TOKENS,
    tokens_set_name=config.REDIS_TOKENS_SET_NAME,
    decode_responses=True,
)
