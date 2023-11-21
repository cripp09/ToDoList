from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.src.auth.models import User
from app.src.database import get_async_session
from app.src.auth.base_config import current_user


router = APIRouter(
    prefix="/itsme",
    tags=["itsme"]
)

@router.get("/itsme")
def protected_route(user: User= Depends(current_user)):
    return f"Hello, {user.username}"

