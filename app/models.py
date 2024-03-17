from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Influencer(Base):
    __tablename__ = "influencer"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    username = Column(String, index=True, unique=True)
    image = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    wallet = Column(String, index=True, nullable=True)
    platform = Column(String, index=True, nullable=True)
    industries = Column(String, index=True, nullable=True)
    follower_count = Column(Integer, nullable=True)
    language = Column(String, nullable=True)
    sex = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    rating = Column(Float, nullable=True)
    bids = relationship("Bid", back_populates="influencer")


class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    username = Column(String, index=True, unique=True)
    image = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    website = Column(String, index=True, nullable=True)
    location = Column(String, index=True, nullable=True)
    size = Column(String, index=True, nullable=True)
    wallet = Column(String, index=True, nullable=True)
    industries = Column(String, index=True, nullable=True)
    language = Column(String, nullable=True)
    bids = relationship("Bid", back_populates="brand")


class Bid(Base):
    __tablename__ = "bid"
    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, index=True, nullable=True)
    platform = Column(String, index=True, nullable=True)
    influencer_username = Column(String, index=True, nullable=True)
    influencer_id = Column(Integer, ForeignKey("influencer.id"), nullable=True)
    influencer = relationship("Influencer", back_populates="bids")
    brand_username = Column(String, index=True, nullable=True)
    brand_id = Column(Integer, ForeignKey("brand.id"), nullable=True)
    brand = relationship("Brand", back_populates="bids")
    title = Column(String, index=True, nullable=True)
    engagement_type = Column(String, index=True, nullable=True)
    evidence = Column(String, index=True, nullable=True)
