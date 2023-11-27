from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.src.tasks.models import task_table
from sqlalchemy import text


from app.src.auth.models import User
from app.src.database import get_async_session, get_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

# Запрос данных из базы данных
async def get_data(user):
    async with get_session() as session:
        query = text(f"SELECT * FROM task where user_id = {user} ")
        result = await session.execute(query)
        print(result)
        data = result.fetchall()
        print(data)
    return data
