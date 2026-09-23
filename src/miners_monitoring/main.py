import asyncio

from miners_monitoring.services.api import get_system_info

from .settings import Settings


async def _run() -> None:
    # Loading app settings
    settings = Settings()

    # DEBUG
    # Fetch system info for each miner
    for miner_name, miner_settings in settings.miners.items():
        print(f"Fetching system info for miner: {miner_name} ({miner_settings.ip})")
        system_info = await get_system_info(miner_settings.ip)
        print(f"System info for {miner_name}: {system_info}")


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
