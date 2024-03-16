from fastapi import APIRouter, Depends

from app.oracle.tasks import process_verify_image

oracle_router = APIRouter()

@oracle_router.get("/verify_image/{url}")
def verify_image(url: str):
    return process_verify_image(url)
