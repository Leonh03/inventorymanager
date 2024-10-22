# models.py
from pydantic import BaseModel, EmailStr, SecretStr

class ConfigUpdateModel(BaseModel):
    masterEmail: EmailStr
    viagogoMail: EmailStr
    viagogoPassword: str  # Just use a regular string

