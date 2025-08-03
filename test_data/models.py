from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    code: int
    type: str
    message: str

class BaseUser(BaseModel):
    results: List[User]