import asyncio

from miners_monitoring.models.miner import MinerInterface
from miners_monitoring.services.api import get_system_info

from .settings import Settings


async def _run() -> None:
    # Loading app settings
    settings = Settings()

    # List of miners
    miners = []

    # Initialization of list of miners based on settings
    for miner_name, miner_settings in settings.miners.items():
        miners.append(MinerInterface(name=miner_name, settings=miner_settings))

    # DEBUG
    for custom_call_name, custom_call_settings in settings.custom_calls.items():
        print(f"Custom call: {custom_call_name} ({custom_call_settings.crontab})")
        print(f"Sequence: {custom_call_settings.sequence}")
    for miner in miners:
        print(miner.settings.name)
        print(miner.settings.ip)
        miner.update(await get_system_info(miner.settings.ip))
        miner.save()
        # print(f"Miner data for {miner.name}: {miner.data}")
        # miner.load()
        print(f"Miner data for {miner.name}: {miner.data}")
    # END DEBUG


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
