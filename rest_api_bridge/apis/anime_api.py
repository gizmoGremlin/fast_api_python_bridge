import httpx
from rest_api_bridge.abstractions.data_fetcher import DataFetcher

class AnimeApi(DataFetcher):
    """
    Implementation of DataFetcher for the AnimeChan API.
    """

    async def fetch_data(self, source: str, params: dict = None):
        """
        Fetch data from the AnimeChan API.

        Args:
            source (str): The endpoint URL.
            params (dict, optional): Additional parameters for the API call.

        Returns:
            dict: JSON response from the AnimeChan API.
        """
        print(f"AnimeApi: Fetching data from {source}...")
        async with httpx.AsyncClient() as client:
            response = await client.get(source, params=params)
            response.raise_for_status()
            return response.json()