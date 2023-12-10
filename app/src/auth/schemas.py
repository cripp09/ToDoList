from fastapi_users import schemas
from typing import Optional
from pydantic import BaseModel

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    
    class Config:
        from_attributes = True

class UserCreate(schemas.BaseUserCreate):
    username :str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserProfile(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    photo: bytes


