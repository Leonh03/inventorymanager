# db.py
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

MONGO_URL = "mongodb://localhost:27017"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URL)

# Database name: InventoryManager
db = client.InventoryManager

config_collection = db.config
inventory_collection = db.inventory

config_collection.create_index([("masterEmail", ASCENDING)], unique=True)
