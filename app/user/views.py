from fastapi import APIRouter, Depends
from app.user.tasks import process_get_user
from app.auth.views import get_token

user_router = APIRouter()

@user_router.get("/user/{username}")
def get_user(username: str, token: str = Depends(get_token)):
    return process_get_user(username)
