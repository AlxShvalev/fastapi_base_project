from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class RunConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_prefix="APP_",
        extra="ignore",
    )


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "change.me"
    name: str = "postgres"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 10
    max_overflow: int = 10

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_prefix="DB_",
        extra="ignore",
    )

    @property
    def database_url(self):
        return PostgresDsn.build(
            scheme="postgres+asyncpg",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            path=self.name,
        )


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    database: DatabaseSettings


settings = Settings()
