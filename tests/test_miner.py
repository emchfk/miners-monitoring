import pytest
from pydantic import ValidationError

from miners_monitoring.models.miner import MinerSettings


def test_miner_settings_default_name_validator_no_name():
    miner_settings = MinerSettings()
    assert miner_settings.name == "my_miner"


def test_miner_settings_default_name_validator_empty_name():
    miner_settings = MinerSettings(name="")
    assert miner_settings.name == "my_miner"


def test_miner_settings_accepts_valid_ipv4_address():
    miner_settings = MinerSettings(ip="10.0.0.42")
    assert miner_settings.ip == "10.0.0.42"


@pytest.mark.parametrize("ip", ["999.1.1.1", "10.0.0", "not-an-ip", "2001:db8::1"])
def test_miner_settings_rejects_invalid_ipv4_address(ip):
    with pytest.raises(ValidationError, match="Invalid IPv4 address format"):
        MinerSettings(ip=ip)
