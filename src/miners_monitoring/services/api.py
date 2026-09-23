from collections.abc import Awaitable, Callable
from typing import Any

import httpx

url_template = "http://{}/api/system/{}"  # Url template for API requests (AxeOS)

Getter = Callable[[str], Awaitable[Any | str]]


# Generic function for asynchronously fetching data from the API
async def fetch_data(api_url: str) -> Any | str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url)
            response.raise_for_status()  # Check if request was successful (status 200-299)

            # Display the JSON content of the response
            return response.json()
        except httpx.HTTPStatusError as e:
            return f"HTTP Error : {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            return f"Request Error : {e}"


# Get functions for specific API endpoints
async def get_system_data(ip: str, endpoint: str) -> Any | str:
    url = url_template.format(ip, endpoint)
    return await fetch_data(url)


def make_getter(endpoint: str) -> Getter:
    async def getter(ip: str) -> Any | str:
        return await get_system_data(ip, endpoint)

    return getter


get_system_info = make_getter("info")
get_asic_settings_info = make_getter("asic")
get_system_statistics = make_getter("statistics")
get_wifi_scan = make_getter("wifi/scan")

# Post functions for specific API endpoints
# def post_restart(ip: str):
#     url = url_template.format(ip,"restart")
#     response = requests.post(url)
#     return response

# def post_identify(ip: str):
#     url = url_template.format(ip,"identify")
#     response = requests.post(url)
#     return response

# Patch functions for specific API endpoints
# def patch_system(ip: str, json_data: dict):
#     url = url_template.format(ip,"")
#     response = requests.patch(url, headers={}, json=json_data)
#     return response
