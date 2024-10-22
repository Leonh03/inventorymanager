# routes/user_routes.py

from fastapi import APIRouter
from controllers import collection_controllers  # Import your controller
import requests


router = APIRouter()

@router.post("/collection/add")
async def fetch_details(event_id: str):
    return await collection_controllers.fetch_details(event_id)

