from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from app.src.auth.base_config import fastapi_users, auth_backend
from app.src.auth.schemas import UserCreate, UserRead
from app.src.auth.router import router as router_user
from app.src.tasks.routers import router as router_tasks

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
    )

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_user)
app.include_router(router_tasks)



