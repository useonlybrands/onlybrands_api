from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     influencer = relationship("Influencer", back_populates="user")
#     brand = relationship("Brand", back_populates="user")
#     new_user = Column(Boolean, default=True)


class Influencer(Base):
    __tablename__ = "influencer"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    wallet = Column(String, index=True)
    platform = Column(String, index=True)
    industries = Column(String, index=True)
    follower_count = Column(Integer)
    language = Column(String)
    sex = Column(String)
    age = Column(Integer)
    rating = Column(Float)
    bids = relationship("Bid", back_populates="influencer")


class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    wallet = Column(String, index=True)
    industries = Column(String, index=True)
    language = Column(String)
    bids = relationship("Bid", back_populates="brand")


class Bid(Base):
    __tablename__ = "bid"
    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, index=True)
    platform = Column(String, index=True)
    influencer_id = Column(Integer, ForeignKey("influencer.id"))
    influencer = relationship("Influencer", back_populates="bids")
    brand_id = Column(Integer, ForeignKey("brand.id"))
    brand = relationship("Brand", back_populates="bids")
    title = Column(String, index=True)
    engagement_type = Column(String, index=True)
