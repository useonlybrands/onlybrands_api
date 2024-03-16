import logging
import logfire

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.models import Base
from app.brand.views import brand_router
from app.database import SessionLocal, engine
from app.influencer.views import influencer_router
from app.bid.views import bid_router
from app.utils import settings


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("startup")

    # Initialize the database
    with SessionLocal():
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)

    yield

    logging.info("shutdown")


app = FastAPI(lifespan=lifespan)

if (
    bool(settings.logfire_token)
    and settings.testing is False
    and settings.dev_mode is False
):
    logfire.configure()
    logfire.instrument_fastapi(app)

app.include_router(influencer_router)
app.include_router(brand_router)
app.include_router(bid_router)
