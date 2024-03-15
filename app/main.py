import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info('startup')
    yield


app = FastAPI(lifespan=lifespan)



