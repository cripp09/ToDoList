from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.src.auth.models import User
from app.src.database import get_async_session
from app.src.auth.base_config import current_user
from app.src.auth.schemas import UserCreate, UserRead

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    #prefix="/itsme",
    #tags=["itsme"]
)

@router.get("/itsme")
def protected_route(user: User= Depends(current_user)):
    return f"Hello, {user.username}"

@router.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
 
@router.get("/sign_in")
def sign_in_get(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request":request})

'''@router.post("/auth/jwt/login")
def sign_in_post(email: str = Form(...), password: str = Form(...)):
    print(email, password)
    return RedirectResponse("/", status_code=303)'''