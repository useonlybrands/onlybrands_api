from app import schemas, crud
from app.database import SessionLocal
from fastapi import HTTPException
from app.schemas import User
from app.models import Influencer
from devtools import debug

db = SessionLocal()


def create_or_update_influencer(data, current_user: User):
    # Check if the current user is authorized to create an influencer
    if current_user.username != data.username and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Check if the influencer already exists by username or email
    influencer = (
        db.query(Influencer)
        .filter(
            (Influencer.username == data.username) | (Influencer.email == data.email)
        )
        .first()
    )

    # If the influencer does not exist, create a new one
    if not influencer:
        influencer = schemas.InfluencerCreate(**data.dict())
        db_influencer = crud.create_influencer(db=db, influencer=influencer)
        return {
            "status": 200,
            "message": "Influencer created successfully",
            "id": db_influencer.id,
        }

    # If the influencer exists, update it
    else:
        updated_influencer = crud.update_influencer(db=db, influencer=influencer, data=data)
        return {
            "status": 200,
            "message": "Influencer updated successfully",
            "id": updated_influencer.id,
        }


def process_delete_influencer(username, current_user: User):
    # Fetch the influencer from the database
    influencer = db.query(Influencer).filter(Influencer.username == username).first()

    # Check if the influencer exists
    if influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")

    # Check if the current user is authorized to delete the influencer
    if current_user.username != influencer.username and not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="current user is not equal to the deleting influencer",
        )

    crud.delete_influencer(db=db, influencer_id=influencer.id)
    return {"status": 200, "message": "Influencer deleted"}


def process_get_influencer(username: str, current_user: User):
    debug(username)
    debug(current_user)
    if current_user is None:
        raise HTTPException(status_code=403, detail="current user not passed")

    influencer = db.query(Influencer).filter(Influencer.username == username).first()
    if influencer is None:
        raise HTTPException(
            status_code=404, detail="Influencer not found in the database"
        )
    return influencer


def process_get_all_influencers(current_user: User):
    if current_user is None:
        raise HTTPException(status_code=403, detail="Not authorized")

    influencers = db.query(Influencer).all()
    return influencers
