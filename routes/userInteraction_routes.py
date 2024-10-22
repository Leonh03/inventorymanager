# userInteraction_routes.py
from fastapi import APIRouter, Depends
from models.models import ConfigUpdateModel
from controllers.userInteraction_controllers import updateConfig

router = APIRouter()

@router.post("/config/update")
async def fetch_details(config_data: ConfigUpdateModel):
    return await updateConfig(config_data)
