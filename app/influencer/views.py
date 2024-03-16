from fastapi import APIRouter, Depends

from app.auth.views import get_token
from app.influencer.tasks import process_create_influencer, process_delete_influencer
from app.schemas import Influencer

influencer_router = APIRouter()


@influencer_router.post('/create_influencer')
def create_influencer(data: Influencer, token: str = Depends(get_token)):
    return process_create_influencer(data)



@influencer_router.delete('/delete_influencer')
def delete_influencer(data: Influencer, token: str = Depends(get_token)):
    return process_delete_influencer(data.id)