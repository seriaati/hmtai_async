from typing import List, Optional
import aiohttp
import json


class HmtaiAPI:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def update_endpoints(self) -> None:
        async with self.session.get("https://hmtai.hatsunia.cfd/v2/endpoints") as resp:
            endpoints = await resp.json()
        with open("endpoints.json", "w") as f:
            json.dump(endpoints, f, indent=4)

    async def get_sfw_endpoints(self) -> List[str]:
        with open("endpoints.json", "r") as f:
            endpoints = json.load(f)
        return endpoints["nsfw"]

    async def get_nsfw_endpoints(self) -> List[str]:
        with open("endpoints.json", "r") as f:
            endpoints = json.load(f)
        return endpoints["nsfw"]

    async def get(self, endpoint: str) -> Optional[str]:
        async with self.session.get(
            f"https://hmtai.hatsunia.cfd/v2/{endpoint}"
        ) as resp:
            data = await resp.json()
        if "url" not in data:
            return None
        return data["url"]
