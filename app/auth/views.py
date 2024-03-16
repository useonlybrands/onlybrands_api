from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from starlette import status

from app.schemas import TokenData
from app.user.tasks import process_get_user
# from app.utils import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# known_tokens = set()


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # if settings.master_token:
        #     known_tokens.add(settings.master_token)
        #
        # # Simulate a database query to find a known token
        # if token not in known_tokens:
        #     raise credentials_exception
        #
        # # If the token is a master token, return a user with all permissions
        # if token == settings.master_token:
        #     return User(username='master', email='master@example.com', new_user=False)

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
