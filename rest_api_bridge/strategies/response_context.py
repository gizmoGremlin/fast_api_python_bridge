from fastapi import Request
from rest_api_bridge.strategies.response_strategy import JSONResponseStrategy, XMLResponseStrategy



class ResponseContext:
    def __init__(self, request: Request):
        self._strategy = self._get_strategy(request.headers.get("Accept"))

    def _get_strategy(self, accept_header: str):
        if 'application/xml' in accept_header:
            return XMLResponseStrategy()
        return JSONResponseStrategy()
    
    def execute_strategy(self, data:dict):
        return self._strategy.format_data(data)
    