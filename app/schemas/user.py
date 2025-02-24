from pydantic import BaseModel, Field # type: ignore

class UserBaseDto(BaseModel):
    Name: str
    Email: str

class UserCreateDto(UserBaseDto):
    Password: str

class UserUpdateDto(UserBaseDto):
    Password: str

class UserDto(UserBaseDto):
    Id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True