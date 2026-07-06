from fastapi import APIRouter

from app.api import mqtt

api_router = APIRouter()

api_router.include_router(mqtt.router, prefix="/mqtt", tags=["mqtt"])