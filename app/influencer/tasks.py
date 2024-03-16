from . import crud, schemas
from app.database import SessionLocal

def process_create_influencer(data):
    db = SessionLocal()
    influencer = schemas.InfluencerCreate(**data.dict())
    db_influencer = crud.create_influencer(db=db, influencer=influencer)
    return {'status': 200, 'message': 'Influencer created successfully', 'id': db_influencer.id}

def process_delete_influencer(influencer_id):
    db = SessionLocal()
    crud.delete_influencer(db=db, influencer_id=influencer_id)
    return {'status': 200, 'message': 'Influencer deleted'}