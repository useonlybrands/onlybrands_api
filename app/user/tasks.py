from fastapi import HTTPException

from app.database import SessionLocal
from app.models import Influencer, Brand
from app.schemas import User
from sqlalchemy.orm import joinedload

db = SessionLocal()

def process_get_user(username: str):
    # Fetch the influencer and brand with the given username from the database
    influencer = db.query(Influencer).options(joinedload(Influencer.user)).filter(Influencer.username == username).first()
    brand = db.query(Brand).options(joinedload(Brand.user)).filter(Brand.username == username).first()

    # If neither an influencer nor a brand with the given username is found, raise a 404 error
    if influencer is None and brand is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Create a User instance with the associated influencer or brand dict
    user = User(
        username=username,
        email=influencer.email if influencer else brand.email,
        new_user=influencer.user.new_user if influencer else brand.user.new_user,
        influencer=influencer.__dict__ if influencer else None,
        brand=brand.__dict__ if brand else None,
    )

    return user