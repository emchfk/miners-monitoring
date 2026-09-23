import asyncio

from miners_monitoring.services.api import get_system_info

from .settings import Settings


async def _run() -> None:
    # Loading app settings
    settings = Settings()

    # DEBUG
    # Fetch system response for each miner
    for miner_name, miner_settings in settings.miners.items():
        print(f"Miner: {miner_name} ({miner_settings.ip})")
        system_response = await get_system_info(miner_settings.ip)
        # system_response = await post_restart(miner_settings.ip)
        print(f"System response for {miner_name}: {system_response}")


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
