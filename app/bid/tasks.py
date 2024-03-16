from . import crud, schemas
from app.database import SessionLocal


def process_create_bid(data):
    db = SessionLocal()
    bid = schemas.BidCreate(**data.dict())
    db_bid = crud.create_bid(db=db, bid=bid)
    return {'status': 200, 'message': 'Bid created successfully', 'id': db_bid.id}


def process_accepted_bid(data):
    db = SessionLocal()
    bid = schemas.BidCreate(**data.dict())
    db_bid = crud.create_bid(db=db, bid=bid)
    return {'status': 200, 'message': 'Bid accepted successfully', 'id': db_bid.id}

def process_complete_bid(data):
    db = SessionLocal()
    bid = schemas.BidCreate(**data.dict())
    db_bid = crud.create_bid(db=db, bid=bid)
    return {'status': 200, 'message': 'Bid completed successfully', 'id': db_bid.id}

def process_delete_bid(bid_id):
    db = SessionLocal()
    crud.delete_bid(db=db, bid_id=bid_id)
    return {'status': 200, 'message': 'Bid deleted'}
