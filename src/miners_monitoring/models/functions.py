from pydantic import BaseModel


# Model for defining custom calls (custom_calls section.)
class CallSettings(BaseModel):
    crontab: str = "*/1 * * * *"
    sequence: list[dict[str, str | dict[str, str]]] = [
        {"function": "print_name", "args": {}}
    ]
