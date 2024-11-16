from fastapi import APIRouter, Request
from rest_api_bridge.apis.anime_api import AnimeApi
from rest_api_bridge.services.anime_service import AnimeService
from rest_api_bridge.strategies.response_context import ResponseContext

anime_api_impl = AnimeApi()
anime_service = AnimeService(anime_api_impl)

anime_router = APIRouter()

@anime_router.get("/anime/quote/")
async def get_anime_quote(request: Request):
    """
    Fetch a random anime quote from the AnimeChan API and return in the requested format.
    """
    endpoint = "https://animechan.io/api/v1/quotes/random"
    raw_data = await anime_service.fetch_data(endpoint)
    processed_data = anime_service.process_data(raw_data)
    data = {
        "message": "Random Anime Quote",
        "data": processed_data if processed_data else "Failed to fetch Anime Quote"
    }

    # Use the response context to return the data in the correct format
    context = ResponseContext(request)
    return context.execute_strategy(data)