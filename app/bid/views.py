from fastapi import APIRouter, Depends

from app.auth.views import get_token
from app.bid.tasks import process_create_bid, process_delete_bid, process_complete_bid, process_accepted_bid
from app.models import Bid

bid_router = APIRouter()


@bid_router.post('/create_bid')
def create_bid(data: Bid, token: str = Depends(get_token)):
    return process_create_bid(data)

@bid_router.post('/accepted_bid')
def accepted_bid(data: Bid, token: str = Depends(get_token)):
    return process_accepted_bid(data)

@bid_router.post('/complete_bid')
def complete_bid(data: Bid, token: str = Depends(get_token)):
    return process_complete_bid(data)

@bid_router.delete('/delete_bid')
def delete_bid(data: Bid, token: str = Depends(get_token)):
    return process_delete_bid(data.id)