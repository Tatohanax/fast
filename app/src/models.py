from bson import ObjectId
from pydantic import BaseModel
from typing import Optional



class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    name: str
    email : str
    age : int
    company : str
    join_date: str
    job_title: str
    gender: str
    salary: int


class ShowUserModel(BaseModel):
    name: str
    email : str
    age : int
    company : str
    join_date: str
    job_title: str
    gender: str
    salary: int

