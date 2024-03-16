import typing as t

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status

from app.database import SessionLocal
from app.schemas import UnauthorizedMessage, TokenData, User
from app.user.tasks import process_get_user
from app.utils import settings

auth_router = APIRouter()

# Auth
known_tokens = set()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# We will handle a missing token ourselves
get_bearer_token = HTTPBearer(auto_error=False)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
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

async def get_token(
    auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
    current_user: User = Depends(process_get_user),
) -> str:
    # If settings.testing is True, return a dummy token
    if settings.testing:
        known_tokens.add(settings.test_token)

    if settings.master_token:
        known_tokens.add(settings.master_token)

    # Simulate a database query to find a known token
    if auth is None or (token := auth.credentials) not in known_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().detail,
            # Assuming UnauthorizedMessage is defined somewhere in your actual code
        )

    # If the token is a master token, return it without user validation
    if token == settings.master_token:
        return token

    # If the token is a user-specific token, proceed with user validation
    return token