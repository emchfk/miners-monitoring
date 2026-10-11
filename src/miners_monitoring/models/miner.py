from ipaddress import IPv4Address
from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from miners_monitoring.config import dirs

DEFAULT_MINER_NAME: str = "my_miner"
"""Default miner name used when no name is provided in the configuration file."""
DEFAULT_FREQUENCY: int = 525
"""Default ASIC frequency value used when resetting."""
DEFAULT_CORE_VOLTAGE: int = 1100
"""Default core voltage value used when resetting."""
OVERHEAT_FREQUENCY: int = 400
"""Frequency value used when the miner is overheating."""
OVERHEAT_CORE_VOLTAGE: int = 1000
"""Core voltage value used when the miner is overheating."""
MINER_METHODS_REGISTER: list[str] = ["print_name", "print_ip"]
"""List of miner methods that can be called via custom calls."""


# Model for defining miner parameters (miner section.)
class MinerSettings(BaseModel):
    """Todo.

    Todo details

    Attributes:
        model_config (ConfigDict): Configuration for the model.
        name (str): miner name.
        ip (str): miner IP address.
        logs (str): path to the miner logs file.
    """

    model_config = ConfigDict(validate_default=True)

    name: str = ""
    ip: str = "192.168.1.100"
    logs: str = ""

    @field_validator("ip")
    def validate_ip(cls, v: str) -> str:
        try:
            IPv4Address(v)
        except ValueError as exc:
            raise ValueError("Invalid IPv4 address format") from exc
        return v

    @field_validator("name")
    def default_name(cls, v: str) -> str:
        if (not v) or (v == ""):
            return DEFAULT_MINER_NAME
        return v

    @field_validator("logs")
    def default_logs(cls, v: str, info: ValidationInfo) -> str:
        if (not v) or (v == ""):
            return str(
                Path(dirs.user_log_dir)
                / f"{info.data.get('name', DEFAULT_MINER_NAME)}.json"
            )
        return v


class MinerData(BaseModel):
    """Todo.

    Todo details

    Attributes:
        tmp (int): temporary attribute for debugging purposes.
    """
    tmp: int = 0


class Miner(BaseModel):
    """Todo.

    Todo details

    Attributes:
        name (str): miner name.
        settings (MinerSettings): miner settings.
        data (MinerData): miner data.
    """

    name: str = DEFAULT_MINER_NAME
    settings: MinerSettings = MinerSettings()
    data: MinerData = MinerData()

    # DEBUGGING
    def print_name(self, msg: str) -> str:
        return f"Miner: {self.settings.name} {msg}"

    def print_ip(self) -> str:
        return f"Miner: {self.settings.ip}"

    # END DEBUGGING
