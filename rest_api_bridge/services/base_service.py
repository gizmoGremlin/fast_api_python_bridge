
from abc import abstractmethod, ABC

from rest_api_bridge.abstractions.data_fetcher import DataFetcher


class BaseDataService(ABC):

    #Base class for services
    
    def __init__(self, api_impl: DataFetcher):
        self._api_impl = api_impl
    
    @abstractmethod
    async def fetch_data(self, endpoint: str, params: dict = None):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

