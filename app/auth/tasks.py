from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from starlette import status

from app.schemas import TokenData
from app.utils import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.public_key,
            algorithms=["RS256"],
            audience="http://localhost:3000",
        )
        username: str = payload.get("username")
        email: str = payload.get("email")
        new_user: bool = payload.get("new_user")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, email=email, new_user=new_user)
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
