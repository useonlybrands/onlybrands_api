from fastapi import HTTPException

from app.database import SessionLocal
from app.models import Influencer, Brand
from app.schemas import User
import sqlalchemy

db = SessionLocal()


def to_dict(model_instance):
    return {c.key: getattr(model_instance, c.key)
            for c in sqlalchemy.inspect(model_instance).mapper.column_attrs}


def process_get_user(username: str, current_user: User):
    # Fetch the influencer and brand with the given username from the database
    influencer = db.query(Influencer).filter(Influencer.username == username).first()
    brand = db.query(Brand).filter(Brand.username == username).first()

    # If neither an influencer nor a brand with the given username is found, raise a 404 error
    if influencer is None and brand is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Create a User instance with the associated influencer or brand dict
    user = User(
        username=username,
        email=influencer.email if influencer else brand.email if brand else None,
        influencer=to_dict(influencer) if influencer else None,
        brand=to_dict(brand) if brand else None,
    )

    # Add a check to ensure that the current_user is authorized to access the requested user's information
    if current_user.username != username:
        raise HTTPException(
            status_code=403, detail="Not authorized to access this user's information"
        )

    return user
