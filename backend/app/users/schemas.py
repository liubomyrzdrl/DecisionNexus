from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class CurrentUser(BaseModel):
    id: int
    name: str = "Demo User"
    role: str = "creator"


def get_current_user():
    return CurrentUser(id=1)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    team_id: Optional[int]
    created_at: datetime
    updated_at: datetime

