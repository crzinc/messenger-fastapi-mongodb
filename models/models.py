from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    username: str
    email: EmailStr  # Валидация адреса электронной почты
    password: str

class Chat(BaseModel):
    name: str
    participants: List[str]

class Message(BaseModel):
    sender: str
    content: str
