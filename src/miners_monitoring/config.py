from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


# Modèle pour la définition des paramètres mineurs (section miners.)
# TODO : move to models?
class MinerSettings(BaseModel):
    name: str = ""
    ip: str = ""
    logs: str = ""


# Modèle pour la définition des paramètres Pushover (section pushover.)
# TODO : move to models?
class PushoverSettings(BaseModel):
    app_token: str = ""
    user_token: str = ""


# TODO : proposer l'édition des paramètres avec Typer ?
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        toml_file="debug_config.toml"
    )  # TODO : load using platformdirs or create if exception

    miners: dict[str, MinerSettings] = Field(default_factory=dict)
    pushover: PushoverSettings = Field(default_factory=PushoverSettings)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


# toml_settings = Settings()
