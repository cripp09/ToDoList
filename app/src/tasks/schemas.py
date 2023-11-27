from datetime import datetime

from pydantic import BaseModel

class TaskModel(BaseModel):
    id: int
    user_id: int
    created_at: datetime

class PostTaskModel(BaseModel):
    title: str
    content: str
    status: str
    priorty: str
    completion_date: str
    project_name: str
    remind_date: str
