import logging
import logfire

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.views import auth_router
from app.models import Base
from app.database import SessionLocal, engine
from app.brand.views import brand_router
from app.influencer.views import influencer_router
from app.bid.views import bid_router
from app.oracle.views import oracle_router
from app.user.views import user_router
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

origins = [
    "http://localhost:3000",  # Allow localhost for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if bool(settings.logfire_token):
    logfire.configure()
    logfire.instrument_fastapi(app)

app.include_router(influencer_router)
app.include_router(brand_router)
app.include_router(bid_router)
app.include_router(user_router)
app.include_router(oracle_router)
app.include_router(auth_router)
