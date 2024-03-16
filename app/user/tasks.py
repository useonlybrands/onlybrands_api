from fastapi import HTTPException
from app.database import SessionLocal
from app.models import User

db = SessionLocal()


def process_get_user(user_id):
    # Fetch the user with the given ID from the database
    user = db.query(User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
