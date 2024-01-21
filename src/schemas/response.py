from .request import Blog
from pydantic import BaseModel
from typing import List

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]


class ShowBlog(BaseModel):
    title: str
    body:str
    creator: ShowUser
