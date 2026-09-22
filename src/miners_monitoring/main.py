from .settings import Settings


def main() -> None:
    # Loading app settings
    settings = Settings()

    # DEBUG:
    print(settings)
