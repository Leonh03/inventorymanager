# userInteraction_controllers.py
from models.models import ConfigUpdateModel
from db import config_collection
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from pydantic import SecretStr

def serialize_mongo_doc(doc):
    """Convert ObjectId to string for MongoDB documents."""
    if not doc:
        return doc
    doc["_id"] = str(doc["_id"])
    return doc

async def updateConfig(config_data: ConfigUpdateModel):
    update_data = config_data.dict()
    try:
        result = await config_collection.update_one(
            {"masterEmail": update_data["masterEmail"]},
            {"$set": update_data},
            upsert=True
        )

        updated_doc = await config_collection.find_one({"masterEmail": update_data["masterEmail"]})
        updated_doc = serialize_mongo_doc(updated_doc)

        if result.modified_count > 0:
            return {
                "success": True,
                "message": "Configuration updated successfully",
                "updated_data": updated_doc
            }
        elif result.upserted_id:
            return {
                "success": True,
                "message": "New configuration inserted successfully",
                "updated_data": updated_doc
            }
        else:
            return {
                "success": True,
                "message": "No changes were made, data already up to date",
                "updated_data": updated_doc
            }
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Configuration with this masterEmail already exists.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
