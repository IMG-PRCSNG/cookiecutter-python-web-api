from pydantic import Field
from pydantic_settings import BaseSettings

DB_SCHEME = "sqlite+pysqlite://"


class AppConfig(BaseSettings):

    database_url: str = Field(f"{DB_SCHEME}/app.db")
