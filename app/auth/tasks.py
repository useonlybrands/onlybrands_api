from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from starlette import status

from app.schemas import TokenData
from app.user.tasks import process_get_user
from app.utils import settings
from app.auth.api import call_world_verify

import json
from typing import Any, Dict
import requests



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.JWTError:
        raise credentials_exception
    user = process_get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def process_world_verify(proof, action_id):
    request_body = {**proof, "action": action_id}
    # Convert the dictionary to JSON string
    request_body = json.dumps(request_body)

    
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Make the HTTP request to your FastAPI endpoint
        response = call_world_verify(request_body, headers)
        
        # Check if the request was successful
        if response.ok:
            # Print the response from the FastAPI endpoint
            return {"status": 200, "code": "success",
        "detail": "This action verified correctly!",}
        else:
            # Print an error message if the request was not successful
            return {"status": 403, "code": response.status_code,
        "detail": response.status_code,}

    except Exception as e:
        # Handle exceptions
        print("An error occurred:", e)
        return {"status": 500, "message": "Internal server error",}

