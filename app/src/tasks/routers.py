from fastapi import APIRouter, Depends, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.src.auth.models import User
from app.src.auth.base_config import current_user
from app.src.tasks.schemas import PostTaskModel,PostTaskModelWithId
from app.src.tasks.utils import create_task, get_profile_with_id, get_task_with_id
from app.src.auth.utils import get_data
from app.src.auth.schemas import UserProfile
from app.src.tasks.utils import profile_edit


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

    html_content = template.render( request = request,
                                    items = items,
                                    page = page,
                                    total_pages = total_pages,)
    return JSONResponse(content = html_content)


@router.post("/dashboard/profile/user")
async def task_with_id(request: Request, user: User = Depends(current_user)):
    data = await get_profile_with_id(user.id)
    if data == []:
        template = templates.get_template('base_user_profile.html')
    else:
        template = templates.get_template('user_profile.html')
    print(data)
    html_content = template.render(request = request,
                                    user = user.username,
                                   data = data)
    
    return JSONResponse(content = html_content)


@router.post("/dashboard/profile/user/edit")
async def edit_profile(request: Request, profile: UserProfile, user: User = Depends(current_user)):
    await profile_edit(profile, user)
    print("successfully")

@router.post("/dashboard/")
async def task_with_id(request: Request, task: PostTaskModelWithId, user: User = Depends(current_user)):
    print(task.id)
    items =  await get_task_with_id(user, task.id)
    template = templates.get_template('dashboard_modal_task.html')
    html_content = template.render(items = items)
    
    return JSONResponse(content = html_content)