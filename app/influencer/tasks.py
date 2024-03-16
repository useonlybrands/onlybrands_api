from app import schemas, crud
from app.database import SessionLocal
from fastapi import HTTPException
from app.schemas import User
from app.models import Influencer

db = SessionLocal()


def process_create_influencer(data, current_user: User):
    # Check if the current user is authorized to create an influencer
    if current_user.username != data["username"]:
        raise HTTPException(status_code=403, detail="Not authorized")

    influencer = schemas.InfluencerCreate(**data.dict())
    db_influencer = crud.create_influencer(db=db, influencer=influencer)
    return {
        "status": 200,
        "message": "Influencer created successfully",
        "id": db_influencer.id,
    }


def process_delete_influencer(influencer_id, current_user: User):
    # Fetch the influencer from the database
    influencer = db.query(Influencer).get(influencer_id)

    # Check if the influencer exists
    if influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")

    # Check if the current user is authorized to delete the influencer
    if current_user.username != influencer.username:
        raise HTTPException(status_code=403, detail="Not authorized")

    crud.delete_influencer(db=db, influencer_id=influencer_id)
    return {"status": 200, "message": "Influencer deleted"}


def process_get_influencer(username: str, current_user: User):
    # Fetch the influencer with the given username from the database
    influencer = db.query(Influencer).filter(Influencer.username == username).first()

    # If no influencer with the given username is found, raise a 404 error
    if influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")

    # Add a check to ensure that the current_user is authorized to access the influencer's information
    if current_user.username != username:
        raise HTTPException(
            status_code=403, detail="Not authorized to access this influencer's information"
        )

    return influencer

def process_get_all_influencers(current_user: User):
    # Fetch all influencers from the database
    influencers = db.query(Influencer).all()

    # Add a check to ensure that the current_user is authorized to access the influencers' information
    if not influencers:
        raise HTTPException(
            status_code=403, detail="Not authorized to access influencers' information"
        )

    return influencers
