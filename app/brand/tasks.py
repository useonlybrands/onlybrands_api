from app import schemas, crud
from app.database import SessionLocal
from fastapi import HTTPException
from app.schemas import User
from app.models import Brand

db = SessionLocal()


def process_create_brand(data, current_user: User):
    # Check if the current user is authorized to create a brand
    if current_user.username != data["username"]:
        raise HTTPException(status_code=403, detail="Not authorized")

    brand = schemas.BrandCreate(**data.dict())
    db_brand = crud.create_brand(db=db, brand=brand)
    return {"status": 200, "message": "Brand created successfully", "id": db_brand.id}


def process_delete_brand(brand_id, current_user: User):
    # Fetch the brand from the database
    brand = db.query(Brand).get(brand_id)

    # Check if the brand exists
    if brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    # Check if the current user is authorized to delete the brand
    if current_user.username != brand.username:
        raise HTTPException(status_code=403, detail="Not authorized")

    crud.delete_brand(db=db, brand_id=brand_id)
    return {"status": 200, "message": "Brand deleted"}
