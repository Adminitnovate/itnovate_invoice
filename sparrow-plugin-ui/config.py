from pydantic import BaseSettings


class Settings(BaseSettings):
    sparrow_key: str = "01234567890"


settings = Settings()