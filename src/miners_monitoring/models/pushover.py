from pydantic import BaseModel


# Model for defining Pushover parameters (pushover section.)
class PushoverSettings(BaseModel):
    app_token: str = ""
    user_token: str = ""
