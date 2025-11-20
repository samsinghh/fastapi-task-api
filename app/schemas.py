from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool

    class Config:
        orm_mode = True

