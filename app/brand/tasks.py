from . import crud, schemas
from app.database import SessionLocal

def process_create_brand(data):
    db = SessionLocal()
    brand = schemas.BrandCreate(**data.dict())
    db_brand = crud.create_brand(db=db, brand=brand)
    return {'status': 200, 'message': 'Brand created successfully', 'id': db_brand.id}

def process_delete_brand(brand_id):
    db = SessionLocal()
    crud.delete_brand(db=db, brand_id=brand_id)
    return {'status': 200, 'message': 'Brand deleted'}