import json
from collections.abc import Awaitable, Callable
from typing import Any

import httpx

url_template = "http://{}/api/system/{}"  # Url template for API requests (AxeOS)

Getter = Callable[[str], Awaitable[Any | str]]


# Generic function for asynchronously interacting with the API
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


async def post_data(api_url: str) -> Any | str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(api_url, headers=None, json=None)
            response.raise_for_status()  # Check if request was successful (status 200-299)

            # Check if the response is JSON and return it, otherwise return the text
            try:
                return response.json()
            except json.JSONDecodeError:
                print(f"{response.text}")
                return None
        except httpx.HTTPStatusError as e:
            return f"HTTP Error : {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            return f"Request Error : {e}"


# GET functions for specific API endpoints
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


# POST functions for specific API endpoints
async def post_system_data(ip: str, endpoint: str) -> Any | str:
    url = url_template.format(ip, endpoint)
    return await post_data(url)


def make_poster(endpoint: str) -> Getter:
    async def poster(ip: str) -> Any | str:
        return await post_system_data(ip, endpoint)

    return poster


post_restart = make_poster("restart")
post_identify = make_poster("identify")


# PATCH functions for specific API endpoints
# def patch_system(ip: str, json_data: dict):
#     url = url_template.format(ip,"")
#     response = requests.patch(url, headers={}, json=json_data)
#     return response
