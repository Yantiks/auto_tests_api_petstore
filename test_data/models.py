from pydantic import BaseModel
from typing import Optional, List, Dict

class User(BaseModel):
    code: int
    type: str
    message: str

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class Pet(BaseModel):
    id: int
    category: Category
    name: Optional[str]
    photoUrls: List[str]
    tags: List[Tag]
    status: str


# {
#     "id": 232323,
#     "category": {
#         "id": 1,
#         "name": "cat 1"
#     },
#     "name": "capybarinya",
#     "photoUrls": [
#         "photourl"
#     ],
#     "tags": [
#         {
#             "id": 1,
#             "name": "tagname"
#         }
#     ],
#     "status": "available"
# }