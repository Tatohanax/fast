from fastapi import (
    APIRouter,
    HTTPException
)
from .models import (
   # UserModel,
    ShowUserModel
)
from .settings import db

from typing import List

router = APIRouter()
"""
@router.post("/", response_description="Add new", response_model=UserModel) 
async def create_user(user: UserModel): 
    new_user = await db["users"].insert_one(user.dict())
    created_user = await db["users"].find_one({"_id": new_user.inserted_id}) 
    created_user.pop('_id')
    return created_user
"""

@router.get("/list", response_description="List all users", response_model=List[ShowUserModel])
async def list_users():
    try:
        users = await db["users"].find({ "age": { "$gte": 18, "$lte": 30 } }).to_list(100)
    except:
         raise HTTPException(status_code=404, detail=f"Not found")
    return users