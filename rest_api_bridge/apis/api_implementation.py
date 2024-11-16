import httpx
from abstractions import APIImplementaion


class AnimeApi(APIImplementaion):
    """
    Implementation for AnimeChan API.
    """

    async def fetch_data(self, endpoint: str, params: dict = None):
        print(f"AnimeApi: Fetching data from AnimeChan API...")
        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint)
            response.raise_for_status()
            return response.json()
        

class CoinCapAPI(APIImplementaion):
    """
    Implementation for CoinCap API.
    """

    BASE_URL = "https://api.coincap.io/v2"  # Ensure the base URL does not repeat

    async def fetch_data(self, endpoint: str, params: dict = None):
        # Ensure no double appending of the base URL
        url = f"{self.BASE_URL}{endpoint}"  # Concatenate the base URL with the endpoint
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()  # Raise an error for any bad status codes
            return response.json() 