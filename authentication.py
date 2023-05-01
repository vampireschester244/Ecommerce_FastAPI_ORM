from dotenv import load_dotenv
import jwt
from fastapi import (FastAPI, Depends, HTTPException, status)

from models import (User, Business, Product, user_pydantic, user_pydanticIn, 
                    product_pydantic,product_pydanticIn, business_pydantic, 
                    business_pydanticIn)
from passlib.context import CryptContext
import os

load_dotenv()
# config_credentials = dict(dotenv_values(".env"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)

    if user and verify_password(password, user.password):
        return user

    return False


async def token_generator(username: str, password: str):
    user = await authenticate_user(username, password)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {
        "id" : user.id,
        "username" : user.username
    }

    token = jwt.encode(token_data, os.getenv('SECRET_KEY'))
    return token


async def verify_token(token: str):
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
