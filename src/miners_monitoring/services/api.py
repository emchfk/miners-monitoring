# AxeOS API
# https://osmu.wiki/bitaxe/api/

# import requests --> httpx

# url_template = "http://{}/api/system/{}"

# # ---------------- GET ----------------
# def get_system_info(ip: str):
#     url = url_template.format(ip,"info")
#     response = requests.get(url)
#     return response

# def get_asic_settings_info(ip: str):
#     url = url_template.format(ip,"asic")
#     response = requests.get(url)
#     return response

# def get_system_statistics(ip: str):
#     url = url_template.format(ip,"statistics")
#     response = requests.get(url)
#     return response

# def get_wifi_scan(ip: str):
#     url = url_template.format(ip,"wifi/scan")
#     response = requests.get(url)
#     return response

# # ---------------- POST ----------------
# def post_restart(ip: str):
#     url = url_template.format(ip,"restart")
#     response = requests.post(url)
#     return response

# def post_identify(ip: str):
#     url = url_template.format(ip,"identify")
#     response = requests.post(url)
#     return response

# # --------------- PATCH ----------------
# def patch_system(ip: str, json_data: dict):
#     url = url_template.format(ip,"")
#     response = requests.patch(url, headers={}, json=json_data)
#     return response
