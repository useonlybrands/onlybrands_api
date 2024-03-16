from pydantic import BaseModel
from typing import Optional

class InfluencerBase(BaseModel):
    email: str
    wallet: str
    platform: str
    industries: str
    follower_count: int
    language: str
    sex: str
    age: int
    rating: float

class InfluencerCreate(InfluencerBase):
    pass

class Influencer(InfluencerBase):
    id: int

    class Config:
        from_attributes = True

class BrandBase(BaseModel):
    name: str
    email: str
    wallet: str
    industries: str
    language: str

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    id: int

    class Config:
        from_attributes = True

class BidBase(BaseModel):
    state: str
    platform: str
    influencer_id: int
    brand_id: int
    title: str
    engagement_type: str

class BidCreate(BidBase):
    pass

class Bid(BidBase):
    id: int

    class Config:
        from_attributes = True


class UnauthorizedMessage(BaseModel):
    detail: str = 'Bearer token missing or unknown'