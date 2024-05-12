# routes.py

from fastapi import APIRouter
from models.models import User, Chat, Message
from services import user_service, chat_service, message_service

user_router = APIRouter(prefix="/users")
chat_router = APIRouter(prefix="/chats")
message_router = APIRouter(prefix="/messages")

@user_router.post("/", response_model=User)
async def create_user(user: User):
    created_user = user_service.create_user(user)
    return created_user

@chat_router.post("/", response_model=Chat)
async def create_chat(chat: Chat):
    created_chat = chat_service.create_chat(chat)
    return created_chat

@message_router.post("/")
async def send_message(message: Message):
    sent_message = message_service.send_message(message)
    return sent_message
