from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from app.src.auth.models import User
from app.src.auth.base_config import current_user
from app.src.tasks.schemas import PostTaskModel
from app.src.tasks import utils
from datetime import datetime  


templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
)

@router.post("/dashboard")
async def create_task_func(request: Request, task: PostTaskModel, c_user: User = Depends(current_user)):
    print(c_user.id)
    print(task)
    
    task1 = await utils.create_task(task, c_user.id)
   
    return templates.TemplateResponse("dashboard.html", {"request":request})