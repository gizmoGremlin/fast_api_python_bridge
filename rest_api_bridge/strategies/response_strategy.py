from abc import ABC, abstractmethod
from fastapi.responses import JSONResponse
from fastapi import Response
from xml.etree.ElementTree import Element, tostring

class ResponseFormatStrategy(ABC):
    @abstractmethod
    def format_data(self, data: dict) -> Response:
        pass

class JSONResponseStrategy(ResponseFormatStrategy):
    def format_data(self, data: dict) -> Response:
        return JSONResponse(content=data)

class XMLResponseStrategy(ResponseFormatStrategy):
    def format_data(self, data: dict) -> Response:
        root = Element("response")
        for key, value in data.items():
            child = Element(key)
            child.text = str(value)
            root.append(child)
        return Response(content=tostring(root), media_type="application/xml")
