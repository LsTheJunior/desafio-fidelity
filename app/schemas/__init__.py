"""
Pacote de schemas para validação de dados da aplicação.
"""

from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

class Comment(BaseModel):
    id: int
    post_id: int
    content: str
    author_id: int

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int
    email: str