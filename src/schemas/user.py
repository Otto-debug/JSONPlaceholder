from pydantic import BaseModel

class AddressSchema(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str

class CompanySchema(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class UserCreateSchema(BaseModel):
    name: str
    username: str
    email: str
    address: AddressSchema
    phone: str
    website: str
    company: CompanySchema

class UserSchema(UserCreateSchema):
    id: int

    class Config:
        orm_mode = True
