import asyncio

from miners_monitoring.models.miner import Miner

from .settings import Settings


async def _run() -> None:
    # Loading app settings
    settings = Settings()

    # List of miners
    miners = []

    # Initialization of list of miners based on settings
    for miner_name, miner_settings in settings.miners.items():
        miners.append(Miner(name=miner_name, settings=miner_settings))

    # DEBUG
    for custom_call_name, custom_call_settings in settings.custom_calls.items():
        print(f"Custom call: {custom_call_name} ({custom_call_settings.crontab})")
        print(f"Sequence: {custom_call_settings.sequence}")
    for miner in miners:
        print(miner.print_name())
        print(miner.print_ip())
        # system_response = await get_system_info(miner.settings.ip)
        # system_response = await post_restart(miner.settings.ip)
        # print(f"System response for {miner.name}: {system_response}")
    # END DEBUG


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
