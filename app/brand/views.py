from fastapi import APIRouter, Depends

from app import schemas
from app.auth.tasks import get_current_user
from app.brand.tasks import (
    process_create_or_update_brand,
    process_delete_brand,
    process_get_brand,
    process_get_all_brands,
)
from app.schemas import User

brand_router = APIRouter()


@brand_router.put("/create_or_update_brand/")
def create_or_update_brand(
    data: schemas.BrandCreate, current_user: User = Depends(get_current_user)
):
    return process_create_or_update_brand(data, current_user)


@brand_router.delete("/delete_brand/{username}")
def delete_brand(username: str, current_user: User = Depends(get_current_user)):
    return process_delete_brand(username, current_user)


@brand_router.get("/brand/{username}")
def get_brand(username: str, current_user: User = Depends(get_current_user)):
    return process_get_brand(username, current_user)


@brand_router.get("/all_brands/")
def get_all_brands(current_user: User = Depends(get_current_user)):
    return process_get_all_brands(current_user)
