import sqlalchemy
from  app.src.database import Base
from sqlalchemy import Column
from app.src.auth.models import user
from sqlalchemy import ForeignKey, DateTime, String, Text


metadata = sqlalchemy.MetaData()


task_table = sqlalchemy.Table(
    "task",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(user.c.id)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("content", sqlalchemy.Text()),
    sqlalchemy.Column("status", sqlalchemy.String(100)),
    sqlalchemy.Column("priorty", sqlalchemy.String(100)),
    sqlalchemy.Column("completion_date", sqlalchemy.DateTime()),
    sqlalchemy.Column("project_name", sqlalchemy.String(100)),
    sqlalchemy.Column("remind_date", sqlalchemy.String(100)),
)   
