from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from .models import (
    UserModel,
    ShowUserModel
)
from .dependecies import (
    get_current_user,
    authenticate_user,
    create_access_token,
    get_password_hash
)
from .settings import db, ACCESS_TOKEN_EXPIRE_MINUTES

from typing import List
from datetime import datetime, timedelta

import re

router = APIRouter()

#@router.post("/", response_description="Add new user" )
#async def create_user(user: UserModel):
#    await user.save()
#    return new_user

@router.post("/", response_description="Add new", response_model=UserModel)
async def create_user(user: UserModel):
    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.get("/list", response_description="List all users", response_model=List[ShowUserModel])
async def list_users():
    users = await db["users"].find().to_list(1000)
    return users