from pydantic import BaseModel

class TodoCreateSchema(BaseModel):
    title: str
    completed: bool
    userId: int

class TodoSchema(TodoCreateSchema):
    id: int

    class Config:
        orm_mode = True