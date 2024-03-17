from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from starlette import status

from app.schemas import TokenData, User
from app.utils import settings
from app.auth.api import call_world_verify

import json


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if token == settings.master_token:
            # Return a user with superadmin permissions
            superuser = User(
                username="superadmin",
                email="superadmin@example.com",
                new_user=False,
                influencer=None,
                brand=None,
                is_superuser=True,
            )
            return superuser
        else:
            payload = jwt.decode(
                token,
                settings.public_key,
                algorithms=["RS256"],
                audience="http://localhost:3000",
                options={"verify_exp": False},
            )
            username: str = payload.get("username")
            email: str = payload.get("email")
            new_user: bool = payload.get("new_user")
            if username is None:
                raise credentials_exception
            token_data = TokenData(
                username=username, email=email, new_user=new_user, is_superuser=False
            )
            user = token_data
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user


def process_world_verify(proof, action_id):
    request_body = {**proof, "action": action_id}
    # # Convert the dictionary to JSON string
    request_body = json.dumps(request_body)

    headers = {"Content-Type": "application/json"}

    try:
        # Make the HTTP request to your FastAPI endpoint
        response = call_world_verify(request_body, headers)

        # Check if the request was successful
        if response.ok:
            # Print the response from the FastAPI endpoint
            return {
                "status": 200,
                "code": "success",
                "detail": "This worldcoin verified correctly!",
            }
        else:
            # Print an error message if the request was not successful
            return {
                "status": 403,
                "code": response.status_code,
                "detail": response.status_code,
            }

    except Exception as e:
        # Handle exceptions
        print("An error occurred:", e)
        return {
            "status": 500,
            "message": "Internal server error",
        }
