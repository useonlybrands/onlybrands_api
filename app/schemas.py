from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    email: str
    new_user: bool
    influencer: dict
    brand: dict


class TokenData(BaseModel):
    username: str
    email: str
    new_user: bool


class InfluencerBase(BaseModel):
    name: Optional[str] = None
    username: str
    image: Optional[str] = None
    email: Optional[str] = None
    wallet: Optional[str] = None
    platform: Optional[str] = None
    industries: Optional[str] = None
    follower_count: Optional[int] = None
    language: Optional[str] = None
    sex: Optional[str] = None
    age: Optional[int] = None
    rating: Optional[float] = None


class InfluencerCreate(InfluencerBase):
    pass


class Influencer(InfluencerBase):
    id: int

    class Config:
        from_attributes = True


class BrandBase(BaseModel):
    name: Optional[str] = None
    username: str
    image: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    size: Optional[str] = None
    wallet: Optional[str] = None
    industries: Optional[str] = None
    language: Optional[str] = None


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int

    class Config:
        from_attributes = True


class BidBase(BaseModel):
    state: Optional[str] = None
    platform: Optional[str] = None
    title: Optional[str] = None
    engagement_type: Optional[str] = None


class BidCreate(BidBase):
    pass


class Bid(BidBase):
    id: int

    class Config:
        from_attributes = True


class UnauthorizedMessage(BaseModel):
    detail: str = "Bearer token missing or unknown"
