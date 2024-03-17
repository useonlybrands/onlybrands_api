import os
from fastapi.testclient import TestClient

from app.brand.tasks import process_create_brand
from app.main import app
from app.utils import settings

settings.testing = True

client = TestClient(app)



class TestBid(TestClient):
    def setUp(self) -> None:
        self.client = TestClient(app)

        self.brand = process_create_brand()