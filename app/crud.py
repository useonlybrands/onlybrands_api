from sqlalchemy.orm import Session
from . import models, schemas


def get_influencer(db: Session, influencer_id: int):
    return (
        db.query(models.Influencer)
        .filter(models.Influencer.id == influencer_id)
        .first()
    )


def get_influencers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Influencer).offset(skip).limit(limit).all()


def create_influencer(db: Session, influencer: schemas.InfluencerCreate):
    db_influencer = models.Influencer(**influencer.dict())
    db.add(db_influencer)
    db.commit()
    db.refresh(db_influencer)
    return db_influencer


def delete_influencer(db: Session, influencer_id: int):
    db_influencer = (
        db.query(models.Influencer)
        .filter(models.Influencer.id == influencer_id)
        .first()
    )
    db.delete(db_influencer)
    db.commit()
    return db_influencer


def get_brand(db: Session, brand_id: int):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()


def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(**brand.dict())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def delete_brand(db: Session, brand_id: int):
    db_brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    db.delete(db_brand)
    db.commit()


def get_bid(db: Session, bid_id: int):
    return db.query(models.Bid).filter(models.Bid.id == bid_id).first()


def get_bids(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bid).offset(skip).limit(limit).all()


def create_bid(db: Session, bid: models.Bid):
    db.add(bid)
    db.commit()
    db.refresh(bid)
    return bid


def delete_bid(db: Session, bid_id: int):
    db_bid = db.query(models.Bid).filter(models.Bid.id == bid_id).first()
    db.delete(db_bid)
    db.commit()
    return db_bid
