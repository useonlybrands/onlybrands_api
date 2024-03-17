from fastapi import APIRouter

from app.auth.tasks import process_world_verify
from app.schemas import WorldVerify

auth_router = APIRouter()


@auth_router.post("/world_verify/")
def world_verify(data: WorldVerify):
    return process_world_verify(data.proof, data.action_id)
