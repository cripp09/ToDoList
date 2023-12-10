from datetime import datetime
from app.src.auth.models import profile
from app.src.auth.schemas import UserRead
from app.src.tasks.schemas import TaskModel
from app.src.tasks.models import task_table
from app.src.database import get_session
from datetime import datetime
from sqlalchemy import text

import base64
from PIL import Image
from io import BytesIO
import psycopg2


async def create_task(task: TaskModel, user: UserRead):
    async with get_session() as session:
        query = await session.execute(
            task_table.insert()
            .values(
                user_id=user,
                created_at=datetime.now(),
                title=task.title,
                content=task.content,
                status=task.status,
                priorty=task.priorty,
                completion_date=datetime.strptime(task.completion_date, '%Y-%m-%d %H:%M'),
                project_name=task.project_name,
                remind_date=task.remind_date,
            )
            
        )

        await session.commit()
        return query

async def profile_edit(prof, user):
    '''image_data = base64.b64decode(prof.photo)
    image = Image.open(BytesIO(image_data))
    #img_byte = image.tobytes()
    image_src = "app/static/img/"+ str(user.id) + "_" + user.username +".png"
    #image = psycopg2.Binary(image_data)'''

    image_data = base64.b64decode(prof.photo)
    image = Image.open(BytesIO(image_data))
    image.save("app/static/img/"+ str(user.id) + "_" + user.username +".png")
    image_src = "img/" + str(user.id) + "_" + user.username +".png"
    async with get_session() as session:
        query = await session.execute(
            profile.update()
            .values(
                first_name=prof.first_name,
                last_name=prof.last_name,
                date_of_birth=datetime.strptime(prof.date_of_birth, '%Y-%m-%d'),
                photo=image_src,
            )
            .where(profile.c.user_id==user.id)
        )
        await session.commit()
        return query


async def get_task_with_id(user: UserRead, task: TaskModel):
    async with get_session() as session:
        query = text(f"SELECT * FROM task WHERE user_id = {user.id} AND id = {task}")
        result = await session.execute(query)
        data = result.fetchall()
    return data

async def get_profile_with_id(user):
    async with get_session() as session:
        query = text(f"SELECT * FROM profile WHERE user_id = {user}")
        result = await session.execute(query)
        data = result.fetchall()
        return data
    