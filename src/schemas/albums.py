from pydantic import BaseModel

class AlbumCreateSchema(BaseModel):
    title: str
    userId: int

class AlbumSchema(AlbumCreateSchema):
    id: int

    class Config:
        orm_mode = True