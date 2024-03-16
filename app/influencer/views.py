from fastapi import APIRouter, Depends

from app import schemas
from app.auth.tasks import get_current_user
from app.influencer.tasks import process_create_influencer, process_delete_influencer
from app.schemas import Influencer, User

influencer_router = APIRouter()


@influencer_router.post("/create_influencer/")
def create_influencer(
    data: schemas.InfluencerCreate, current_user: User = Depends(get_current_user)
):
    return process_create_influencer(data, current_user)


@influencer_router.delete("/delete_influencer/")
def delete_influencer(data: Influencer, current_user: User = Depends(get_current_user)):
    return process_delete_influencer(data.id, current_user)
