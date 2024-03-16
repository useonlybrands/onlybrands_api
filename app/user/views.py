from fastapi import APIRouter, Depends

from app.auth.tasks import get_current_user
from app.user.tasks import process_get_user
from app.schemas import User

user_router = APIRouter()


@user_router.get("/user/{username}")
def get_user(username: str, current_user: User = Depends(get_current_user)):
    return process_get_user(username, current_user)
