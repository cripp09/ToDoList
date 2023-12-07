from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.src.auth.models import User
from app.src.auth.base_config import current_user
from app.src.tasks.schemas import PostTaskModel,PostTaskModelWithId
from app.src.tasks.utils import create_task, get_task_with_id
from app.src.auth.utils import get_data
import json

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
)

@router.post("/dashboard/{page}")
async def create_task_func(page: int,request: Request, task: PostTaskModel, user: User = Depends(current_user)):
    await create_task(task, user.id)
    data =  await get_data(user.id)
    
    total_items = len(data)
    items_per_page = 5# Количество элементов на одной странице
    total_pages = total_items // items_per_page
    offset = (page - 1) * items_per_page
    items = data[offset:offset + items_per_page]

    template = templates.get_template('dashboard_update.html')
    html_content = template.render(items = items,
                                    page = page,
                                    total_pages = total_pages)
    return JSONResponse(content = html_content)


@router.post("/dashboard/")
async def task_with_id(request: Request, task: PostTaskModelWithId, user: User = Depends(current_user)):
    print(task.id)
    items =  await get_task_with_id(user, task.id)
    template = templates.get_template('dashboard_modal_task.html')
    html_content = template.render(items = items)
    
    return JSONResponse(content = html_content)