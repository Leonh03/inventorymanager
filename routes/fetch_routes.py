# routes/user_routes.py

from fastapi import APIRouter
from controllers import fetch_controllers  # Import your controller
import requests


router = APIRouter()

@router.get("/fetch/details/{event_id}")
async def fetch_details(event_id: str):
    return await fetch_controllers.fetch_details(event_id)

