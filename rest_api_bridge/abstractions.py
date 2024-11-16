from abc import ABC, abstractmethod


class APIImplementaion(ABC):
    """
    Abstract base class for specific API implementations
    """
    @abstractmethod
    async def fetch_data(self, url:str, params: dict = None):
        pass
