from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from jinja2 import Environment, FileSystemLoader
from app.src.auth.models import User
from app.src.database import get_async_session, get_session
from fastapi import HTTPException
import smtplib
from email.mime.text import MIMEText

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

# Запрос данных из базы данных
async def get_data(user):
    async with get_session() as session:
        query = text(f"SELECT * FROM task WHERE user_id = {user} ")
        result = await session.execute(query)
        data = result.fetchall()
    return data


def send_mail_verify(user, token):
    # Загружаем шаблон email
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("send_mail_token.html")
    html_content = template.render(token=token, username=user.username)
    message = MIMEText(html_content, "html")

    server = smtplib.SMTP('178.236.247.244')
    email_from = "support@xn--80aapsk0acddg.xn--p1ai"
    email_to = user.email
    try:
        message["From"] = email_from
        message["To"] = email_to
        message["Subject"] = "Верификация почты!"
        server.sendmail(email_from, email_to, message.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Не удалось отправить письмо: {str(e)}")
