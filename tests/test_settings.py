from pathlib import Path

import tomli_w
from pydantic_settings import SettingsConfigDict

from miners_monitoring.config import dirs
from miners_monitoring.models.miner import DEFAULT_MINER_NAME, MinerSettings
from miners_monitoring.models.pushover import PushoverSettings
from miners_monitoring.settings import Settings


# Testing missing config file
def test_settings_missing_config_file(monkeypatch, tmp_path):
    config_file = tmp_path / "config.toml"

    monkeypatch.setattr("miners_monitoring.settings.CONFIG_FILE", config_file)
    monkeypatch.setattr(
        Settings,
        "model_config",
        SettingsConfigDict(toml_file=str(config_file)),
    )

    settings = Settings()

    assert settings.miners["my_miner"] == MinerSettings(
        name="my_miner",
        ip="192.168.1.100",
        logs=str(Path(dirs.user_log_dir) / f"{DEFAULT_MINER_NAME}.json"),
    )
    assert settings.pushover == PushoverSettings(app_token="", user_token="")


# Testing existing config file
def test_settings_existing_config_file(monkeypatch, tmp_path):
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        tomli_w.dumps(
            {
                "miners": {
                    "a_miner": {
                        "name": "a miner",
                        "ip": "0.0.0.0",
                        "logs": "/path/to/logs/a_miner.json",
                    },
                    "another_miner": {
                        "name": "another miner",
                        "ip": "1.1.1.1",
                        "logs": "/path/to/logs/another_miner.json",
                    },
                },
                "pushover": {"app_token": "a", "user_token": "b"},
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr("miners_monitoring.settings.CONFIG_FILE", config_file)
    monkeypatch.setattr(
        Settings,
        "model_config",
        SettingsConfigDict(toml_file=str(config_file)),
    )

    settings = Settings()

    assert settings.miners["a_miner"] == MinerSettings(
        name="a miner", ip="0.0.0.0", logs="/path/to/logs/a_miner.json"
    )
    assert settings.miners["another_miner"] == MinerSettings(
        name="another miner", ip="1.1.1.1", logs="/path/to/logs/another_miner.json"
    )
    assert settings.pushover == PushoverSettings(app_token="a", user_token="b")
