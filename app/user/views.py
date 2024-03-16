from fastapi import APIRouter, Depends
from app.user.tasks import process_get_user
from app.auth.views import get_token

user_router = APIRouter()

@user_router.get("/user/{user_id}")
def get_user(user_id: int, token: str = Depends(get_token)):
    return process_get_user(user_id)
