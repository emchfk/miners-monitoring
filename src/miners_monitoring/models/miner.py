from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from miners_monitoring.config import dirs

DEFAULT_MINER_NAME = "my_miner"


class MinerSettings(BaseModel):
    model_config = ConfigDict(validate_default=True)

    name: str = ""
    ip: str = "192.168.1.100"
    logs: str = ""

    # TODO : add validation for IP address format, IPV4 format verification
    # @field_validator("ip")
    # def validate_ip(cls, v: str) -> str:
    #     # Simple IP address validation (basic)
    #     if not v:
    #         raise ValueError("IP address is required")
    #     if not v.count(".") == 3:
    #         raise ValueError("Invalid IP address format")
    #     return v

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
