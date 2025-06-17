from typing import Any, cast

from core import config
from redis import Redis
from schemas.film import FilmSchema

from api.v1.auth.services.film_storage_helper import BaseBookStorageHelper


class RedisBookStorageHelper(BaseBookStorageHelper):
    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        books_hash_name: str,
        decode_responses: bool = True,
    ) -> None:
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=decode_responses,
        )
        self.books_hash_name = books_hash_name

    def add_film(
        self,
        film_schema: FilmSchema,
    ) -> None:
        self.redis.hset(
            name=self.books_hash_name,
            key=film_schema.slug,
            value=film_schema.model_dump_json(),
        )

    def delete_film(
        self,
        slug: str,
    ) -> None:
        self.redis.hdel(self.books_hash_name, slug)

    def get_all_films(self) -> list[Any]:
        result = cast(list[Any], self.redis.hvals(self.books_hash_name))
        return result

    def get_film_details(
        self,
        slug: str,
    ) -> str | None:
        return cast(
            str,
            self.redis.hget(
                name=self.books_hash_name,
                key=slug,
            ),
        )

    def film_exists(self, slug: str) -> bool:
        return cast(
            bool,
            self.redis.hexists(
                name=self.books_hash_name,
                key=slug,
            ),
        )


redis_films_storage = RedisBookStorageHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_FILMS,
    books_hash_name=config.REDIS_FILMS_HASH_NAME,
)
