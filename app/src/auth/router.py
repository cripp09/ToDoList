from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from app.src.auth.models import User
from app.src.auth.base_config import current_user
from app.src.auth.utils import get_data
from app.src.database import get_session


templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
)

@router.get("/itsme")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@router.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
 
@router.get("/sign_in")
def sign_in_get(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request":request})


@router.get("/dashboard")
async def sign_in_get(request: Request, user: User = Depends(current_user)):
    username = user.username
    data = await get_data(user.id)
          
    return templates.TemplateResponse("dashboard.html", {"request":request,
                                                         'username': username,
                                                         "data": data})