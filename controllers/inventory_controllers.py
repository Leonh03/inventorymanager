from db import config_collection
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from pydantic import SecretStr

