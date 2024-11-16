from fastapi import APIRouter, Request
from rest_api_bridge.apis.coincap_api import CoinCapAPI

from rest_api_bridge.services.coincap_service import CoinCapService
from rest_api_bridge.strategies.response_context import ResponseContext

coincap_api_impl = CoinCapAPI()
coincap_service = CoinCapService(coincap_api_impl)

coincap_router = APIRouter()

@coincap_router.get("/coincap/data/")
async def get_coincap_data(request: Request):
    """
    Fetch data from the CoinCap API and return in the requested format.
    """
    endpoint = "/assets"
    raw_data = await coincap_service.fetch_data(endpoint)
    processed_data = coincap_service.process_data(raw_data)
    data = {
        "message": "CoinCap Data",
        "data": processed_data if processed_data else "Failed to fetch CoinCap data"
    }

    # Use the response context to return the data in the correct format
    context = ResponseContext(request)
    return context.execute_strategy(data)
