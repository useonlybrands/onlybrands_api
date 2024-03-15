from typing import List
from pydantic import BaseModel

class Influencer(BaseModel):
    email: str
    wallet: str
    platform: str
    industries: List[str]
    follower_count: int
    language: str
    sex: str
    age: int
    rating: float

class Brand(BaseModel):
    name: str
    email: str
    wallet: str
    industries: List[str]
    language: str

class Bid(BaseModel):
    state: List[str]
    platform: List[str]
    influencer: Influencer
    brand: Brand
    title: str
    engagement_type: list



class UnauthorizedMessage(BaseModel):
    detail: str = 'Bearer token missing or unknown'