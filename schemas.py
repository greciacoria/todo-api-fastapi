from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

class TaskOut(BaseModel):
    id: int
    title: str
    done: bool

    class Config:
        from_attributes = True
