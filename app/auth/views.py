from fastapi import APIRouter, Depends

from app import schemas
from app.auth.tasks import get_current_user
from app.auth.tasks import (
    process_world_verify,
)
from app.user.views import user_router
from app.schemas import Bid, User

@user_router.post("/world_verify/")
def world_verify(
    proof: object, action_id: str
):
    return process_world_verify(proof, action_id)