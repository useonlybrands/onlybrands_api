from fastapi import APIRouter, Depends

from app.auth.views import get_token
from app.brand.tasks import process_create_brand, process_delete_brand
from app.schemas import Brand

brand_router = APIRouter()


@brand_router.post('/create_brand')
def create_brand(data: Brand, token: str = Depends(get_token)):
    return process_create_brand(data)



@brand_router.delete('/delete_brand')
def delete_brand(data: Brand, token: str = Depends(get_token)):
    return process_delete_brand(data.id)