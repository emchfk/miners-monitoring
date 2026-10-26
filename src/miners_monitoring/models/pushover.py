from pydantic import BaseModel


# Model for defining Pushover parameters (pushover section.)
class PushoverSettings(BaseModel):
    """Pushover settings model for configuring Pushover API parameters.

    Attributes:
        app_token (str): The application token for Pushover.
        user_token (str): The user token for Pushover.
    """

    app_token: str = ""
    user_token: str = ""


class PushoverInterface(BaseModel):
    """Pushover interface model for sending notifications via Pushover API.

    Attributes:
        settings (PushoverSettings): The Pushover settings for configuring the API parameters.
    """

    settings: PushoverSettings = PushoverSettings()
