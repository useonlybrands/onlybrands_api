from fastapi import APIRouter, Depends

from app import schemas
from app.auth.tasks import get_current_user
from app.influencer.tasks import (
    create_or_update_influencer,
    process_delete_influencer,
    process_get_influencer,
    process_get_all_influencers,
)
from app.schemas import User

influencer_router = APIRouter()


@influencer_router.post("/influencer/")
def create_or_update_influencer(
    data: schemas.InfluencerCreate, current_user: User = Depends(get_current_user)
):
    return create_or_update_influencer(data, current_user)


@influencer_router.delete("/delete_influencer/{username}")
def delete_influencer(username: str, current_user: User = Depends(get_current_user)):
    return process_delete_influencer(username, current_user)


@influencer_router.get("/influencer/{username}")
def get_influencer(username: str, current_user: User = Depends(get_current_user)):
    return process_get_influencer(username, current_user)


@influencer_router.get("/all_influencers/")
def get_all_influencers(current_user: User = Depends(get_current_user)):
    return process_get_all_influencers(current_user)
