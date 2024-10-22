# routes/user_routes.py

from fastapi import APIRouter
from controllers import inventory_controllers  # Import your controller
import requests


router = APIRouter()

@router.get("/inventory/getAllTickets")
async def fetch_details(event_id: str):
    return await inventory_controllers.fetch_details(event_id)

