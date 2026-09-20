from ipaddress import IPv4Address
from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from miners_monitoring.config import dirs

DEFAULT_MINER_NAME = "my_miner"


# Model for defining miner parameters (miner section.)
class MinerSettings(BaseModel):
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


class Miner(BaseModel):
    settings: MinerSettings = MinerSettings()
