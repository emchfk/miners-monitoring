from ipaddress import IPv4Address
from pathlib import Path
from typing import Any

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


class Asic(BaseModel):
    """Todo.

    Todo details

    Generated using <code>datamodel-codegen</code> with <code>--force-optional</code> option.

    Attributes:
        total (float | None): Total hashrate of the ASIC.
        domains (list[float] | None): List of hashrates for each domain of the ASIC.
        errorCount (int | None): Number of errors encountered by the ASIC.
    """

    total: float | None = None
    domains: list[float] | None = None
    errorCount: int | None = None


class HashrateMonitor(BaseModel):
    """Todo.

    Todo details

    Generated using <code>datamodel-codegen</code> with <code>--force-optional</code> option.

    Attributes:
        asics (list[Asic] | None): List of ASICs monitored by the hashrate monitor.
    """

    asics: list[Asic] | None = None


class MinerData(BaseModel):
    """Todo.

    Todo details

    Generated using <code>datamodel-codegen</code> with <code>--force-optional</code> option.

    Attributes:
        power (float | None): Power consumption of the miner.
        voltage (float | None): Voltage of the miner.
        current (float | None): Current of the miner.
        temp (float | None): Temperature of the miner.
        temp2 (int | None): Secondary temperature of the miner.
        vrTemp (int | None): VR temperature of the miner.
        maxPower (int | None): Maximum power of the miner.
        nominalVoltage (int | None): Nominal voltage of the miner.
        hashRate (float | None): Hashrate of the miner.
        hashRate_1m (float | None): 1-minute hashrate of the miner.
        hashRate_10m (float | None): 10-minute hashrate of the miner.
        hashRate_1h (float | None): 1-hour hashrate of the miner.
        expectedHashrate (int | None): Expected hashrate of the miner.
        errorPercentage (float | None): Error percentage of the miner.
        bestDiff (int | None): Best difficulty of the miner.
        bestSessionDiff (int | None): Best session difficulty of the miner.
        poolDifficulty (int | None): Pool difficulty of the miner.
        isUsingFallbackStratum (int | None): Indicates if the miner is using fallback stratum.
        poolAddrFamily (int | None): Pool address family of the miner.
        isPSRAMAvailable (int | None): Indicates if PSRAM is available on the miner.
        freeHeap (int | None): Free heap memory of the miner.
        freeHeapInternal (int | None): Free internal heap memory of the miner.
        freeHeapSpiram (int | None): Free SPI RAM heap memory of the miner.
        coreVoltage (int | None): Core voltage of the miner.
        coreVoltageActual (int | None): Actual core voltage of the miner.
        frequency (int | None): Frequency of the miner.
        ssid (str | None): SSID of the miner's Wi-Fi network.
        macAddr (str | None): MAC address of the miner.
        hostname (str | None): Hostname of the miner.
        ipv4 (str | None): IPv4 address of the miner.
        ipv6 (str | None): IPv6 address of the miner.
        wifiStatus (str | None): Wi-Fi status of the miner.
        wifiRSSI (int | None): Wi-Fi RSSI of the miner.
        apEnabled (int | None): Indicates if the access point is enabled on the miner.
        sharesAccepted (int | None): Number of accepted shares by the miner.
        sharesRejected (int | None): Number of rejected shares by the miner.
        sharesRejectedReasons (list[Any] | None): List of reasons for rejected shares.
        uptimeSeconds (int | None): Uptime of the miner in seconds.
        smallCoreCount (int | None): Count of small cores in the miner.
        ASICModel (str | None): Model of the ASIC in the miner.
        stratumURL (str | None): Stratum URL of the miner.
        stratumPort (int | None): Stratum port of the miner.
        stratumUser (str | None): Stratum user of the miner.
        stratumSuggestedDifficulty (int | None): Suggested difficulty for the stratum.
        stratumExtranonceSubscribe (int | None): Extranonce subscription for the stratum.
        fallbackStratumURL (str | None): Fallback stratum URL of the miner.
        fallbackStratumPort (int | None): Fallback stratum port of the miner.
        fallbackStratumUser (str | None): Fallback stratum user of the miner.
        fallbackStratumSuggestedDifficulty (int | None): Suggested difficulty for the fallback stratum.
        fallbackStratumExtranonceSubscribe (int | None): Extranonce subscription for the fallback stratum.
        responseTime (float | None): Response time of the miner.
        version (str | None): Version of the miner's firmware.
        axeOSVersion (str | None): Version of the AxeOS on the miner.
        idfVersion (str | None): Version of the IDF on the miner.
        boardVersion (str | None): Version of the board on the miner.
        resetReason (str | None): Reason for the last reset of the miner.
        runningPartition (str | None): Running partition of the miner.
        overheat_mode (int | None): Indicates if the miner is in overheat mode.
        overclockEnabled (int | None): Indicates if overclocking is enabled on the miner.
        display (str | None): Display type of the miner.
        rotation (int | None): Display rotation of the miner.
        invertscreen (int | None): Indicates if the display screen is inverted on the miner.
        displayTimeout (int | None): Display timeout of the miner.
        autofanspeed (int | None): Indicates if automatic fan speed control is enabled on the miner.
        fanspeed (float | None): Fan speed of the miner.
        manualFanSpeed (int | None): Manual fan speed setting of the miner.
        minFanSpeed (int | None): Minimum fan speed setting of the miner.
        temptarget (int | None): Target temperature setting of the miner.
        fanrpm (int | None): Fan RPM of the miner.
        fan2rpm (int | None): Second fan RPM of the miner.
        statsFrequency (int | None): Frequency of statistics collection on the miner.
        blockFound (int | None): Number of blocks found by the miner.
        blockHeight (int | None): Current block height of the miner.
        scriptsig (str | None): Script signature of the miner.
        networkDifficulty (int | None): Network difficulty of the miner.
        hashrateMonitor (HashrateMonitor | None): Hashrate monitor data of the miner.
    """

    power: float | None = None
    voltage: float | None = None
    current: float | None = None
    temp: float | None = None
    temp2: int | None = None
    vrTemp: int | None = None
    maxPower: int | None = None
    nominalVoltage: int | None = None
    hashRate: float | None = None
    hashRate_1m: float | None = None
    hashRate_10m: float | None = None
    hashRate_1h: float | None = None
    expectedHashrate: int | None = None
    errorPercentage: float | None = None
    bestDiff: int | None = None
    bestSessionDiff: int | None = None
    poolDifficulty: int | None = None
    isUsingFallbackStratum: int | None = None
    poolAddrFamily: int | None = None
    isPSRAMAvailable: int | None = None
    freeHeap: int | None = None
    freeHeapInternal: int | None = None
    freeHeapSpiram: int | None = None
    coreVoltage: int | None = None
    coreVoltageActual: int | None = None
    frequency: int | None = None
    ssid: str | None = None
    macAddr: str | None = None
    hostname: str | None = None
    ipv4: str | None = None
    ipv6: str | None = None
    wifiStatus: str | None = None
    wifiRSSI: int | None = None
    apEnabled: int | None = None
    sharesAccepted: int | None = None
    sharesRejected: int | None = None
    sharesRejectedReasons: list[Any] | None = None
    uptimeSeconds: int | None = None
    smallCoreCount: int | None = None
    ASICModel: str | None = None
    stratumURL: str | None = None
    stratumPort: int | None = None
    stratumUser: str | None = None
    stratumSuggestedDifficulty: int | None = None
    stratumExtranonceSubscribe: int | None = None
    fallbackStratumURL: str | None = None
    fallbackStratumPort: int | None = None
    fallbackStratumUser: str | None = None
    fallbackStratumSuggestedDifficulty: int | None = None
    fallbackStratumExtranonceSubscribe: int | None = None
    responseTime: float | None = None
    version: str | None = None
    axeOSVersion: str | None = None
    idfVersion: str | None = None
    boardVersion: str | None = None
    resetReason: str | None = None
    runningPartition: str | None = None
    overheat_mode: int | None = None
    overclockEnabled: int | None = None
    display: str | None = None
    rotation: int | None = None
    invertscreen: int | None = None
    displayTimeout: int | None = None
    autofanspeed: int | None = None
    fanspeed: float | None = None
    manualFanSpeed: int | None = None
    minFanSpeed: int | None = None
    temptarget: int | None = None
    fanrpm: int | None = None
    fan2rpm: int | None = None
    statsFrequency: int | None = None
    blockFound: int | None = None
    blockHeight: int | None = None
    scriptsig: str | None = None
    networkDifficulty: int | None = None
    hashrateMonitor: HashrateMonitor | None = None


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
    def update_data(self, json_data: str) -> None:
        """Update the miner's data with the provided JSON data."""
        self.data = MinerData.model_validate(json_data)

    def print_name(self, msg: str) -> str:
        return f"Miner: {self.settings.name} {msg}"

    def print_ip(self) -> str:
        return f"Miner: {self.settings.ip}"

    # END DEBUGGING
