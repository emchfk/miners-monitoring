import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)
from tomli_w import dump

from miners_monitoring.config import dirs
from miners_monitoring.models.miner import MinerSettings
from miners_monitoring.models.pushover import PushoverSettings

CONFIG_FILE = Path(dirs.user_config_dir) / "config.toml"


# Write the configuration file if it does not exist, or update/correct it with the current settings if it does exist
def write_config_file(config_file: Path, settings: dict[str, object]) -> None:
    config_file.parent.mkdir(parents=True, exist_ok=True)
    with config_file.open("wb") as file:
        dump(settings, file)
    print(
        f"Configuration file location: {config_file}."
        "\nEdit the file to change settings, or delete it to reset to defaults."
    )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        toml_file=os.fspath(CONFIG_FILE),
    )

    miners: dict[str, MinerSettings] = {"my_miner": MinerSettings()}
    pushover: PushoverSettings = Field(default_factory=PushoverSettings)

    def __init__(self) -> None:
        super().__init__()
        write_config_file(CONFIG_FILE, self.model_dump())

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
