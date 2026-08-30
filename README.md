<div id="toc">
  <ul align="center" style="list-style: none">
    <summary>
      <h1>
        miners-monitoring
      </h1>
    </summary>
    <em>Self-hostable python app to monitor AxeOS local network miners</em>
  </ul>
</div>

## Description

**MINERS-MONITORING** is a self-hostable python app dedicated to monitoring miners running [AxeOS](https://www.bitaxe.org/) on your local network.

## Features

TODO

## Requirements

You need to have:

* An active cryptocurrency mining device running [AxeOS](https://www.bitaxe.org/);
* A [PUSHOVER](https://pushover.net/) account, with a defined application API Token.

## Example

TODO

## Setting up

### Setting up Python environment

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Updating environment

To update/upgrade pip and detect outdated packages, use the following commands:

``` bash
pip install --upgrade pip
pip list --outdated
```

### Setting up application parameters

Rename the file *.toml.example* to *.toml* and update the parameters:

``` bash
TODO
```

Never commit this file, it contains extremely private data!

## Running as service

### Installation

Copy the main script service file to the following location:

``` bash
sudo cp .service /etc/systemd/system/miners-monitoring.service
```

Reload the systemd configuration:

``` bash
sudo systemctl daemon-reload
```

Activate the automatic start when booting:

``` bash
sudo systemctl enable miners-monitoring.service
```

Start the service:

``` bash
sudo systemctl start miners-monitoring.service
```

To check the service status:

``` bash
sudo systemctl status miners-monitoring.service
```

### Logs

To see the logs in real-time:

``` bash
journalctl -u miners-monitoring.service -f
```

To see previous logs:

``` bash
journalctl -u miners-monitoring.service
```

### Checks

To check the service is active:

``` bash
sudo systemctl is-active miners-monitoring.service
```

This should return *active*.

To check the service is activated at boot:

``` bash
sudo systemctl is-enabled miners-monitoring.service
```

This should return *enabled*.

## Bitaxe API

See dedicated OSMU wiki: [Bitaxe API](https://osmu.wiki/bitaxe/api/) and curl converter: [curlconverter](https://curlconverter.com/python/).

For reference, below is the content of the response sent back when adressing /system/info:

```json
{
    'power': 20.3157349, 
    'voltage': 4945.3125, 
    'current': 13953.125, 
    'temp': 60.125, 
    'temp2': -1, 
    'vrTemp': 87, 
    'maxPower': 40, 
    'nominalVoltage': 5, 
    'hashRate': 1010.1762695, 
    'hashRate_1m': 1079.3968506,
    'hashRate_10m': 1069.6203613, 
    'hashRate_1h': 1070.3803711, 
    'expectedHashrate': 1071, 
    'errorPercentage': 4.4217687, 
    'bestDiff': 56102590133, 
    'bestSessionDiff': 51212739, 
    'poolDifficulty': 250000, 
    'isUsingFallbackStratum': 0, 
    'poolAddrFamily': 2, 
    'isPSRAMAvailable': 1, 
    'freeHeap': 8164068, 
    'freeHeapInternal': 105207, 
    'freeHeapSpiram': 8090832, 
    'coreVoltage': 1100, 
    'coreVoltageActual': 1097, 
    'frequency': 525, 
    'ssid': 'WifiName', 
    'macAddr': 'AA:AA:AA:AA:AA:AA', 
    'hostname': 'bitaxe', 
    'ipv4': 'xxx.xxx.xxx.xxx', 
    'ipv6': 'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx', 
    'wifiStatus': 'Connected!',
    'wifiRSSI': -58, 
    'apEnabled': 0, 
    'sharesAccepted': 485, 
    'sharesRejected': 0, 
    'sharesRejectedReasons': [], 
    'uptimeSeconds': 491283, 
    'smallCoreCount': 2040,
    'ASICModel': 'BM1370', 
    'stratumURL': 'bestpool.org', 
    'stratumPort': 8004, 
    'stratumUser': 'myadress.bitaxe', 
    'stratumSuggestedDifficulty': 1000, 
    'stratumExtranonceSubscribe': 0, 
    'fallbackStratumURL': '', 
    'fallbackStratumPort': 8004, 
    'fallbackStratumUser': '', 
    'fallbackStratumSuggestedDifficulty': 1000, 
    'fallbackStratumExtranonceSubscribe': 0, 
    'responseTime': 10.517, 
    'version': 'v2.12.0', 
    'axeOSVersion': 'v2.12.0', 
    'idfVersion': 'v5.5.1', 
    'boardVersion': '601', 
    'resetReason': 'Software reset via esp_restart',
    'runningPartition': 'ota_0', 
    'overheat_mode': 0, 
    'overclockEnabled': 0, 
    'display': 'SSD1306 (128x32)', 
    'rotation': 0, 
    'invertscreen': 0, 
    'displayTimeout': 1, 
    'autofanspeed': 1, 
    'fanspeed': 57.068367, 
    'manualFanSpeed': 100, 
    'minFanSpeed': 20, 
    'temptarget': 60, 
    'fanrpm': 4131, 
    'fan2rpm': 0, 
    'statsFrequency': 30, 
    'blockFound': 0, 
    'blockHeight': 23874172, 
    'scriptsig': 'xxx.bestpool.org', 
    'networkDifficulty': 648142255, 
    'hashrateMonitor': {
        'asics': [{'total': 1010.1762695, 'domains': [255.1210632, 255.9800415, 243.9541321, 255.9800415], 'errorCount': 4042626}]
    }
}
```