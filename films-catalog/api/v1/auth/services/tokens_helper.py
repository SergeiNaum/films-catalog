import secrets
from abc import ABC, abstractmethod


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
