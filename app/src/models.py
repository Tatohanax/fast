from pydantic import BaseModel
from typing import Optional

"""
class UserModel(BaseModel):
    name: str
    email : str
    age : int
    company : str
    join_date: str
    job_title: str
    gender: str
    salary: int
"""

class ShowUserModel(BaseModel):
    name: str
    email : str
    age : int
    company : str
    join_date: str
    job_title: str
    gender: str
    salary: int

