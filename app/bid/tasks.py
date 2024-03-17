from app import crud
from app.database import SessionLocal
from fastapi import HTTPException
from app.models import Bid, Influencer, Brand
from app.schemas import User

db = SessionLocal()


def process_create_or_update_bid(data, current_user: User):
    # Check if the current user is authorized to create a bid
    if current_user.username != data.brand_username and not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="current user does not match creating bid username",
        )

    # a brand creates a bid therefore the brand_username is required
    if data.brand_username:
        brand = db.query(Brand).filter(Brand.username == data.brand_username).first()
        if brand is None:
            raise HTTPException(
                status_code=404, detail="Brand not found in the database"
            )

        data.brand_id = brand.id
        data.brand = brand
    else:
        raise HTTPException(
            status_code=404, detail="brand_username is required to create a bid."
        )

    # set the brand status default to pending
    data.state = data.state if data.state else "pending"

    # Check if the bid already exists by title
    bid = (
        db.query(Bid)
        .filter(Bid.title == data.title)
        .first()
    )

    # If the bid does not exist, create a new one
    if not bid:
        bid = Bid(
            state=data.state,
            platform=data.platform,
            influencer_username=data.influencer_username,
            influencer_id=data.influencer_id,
            influencer=data.influencer,
            brand_username=data.brand_username,
            brand_id=data.brand_id,
            brand=data.brand,
            title=data.title,
            engagement_type=data.engagement_type,
        )
        db_bid = crud.create_bid(db=db, bid=bid)
        return {"status": 200, "message": "Bid created successfully", "id": db_bid.id}

    # If the bid exists, update it
    else:
        updated_bid = crud.update_bid(db=db, bid=bid, data=data)
        return {"status": 200, "message": "Bid updated successfully", "id": updated_bid.id}


def process_accepted_bid(bid_id: int, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(bid_id)

    # Check if the bid exists and if the current user is the associated influencer
    if bid is None:
        raise HTTPException(
            status_code=403,
            detail="Bid not found in the database",
        )

    # get influencer
    influencer = (
        db.query(Influencer)
        .filter(Influencer.username == current_user.username)
        .first()
    )

    # update the bid with influencer
    bid.influencer_id = influencer.id
    bid.influencer = influencer
    bid.state = "accepted"
    db.commit()
    return {"status": 200, "message": "Bid accepted successfully", "id": bid.id}


def process_complete_bid(data, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(data.bid_id)

    # Check if the bid exists and if the current user is the associated influencer
    if bid is None:
        raise HTTPException(
            status_code=403,
            detail="Bid not found in the database",
        )

    # get influencer
    influencer = (
        db.query(Influencer)
        .filter(Influencer.username == current_user.username)
        .first()
    )

    # check the influencer is the one who accepted the bid
    if influencer.id != bid.influencer_id:
        raise HTTPException(
            status_code=403,
            detail="influencer does not match the one who accepted the bid",
        )

    bid.state = "completed"
    bid.evidence = data.evidence
    db.commit()
    return {"status": 200, "message": "Bid accepted successfully", "id": bid.id}


def process_delete_bid(bid_id, current_user: User):
    # Fetch the bid from the database
    bid = db.query(Bid).get(bid_id)

    # Check if the bid exists and if the current user is the associated brand
    if (
        bid is None
        or bid.brand_username != current_user.username
        and not current_user.is_superuser
    ):
        raise HTTPException(
            status_code=403, detail="current username does not match bid.brand.username"
        )

    crud.delete_bid(db=db, bid_id=bid_id)
    return {"status": 200, "message": "Bid deleted"}
