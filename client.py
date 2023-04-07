import typing

import aiohttp

from .enum import EndpointType


class HmtaiAPI:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def get_endpoints(self, type: EndpointType) -> typing.List[str]:
        """Get all endpoints of a certain type.

        Args:
            type (EndpointType): The type of endpoints to get.

        Returns:
            typing.List[str]: A list of endpoints.
        """
        async with self.session.get("https://hmtai.hatsunia.cfd/v2/endpoints") as resp:
            endpoints: typing.Dict[str, typing.Any] = await resp.json()
        return endpoints.get(type.value, [])

    async def get_image(self, endpoint: str) -> typing.Optional[str]:
        """Get a random image from a certain endpoint.

        Args:
            endpoint (str): The endpoint to get the image from.

        Returns:
            typing.Optional[str]: The URL of the image. None if the endpoint is invalid.
        """
        async with self.session.get(
            f"https://hmtai.hatsunia.cfd/v2/{endpoint}"
        ) as resp:
            data = await resp.json()
        if "url" not in data:
            return None

        return data["url"]
