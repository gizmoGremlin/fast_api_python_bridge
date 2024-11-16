import httpx
from rest_api_bridge.abstractions.data_fetcher import DataFetcher

class CoinCapAPI(DataFetcher):
    """
    Implementation of DataFetcher for the CoinCap API.
    """

    BASE_URL = "https://api.coincap.io/v2"

    async def fetch_data(self, source: str, params: dict = None):
        """
        Fetch data from the CoinCap API.

        Args:
            source (str): The endpoint path (relative to BASE_URL).
            params (dict, optional): Additional parameters for the API call.

        Returns:
            dict: JSON response from the CoinCap API.
        """
        url = f"{self.BASE_URL}{source}"
        print(f"CoinCapAPI: Fetching data from {url}...")
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()