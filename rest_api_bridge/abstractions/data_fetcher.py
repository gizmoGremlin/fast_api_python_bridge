from abc import ABC, abstractmethod


class DataFetcher(ABC):
    """
    Abstract base class for fetching data from various sources.

    Subclasses must implement the `fetch_data` method, which specifies 
    how to fetch data from a given source. This can include APIs, databases, files, etc.
    """

    @abstractmethod
    async def fetch_data(self, source: str, params: dict = None):
        """
        Fetch data from the specified source.

        Args:
            source (str): The data source (e.g., URL, file path, database query).
            params (dict, optional): Additional parameters for data fetching.

        Returns:
            Data from the specified source, structured as needed by the implementation.
        """
        pass
