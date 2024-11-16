from fastapi import FastAPI
from rest_api_bridge.routes.anime_router import anime_router
from rest_api_bridge.routes.coincap_router import coincap_router

app = FastAPI()

# Include routers
app.include_router(anime_router, prefix="/api/v1", tags=["anime"])
app.include_router(coincap_router, prefix="/api/v1", tags=["coincap"])
