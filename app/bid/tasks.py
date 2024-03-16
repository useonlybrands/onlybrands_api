from app import crud, schemas
from app.database import SessionLocal
from fastapi import HTTPException
from app.models import Bid
from app.schemas import User

db = SessionLocal()


def process_create_bid(data, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(data.bid_id)

    # Check if the bid exists and if the current user is the associated brand
    if bid is None or bid.brand.username != current_user.username:
        raise HTTPException(status_code=403, detail="current username does not match bid.brand.username")

    bid = schemas.BidCreate(**data.dict())
    db_bid = crud.create_bid(db=db, bid=bid)
    return {"status": 200, "message": "Bid created successfully", "id": db_bid.id}


def process_accepted_bid(data, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(data.bid_id)

    # Check if the bid exists and if the current user is the associated influencer
    if bid is None or bid.influencer.username != current_user.username:
        raise HTTPException(status_code=403, detail="current username does not match bid.influencer.username")

    bid.state = "accepted"
    db.commit()
    return {"status": 200, "message": "Bid accepted successfully", "id": bid.id}


def process_complete_bid(data, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(data.bid_id)

    # Check if the bid exists and if the current user is the associated influencer
    if bid is None or bid.influencer.username != current_user.username:
        raise HTTPException(status_code=403, detail="current username does not match bid.influencer.username")

    bid.state = "completed"
    db.commit()
    return {"status": 200, "message": "Bid completed successfully", "id": bid.id}


def process_delete_bid(bid_id, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(bid_id)

    # Check if the bid exists and if the current user is the associated brand
    if bid is None or bid.brand.username != current_user.username:
        raise HTTPException(status_code=403, detail="current username does not match bid.brand.username")

    crud.delete_bid(db=db, bid_id=bid_id)
    return {"status": 200, "message": "Bid deleted"}
