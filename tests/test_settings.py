from pathlib import Path

from pydantic_settings import SettingsConfigDict

from miners_monitoring.config import dirs
from miners_monitoring.models.miner import DEFAULT_MINER_NAME
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

    assert settings.miners["my_miner"].name == "my_miner"
    assert settings.miners["my_miner"].ip == "192.168.1.100"
    assert settings.miners["my_miner"].logs == str(
        Path(dirs.user_log_dir) / f"{DEFAULT_MINER_NAME}.json"
    )
    assert settings.pushover.app_token == ""
    assert settings.pushover.user_token == ""


# Testing existing config file
def test_settings_existing_config_file(monkeypatch, tmp_path):
    # TODO : create a function in conftest to create a temporary config file
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        "[miners.a_miner]\n"
        'name = "a miner"\n'
        'ip = "0.0.0.0"\n'
        'logs = "/path/to/logs/a_miner.json"\n'
        "[miners.another_miner]\n"
        'name = "another miner"\n'
        'ip = "1.1.1.1"\n'
        'logs = "/path/to/logs/another_miner.json"\n'
        "[pushover]\n"
        'app_token = "a"\n'
        'user_token = "b"\n',
        encoding="utf-8",
    )

    monkeypatch.setattr("miners_monitoring.settings.CONFIG_FILE", config_file)
    monkeypatch.setattr(
        Settings,
        "model_config",
        SettingsConfigDict(toml_file=str(config_file)),
    )

    settings = Settings()

    assert settings.miners["a_miner"].name == "a miner"
    assert settings.miners["a_miner"].ip == "0.0.0.0"
    assert settings.miners["a_miner"].logs == "/path/to/logs/a_miner.json"
    assert settings.miners["another_miner"].name == "another miner"
    assert settings.miners["another_miner"].ip == "1.1.1.1"
    assert settings.miners["another_miner"].logs == "/path/to/logs/another_miner.json"
    assert settings.pushover.app_token == "a"
    assert settings.pushover.user_token == "b"
