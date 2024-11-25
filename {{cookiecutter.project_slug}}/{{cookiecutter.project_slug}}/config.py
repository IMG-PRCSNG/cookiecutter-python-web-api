from typing import Type, Tuple
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict, JsonConfigSettingsSource, PydanticBaseSettingsSource
from {{cookiecutter.project_slug}}.inference import BaseModelConfig
DB_SCHEME = "sqlite+pysqlite://"


class AppConfig(BaseSettings):

    database_url: str = Field(f"{DB_SCHEME}/app.db")
    inference: dict[str, BaseModelConfig] = {}

    model_config = SettingsConfigDict(json_file='config.json', json_file_encoding='utf-8')

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (init_settings, JsonConfigSettingsSource(settings_cls),)