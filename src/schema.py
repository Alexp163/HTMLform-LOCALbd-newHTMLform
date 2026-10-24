from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    nickname: str
    password: str
    data: str


class UserReadSchema(BaseModel):
    nickname: str
    password: str
    data: str


class AccessTokenSchema(BaseModel):
    access_token: str
    token_type: str
