from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    secondname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    secondname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priorty: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priorty: int