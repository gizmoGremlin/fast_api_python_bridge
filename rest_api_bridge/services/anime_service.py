


from services.base_service import BaseDataService


class AnimeService(BaseDataService):
    """
    A specific DataService implementation for fetching anime quotes from AnimeChan API.
    """

    async def fetch_data(self, endpoint: str, params: dict = None):
        print(f"AnimeService: Fetching data from '{endpoint}'...")
        return await self._api_impl.fetch_data(endpoint, params)

    def process_data(self, data):
        """
        Process and return the quote data.
        """
        print("AnimeService: Processing data...")
        if not data or "data" not in data:
            print(f"AnimeService: Invalid data received: {data}")
            return None
        quote_data = data["data"]
        return {
            "quote": quote_data["content"],
            "character": quote_data["character"]["name"],
            "anime": quote_data["anime"]["name"],
        }
