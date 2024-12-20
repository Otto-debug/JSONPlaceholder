from pydantic import BaseModel

class PhotoCreateSchema(BaseModel):
    title: str
    url: str
    thumbnailUrl: str
    albumId: int

class PhotoSchema(PhotoCreateSchema):
    id: int

    class Config:
        orm_mode = True