from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "change.me"
    name: str = "postgres"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 10
    max_overflow: int = 10

    @property
    def database_url(self):
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            path=self.name,
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="APP_",
        env_nested_delimiter="__",
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseSettings


settings = Settings()
