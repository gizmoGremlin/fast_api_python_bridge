


from services.base_service import BaseDataService


class CoinCapService(BaseDataService):
    """
    A specific DataService implementation for fetching data from CoinCap API.
    """

    async def fetch_data(self, endpoint: str, params: dict = None):
        print(f"CoinCapService: Fetching data from '{endpoint}'...")
        return await self._api_impl.fetch_data(endpoint, params)

    def process_data(self, data):
        """
        Process the fetched data into a simplified format.
        """
        try:
            assets = data.get("data", [])
            return [
                {
                    "id": asset["id"],
                    "rank": asset["rank"],
                    "symbol": asset["symbol"],
                    "priceUsd": asset["priceUsd"]
                }
                for asset in assets
            ]
        except Exception as e:
            print(f"Error processing data: {e}")
            return []