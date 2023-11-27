from datetime import datetime
from app.src.auth.schemas import UserRead
from app.src.tasks.schemas import TaskModel
from app.src.tasks.models import task_table
from app.src.database import get_session
from datetime import datetime


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