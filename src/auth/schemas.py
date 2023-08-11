import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr


class TunedModel(BaseModel):
    class Config:
        """Tells pydantic to convert even not dict obj into json"""


class ShowUser(TunedModel):
    id: uuid.UUID
    username: str
    name: str
    surname: str
    hashed_password: str
    email: EmailStr
    registered_at: datetime
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    username: str
    email: EmailStr
    hashed_password: str
