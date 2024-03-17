from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    email: str
    new_user: Optional[bool] = None
    influencer: Optional[dict] = None
    brand: Optional[dict] = None
    is_superuser: Optional[bool] = False


class TokenData(BaseModel):
    username: str
    email: str
    new_user: bool
    is_superuser: bool


class CompleteBid(BaseModel):
    bid_id: int
    evidence: str


class WorldVerify(BaseModel):
    proof: str
    action_id: str


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
    state: Optional[str] = None  # pending, denied, accepted, completed
    platform: Optional[str] = None
    influencer_username: Optional[str] = None
    influencer_id: Optional[int] = None
    influencer: Optional[Influencer] = None
    brand_username: Optional[str] = None
    brand_id: Optional[int] = None
    brand: Optional[Brand] = None
    title: Optional[str] = None
    engagement_type: Optional[str] = None
    evidence: Optional[str] = None


class BidCreate(BidBase):
    pass


class Bid(BidBase):
    id: int

    class Config:
        from_attributes = True


class UnauthorizedMessage(BaseModel):
    detail: str = "Bearer token missing or unknown"
