import json
from collections.abc import Awaitable, Callable
from typing import Any, Literal

import httpx

url_template = "http://{}/api/system/{}"  # Url template for API requests (AxeOS)

Getter = Callable[[str], Awaitable[Any | str]]
Poster = Callable[[str], Awaitable[Any | str]]


RequestMethod = Literal["get", "post"]  # TODO : patch


# Generic function for asynchronously interacting with the API
async def api_interaction(api_url: str, method: RequestMethod = "get") -> Any | str:
    async with httpx.AsyncClient() as client:
        try:
            if method == "get":
                response = await client.get(api_url)
            elif method == "post":
                response = await client.post(api_url, headers=None, json=None)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()  # Check if request was successful (status 200-299)

            # Check if the response is JSON and return it, otherwise return the text
            try:
                return response.json()
            except json.JSONDecodeError:
                return response.text
        except httpx.HTTPStatusError as e:
            return f"HTTP Error : {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            return f"Request Error : {e}"


async def request_system_data(
    ip: str, endpoint: str, method: RequestMethod = "get"
) -> Any | str:
    url = url_template.format(ip, endpoint)
    return await api_interaction(url, method=method)


def make_getter(endpoint: str) -> Getter:
    async def getter(ip: str) -> Any | str:
        return await request_system_data(ip, endpoint, "get")

    return getter


def make_poster(endpoint: str) -> Poster:
    async def poster(ip: str) -> Any | str:
        return await request_system_data(ip, endpoint, "post")

    return poster


get_system_info = make_getter("info")
get_asic_settings_info = make_getter("asic")
get_system_statistics = make_getter("statistics")
get_wifi_scan = make_getter("wifi/scan")


post_restart = make_poster("restart")
post_identify = make_poster("identify")


# PATCH functions for specific API endpoints
# def patch_system(ip: str, json_data: dict):
#     url = url_template.format(ip,"")
#     response = requests.patch(url, headers={}, json=json_data)
#     return response
