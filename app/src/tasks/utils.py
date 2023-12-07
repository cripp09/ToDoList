from datetime import datetime
from app.src.auth.schemas import UserRead
from app.src.tasks.schemas import TaskModel
from app.src.tasks.models import task_table
from app.src.database import get_session
from datetime import datetime
from sqlalchemy import text


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


async def get_task_with_id(user: UserRead, task: TaskModel):
    async with get_session() as session:
        query = text(f"SELECT * FROM task WHERE user_id = {user.id} AND id = {task}")
        result = await session.execute(query)
        data = result.fetchall()
        print(data)
    return data