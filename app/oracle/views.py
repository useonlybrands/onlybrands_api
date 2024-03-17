from fastapi import APIRouter

from app.oracle.tasks import process_verify_image

oracle_router = APIRouter()


@oracle_router.get("/verify_image")
def verify_image(url: str = None):
    if url is None:
        return {"status": 400, "error": "URL parameter is missing"}
    return process_verify_image(url)
