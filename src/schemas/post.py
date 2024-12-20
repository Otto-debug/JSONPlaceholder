from pydantic import BaseModel

class PostCreateSchema(BaseModel):
    title: str
    body: str
    userId: int

class PostSchema(PostCreateSchema):
    id: int

    class Config:
        orm_mode = True