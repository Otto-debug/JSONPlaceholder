from pydantic import BaseModel

class CommentsCreateSchema(BaseModel):
    name: str
    email: str
    body: str
    postId: int

class CommentsSchema(CommentsCreateSchema):
    id: int

    class Config:
        orm_mode = True