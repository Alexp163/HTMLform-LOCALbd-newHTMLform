from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    nickname: str
    password: str
    data: str


class UserReadSchema(BaseModel):
    id: str
    nickname: str
    data: str


class AccessTokenSchema(BaseModel):
    access_token: str
    token_type: str


class PacientDataCreateSchema(BaseModel):
    name: str 
    age: int 
    med_history: str 
    story_life: str 
    symptoms: str 
    local_status: str 
    diagnosis: str 
    med_tactis: str 
    med_final: str 

class PacientDataReadSchema(BaseModel):
    name: str 
    age: int 
    med_history: str 
    story_life: str 
    symptoms: str 
    local_status: str 
    diagnosis: str 
    med_tactis: str 
    med_final: str 


class PacientDataUpdateSchema(BaseModel):
    name: str 
    age: int 
    med_history: str 
    story_life: str 
    symptoms: str 
    local_status: str 
    diagnosis: str 
    med_tactiсs: str 
    med_final: str 

    