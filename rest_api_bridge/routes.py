
from apis.api_implementation import AnimeApi, CoinCapAPI
from services.anime_service import AnimeService
from services.coincap_service import CoinCapService
from fastapi import APIRouter

anime_api_impl = AnimeApi()
coincap_api_impl = CoinCapAPI()


anime_service = AnimeService(anime_api_impl)
coincap_service = CoinCapService(coincap_api_impl)


router = APIRouter()


@router.get("/anime/quote/")
async def get_anime_quote():
    """
    Fetch a random anime quote from the AnimeChan API.
    """
    endpoint = "https://animechan.io/api/v1/quotes/random"
    raw_data = await anime_service.fetch_data(endpoint)
    processed_data = anime_service.process_data(raw_data)
    if processed_data:
        return {
            "message": "Random Anime Quote",
            "data": processed_data,
        }
    return {"message": "Failed to fetch Anime Quote"}


@router.get("/coincap/data/")
async def get_coincap_data():
    """
    Fetch data from the CoinCap API.
    """
    endpoint = "/assets"  # Only provide the relative path
    raw_data = await coincap_service.fetch_data(endpoint)
    processed_data = coincap_service.process_data(raw_data)
    if processed_data:
        return {
            "message": "CoinCap Data",
            "data": processed_data,
        }
    return {"message": "Failed to fetch CoinCap data"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          