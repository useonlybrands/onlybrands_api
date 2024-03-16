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
