from fastapi import APIRouter, Depends

from app import schemas
from app.auth.views import get_current_user
from app.brand.tasks import process_create_brand, process_delete_brand
from app.schemas import Brand, User

brand_router = APIRouter()


@brand_router.post("/create_brand/")
def create_brand(
    data: schemas.BrandCreate, current_user: User = Depends(get_current_user)
):
    return process_create_brand(data, current_user)


@brand_router.delete("/delete_brand/")
def delete_brand(data: Brand, current_user: User = Depends(get_current_user)):
    return process_delete_brand(data.id, current_user)
