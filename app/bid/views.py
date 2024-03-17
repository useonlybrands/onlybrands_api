from fastapi import APIRouter, Depends

from app import schemas
from app.auth.tasks import get_current_user
from app.bid.tasks import (
    process_create_bid,
    process_delete_bid,
    process_complete_bid,
    process_accepted_bid,
)
from app.schemas import User, CompleteBid

bid_router = APIRouter()


@bid_router.post("/create_bid/")
def create_bid(data: schemas.BidCreate, current_user: User = Depends(get_current_user)):
    return process_create_bid(data, current_user)


@bid_router.post("/accept_bid/{id}")
def accepted_bid(id: int, current_user: User = Depends(get_current_user)):
    return process_accepted_bid(id, current_user)


@bid_router.post("/complete_bid/")
def complete_bid(data: CompleteBid, current_user: User = Depends(get_current_user)):
    return process_complete_bid(data, current_user)


@bid_router.delete("/delete_bid/{id}")
def delete_bid(id: int, current_user: User = Depends(get_current_user)):
    return process_delete_bid(id, current_user)
